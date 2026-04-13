#!/usr/bin/env python3
"""Validate governed node frontmatter from the canonical schema registry.

This validator consumes schemas/schema_registry.json and the referenced
logos_node_min schema file. It intentionally targets bounded content-node
surfaces plus markdown files that opt into the node contract, so governance
notes with lighter metadata are not treated as node-contract failures by
default.
"""
from __future__ import annotations

from validation_contracts import (
    ROOT,
    activates_contract,
    extract_frontmatter,
    get_contract,
    load_contract_schema,
    load_schema_registry,
    parse_simple_yaml,
    resolve_contract_paths,
    schema_failures,
)


def main() -> int:
    root = ROOT
    registry = load_schema_registry(root)
    contract = get_contract(registry, "logos_node_min")
    schema = load_contract_schema(contract, root)
    hard_failures = []
    soft_warnings = []
    recommended = contract.get("recommended_keys", [])

    for path in resolve_contract_paths(contract, root):
        text = path.read_text(encoding="utf-8")
        fm = extract_frontmatter(text)
        if fm is None:
            continue

        data = parse_simple_yaml(fm)
        if not activates_contract(data, contract):
            continue

        failures = schema_failures(data, schema)
        if failures:
            hard_failures.append((path.relative_to(root).as_posix(), failures))

        missing_recommended = [key for key in recommended if key not in data]
        if missing_recommended:
            soft_warnings.append((path.relative_to(root).as_posix(), missing_recommended))

    for path, absent in soft_warnings:
        print(f"WARN {path}: missing recommended keys {', '.join(absent)}")
    if hard_failures:
        for path, failures in hard_failures:
            print(f"FAIL {path}: {'; '.join(failures)}")
        return 1
    print("Node frontmatter validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
