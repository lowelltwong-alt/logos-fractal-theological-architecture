# Action Patterns

## Purpose

This file defines governed action patterns for how important changes should happen inside the repository's ontology and graph layers.

A strong ontology does not only model things. It also models important classes of change.

This file should be read together with:
- `interface-patterns.md`
- `promotion-thresholds.md`
- `schema-compatibility-policy.md`
- `fractal-rules.md`

## Core principle

An action pattern answers:
what kind of governed change is being made to a node, edge, schema, or classification?

This matters because some changes are not just edits. They are ontology events.

## Why action patterns matter

Without governed action patterns, the repository risks:
- silent promotion decisions
- quiet reclassification of boundary-sensitive sources
- schema changes with no clear governance path
- important edge revisions that leave weak auditability

With action patterns, the repository can treat certain changes as explicit classes of action rather than accidental edits.

## Recommended action families

### `promote_node`
Use when a repeated local section, concept, or pattern becomes its own reusable node.

Typical expectations:
- threshold rationale
- parent/source references
- new anchor and node type
- review where appropriate

### `promote_edge`
Use when a repeated or high-value local connection becomes a first-class relationship object.

Typical expectations:
- relation rationale
- source and target refs
- provenance and confidence

### `reclassify_boundary_object`
Use when a translation, noncanonical source, or disputed object changes classification in a meaningful way.

Typical expectations:
- prior classification
- new classification
- reason for change
- reviewer expectation

### `supersede_edge`
Use when a governed relationship object is replaced, narrowed, corrected, or retired.

Typical expectations:
- prior edge reference
- replacement edge reference
- reason for supersession
- retained audit trail

### `version_schema`
Use when a machine-readable shape or object grammar changes in a compatibility-sensitive way.

Typical expectations:
- schema change note
- additive vs breaking classification
- migration expectation if needed

### `approve_for_core_use`
Use when an object moves from working or proposed state into a more trusted role in the repository.

Typical expectations:
- review state update
- reviewer attribution
- clearer trust zone or use-case status

## Action rule

Do not model every tiny edit as an ontology action.

Use action patterns when the change is structurally or governance-significant.

Examples include:
- promotion
- boundary reclassification
- schema versioning
- edge supersession
- trust-level elevation

## Why this is fractal

Action patterns make the repository more fractal because change itself begins to follow repeatable grammar.

That means the repository can recur not only in how it stores nodes, but also in how it governs transformation of those nodes.

## Summary principle

A world-class ontology governs important change patterns, not only object types.

Action patterns help the repository preserve meaning, trust, and auditability as it grows.
