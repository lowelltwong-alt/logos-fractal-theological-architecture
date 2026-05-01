---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: validation_infra
---

# Validation Infrastructure Template

## Settings

- Reasoning effort: xhigh
- Internet: off unless official tool documentation is required
- Permissions: conservative
- Mode: Edit

## Required scope

Use this route for schemas, validators, scripts, workflow checks, PR templates, and CI changes.

## Required prompt fields

- Target branch:
- PR title:
- Validation surface touched:
- Existing workflow/scripts inspected:
- Expected failure mode fixed:
- Non-goals:
- Validation expected:

## Required work

Make the smallest possible validator, schema, or workflow change. Preserve existing validation style and do not rewrite the validation system unless explicitly requested.

## Forbidden

Do not change theology, source packets, doctrine, concepts, claims, graph data, or ingestion content except to fix metadata required by validation.

## Required PR note

State which validation surface changed, what failure mode it addresses, and how it avoids broad validator drift.
