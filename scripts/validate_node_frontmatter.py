#!/usr/bin/env python3
"""Minimal validation for Logos markdown frontmatter.

This script uses simple text parsing so it can run with no third-party
dependencies. It checks only for the presence of key fields in frontmatter.
"""
from __future__ import annotations

import pathlib
import sys

REQUIRED_KEYS = {
    "id",
    "anchor",
    "title",
    "node_type",
    "status",
    "review_status",
}

EXTRA_RECOMMENDED = {"address", "trust_zone", "lifecycle_state", "ai_usage_posture"}


def extract_frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    try:
        _, rest = text.split("---\n", 1)
        frontmatter, _ = rest.split("\n---\n", 1)
        return frontmatter
    except ValueError:
        return None


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
    targets = [root / "docs"]
    hard_failures = []
    soft_warnings = []
    for base in targets:
        for path in base.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            fm = extract_frontmatter(text)
            if fm is None:
                continue
            data = parse_simple_yaml(fm)
            missing_required = sorted(REQUIRED_KEYS - data.keys())
            if missing_required:
                hard_failures.append((path.as_posix(), missing_required))
            missing_recommended = sorted(EXTRA_RECOMMENDED - data.keys())
            if missing_recommended:
                soft_warnings.append((path.as_posix(), missing_recommended))
    for path, absent in soft_warnings:
        print(f"WARN {path}: missing recommended keys {', '.join(absent)}")
    if hard_failures:
        for path, absent in hard_failures:
            print(f"FAIL {path}: missing required keys {', '.join(absent)}")
        return 1
    print("Node frontmatter validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
