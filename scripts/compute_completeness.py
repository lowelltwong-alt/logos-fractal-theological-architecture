#!/usr/bin/env python3
"""Compute architectural completeness scores for governed graph nodes."""
from __future__ import annotations

import argparse
import json
import pathlib
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


DIMENSIONS = [
    "identity",
    "provenance",
    "trust",
    "relation_coverage",
    "retrieval_neighborhood",
    "review_posture",
]

WEIGHTS = {
    "identity": 0.20,
    "provenance": 0.20,
    "trust": 0.15,
    "relation_coverage": 0.20,
    "retrieval_neighborhood": 0.10,
    "review_posture": 0.15,
}

DEFAULT_REQUIREMENTS = {
    "required_identity_fields": ["id", "anchor", "title", "version", "status"],
    "required_provenance_fields": ["created_by", "last_modified_by", "asserted_by", "review_state"],
    "accepted_trust_zones": [
        "canonical",
        "tradition-scoped",
        "proposed",
        "inferred",
        "deprecated",
        "learning-sidecar",
    ],
    "required_relationship_keys": ["typed_edges", "related_to"],
    "minimum_typed_edges": 1,
    "minimum_retrieval_links": 1,
    "accepted_review_states": ["editor_reviewed", "community_proposed", "unreviewed"],
    "preferred_review_states": ["editor_reviewed"],
}


@dataclass
class Node:
    path: pathlib.Path
    node_id: str
    node_type: str
    data: dict[str, Any]


def load_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=None, help="Repository root (defaults to script parent parent)")
    parser.add_argument(
        "--requirements",
        default="data/graph/completeness_requirements.json",
        help="Path to completeness requirements JSON (repo-relative by default)",
    )
    parser.add_argument(
        "--out-dir",
        default="reports/completeness",
        help="Output directory for completeness reports (repo-relative by default)",
    )
    parser.add_argument(
        "--run-ts",
        default=None,
        help="UTC timestamp label (YYYYMMDDTHHMMSSZ). Defaults to now.",
    )
    return parser.parse_args()


def resolve_repo_path(root: pathlib.Path, target: str) -> pathlib.Path:
    path = pathlib.Path(target)
    return path if path.is_absolute() else root / path


def load_requirements(path: pathlib.Path) -> dict[str, Any]:
    payload = load_json(path)
    reqs = payload.get("node_type_requirements", {})
    if not isinstance(reqs, dict):
        raise ValueError("node_type_requirements must be an object")
    return reqs


def discover_nodes(root: pathlib.Path) -> list[Node]:
    graph_root = root / "data/graph"
    nodes: list[Node] = []
    for path in sorted(graph_root.rglob("*.json")):
        if "templates" in path.parts or "examples" in path.parts:
            continue
        data = load_json(path)
        identity = data.get("identity") if isinstance(data.get("identity"), dict) else {}
        node_id = identity.get("id") or data.get("id")
        node_type = data.get("node_type")
        if not node_id or not node_type:
            continue
        nodes.append(Node(path=path, node_id=node_id, node_type=node_type, data=data))
    return nodes


def gather_retrieval_links(root: pathlib.Path) -> dict[str, set[str]]:
    links: dict[str, set[str]] = {}
    retrieval_root = root / "data/retrieval"
    for path in sorted(retrieval_root.glob("*.yaml")):
        current_section: str | None = None
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.rstrip()
            if not line:
                continue
            if not line.startswith(" ") and line.endswith(":"):
                key = line[:-1].strip()
                current_section = key if key in {"included_objects", "included_claims"} else None
                continue
            if current_section and line.lstrip().startswith("- "):
                obj = line.lstrip()[2:].strip()
                if obj:
                    links.setdefault(obj, set()).add(path.name)
    return links


def gather_centrality(nodes: list[Node], root: pathlib.Path) -> dict[str, int]:
    centrality = {node.node_id: 0 for node in nodes}

    for node in nodes:
        rel = node.data.get("relationships") if isinstance(node.data.get("relationships"), dict) else {}
        typed_edges = rel.get("typed_edges") if isinstance(rel.get("typed_edges"), list) else []
        for edge in typed_edges:
            if not isinstance(edge, dict):
                continue
            target = edge.get("target")
            if target in centrality:
                centrality[target] += 1
        for key in ["related_to", "depends_on", "enables", "children", "parents"]:
            values = rel.get(key)
            if not isinstance(values, list):
                continue
            for target in values:
                if target in centrality:
                    centrality[target] += 1

    for path in sorted((root / "data/claims").glob("*.yaml")):
        fields: dict[str, str] = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            if ":" not in line or line.startswith(" "):
                continue
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
        for key in ["subject", "object"]:
            node_id = fields.get(key)
            if node_id in centrality:
                centrality[node_id] += 1

    return centrality


def ratio(present: int, expected: int) -> float:
    if expected <= 0:
        return 1.0
    return max(0.0, min(1.0, present / expected))


