#!/usr/bin/env python3
"""Validate governed external mapping objects against the canonical registry."""
from __future__ import annotations

import json
import pathlib
import re
from collections import defaultdict
from typing import Any

from validation_contracts import (
    ROOT,
    extract_graph_object_ids,
    get_contract,
    iter_string_values,
    load_contract_schema,
    load_controlled_vocabulary_source,
    load_schema_registry,
    resolve_contract_paths,
)


def load_json(path: pathlib.Path) -> dict[str, Any]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    return raw if isinstance(raw, dict) else {}


def schema_properties(schema: dict[str, Any], *keys: str) -> dict[str, Any]:
    current = schema
    for key in keys:
        current = current.get("properties", {}).get(key, {})
    return current


def primary_graph_id(raw: dict[str, Any]) -> str | None:
    identity = raw.get("identity")
    if isinstance(identity, dict):
        identity_id = identity.get("id")
        if isinstance(identity_id, str) and identity_id:
            return identity_id

    top_level_id = raw.get("id")
    if isinstance(top_level_id, str) and top_level_id:
        return top_level_id

    address = raw.get("address")
    if isinstance(address, dict):
        address_id = address.get("id")
        if isinstance(address_id, str) and address_id:
            return address_id

    return None


def effective_object_type(raw: dict[str, Any]) -> str:
    top_level = raw.get("object_type")
    if isinstance(top_level, str) and top_level:
        return top_level

    classification = raw.get("classification")
    if isinstance(classification, dict):
        classified = classification.get("object_type")
        if isinstance(classified, str) and classified:
            return classified

    return ""


def require_string(
    path: pathlib.Path,
    container: dict[str, Any],
    field: str,
    failures: list[str],
    *,
    min_length: int = 1,
    pattern: str | None = None,
    allowed_values: list[str] | None = None,
) -> str | None:
    value = container.get(field)
    if not isinstance(value, str) or len(value) < min_length:
        failures.append(f"{path.as_posix()}: missing or invalid `{field}`")
        return None
    if pattern and re.fullmatch(pattern, value) is None:
        failures.append(f"{path.as_posix()}: `{field}` value '{value}' does not match required pattern")
        return None
    if allowed_values and value not in allowed_values:
        failures.append(
            f"{path.as_posix()}: `{field}` value '{value}' must be one of {', '.join(allowed_values)}"
        )
        return None
    return value


def collect_graph_index(paths: list[pathlib.Path]) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for path in paths:
        raw = load_json(path)
        for object_id in extract_graph_object_ids(raw):
            index[object_id] = {
                "path": path,
                "raw": raw,
                "object_type": effective_object_type(raw),
                "trust_zone": raw.get("trust_zone"),
            }
    return index


def validate_non_mapping_external_usage(
    path: pathlib.Path,
    raw: dict[str, Any],
    handle_token_re: re.Pattern[str],
) -> list[str]:
    failures: list[str] = []
    for object_id in extract_graph_object_ids(raw):
        if object_id.startswith("ext."):
            failures.append(
                f"{path.as_posix()}: canonical graph object ID '{object_id}' must not use an external handle"
            )

    seen_tokens: set[str] = set()
    for value in iter_string_values(raw):
        for token in handle_token_re.findall(value):
            if token in seen_tokens:
                continue
            seen_tokens.add(token)
            failures.append(
                f"{path.as_posix()}: external handle '{token}' must live only in external mapping objects"
            )
    return failures


