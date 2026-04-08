#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib


def generate_edge_id(source: str, verb: str, target: str) -> str:
    basis = f"{source}|{verb}|{target}".strip()
    digest = hashlib.sha1(basis.encode("utf-8")).hexdigest()[:10]
    return f"edge.{digest}.{source}__{verb}__{target}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministically generate an edge ID.")
    parser.add_argument("--source", required=True)
    parser.add_argument("--verb", required=True)
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    print(generate_edge_id(args.source, args.verb, args.target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
