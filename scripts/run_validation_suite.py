#!/usr/bin/env python3
"""Run the shared default validation suite for local, CI, and semantic merge."""
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys

from validation_contracts import (
    DEFAULT_VALIDATION_SCOPE_NOTE,
    count_prefixed_lines,
    default_validation_commands,
)


def run_validator(command: list[str], root: pathlib.Path) -> dict[str, object]:
    proc = subprocess.run(command, cwd=root, capture_output=True, text=True)
    stdout = proc.stdout.strip()
    stderr = proc.stderr.strip()
    return {
        "command": " ".join(command),
        "returncode": proc.returncode,
        "stdout": stdout,
        "stderr": stderr,
        "failure_count": count_prefixed_lines(stdout, "FAIL "),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the shared default validation suite.")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON only.",
    )
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parents[1]
    validators = []
    for spec in default_validation_commands(sys.executable):
        result = run_validator(spec["command"], root)
        result["name"] = spec["name"]
        validators.append(result)

    failed_validator_count = sum(1 for result in validators if result["returncode"] != 0)
    payload = {
        "suite_name": "default_validation_suite",
        "scope_note": DEFAULT_VALIDATION_SCOPE_NOTE,
        "failed_validator_count": failed_validator_count,
        "validators": validators,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(DEFAULT_VALIDATION_SCOPE_NOTE)
        for result in validators:
            status = "PASS" if result["returncode"] == 0 else "FAIL"
            print(f"[{status}] {result['name']}")
            if result["stdout"]:
                print(result["stdout"])
            if result["stderr"]:
                print(result["stderr"], file=sys.stderr)
        if failed_validator_count:
            print(
                f"Validation suite failed: {failed_validator_count} of {len(validators)} validators returned non-zero."
            )
        else:
            print(f"Validation suite passed ({len(validators)} validators).")

    return 1 if failed_validator_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
