---
object_type: graph_scheme
trust_zone: canonical
lifecycle_status: active
provenance_note: "Created on 2026-04-08 to define canonical-safe ingestion grammar for external taxonomy crosswalks."
reason_for_inclusion: "Provide stable mapping semantics so external systems can be federated without mutating canonical identity."
---

# External Mapping Scheme

## Purpose

Define a canonical mapping grammar for crosswalking external taxonomies into this repository without contaminating canonical identifiers.

## Mapping relation types

Allowed `mapping_type` values:

- `exact_match`
- `close_match`
- `broader`
- `narrower`
- `related`

## Canonical identity protection rule

External systems **must never** overwrite canonical IDs.

- Canonical IDs stay in repository-native object identity fields.
- External references are attached only through `external_mapping_object` records.
- Any direct external identifier in non-mapping object identity is invalid.

## Namespace policy for external handles

External references must use this handle form:

- `ext.<source>.<id>`

Where:

- `<source>` is a stable dataset/provider token (for example: `strongs`, `wikidata`, `snomed`)
- `<id>` is the source-native key (normalized for filesystem-safe usage)

Examples:

- `ext.strongs.h7225`
- `ext.wikidata.q131208`

## Trust-zone direction rule

Apply trust-zone direction checks to mapping dependencies:

- Lower-trust mapping objects may reference higher-trust canonical targets.
- Higher-trust mapping objects may not depend on lower-trust targets.
- Canonical targets remain authoritative; mappings are bridges, not replacements.

## Ingestion validation requirements

The ingestion validator must fail when it finds:

1. unresolved external references (missing or malformed `ext.<source>.<id>` handles)
2. duplicate canonical-target mapping pairs
3. forbidden trust-zone direction from mapping object to canonical target

## Summary principle

External crosswalks are first-class, governed mapping objects that preserve interoperability while protecting canonical identity.
