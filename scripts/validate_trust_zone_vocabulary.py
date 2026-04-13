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

from validation_contracts import (
    ROOT,
    extract_frontmatter,
    load_controlled_vocabulary_source,
    load_schema_registry,
    parse_simple_yaml,
)

REPORT_PATH = pathlib.Path("data/reports/controlled-vocabulary-report.json")


def check_record(
    path: pathlib.Path,
    data: dict[str, object],
    origin: str,
    root: pathlib.Path,
    allowed_values: dict[str, set[str]],
    migration_aliases: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    for field, allowed in allowed_values.items():
        if field not in data:
            continue
        value = data[field]
        if not isinstance(value, str):
            continue
        if value in allowed:
            continue

        normalized = migration_aliases.get(field, {}).get(value)
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


def validate_docs(
    root: pathlib.Path,
    allowed_values: dict[str, set[str]],
    migration_aliases: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    for path in (root / "docs").rglob("*.md"):
        fm = extract_frontmatter(path.read_text(encoding="utf-8"))
        if fm is None:
            continue
        data = parse_simple_yaml(fm)
        violations.extend(
            check_record(path, data, "markdown_frontmatter", root, allowed_values, migration_aliases)
        )
    return violations


def validate_yaml_tree(
    root: pathlib.Path,
    rel_dir: str,
    allowed_values: dict[str, set[str]],
    migration_aliases: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    base = root / rel_dir
    if not base.exists():
        return violations
    for path in base.rglob("*.yaml"):
        data = parse_simple_yaml(path.read_text(encoding="utf-8"))
        violations.extend(check_record(path, data, "yaml", root, allowed_values, migration_aliases))
    return violations


def validate_json_templates(
    root: pathlib.Path,
    allowed_values: dict[str, set[str]],
    migration_aliases: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
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
        violations.extend(check_record(path, data, "json_template", root, allowed_values, migration_aliases))
    return violations


def write_report(
    root: pathlib.Path,
    violations: list[dict[str, str]],
    vocabulary_source_path: str,
) -> pathlib.Path:
    report_path = root / REPORT_PATH
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "validator": "controlled_vocabulary",
        "controlled_vocabulary_source": vocabulary_source_path,
        "violation_count": len(violations),
        "violations": violations,
    }
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report_path


def main() -> int:
    root = ROOT
    registry = load_schema_registry(root)
    source_meta, controlled_values = load_controlled_vocabulary_source(registry, root)
    allowed_values = {
        field: set(controlled_values[field]["allowed_values"])
        for field in source_meta.get("fields", [])
    }
    migration_aliases = {
        field: dict(controlled_values[field]["aliases"])
        for field in source_meta.get("fields", [])
    }

    violations: list[dict[str, str]] = []
    violations.extend(validate_docs(root, allowed_values, migration_aliases))
    violations.extend(validate_yaml_tree(root, "data", allowed_values, migration_aliases))
    violations.extend(validate_yaml_tree(root, "examples", allowed_values, migration_aliases))
    violations.extend(validate_json_templates(root, allowed_values, migration_aliases))

    report_path = write_report(root, violations, source_meta["path"])

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
