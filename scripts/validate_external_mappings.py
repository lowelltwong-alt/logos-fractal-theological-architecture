#!/usr/bin/env python3
"""Validate external mapping objects and external-handle ingestion rules."""
from __future__ import annotations

import json
import pathlib
import re
from collections import defaultdict

ALLOWED_MAPPING_TYPES = {"exact_match", "close_match", "broader", "narrower", "related"}
ALLOWED_TRUST_ZONES = {
    "canonical",
    "tradition-scoped",
    "proposed",
    "inferred",
    "deprecated",
    "learning-sidecar",
}

TRUST_RANK = {
    "learning-sidecar": 0,
    "inferred": 1,
    "proposed": 2,
    "tradition-scoped": 3,
    "canonical": 4,
    "deprecated": 0,
}

EXTERNAL_HANDLE_RE = re.compile(r"^ext\.[a-z0-9][a-z0-9_-]*\.[A-Za-z0-9._:-]+$")
EXTERNAL_HANDLE_TOKEN_RE = re.compile(r"\bext\.[a-z0-9][a-z0-9_-]*\.[A-Za-z0-9._:-]+\b")


def iter_graph_json(root: pathlib.Path):
    for path in (root / "data" / "graph").rglob("*.json"):
        if "templates" in path.parts:
            continue
        yield path


def load_json(path: pathlib.Path) -> dict:
    raw = json.loads(path.read_text(encoding="utf-8"))
    return raw if isinstance(raw, dict) else {}


def extract_identity_ids(raw: dict) -> set[str]:
    ids: set[str] = set()
    if isinstance(raw.get("id"), str) and raw["id"]:
        ids.add(raw["id"])
    identity = raw.get("identity")
    if isinstance(identity, dict):
        if isinstance(identity.get("id"), str) and identity["id"]:
            ids.add(identity["id"])
    return ids


def collect_canonical_ids(root: pathlib.Path) -> set[str]:
    ids: set[str] = set()
    for path in iter_graph_json(root):
        raw = load_json(path)
        if raw.get("object_type") == "external_mapping_object":
            continue
        for obj_id in extract_identity_ids(raw):
            if not obj_id.startswith("ext."):
                ids.add(obj_id)
    return ids


def find_external_handle_tokens(value):
    if isinstance(value, str):
        return EXTERNAL_HANDLE_TOKEN_RE.findall(value)
    if isinstance(value, list):
        found = []
        for item in value:
            found.extend(find_external_handle_tokens(item))
        return found
    if isinstance(value, dict):
        found = []
        for v in value.values():
            found.extend(find_external_handle_tokens(v))
        return found
    return []


def validate_non_mapping_external_usage(path: pathlib.Path, raw: dict) -> list[str]:
    failures: list[str] = []
    if raw.get("object_type") == "external_mapping_object":
        return failures

    identity = raw.get("identity")
    if isinstance(identity, dict):
        identity_id = identity.get("id")
        if isinstance(identity_id, str) and identity_id.startswith("ext."):
            failures.append(
                f"{path.as_posix()}: canonical identity.id must not be external handle '{identity_id}'"
            )

    for token in find_external_handle_tokens(raw):
        failures.append(
            f"{path.as_posix()}: external handle '{token}' must live in external mapping objects"
        )
    return failures


def validate_mapping_object(path: pathlib.Path, raw: dict, canonical_ids: set[str]) -> tuple[list[str], tuple[str, str] | None]:
    failures: list[str] = []
    mapping = raw.get("mapping")
    if not isinstance(mapping, dict):
        return [f"{path.as_posix()}: missing `mapping` object"], None

    mapping_type = mapping.get("mapping_type")
    if mapping_type not in ALLOWED_MAPPING_TYPES:
        failures.append(
            f"{path.as_posix()}: invalid mapping_type '{mapping_type}' (allowed: {sorted(ALLOWED_MAPPING_TYPES)})"
        )

    canonical_id = mapping.get("canonical_id")
    if not isinstance(canonical_id, str) or not canonical_id:
        failures.append(f"{path.as_posix()}: missing mapping.canonical_id")
    elif canonical_id not in canonical_ids:
        failures.append(f"{path.as_posix()}: unresolved canonical target '{canonical_id}'")

    external_ref = mapping.get("external_ref")
    handle = None
    if not isinstance(external_ref, dict):
        failures.append(f"{path.as_posix()}: missing mapping.external_ref object")
    else:
        handle = external_ref.get("handle")
        if not isinstance(handle, str) or not EXTERNAL_HANDLE_RE.match(handle):
            failures.append(
                f"{path.as_posix()}: unresolved external reference handle '{handle}' (expected ext.<source>.<id>)"
            )

    mapping_zone = raw.get("trust_zone")
    canonical_zone = mapping.get("canonical_trust_zone")
    if mapping_zone not in ALLOWED_TRUST_ZONES:
        failures.append(f"{path.as_posix()}: invalid trust_zone '{mapping_zone}'")
    if canonical_zone not in ALLOWED_TRUST_ZONES:
        failures.append(f"{path.as_posix()}: invalid canonical_trust_zone '{canonical_zone}'")
    if mapping_zone in TRUST_RANK and canonical_zone in TRUST_RANK:
        if TRUST_RANK[mapping_zone] > TRUST_RANK[canonical_zone]:
            failures.append(
                f"{path.as_posix()}: forbidden trust-zone direction '{mapping_zone}' -> '{canonical_zone}'"
            )

    key = None
    if isinstance(canonical_id, str) and canonical_id and isinstance(handle, str) and handle:
        key = (canonical_id, handle)
    return failures, key


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    canonical_ids = collect_canonical_ids(root)
    failures: list[str] = []
    seen_pairs: dict[tuple[str, str], list[str]] = defaultdict(list)

    for path in iter_graph_json(root):
        raw = load_json(path)
        if raw.get("object_type") == "external_mapping_object":
            mapping_failures, pair = validate_mapping_object(path, raw, canonical_ids)
            failures.extend(mapping_failures)
            if pair:
                seen_pairs[pair].append(path.as_posix())
        else:
            failures.extend(validate_non_mapping_external_usage(path, raw))

    for pair, locations in seen_pairs.items():
        if len(locations) > 1:
            failures.append(
                f"duplicate canonical-target mapping {pair[0]} -> {pair[1]} across {', '.join(sorted(locations))}"
            )

    if failures:
        for failure in failures:
            print("FAIL", failure)
        return 1

    print("External mapping validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
