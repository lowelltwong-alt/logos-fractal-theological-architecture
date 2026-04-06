---
object_type: phase_definition
trust_zone: proposed
lifecycle_status: draft
provenance_note: "Created on 2026-04-05 after reviewing the existing hermeneutics and primary-sources docs."
reason_for_inclusion: "Add a dedicated Phase 2 document for source handling and interpretation without duplicating the existing governance baseline."
---

# Phase 2 - Source and Interpretation

Phase 2 adds the first disciplined layer that sits between raw sources and doctrinal conclusions.

Its job is to keep source objects, interpretive work, doctrine views, and doctrine assessments distinct.

## Phase 2 focus

Phase 2 does four things:

1. makes source-bearing objects explicit
2. makes interpretive acts explicit
3. preserves links from doctrine work back to source and interpretation layers
4. prevents doctrine claims from pretending to be raw source facts

## Required separations

- a source object is not a doctrine topic
- a passage interpretation is not a doctrine view
- a doctrine view is not a doctrine assessment
- an assessment must name the view and baseline it is judging

## Minimum governed objects for this phase

- source_object
- passage_interpretation
- doctrine_topic
- doctrine_view
- doctrine_assessment

Each object should remain independently identifiable and traceable.

## Phase 2 exit criteria

- doctrine views can point back to source-facing or interpretation-facing material
- doctrine assessments can point to both the doctrine topic and doctrine view they judge
- provenance remains visible when moving from source to interpretation to doctrine
- lower-trust interpretation work does not silently become canonical doctrine

## Adjacent existing docs

This phase note is intentionally lean.

Use these existing docs beside it:

- `docs/hermeneutics/README.md`
- `docs/primary-sources/ontology-and-taxonomy.md`
- `docs/governance/doctrine-constitution.md`

## Summary rule

Phase 2 is successful when the repository can move from source to interpretation to doctrine without collapsing those layers into one object.
