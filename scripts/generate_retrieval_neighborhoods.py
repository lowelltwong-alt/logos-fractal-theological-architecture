#!/usr/bin/env python3
"""Generate governed retrieval neighborhoods from claims + graph objects.

Deterministic rules:
- Seed from claims whose subject/object is the focus object.
- Expand up to configured depth using allowed predicates per neighborhood type.
- Apply trust-zone filter to claims.
- Add lexical + translation context claims when attached to included text nodes.
- Add typed-edge context from graph relationship objects and typed_edges arrays.
- Emit YAML and JSON artifacts in data/retrieval/.
"""
from __future__ import annotations

import json
import pathlib
from collections import defaultdict, deque
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
CLAIMS_DIR = ROOT / "data" / "claims"
GRAPH_DIR = ROOT / "data" / "graph"
RETRIEVAL_DIR = ROOT / "data" / "retrieval"

ALLOWED_TRUST_ZONES = {"canonical", "tradition-scoped", "proposed"}
STALE_AFTER_DAYS = 30

NEIGHBORHOOD_RULES = {
    "passage": {
        "max_depth": 2,
        "allowed_predicates": {
            "grounds",
            "informs",
            "clarifies",
            "renders",
            "attests",
            "anchors",
            "constrains",
        },
    },
    "application": {
        "max_depth": 2,
        "allowed_predicates": {
            "anchors",
            "constrains",
            "informs",
            "grounds",
            "clarifies",
            "renders",
            "attests",
        },
    },
    "concept": {
        "max_depth": 2,
        "allowed_predicates": {"informs", "grounds", "clarifies", "constrains", "attests"},
    },
    "doctrine": {
        "max_depth": 2,
        "allowed_predicates": {"informs", "grounds", "constrains", "clarifies", "attests"},
    },
    "comparison": {
        "max_depth": 1,
        "allowed_predicates": {"renders", "attests", "clarifies", "grounds"},
    },
}


def parse_simple_yaml(path: pathlib.Path) -> dict:
    data: dict[str, object] = {}
    list_key: str | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and list_key:
            data.setdefault(list_key, [])
            assert isinstance(data[list_key], list)
            data[list_key].append(line[4:].strip())
            continue
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            list_key = key
            data[key] = []
        else:
            list_key = None
            data[key] = value
    return data


def object_kind(object_id: str) -> str:
    if object_id.startswith("text.") or object_id.startswith("verse.") or object_id.startswith("passage."):
        return "passage"
    if object_id.startswith("application."):
        return "application"
    if object_id.startswith("concept.") or object_id.startswith("biblical_theme."):
        return "concept"
    if object_id.startswith("doctrine."):
        return "doctrine"
    return "comparison"


def load_claims() -> list[dict]:
    claims: list[dict] = []
    for path in sorted(CLAIMS_DIR.glob("*.yaml")):
        c = parse_simple_yaml(path)
        c["_path"] = path
        claims.append(c)
    return claims


def build_claim_index(claims: list[dict]) -> dict[str, list[dict]]:
    idx: dict[str, list[dict]] = defaultdict(list)
    for c in claims:
        subject = str(c.get("subject", ""))
        obj = str(c.get("object", ""))
        if subject:
            idx[subject].append(c)
        if obj:
            idx[obj].append(c)
    return idx


def load_graph_index() -> tuple[dict[str, dict], list[dict]]:
    node_index: dict[str, dict] = {}
    relationship_objects: list[dict] = []
    for path in GRAPH_DIR.rglob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        node_id = data.get("identity", {}).get("id")
        if isinstance(node_id, str) and node_id:
            node_index[node_id] = data
        if data.get("node_type") == "cross_reference_node" and "edge" in data:
            relationship_objects.append(data)
    return node_index, relationship_objects


def yaml_dump(data: dict) -> str:
    lines: list[str] = []
    for k, v in data.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        elif isinstance(v, dict):
            lines.append(f"{k}:")
            for sk, sv in v.items():
                lines.append(f"  {sk}: {sv}")
        else:
            lines.append(f"{k}: {v}")
    return "\n".join(lines) + "\n"


