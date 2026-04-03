#!/usr/bin/env python3
"""Minimal validation for Logos claim YAML files.

This script intentionally performs lightweight validation so the repository can
start enforcing structure before a fuller schema toolchain is added.
"""
from __future__ import annotations

import pathlib
import sys

REQUIRED_KEYS = {
    "claim_id",
    "subject",
    "predicate",
    "object",
    "epistemic_status",
    "review_status",
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
        data[key.strip()] = value.strip()
    return data


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    claims_dir = root / "data" / "claims"
    missing = []
    for path in claims_dir.glob("*.yaml"):
        data = parse_simple_yaml(path.read_text(encoding="utf-8"))
        absent = sorted(REQUIRED_KEYS - data.keys())
        if absent:
            missing.append((path.as_posix(), absent))
    if missing:
        for path, absent in missing:
            print(f"FAIL {path}: missing keys {', '.join(absent)}")
        return 1
    print("Claim validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
