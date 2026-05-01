#!/usr/bin/env python3
"""Validate required governance metadata in markdown frontmatter.

Rules enforced:
- For markdown files with YAML frontmatter in docs/governance/, require:
  object_type, trust_zone, lifecycle_status, provenance_note, reason_for_inclusion
- trust_zone must be one of the allowed values.
"""
from __future__ import annotations

import pathlib

REQUIRED_KEYS = {
    "object_type",
    "trust_zone",
    "provenance_note",
    "reason_for_inclusion",
}

ALLOWED_TRUST_ZONES = {
    "canonical",
    "tradition-scoped",
    "proposed",
    "governance_instructions",
    "inferred",
    "deprecated",
    "learning-sidecar",
}


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
        data[key.strip()] = value.strip().strip('"')
    return data


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    base = root / "docs" / "governance"

    failures: list[str] = []
    checked = 0

    for path in base.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        fm = extract_frontmatter(text)
        if fm is None:
            continue

        checked += 1
        data = parse_simple_yaml(fm)

        missing = sorted(REQUIRED_KEYS - data.keys())
        if missing:
            failures.append(f"FAIL {path.as_posix()}: missing keys {', '.join(missing)}")

        if "lifecycle_status" not in data and "lifecycle_state" not in data:
            failures.append(
                f"FAIL {path.as_posix()}: missing lifecycle key (need lifecycle_status or lifecycle_state)"
            )

        tz = data.get("trust_zone")
        if tz and tz not in ALLOWED_TRUST_ZONES:
            failures.append(
                f"FAIL {path.as_posix()}: trust_zone '{tz}' is not allowed"
            )

    if failures:
        for item in failures:
            print(item)
        return 1

    print(
        f"Governance metadata validation passed (checked {checked} file(s) with frontmatter)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
