# Shared Properties

## Purpose

This file defines shared property families that should be reused across multiple node types instead of being re-invented locally each time.

A strong ontology does not only standardize node types and relationship verbs. It also standardizes recurring properties so metadata remains consistent, governable, and machine-legible.

This file should be read together with:
- `interface-patterns.md`
- `schema-compatibility-policy.md`
- `translation-trust-and-sectarian-classification.md`
- `noncanonical-and-heresy-classification.md`

## Core principle

If a property recurs across multiple node families and carries the same meaning, it should usually be treated as a shared property rather than a local invention.

This improves:
- consistency
- graph readability
- validation
- future automation
- cross-domain search and grouping

## Major shared property families

### Identity properties
Use across most governed nodes and objects.

Examples:
- `id`
- `anchor`
- `title`
- `slug`
- `version`
- `status`

### Review properties
Use across reviewable nodes.

Examples:
- `review_status`
- `review_cycle`
- `reviewed_by`
- `last_reviewed`
- `review_notes`

### Provenance properties
Use across any node or object with meaningful source or authorship history.

Examples:
- `created_by`
- `last_modified_by`
- `asserted_by`
- `derived_from`
- `source_refs`
- `evidence`

### Trust and boundary properties
Use across boundary-sensitive objects.

Examples:
- `confidence`
- `use_case_limit`
- `warning`
- `canonical_status`
- `historical_authenticity`
- `doctrinal_alignment`

### Translation properties
Use across translation witness objects and translation-sensitive nodes.

Examples:
- `translation_philosophy`
- `textual_base_quality`
- `provenance_claim_status`
- `doctrinal_tendency`
- `manipulation_risk`

### Machine-readable object properties
Use across graph and concordance objects.

Examples:
- `object_version`
- `schema_version`
- `object_type`
- `compatibility_status`
- `last_validated`

## Shared-property rule

Do not create local synonyms for the same recurring property meaning unless a real distinction exists and is documented.

Prefer:
- one shared property name
- one defined meaning
- reuse across object families

## Why this is fractal

Shared properties make the repository more fractal because they allow the same metadata grammar to recur across different domains.

That means a translation node, a doctrine node, a graph object, and a boundary-source object can all remain different while still sharing a stable property vocabulary where appropriate.

## Summary principle

Shared properties are part of ontology discipline.

They keep repeated metadata from drifting into several incompatible local dialects.