def score_node(node: Node, req: dict[str, Any], retrieval_links: dict[str, set[str]]) -> dict[str, Any]:
    identity = node.data.get("identity") if isinstance(node.data.get("identity"), dict) else {}
    provenance = node.data.get("provenance") if isinstance(node.data.get("provenance"), dict) else {}
    entity_model = node.data.get("entity_model") if isinstance(node.data.get("entity_model"), dict) else {}
    relationships = node.data.get("relationships") if isinstance(node.data.get("relationships"), dict) else {}
    concordance = node.data.get("concordance") if isinstance(node.data.get("concordance"), dict) else {}

    required_identity = req.get("required_identity_fields", DEFAULT_REQUIREMENTS["required_identity_fields"])
    required_provenance = req.get("required_provenance_fields", DEFAULT_REQUIREMENTS["required_provenance_fields"])
    required_relationship_keys = req.get("required_relationship_keys", DEFAULT_REQUIREMENTS["required_relationship_keys"])
    minimum_typed_edges = int(req.get("minimum_typed_edges", DEFAULT_REQUIREMENTS["minimum_typed_edges"]))
    minimum_retrieval_links = int(req.get("minimum_retrieval_links", DEFAULT_REQUIREMENTS["minimum_retrieval_links"]))
    accepted_review_states = req.get("accepted_review_states", DEFAULT_REQUIREMENTS["accepted_review_states"])
    preferred_review_states = req.get("preferred_review_states", DEFAULT_REQUIREMENTS["preferred_review_states"])

    present_identity = sum(1 for key in required_identity if identity.get(key))
    present_provenance = sum(1 for key in required_provenance if provenance.get(key))

    trust_zone = entity_model.get("canonical_status") or node.data.get("trust_zone") or ""
    accepted_trust = req.get("accepted_trust_zones", DEFAULT_REQUIREMENTS["accepted_trust_zones"])
    trust_score = 1.0 if trust_zone in accepted_trust else 0.0

    present_relationship_keys = sum(
        1 for key in required_relationship_keys if key in relationships and relationships.get(key) not in (None, "", [])
    )
    typed_edges = relationships.get("typed_edges") if isinstance(relationships.get("typed_edges"), list) else []
    typed_edge_score = ratio(len(typed_edges), minimum_typed_edges)
    relation_coverage = (ratio(present_relationship_keys, len(required_relationship_keys)) + typed_edge_score) / 2

    retrieval_count = len(retrieval_links.get(node.node_id, set()))
    concordance_links = 0
    for key in ["concepts", "doctrines", "topics", "entities", "cross_reference_edges", "translation_witnesses"]:
        values = concordance.get(key)
        if isinstance(values, list):
            concordance_links += len([value for value in values if value])
    retrieval_signal = retrieval_count + concordance_links
    retrieval_neighborhood = ratio(retrieval_signal, minimum_retrieval_links)

    review_state = provenance.get("review_state")
    if review_state in preferred_review_states:
        review_posture = 1.0
    elif review_state in accepted_review_states:
        review_posture = 0.65
    else:
        review_posture = 0.0

    dim_scores = {
        "identity": ratio(present_identity, len(required_identity)),
        "provenance": ratio(present_provenance, len(required_provenance)),
        "trust": trust_score,
        "relation_coverage": relation_coverage,
        "retrieval_neighborhood": retrieval_neighborhood,
        "review_posture": review_posture,
    }

    completeness_score = sum(dim_scores[k] * WEIGHTS[k] for k in DIMENSIONS)

    missing = {
        "identity": [key for key in required_identity if not identity.get(key)],
        "provenance": [key for key in required_provenance if not provenance.get(key)],
        "relationships": [
            key for key in required_relationship_keys if key not in relationships or relationships.get(key) in (None, "", [])
        ],
    }

    return {
        "node_id": node.node_id,
        "node_type": node.node_type,
        "path": "",
        "dimension_scores": dim_scores,
        "weighted_score": round(completeness_score, 4),
        "weighted_score_pct": round(completeness_score * 100, 2),
        "trust_zone_value": trust_zone,
        "review_state": review_state,
        "retrieval_references": sorted(retrieval_links.get(node.node_id, set())),
        "missing_requirements": missing,
    }


