#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
import unicodedata


def slug(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    lowered = ascii_only.lower()
    return re.sub(r"[^a-z0-9]+", "_", lowered).strip("_") or "unnamed"


def generate_node_id(node_type: str, label: str) -> str:
    type_token = slug(node_type)
    label_token = slug(label)
    digest = hashlib.sha1(f"{type_token}:{label_token}".encode("utf-8")).hexdigest()[:10]
    return f"{type_token}.{label_token}.{digest}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministically generate a node ID.")
    parser.add_argument("--node-type", required=True)
    parser.add_argument("--label", required=True)
    args = parser.parse_args()
    print(generate_node_id(args.node_type, args.label))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
