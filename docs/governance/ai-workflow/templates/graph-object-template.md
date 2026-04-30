---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: graph_object
---

# Graph Object Template

## Settings

- Reasoning effort: xhigh
- Internet: off
- Permissions: conservative
- Mode: Edit

## Required scope

Use this route for graph objects, relationship objects, or typed relationship data.

Default allowed paths: `data/graph/` and `data/relationships/`.

## Required prompt fields

- Target branch:
- PR title:
- Relationship vocabulary used:
- Source or claim basis:
- Graph object pattern inspected:
- Trust zones touched:
- Non-goals:
- Validation expected:

## Required work

Use approved relationship vocabulary. Every edge must have provenance, direction, source, target, relationship type, review status, and assertion mode.

## Forbidden

Do not use generic `related_to`. Do not create unsupported edges. Do not represent inferred material as asserted. Do not create graph objects before vocabulary and claim/source basis exist.

## Required PR note

State relationship vocabulary used, basis for each relationship, and why graph promotion is appropriate.
