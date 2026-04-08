#!/usr/bin/env python3
"""Cross-reference validation for Logos bootstrap.

Collects known object IDs from markdown frontmatter and machine-readable graph JSON
objects, then checks that claim objects and retrieval neighborhoods reference
existing IDs.
"""
from __future__ import annotations

import json
import pathlib

OBJECT_ID_SOURCE_HINT = (
    "expected ID from docs markdown frontmatter `id` or data/graph JSON "
    "`identity.id`/`id`/`address.id`"
)


def extract_frontmatter(text: str) -> str | None:
    if not text.startswith('---\n'):
        return None
    try:
        _, rest = text.split('---\n', 1)
        frontmatter, _ = rest.split('\n---\n', 1)
        return frontmatter
    except ValueError:
        return None


def parse_simple_yaml(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith('#'):
            continue
        if line.startswith(' ') or line.startswith('-'):
            continue
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        data[key.strip()] = value.strip()
    return data


def extract_graph_object_ids(path: pathlib.Path) -> set[str]:
    """Extract supported object IDs from one graph JSON file."""
    raw = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(raw, dict):
        return set()

    ids: set[str] = set()

    top_level_id = raw.get('id')
    if isinstance(top_level_id, str) and top_level_id:
        ids.add(top_level_id)

    identity = raw.get('identity')
    if isinstance(identity, dict):
        identity_id = identity.get('id')
        if isinstance(identity_id, str) and identity_id:
            ids.add(identity_id)

    address = raw.get('address')
    if isinstance(address, dict):
        address_id = address.get('id')
        if isinstance(address_id, str) and address_id:
            ids.add(address_id)

    return ids


def collect_ids(root: pathlib.Path) -> set[str]:
    ids: set[str] = set()

    for path in (root / 'docs').rglob('*.md'):
        fm = extract_frontmatter(path.read_text(encoding='utf-8'))
        if fm is None:
            continue
        data = parse_simple_yaml(fm)
        obj_id = data.get('id')
        if obj_id:
            ids.add(obj_id)

    for path in (root / 'data' / 'graph').rglob('*.json'):
        ids.update(extract_graph_object_ids(path))

    return ids


def collect_claim_ids(root: pathlib.Path) -> set[str]:
    ids: set[str] = set()
    for path in (root / 'data' / 'claims').glob('*.yaml'):
        data = parse_simple_yaml(path.read_text(encoding='utf-8'))
        claim_id = data.get('claim_id')
        if claim_id:
            ids.add(claim_id)
    return ids


def check_claim_refs(root: pathlib.Path, known_ids: set[str]) -> list[str]:
    failures: list[str] = []
    for path in (root / 'data' / 'claims').glob('*.yaml'):
        data = parse_simple_yaml(path.read_text(encoding='utf-8'))
        for key in ('subject', 'object'):
            ref = data.get(key)
            if ref and ref not in known_ids:
                failures.append(
                    f"{path.as_posix()}: missing `{key}` reference '{ref}' "
                    f"({OBJECT_ID_SOURCE_HINT})"
                )
    return failures


def check_retrieval_refs(root: pathlib.Path, known_ids: set[str], claim_ids: set[str]) -> list[str]:
    failures: list[str] = []
    for path in (root / 'data' / 'retrieval').glob('*.yaml'):
        lines = path.read_text(encoding='utf-8').splitlines()
        mode = None
        for raw in lines:
            line = raw.rstrip()
            if line.startswith('included_objects:'):
                mode = 'objects'
                continue
            if line.startswith('included_claims:'):
                mode = 'claims'
                continue
            if not line.startswith('  - '):
                continue
            value = line[4:].strip()
            if mode == 'objects' and value not in known_ids:
                failures.append(
                    f"{path.as_posix()}: missing `included_objects` reference '{value}' "
                    f"({OBJECT_ID_SOURCE_HINT})"
                )
            if mode == 'claims' and value not in claim_ids:
                failures.append(
                    f"{path.as_posix()}: missing `included_claims` reference '{value}' "
                    "(expected claim ID from data/claims/*.yaml `claim_id`)"
                )
    return failures


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    known_ids = collect_ids(root)
    claim_ids = collect_claim_ids(root)
    failures = []
    failures.extend(check_claim_refs(root, known_ids))
    failures.extend(check_retrieval_refs(root, known_ids, claim_ids))
    if failures:
        for f in failures:
            print('FAIL', f)
        return 1
    print('Cross-reference validation passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
