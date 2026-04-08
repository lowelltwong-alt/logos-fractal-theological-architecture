#!/usr/bin/env python3
"""Validation checks for auto-generated retrieval neighborhood bundles."""
from __future__ import annotations

import pathlib
from collections import defaultdict
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
CLAIMS_DIR = ROOT / "data" / "claims"
RETRIEVAL_DIR = ROOT / "data" / "retrieval"

HIGH_VALUE_PREDICATES = {"grounds", "anchors", "constrains", "informs"}


def parse_simple_yaml(path: pathlib.Path) -> dict[str, object]:
    data: dict[str, object] = {}
    current_list_key: str | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_list_key:
            data.setdefault(current_list_key, [])
            assert isinstance(data[current_list_key], list)
            data[current_list_key].append(line[4:].strip())
            continue
        if line.startswith(" "):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            current_list_key = key
            data[key] = []
        else:
            current_list_key = None
            data[key] = value
    return data


def parse_freshness(path: pathlib.Path) -> tuple[str | None, str | None]:
    generated_at = None
    stale_after_days = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if line.startswith("  generated_at:"):
            generated_at = line.split(":", 1)[1].strip()
        if line.startswith("  stale_after_days:"):
            stale_after_days = line.split(":", 1)[1].strip()
    return generated_at, stale_after_days


def main() -> int:
    failures: list[str] = []

    degree: dict[str, int] = defaultdict(int)
    for claim_path in sorted(CLAIMS_DIR.glob("*.yaml")):
        claim = parse_simple_yaml(claim_path)
        if claim.get("predicate") not in HIGH_VALUE_PREDICATES:
            continue
        subject = str(claim.get("subject", ""))
        obj = str(claim.get("object", ""))
        if subject:
            degree[subject] += 1
        if obj:
            degree[obj] += 1

    high_value_nodes = {node for node, deg in degree.items() if deg >= 2}

    generated_files = sorted(RETRIEVAL_DIR.glob("*-neighborhood.auto.yaml"))
    focus_to_file: dict[str, pathlib.Path] = {}
    for path in generated_files:
        data = parse_simple_yaml(path)
        focus = str(data.get("focus_object", ""))
        if focus:
            focus_to_file[focus] = path

        generated_at, stale_after_days = parse_freshness(path)
        if not generated_at or not stale_after_days:
            failures.append(f"FAIL {path.as_posix()}: incomplete freshness metadata")
            continue
        try:
            generated_dt = datetime.strptime(generated_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            stale_days = int(stale_after_days)
            age_days = (datetime.now(timezone.utc) - generated_dt).days
            if age_days > stale_days:
                failures.append(
                    f"FAIL {path.as_posix()}: stale neighborhood (age_days={age_days}, stale_after_days={stale_days})"
                )
        except ValueError:
            failures.append(f"FAIL {path.as_posix()}: invalid freshness values")

    for node in sorted(high_value_nodes):
        if node not in focus_to_file:
            failures.append(
                f"FAIL high-value node {node}: no maintained auto neighborhood artifact found"
            )

    if failures:
        print("\n".join(failures))
        return 1

    print(
        f"Retrieval neighborhood validation passed ({len(generated_files)} artifacts; {len(high_value_nodes)} high-value nodes covered)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
