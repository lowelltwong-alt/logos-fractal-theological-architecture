---
object_type: architecture_decision_record
trust_zone: canonical
lifecycle_status: active
provenance_note: "Added on 2026-04-13 while salvaging the durable exceptions-lake architecture decision from old PR #17 onto the cleaned baseline."
reason_for_inclusion: "Preserve the architecture-level decision that the repository learns through reviewable escalation rather than silent self-modification."
---

# Exceptions Lake Architecture Decision

## Decision

The repository intentionally keeps an exceptions-lake and learning-loop layer as part of the core architecture.

This layer remains distinct from:
- ontology
- taxonomy
- doctrine content
- ordering profiles
- governance rules

## Why this remains explicit

A living theological architecture needs a governed place to record where reality resists the current model without silently changing doctrine, taxonomy, or policy.

Without that layer, the repository tends to fail in one of two ways:

1. silent mutation
2. rigid brittleness

The exceptions-lake pattern therefore remains part of the architecture because it preserves pressure, review, lineage, and doctrinal accountability together.

## Core operating principle

The system should learn through reviewable escalation, not through silent self-modification.

That means the repository keeps these states distinct:
- expectation
- exception
- adaptation
- approved governed change

## Design consequence

This is not an optional sidecar.

It is part of the repository DNA because the project is trying to stay:
- recursive
- governable
- pressure-aware
- self-correcting under review
- resistant to silent deformation

## Current implementation surfaces

This decision is expressed in:
- `README.md`
- `docs/governance/exceptions-lake-and-learning-loop.md`
- `docs/governance/exceptioncase-and-learningsignal-primitives.md`
- `docs/governance/exceptions-lake-integration-note.md`
- `docs/roadmap/exceptions-lake-learning-loop-roadmap-extension.md`
- `docs/roadmap/repository-integration-map.md`
- `data/graph/schemes/exceptions-lake.md`

Historical incoming material is preserved separately in:
- `incoming/exceptions-lake/README.md`

That incoming area is archival only and must not be treated as a canonical authored source.

## Promotion rule

No exception should directly overwrite the original expectation.

Exceptions, resolutions, and promotions remain append-only and traceable. Only reviewed changes should flow back into governed repository surfaces.

## Review trigger

Review this decision if:
- the canonical exception address grammar changes
- the repository collapses exception and adaptation into one layer
- a proposal attempts to remove the exceptions-lake layer as mere cleanup
