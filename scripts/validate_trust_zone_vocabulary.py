#!/usr/bin/env python3
"""Validate controlled vocabulary fields and emit a machine-readable report.

Checks enum membership for governed fields across:
- Markdown frontmatter under docs/
- YAML files under data/ and examples/
- JSON templates under data/graph/templates/
"""
from __future__ import annotations

import json
import pathlib
import sys

ALLOWED_VALUES: dict[str, set[str]] = {
    "trust_zone": {
        "canonical",
        "tradition-scoped",
        "proposed",
        "inferred",
        "deprecated",
        "learning-sidecar",
    },
    "lifecycle_status": {
        "draft",
        "active",
        "deprecated",
        "superseded",
        "archived",
    },
}

MIGRATION_ALIASES: dict[str, dict[str, str]] = {
    "trust_zone": {
        "core_trusted": "canonical",
        "reviewed_specialized": "tradition-scoped",
        "working_proposed": "proposed",
        "boundary_restricted": "learning-sidecar",
        "experimental_graph": "inferred",
    }
}

REPORT_PATH = pathlib.Path("data/reports/controlled-vocabulary-report.json")


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
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def check_record(path: pathlib.Path, data: dict[str, str], origin: str, root: pathlib.Path) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    for field, allowed in ALLOWED_VALUES.items():
        if field not in data:
            continue
        value = data[field]
        if value in allowed:
            continue

        normalized = MIGRATION_ALIASES.get(field, {}).get(value)
        if normalized in allowed:
            message = (
                f"non-canonical alias '{value}' found; normalize to '{normalized}'"
            )
        else:
            message = (
                f"value '{value}' is not in controlled vocabulary"
            )

        violations.append(
            {
                "path": path.relative_to(root).as_posix(),
                "field": field,
                "value": value,
                "origin": origin,
                "message": message,
            }
        )
    return violations


def validate_docs(root: pathlib.Path) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    for path in (root / "docs").rglob("*.md"):
        fm = extract_frontmatter(path.read_text(encoding="utf-8"))
        if fm is None:
            continue
        data = parse_simple_yaml(fm)
        violations.extend(check_record(path, data, "markdown_frontmatter", root))
    return violations


def validate_yaml_tree(root: pathlib.Path, rel_dir: str) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    base = root / rel_dir
    if not base.exists():
        return violations
    for path in base.rglob("*.yaml"):
        data = parse_simple_yaml(path.read_text(encoding="utf-8"))
        violations.extend(check_record(path, data, "yaml", root))
    return violations


def validate_json_templates(root: pathlib.Path) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    base = root / "data" / "graph" / "templates"
    if not base.exists():
        return violations

    for path in base.rglob("*.json"):
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            violations.append(
                {
                    "path": path.relative_to(root).as_posix(),
                    "field": "<file>",
                    "value": "<invalid-json>",
                    "origin": "json_template",
                    "message": f"invalid JSON: {exc}",
                }
            )
            continue

        if not isinstance(raw, dict):
            continue

        data = {k: str(v) for k, v in raw.items() if isinstance(v, (str, int, float))}
        violations.extend(check_record(path, data, "json_template", root))
    return violations


def write_report(root: pathlib.Path, violations: list[dict[str, str]]) -> pathlib.Path:
    report_path = root / REPORT_PATH
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "validator": "controlled_vocabulary",
        "violation_count": len(violations),
        "violations": violations,
    }
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report_path


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[1]
    violations: list[dict[str, str]] = []
    violations.extend(validate_docs(root))
    violations.extend(validate_yaml_tree(root, "data"))
    violations.extend(validate_yaml_tree(root, "examples"))
    violations.extend(validate_json_templates(root))

    report_path = write_report(root, violations)

    if violations:
        for violation in violations:
            print(
                "FAIL "
                f"{violation['path']}: {violation['field']}={violation['value']} "
                f"({violation['message']})"
            )
        print(f"Machine-readable report: {report_path.as_posix()}")
        return 1

    print("Controlled vocabulary validation passed.")
    print(f"Machine-readable report: {report_path.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