def main() -> int:
    root = ROOT
    registry = load_schema_registry(root)
    contract = get_contract(registry, "logos_external_mapping_object")
    schema = load_contract_schema(contract, root)
    _, controlled_values = load_controlled_vocabulary_source(registry, root)

    trust_zone_values = controlled_values["trust_zone"]["allowed_values"]
    trust_rank = {value: index for index, value in enumerate(trust_zone_values)}

    mapping_schema = schema_properties(schema, "mapping")
    external_ref_schema = schema_properties(schema, "mapping", "external_ref")
    identity_schema = schema_properties(schema, "identity")
    provenance_schema = schema_properties(schema, "provenance")
    review_schema = schema_properties(schema, "review")

    mapping_type_values = mapping_schema.get("properties", {}).get("mapping_type", {}).get("enum", [])
    handle_pattern = external_ref_schema.get("properties", {}).get("handle", {}).get("pattern")
    source_pattern = external_ref_schema.get("properties", {}).get("source", {}).get("pattern")
    handle_token_re = re.compile(handle_pattern) if isinstance(handle_pattern, str) else re.compile(r"^$")

    graph_paths = resolve_contract_paths(contract, root)
    graph_index = collect_graph_index(graph_paths)

    failures: list[str] = []
    seen_pairs: defaultdict[tuple[str, str], list[str]] = defaultdict(list)
    target_object_type = contract.get("object_type")

    for path in graph_paths:
        raw = load_json(path)
        object_type = effective_object_type(raw)

        if object_type != target_object_type:
            failures.extend(validate_non_mapping_external_usage(path, raw, handle_token_re))
            continue

        required_top = [key for key in schema.get("required", []) if key not in raw]
        if required_top:
            failures.append(
                f"{path.as_posix()}: missing required top-level keys {', '.join(required_top)}"
            )

        if raw.get("object_type") != target_object_type:
            failures.append(
                f"{path.as_posix()}: object_type must be '{target_object_type}'"
            )

        trust_zone = require_string(
            path,
            raw,
            "trust_zone",
            failures,
            allowed_values=trust_zone_values,
        )

        identity = raw.get("identity")
        if not isinstance(identity, dict):
            failures.append(f"{path.as_posix()}: missing `identity` object")
            identity = {}
        for field in identity_schema.get("required", []):
            rule = identity_schema.get("properties", {}).get(field, {})
            require_string(
                path,
                identity,
                field,
                failures,
                min_length=rule.get("minLength", 1),
                pattern=rule.get("pattern"),
            )

        mapping = raw.get("mapping")
        if not isinstance(mapping, dict):
            failures.append(f"{path.as_posix()}: missing `mapping` object")
            mapping = {}

        mapping_type = require_string(
            path,
            mapping,
            "mapping_type",
            failures,
            allowed_values=mapping_type_values,
        )
        canonical_id = require_string(path, mapping, "canonical_id", failures)

        external_ref = mapping.get("external_ref")
        if not isinstance(external_ref, dict):
            failures.append(f"{path.as_posix()}: missing `mapping.external_ref` object")
            external_ref = {}

        handle = require_string(
            path,
            external_ref,
            "handle",
            failures,
            pattern=handle_pattern,
        )
        source = require_string(
            path,
            external_ref,
            "source",
            failures,
            pattern=source_pattern,
        )
        source_id = require_string(path, external_ref, "source_id", failures)
        source_trust_zone = external_ref.get("source_trust_zone")
        if isinstance(source_trust_zone, str) and source_trust_zone not in trust_rank:
            failures.append(
                f"{path.as_posix()}: `mapping.external_ref.source_trust_zone` value '{source_trust_zone}' is not in the controlled vocabulary"
            )

        if handle and source and not handle.startswith(f"ext.{source}."):
            failures.append(
                f"{path.as_posix()}: external handle '{handle}' does not match source '{source}'"
            )
        if handle and source and source_id:
            expected_handle = f"ext.{source}.{source_id}"
            if handle != expected_handle:
                failures.append(
                    f"{path.as_posix()}: external handle '{handle}' must equal '{expected_handle}'"
                )

        provenance = raw.get("provenance")
        if not isinstance(provenance, dict):
            failures.append(f"{path.as_posix()}: missing `provenance` object")
            provenance = {}
        for field in provenance_schema.get("required", []):
            value = provenance.get(field)
            if field in {"derived_from", "source_refs"}:
                if not isinstance(value, list):
                    failures.append(f"{path.as_posix()}: `provenance.{field}` must be an array")
            elif not isinstance(value, str) or not value:
                failures.append(f"{path.as_posix()}: missing or invalid `provenance.{field}`")

        review = raw.get("review")
        if not isinstance(review, dict):
            failures.append(f"{path.as_posix()}: missing `review` object")
            review = {}
        for field in review_schema.get("required", []):
            value = review.get(field)
            if not isinstance(value, str) or not value:
                failures.append(f"{path.as_posix()}: missing or invalid `review.{field}`")

        if canonical_id:
            target = graph_index.get(canonical_id)
            if target is None:
                failures.append(f"{path.as_posix()}: unresolved canonical target '{canonical_id}'")
            else:
                if target["path"] == path:
                    failures.append(f"{path.as_posix()}: canonical target '{canonical_id}' must not resolve to the mapping object itself")
                if target["object_type"] == target_object_type:
                    failures.append(
                        f"{path.as_posix()}: canonical target '{canonical_id}' must resolve to a non-mapping graph object"
                    )

                target_zone = target.get("trust_zone")
                if isinstance(target_zone, str) and trust_zone and target_zone in trust_rank and trust_zone in trust_rank:
                    if trust_rank[trust_zone] < trust_rank[target_zone]:
                        failures.append(
                            f"{path.as_posix()}: forbidden trust-zone direction '{trust_zone}' -> '{target_zone}'"
                        )

        if canonical_id and handle:
            seen_pairs[(canonical_id, handle)].append(path.as_posix())

        if mapping_type and canonical_id:
            derived_from = provenance.get("derived_from") if isinstance(provenance, dict) else None
            if isinstance(derived_from, list) and canonical_id not in derived_from:
                failures.append(
                    f"{path.as_posix()}: provenance.derived_from should include canonical target '{canonical_id}'"
                )

    for (canonical_id, handle), locations in sorted(seen_pairs.items()):
        if len(locations) > 1:
            failures.append(
                f"duplicate canonical-target mapping {canonical_id} -> {handle} across {', '.join(sorted(locations))}"
            )

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    print("External mapping validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
