#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import unicodedata


def slug_token(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    lowered = ascii_only.lower()
    collapsed = re.sub(r"[^a-z0-9]+", "_", lowered).strip("_")
    return collapsed or "unnamed"


def generate_anchor(family: str, label: str) -> str:
    family_token = family.strip().lower().replace("_", ".")
    family_token = re.sub(r"[^a-z0-9.]+", "", family_token).strip(".")
    if not family_token:
        family_token = "concept"
    return f"{family_token}.{slug_token(label)}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministically generate a governance-safe anchor.")
    parser.add_argument("--family", required=True, help="Anchor family, e.g. doctrine, concept, tradition")
    parser.add_argument("--label", required=True, help="Human-readable label")
    args = parser.parse_args()
    print(generate_anchor(args.family, args.label))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
