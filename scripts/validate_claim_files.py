#!/usr/bin/env python3
"""Validate claim YAML files from the canonical schema registry."""
from __future__ import annotations

from validation_contracts import (
    ROOT,
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
    contract = get_contract(registry, "logos_claim_min")
    schema = load_contract_schema(contract, root)
    failures = []

    for path in resolve_contract_paths(contract, root):
        data = parse_simple_yaml(path.read_text(encoding="utf-8"))
        record_failures = schema_failures(data, schema)
        if record_failures:
            failures.append((path.relative_to(root).as_posix(), record_failures))

    if failures:
        for path, record_failures in failures:
            print(f"FAIL {path}: {'; '.join(record_failures)}")
        return 1
    print("Claim validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
