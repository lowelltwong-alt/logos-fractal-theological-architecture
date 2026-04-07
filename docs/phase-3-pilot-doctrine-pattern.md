---
object_type: phase_definition
trust_zone: proposed
lifecycle_status: draft
provenance_note: "Created on 2026-04-06 to define the layer after the Trinity pilot object set."
reason_for_inclusion: "Make the architectural advantage visible by introducing explicit relationship objects around a pilot doctrine topic."
---

# Phase 3 - Pilot Doctrine Pattern

## Why Phase 3 exists

Phase 2 established source, interpretation, doctrine view, and doctrine assessment as separate object layers.

Phase 3 exists to make those layers visibly connected through explicit relationship objects, so maintainers can inspect the doctrinal network without collapsing topic, view, and judgment into a single node.

## Why relationship objects matter

Relationship objects turn implicit links into governed records.

They matter because each connection now has:

- its own identifier
- a relationship type
- a source and target
- independent lifecycle handling

That makes the structure auditable, extensible, and easier to review in small edits.

## The minimal pilot doctrine pattern

For one doctrine topic (`trinity`), the pilot pattern is:

1. one doctrine topic anchor
2. multiple doctrine views
3. baseline-scoped doctrine assessments
4. relationship objects for:
   - topic -> view (`has_view`)
   - view -> assessment (`assessed_by`)
   - view -> passage grounding (`grounded_in_passage`)
   - view -> view contrast (`contrasts_with`)
   - view -> view proximity (`neighboring_view`)
5. one network manifest that lists nodes and relationship objects together

## What users should now be able to see

Users should be able to see, at a glance:

- one topic holding multiple competing views
- Nicene and Arian views coexisting structurally
- rejection of Arianism expressed in assessment objects, not in the topic identity
- scriptural grounding attached to a specific view
- explicit contrast and neighboring-view links between views

## What Phase 3 does not yet do

Phase 3 does not yet provide:

- weighted coherence scoring across the network
- automated tension detection across many topics
- editor workflow automation for review and promotion
- large-scale comparative import beyond the pilot doctrine area

## Definition of done for Phase 3

Phase 3 is done when:

- Trinity pilot views are connected by explicit relationship objects
- at least one rejected view remains represented as a view object
- rejection status is carried by assessment objects under a baseline
- grounding, contrast, and neighboring-view relationships are present
- the pilot network is summarized in a single machine-readable manifest