def percentile_rank(values: list[int], value: int) -> float:
    if not values:
        return 0.0
    lower = sum(1 for v in values if v <= value)
    return round(lower / len(values), 4)


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve() if args.root else pathlib.Path(__file__).resolve().parents[1]
    requirements_path = resolve_repo_path(root, args.requirements)
    out_dir = resolve_repo_path(root, args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    run_ts = args.run_ts or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    req_by_type = load_requirements(requirements_path)
    nodes = discover_nodes(root)
    retrieval_links = gather_retrieval_links(root)
    centrality_map = gather_centrality(nodes, root)
    all_centralities = list(centrality_map.values())

    reports = []
    for node in nodes:
        req = req_by_type.get(node.node_type, DEFAULT_REQUIREMENTS)
        report = score_node(node, req, retrieval_links)
        report["path"] = node.path.relative_to(root).as_posix()
        centrality = centrality_map.get(node.node_id, 0)
        report["centrality"] = {
            "incoming_reference_count": centrality,
            "percentile": percentile_rank(all_centralities, centrality),
        }
        priority_index = (1.0 - report["weighted_score"]) * (1.0 + report["centrality"]["percentile"])
        report["remediation_priority_index"] = round(priority_index, 4)
        report["needs_overnight_remediation"] = (
            report["weighted_score"] < 0.75 and report["centrality"]["percentile"] >= 0.6
        )
        reports.append(report)

    reports.sort(key=lambda item: item["weighted_score"])
    prioritized = sorted(reports, key=lambda item: item["remediation_priority_index"], reverse=True)

    overview = {
        "run_timestamp": run_ts,
        "node_count": len(reports),
        "average_score": round(sum(item["weighted_score"] for item in reports) / max(len(reports), 1), 4),
        "median_score": round(reports[len(reports) // 2]["weighted_score"] if reports else 0.0, 4),
        "threshold_counts": {
            "lt_0_60": sum(1 for item in reports if item["weighted_score"] < 0.60),
            "lt_0_75": sum(1 for item in reports if item["weighted_score"] < 0.75),
            "gte_0_90": sum(1 for item in reports if item["weighted_score"] >= 0.90),
        },
    }

    node_scores_path = out_dir / f"node_scores_{run_ts}.json"
    prioritized_path = out_dir / f"prioritized_remediation_{run_ts}.json"
    latest_path = out_dir / "latest_node_scores.json"
    latest_prioritized_path = out_dir / "latest_prioritized_remediation.json"
    history_path = out_dir / "history.jsonl"
    trend_path = out_dir / "trend_latest.json"

    node_scores_payload = {
        "metadata": {
            "object_type": "completeness_assessment_report",
            "trust_zone": "proposed",
            "lifecycle_status": "active",
            "provenance_note": "Generated by scripts/compute_completeness.py from governed graph objects.",
            "reason_for_inclusion": "Track architectural completeness per node and prioritize remediation work.",
        },
        "overview": overview,
        "scores": reports,
    }

    prioritized_payload = {
        "metadata": {
            "object_type": "remediation_priority_report",
            "trust_zone": "proposed",
            "lifecycle_status": "active",
            "provenance_note": "Generated by scripts/compute_completeness.py using weighted score and centrality percentile.",
            "reason_for_inclusion": "Queue low-completeness, high-centrality nodes for overnight remediation.",
        },
        "run_timestamp": run_ts,
        "prioritized_nodes": prioritized,
    }

    node_scores_path.write_text(json.dumps(node_scores_payload, indent=2) + "\n", encoding="utf-8")
    prioritized_path.write_text(json.dumps(prioritized_payload, indent=2) + "\n", encoding="utf-8")
    latest_path.write_text(json.dumps(node_scores_payload, indent=2) + "\n", encoding="utf-8")
    latest_prioritized_path.write_text(json.dumps(prioritized_payload, indent=2) + "\n", encoding="utf-8")

    history_entry = {
        "run_timestamp": run_ts,
        "node_count": overview["node_count"],
        "average_score": overview["average_score"],
        "median_score": overview["median_score"],
        "threshold_counts": overview["threshold_counts"],
    }
    with history_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(history_entry) + "\n")

    history = [json.loads(line) for line in history_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    previous = history[-2] if len(history) > 1 else None
    delta = None
    if previous is not None:
        delta = {
            "average_score_delta": round(overview["average_score"] - float(previous.get("average_score", 0.0)), 4),
            "median_score_delta": round(overview["median_score"] - float(previous.get("median_score", 0.0)), 4),
            "lt_0_75_delta": overview["threshold_counts"]["lt_0_75"] - int(previous.get("threshold_counts", {}).get("lt_0_75", 0)),
        }

    trend_payload = {
        "metadata": {
            "object_type": "completeness_trend_report",
            "trust_zone": "proposed",
            "lifecycle_status": "active",
            "provenance_note": "Built from reports/completeness/history.jsonl by scripts/compute_completeness.py.",
            "reason_for_inclusion": "Show structural completeness improvement (or regression) across runs.",
        },
        "run_timestamp": run_ts,
        "latest": overview,
        "previous": previous,
        "delta": delta,
        "history": history,
    }
    trend_path.write_text(json.dumps(trend_payload, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote: {node_scores_path.relative_to(root)}")
    print(f"Wrote: {prioritized_path.relative_to(root)}")
    print(f"Wrote: {latest_path.relative_to(root)}")
    print(f"Wrote: {latest_prioritized_path.relative_to(root)}")
    print(f"Wrote: {history_path.relative_to(root)}")
    print(f"Wrote: {trend_path.relative_to(root)}")
    print(f"Computed completeness for {len(reports)} nodes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
