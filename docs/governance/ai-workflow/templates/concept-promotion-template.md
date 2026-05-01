---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: concept_promotion
---

# Concept Promotion Template

## Settings

- Reasoning effort: high
- Internet: off
- Permissions: conservative
- Mode: Edit

## Required scope

Use this route to promote staged research into concept or doctrine node files.

Default allowed paths: `docs/concepts/` and `docs/doctrine/`.

## Required prompt fields

- Target branch:
- PR title:
- Source research packet:
- Concepts or doctrine nodes touched:
- Existing files inspected:
- Trust zones touched:
- Non-goals:
- Validation expected:

## Required work

Inspect existing concept and doctrine files before creating new nodes. Avoid duplicates. Preserve existing naming and metadata conventions.

## Forbidden

Do not create claim objects or graph objects. Do not add counseling content unless explicitly routed. Do not create source-ingestion outputs.

## Required PR note

State which staged research informed the promoted concept or doctrine node and whether any existing node was audited instead of duplicated.
