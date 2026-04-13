---
object_type: graph_scheme
trust_zone: canonical
lifecycle_status: active
provenance_note: "Created on 2026-04-13 on top of the post-PR-29 cleaned baseline to define governed external taxonomy crosswalks without overwriting canonical repository identity."
reason_for_inclusion: "Provide a canonical-safe grammar for external mappings that fits the current graph, schema, and validator architecture."
---

# External Mapping Scheme

## Purpose

This scheme defines how external taxonomy references may be represented in the repository without turning outside identifiers into canonical repository identity.

## Core rule

Canonical repository IDs remain authoritative.

External references must be attached through governed external mapping objects rather than being written directly into canonical graph object identity.

## Handle grammar

External references use this handle form:

- `ext.<source>.<id>`

Where:
- `<source>` is a stable lower-case dataset/provider token
- `<id>` is the source-native identifier carried forward in normalized form

## Mapping relation vocabulary

Allowed `mapping_type` values:

- `exact_match`
- `close_match`
- `broader`
- `narrower`
- `related`

## Validation expectations

External mapping validation should fail when:

1. a handle does not match `ext.<source>.<id>`
2. a mapping points at a missing or non-canonical target object
3. a duplicate canonical-target mapping pair appears more than once
4. an external handle appears in non-mapping graph objects
5. a higher-trust mapping object depends on a lower-trust target object

## Summary principle

External mappings are governed bridge objects for interoperability.

They support crosswalks and federation while preserving canonical repository identity inside the repository itself.
