---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: source_document_integration_map
---

# Source Document Integration Map Template

## Settings

- Reasoning effort: medium
- Internet: off
- Permissions: conservative
- Mode: Edit

## Required scope

Use this route to map source packets, research families, uploaded document families, and existing repo workstreams.

Default allowed path: `docs/roadmap/`.

## Required prompt fields

- Target branch:
- PR title:
- Source families to inspect:
- Expected output file:
- Non-goals:
- Validation expected:

## Required work

Create a map that identifies each source family, repo location, what it informs, what it must not be used for, trust zone, promotion path, and next recommended action.

## Forbidden

Do not copy full source documents. Do not promote claims. Do not create graph objects. Do not ingest Bible text. Do not activate counseling or runtime agents.

## Required PR note

State that the PR improves source navigation and routing without changing doctrine, claims, graph data, or source ingestion policy unless explicitly included in scope.
