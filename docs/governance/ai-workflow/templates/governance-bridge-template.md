---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: governance_bridge
---

# Governance Bridge Template

## Settings

- Reasoning effort: high
- Internet: off unless official documentation is required
- Permissions: conservative
- Mode: Edit

## Required scope

Use this route to promote staged research into governed reference, vocabulary, or policy documents.

Default allowed paths: `docs/governance/` and `docs/roadmap/`.

## Required prompt fields

- Target branch:
- PR title:
- Staged research source:
- Target governed document:
- Trust zones touched:
- Non-goals:
- Validation expected:

## Required work

Create a human-readable governed bridge that preserves source boundaries and explains what the bridge may and may not influence.

## Forbidden

Do not create claim objects, graph objects, runtime agents, validators, source text ingestion, or new schema unless explicitly routed separately.

## Required PR note

State that the PR promotes staged research only into a governed bridge/reference surface and does not make it canonical doctrine, claim data, or graph truth.
