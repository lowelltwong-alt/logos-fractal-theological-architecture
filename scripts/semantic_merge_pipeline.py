#!/usr/bin/env python3
"""Semantic merge checks and artifacts for governed graph changes.

This script extends text-level conflict checks with semantic integrity checks.
It writes CI-consumable artifacts under reports/semantic-merge/.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import subprocess
import sys
from collections import Counter, defaultdict

TRUST_ORDER = {
    "canonical": 0,
    "tradition-scoped": 1,
    "proposed": 2,
    "inferred": 3,
    "deprecated": 4,
    "learning-sidecar": 5,
}


def parse_simple_yaml(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("-"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def stable_slug(value: str) -> str:
    return re.sub(r"[^a-z0-9._-]+", "-", value.lower()).strip("-") or "item"


def load_example_nodes(root: pathlib.Path) -> list[dict[str, str]]:
    nodes: list[dict[str, str]] = []
    for path in sorted((root / "examples").glob("*.yaml")):
        parsed = parse_simple_yaml(path.read_text(encoding="utf-8"))
        parsed["_path"] = path.relative_to(root).as_posix()
        if parsed.get("id"):
            nodes.append(parsed)
    return nodes


def load_graph_nodes(root: pathlib.Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for path in sorted((root / "data" / "graph").rglob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            continue
        identity = raw.get("identity") if isinstance(raw.get("identity"), dict) else {}
        classification = raw.get("classification") if isinstance(raw.get("classification"), dict) else {}
        edge = raw.get("edge") if isinstance(raw.get("edge"), dict) else {}
        relationships = raw.get("relationships") if isinstance(raw.get("relationships"), dict) else {}

        node_id = None
        if isinstance(identity.get("id"), str):
            node_id = identity["id"]
        elif isinstance(raw.get("id"), str):
            node_id = raw["id"]

        if not node_id:
            continue

        rows.append(
            {
                "id": node_id,
                "title": identity.get("title") if isinstance(identity.get("title"), str) else "",
                "node_type": raw.get("node_type") if isinstance(raw.get("node_type"), str) else "",
                "object_type": classification.get("object_type") if isinstance(classification.get("object_type"), str) else "",
                "trust_zone": raw.get("trust_zone") if isinstance(raw.get("trust_zone"), str) else "",
                "relationships": relationships,
                "edge": edge,
                "path": path.relative_to(root).as_posix(),
            }
        )
    return rows


def make_conflict(kind: str, path: str, key: str, details: str, suggestion: str) -> dict[str, str]:
    return {
        "conflict_type": kind,
        "path": path,
        "key": key,
        "details": details,
        "proposed_resolution": suggestion,
    }


def semantic_conflicts(example_nodes: list[dict[str, str]], graph_nodes: list[dict[str, object]]) -> list[dict[str, str]]:
    conflicts: list[dict[str, str]] = []

    # ID collision (within examples + graph IDs).
    id_sources: defaultdict[str, list[str]] = defaultdict(list)
    for node in example_nodes:
        id_sources[node["id"]].append(node["_path"])
    for node in graph_nodes:
        id_sources[str(node["id"])].append(str(node["path"]))
    for node_id, paths in sorted(id_sources.items()):
        if len(paths) > 1:
            conflicts.append(
                make_conflict(
                    "id_collision",
                    ", ".join(paths),
                    node_id,
                    f"ID appears {len(paths)} times.",
                    "Consolidate duplicate nodes or replace one ID with deterministic non-colliding ID.",
                )
            )

    # Edge collision from examples relationship objects and graph edge objects.
    edge_index: defaultdict[str, list[str]] = defaultdict(list)
    for node in example_nodes:
        if {"source_id", "target_id", "relationship_type"}.issubset(node.keys()):
            key = f"{node['source_id']}|{node['relationship_type']}|{node['target_id']}"
            edge_index[key].append(node["_path"])
    for node in graph_nodes:
        edge = node.get("edge")
        if isinstance(edge, dict):
            src = edge.get("source")
            rel = edge.get("relationship_type")
            tgt = edge.get("target")
            if isinstance(src, str) and isinstance(rel, str) and isinstance(tgt, str):
                edge_index[f"{src}|{rel}|{tgt}"].append(str(node["path"]))
    for key, paths in sorted(edge_index.items()):
        if len(paths) > 1:
            conflicts.append(
                make_conflict(
                    "edge_collision",
                    ", ".join(paths),
                    key,
                    f"Edge tuple appears {len(paths)} times.",
                    "Keep one canonical relationship object and deprecate or merge duplicate edge records.",
                )
            )

    # Forbidden trust dependency direction: higher trust must not depend on lower trust.
    graph_by_id = {str(n["id"]): n for n in graph_nodes}
    for node in graph_nodes:
        source_zone = str(node.get("trust_zone") or "")
        relationships = node.get("relationships")
        if not isinstance(relationships, dict):
            continue
        depends_on = relationships.get("depends_on")
        if not isinstance(depends_on, list):
            continue
        for dep in depends_on:
            if not isinstance(dep, str) or dep not in graph_by_id:
                continue
            target_zone = str(graph_by_id[dep].get("trust_zone") or "")
            if source_zone in TRUST_ORDER and target_zone in TRUST_ORDER:
                if TRUST_ORDER[source_zone] < TRUST_ORDER[target_zone]:
                    conflicts.append(
                        make_conflict(
                            "forbidden_trust_dependency_direction",
                            str(node["path"]),
                            f"{node['id']} -> {dep}",
                            f"{source_zone} node depends on lower-trust {target_zone} node.",
                            "Reverse dependency direction, move dependency to a peer/higher-trust node, or re-zone the dependent object.",
                        )
                    )

    # Duplicate semantic nodes: same normalized title + node_type in graph.
    semantic_index: defaultdict[str, list[str]] = defaultdict(list)
    for node in graph_nodes:
        title = stable_slug(str(node.get("title") or ""))
        node_type = stable_slug(str(node.get("node_type") or ""))
        if title == "" or node_type == "":
            continue
        key = f"{node_type}|{title}"
        semantic_index[key].append(str(node.get("path")))
    for key, paths in sorted(semantic_index.items()):
        if len(paths) > 1:
            conflicts.append(
                make_conflict(
                    "duplicate_semantic_node",
                    ", ".join(paths),
                    key,
                    f"Semantic signature repeats {len(paths)} times.",
                    "Choose one canonical node; link alternates via alias/deprecation metadata instead of duplicate semantics.",
                )
            )

    return conflicts


def orphan_report(graph_nodes: list[dict[str, object]]) -> dict[str, object]:
    known_ids = {str(n["id"]) for n in graph_nodes}
    out_degree: Counter[str] = Counter()
    in_degree: Counter[str] = Counter()

    for node in graph_nodes:
        source_id = str(node["id"])
        rels = node.get("relationships")
        if isinstance(rels, dict):
            for key in ("depends_on", "related_to", "children", "parents", "enables", "supersedes", "superseded_by"):
                targets = rels.get(key)
                if not isinstance(targets, list):
                    continue
                for target in targets:
                    if isinstance(target, str) and target in known_ids:
                        out_degree[source_id] += 1
                        in_degree[target] += 1

        edge = node.get("edge")
        if isinstance(edge, dict):
            src = edge.get("source")
            tgt = edge.get("target")
            if isinstance(src, str) and isinstance(tgt, str) and src in known_ids and tgt in known_ids:
                out_degree[src] += 1
                in_degree[tgt] += 1

    orphans = [
        {
            "id": str(n["id"]),
            "path": str(n["path"]),
        }
        for n in graph_nodes
        if out_degree[str(n["id"])] == 0 and in_degree[str(n["id"])] == 0
    ]

    return {
        "total_graph_nodes": len(graph_nodes),
        "orphans": sorted(orphans, key=lambda x: x["id"]),
        "orphan_count": len(orphans),
    }


def run_command(command: list[str], root: pathlib.Path) -> dict[str, object]:
    proc = subprocess.run(command, cwd=root, capture_output=True, text=True)
    return {
        "command": " ".join(command),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def write_json(path: pathlib.Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_drift_debt_report(root: pathlib.Path, summary: dict[str, object]) -> pathlib.Path:
    report_path = root / "reports" / "drift-debt-report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    ts = summary["generated_at"]
    lines = [
        "---",
        "object_type: drift_debt_report",
        "trust_zone: proposed",
        "lifecycle_status: active",
        f'provenance_note: "Generated by scripts/semantic_merge_pipeline.py on {ts}."',
        "reason_for_inclusion: \"Track semantic merge debt trends over time in a committed report.\"",
        "---",
        "",
        "# Drift Debt Report",
        "",
        "| generated_at | conflicts | orphans | broken_cross_refs | broken_local_links |",
        "|---|---:|---:|---:|---:|",
    ]
    if report_path.exists():
        existing = report_path.read_text(encoding="utf-8").splitlines()
        rows = [line for line in existing if re.match(r"\|\d{4}-\d{2}-\d{2}T", line)]
    else:
        rows = []
    row = (
        f"|{ts}|{summary['conflict_count']}|{summary['orphan_count']}|"
        f"{summary['broken_cross_reference_count']}|{summary['broken_local_link_count']}|"
    )
    rows.append(row)
    rows = rows[-30:]
    lines.extend(rows)
    lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def run_pipeline(root: pathlib.Path, snapshot_only: bool) -> int:
    out_dir = root / "reports" / "semantic-merge"
    resolutions_dir = out_dir / "proposed-semantic-merge-resolution"
    resolutions_dir.mkdir(parents=True, exist_ok=True)

    graph_nodes = load_graph_nodes(root)
    snapshot = {
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "graph_node_count": len(graph_nodes),
        "graph_ids": sorted(str(node["id"]) for node in graph_nodes),
    }
    write_json(out_dir / "graph-integrity-snapshot.json", snapshot)

    if snapshot_only:
        return 0

    examples = load_example_nodes(root)
    conflicts = semantic_conflicts(examples, graph_nodes)
    orphan_data = orphan_report(graph_nodes)

    cross_ref_check = run_command([sys.executable, "scripts/validate_cross_references.py"], root)
    local_link_check = run_command([sys.executable, "scripts/validate_internal_links.py", "--all-markdown"], root)

    for idx, conflict in enumerate(conflicts, start=1):
        write_json(resolutions_dir / f"conflict-{idx:03d}-{stable_slug(conflict['conflict_type'])}.json", conflict)

    cross_ref_failures = sum(1 for line in cross_ref_check["stdout"].splitlines() if line.startswith("FAIL "))
    local_link_failures = sum(1 for line in local_link_check["stdout"].splitlines() if line.startswith("FAIL "))

    summary = {
        "generated_at": snapshot["generated_at"],
        "conflict_count": len(conflicts),
        "orphan_count": orphan_data["orphan_count"],
        "broken_cross_reference_count": cross_ref_failures,
        "broken_local_link_count": local_link_failures,
        "cross_reference_check": cross_ref_check,
        "local_link_check": local_link_check,
    }

    write_json(out_dir / "semantic-conflicts.json", {"conflicts": conflicts})
    write_json(out_dir / "orphan-detection.json", orphan_data)
    write_json(out_dir / "summary.json", summary)
    drift_report_path = update_drift_debt_report(root, summary)

    print(f"Wrote semantic merge artifacts to: {out_dir.relative_to(root).as_posix()}")
    print(f"Updated rolling drift debt report: {drift_report_path.relative_to(root).as_posix()}")

    has_errors = len(conflicts) > 0
    return 1 if has_errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run semantic merge checks and generate artifacts.")
    parser.add_argument(
        "--snapshot-only",
        action="store_true",
        help="Only generate graph-integrity-snapshot.json (for post-merge artifact requirements).",
    )
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parents[1]
    return run_pipeline(root, snapshot_only=args.snapshot_only)


if __name__ == "__main__":
    raise SystemExit(main())
