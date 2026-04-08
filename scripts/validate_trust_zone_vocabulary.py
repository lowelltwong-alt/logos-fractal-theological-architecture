#!/usr/bin/env python3
"""Validate trust_zone values against the controlled vocabulary.

Checks:
- Markdown frontmatter under docs/
- YAML records under data/claims/
- YAML records under data/retrieval/
"""
from __future__ import annotations

import pathlib
import sys

ALLOWED_TRUST_ZONES = {
    "canonical",
    "tradition-scoped",
    "proposed",
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
        data[key.strip()] = value.strip()
    return data


def validate_docs(root: pathlib.Path) -> list[str]:
    failures: list[str] = []
    for path in (root / "docs").rglob("*.md"):
        fm = extract_frontmatter(path.read_text(encoding="utf-8"))
        if fm is None:
            continue
        data = parse_simple_yaml(fm)
        trust_zone = data.get("trust_zone")
        if trust_zone and trust_zone not in ALLOWED_TRUST_ZONES:
            failures.append(
                f"{path.as_posix()}: invalid trust_zone '{trust_zone}' in frontmatter"
            )
    return failures


def validate_yaml_records(root: pathlib.Path, relative_dir: str) -> list[str]:
    failures: list[str] = []
    for path in (root / relative_dir).glob("*.yaml"):
        data = parse_simple_yaml(path.read_text(encoding="utf-8"))
        trust_zone = data.get("trust_zone")
        if trust_zone and trust_zone not in ALLOWED_TRUST_ZONES:
            failures.append(f"{path.as_posix()}: invalid trust_zone '{trust_zone}'")
    return failures


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    failures: list[str] = []
    failures.extend(validate_docs(root))
    failures.extend(validate_yaml_records(root, "data/claims"))
    failures.extend(validate_yaml_records(root, "data/retrieval"))

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    print("Trust-zone vocabulary validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