def collect_neighborhood(
    focus: str,
    claims_idx: dict[str, list[dict]],
    rules: dict,
    node_index: dict[str, dict],
    relationship_objects: list[dict],
) -> tuple[list[str], list[str], list[str]]:
    included_objects: set[str] = {focus}
    included_claims: set[str] = set()
    typed_edges: set[str] = set()

    q = deque([(focus, 0)])
    seen = {focus}
    while q:
        current, depth = q.popleft()
        for c in claims_idx.get(current, []):
            if c.get("trust_zone") not in ALLOWED_TRUST_ZONES:
                continue
            pred = c.get("predicate")
            if pred not in rules["allowed_predicates"]:
                continue
            cid = str(c.get("claim_id", ""))
            subj = str(c.get("subject", ""))
            obj = str(c.get("object", ""))
            if cid:
                included_claims.add(cid)
            for nxt in (subj, obj):
                if nxt:
                    included_objects.add(nxt)
                    if depth + 1 <= rules["max_depth"] and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, depth + 1))

    text_nodes = [o for o in included_objects if o.startswith("text.")]
    for text_node in text_nodes:
        for c in claims_idx.get(text_node, []):
            if c.get("trust_zone") not in ALLOWED_TRUST_ZONES:
                continue
            if c.get("predicate") in {"clarifies", "renders", "attests"}:
                cid = str(c.get("claim_id", ""))
                subj = str(c.get("subject", ""))
                obj = str(c.get("object", ""))
                if cid:
                    included_claims.add(cid)
                if subj:
                    included_objects.add(subj)
                if obj:
                    included_objects.add(obj)

    # typed-edge context from graph nodes
    for obj_id in list(included_objects):
        node = node_index.get(obj_id)
        if not node:
            continue
        for edge in node.get("relationships", {}).get("typed_edges", []):
            target = edge.get("target")
            rel_type = edge.get("relationship_type")
            if isinstance(target, str):
                included_objects.add(target)
            if rel_type and target:
                typed_edges.add(f"{obj_id}:{rel_type}:{target}")
        for edge_id in node.get("concordance", {}).get("cross_reference_edges", []):
            if isinstance(edge_id, str):
                typed_edges.add(edge_id)

    # relationship artifacts where endpoints overlap included objects
    for rel in relationship_objects:
        edge = rel.get("edge", {})
        src = edge.get("source")
        tgt = edge.get("target")
        rel_id = rel.get("identity", {}).get("id")
        rel_type = edge.get("relationship_type")
        if src in included_objects or tgt in included_objects:
            if isinstance(src, str):
                included_objects.add(src)
            if isinstance(tgt, str):
                included_objects.add(tgt)
            if isinstance(rel_id, str):
                typed_edges.add(rel_id)
            elif src and rel_type and tgt:
                typed_edges.add(f"{src}:{rel_type}:{tgt}")

    return sorted(included_objects), sorted(included_claims), sorted(typed_edges)


def slug_from_focus(focus: str) -> str:
    return focus.replace(".", "-")


def main() -> int:
    claims = load_claims()
    claims_idx = build_claim_index(claims)
    node_index, relationship_objects = load_graph_index()

    # high-value heuristic: claim-degree >= 2
    degrees: dict[str, int] = defaultdict(int)
    for c in claims:
        subj = str(c.get("subject", ""))
        obj = str(c.get("object", ""))
        if subj:
            degrees[subj] += 1
        if obj:
            degrees[obj] += 1

    focus_nodes = sorted(k for k, v in degrees.items() if v >= 2)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    for focus in focus_nodes:
        n_type = object_kind(focus)
        rules = NEIGHBORHOOD_RULES[n_type]
        objects, claim_ids, typed_edges = collect_neighborhood(
            focus, claims_idx, rules, node_index, relationship_objects
        )
        artifact = {
            "object_type": "retrieval_neighborhood_bundle",
            "trust_zone": "proposed",
            "lifecycle_status": "active",
            "provenance_note": "Auto-generated by scripts/generate_retrieval_neighborhoods.py from claims + graph context.",
            "reason_for_inclusion": "Operationalize deterministic retrieval neighborhoods with trust filtering and freshness tracking.",
            "neighborhood_id": f"retrieval.{focus.replace('.', '_')}.auto.v1",
            "focus_object": focus,
            "neighborhood_type": n_type,
            "review_status": "unreviewed",
            "trust_filter": ",".join(sorted(ALLOWED_TRUST_ZONES)),
            "freshness": {
                "generated_at": generated_at,
                "stale_after_days": STALE_AFTER_DAYS,
            },
            "included_objects": objects,
            "included_claims": claim_ids,
            "included_typed_edges": typed_edges,
        }
        slug = slug_from_focus(focus)
        yaml_path = RETRIEVAL_DIR / f"{slug}-neighborhood.auto.yaml"
        json_path = RETRIEVAL_DIR / f"{slug}-neighborhood.auto.json"
        yaml_path.write_text(yaml_dump(artifact), encoding="utf-8")
        json_path.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")

    print(f"Generated {len(focus_nodes)} neighborhood bundles in {RETRIEVAL_DIR.as_posix()}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
