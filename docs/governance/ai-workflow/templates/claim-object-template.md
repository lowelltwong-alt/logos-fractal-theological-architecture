---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: claim_object
---

# Claim Object Template

## Settings

- Reasoning effort: xhigh
- Internet: off unless source-status verification is required
- Permissions: conservative
- Mode: Edit

## Required scope

Use this route for machine-readable claim objects.

Default allowed path: `data/claims/`.

## Required prompt fields

- Target branch:
- PR title:
- Claim candidates:
- Source basis:
- Concept/doctrine basis:
- Schema or pattern inspected:
- Trust zones touched:
- Non-goals:
- Validation expected:

## Required work

Use existing claim object patterns and schemas. Keep claims proposed/draft unless the repo pattern says otherwise. Every claim must have source basis, scope, provenance, review status, and downstream limitation notes.

## Forbidden

Do not create unsupported claims. Do not create graph objects. Do not treat inferred material as asserted. Do not use protected source text as evidence.

## Required PR note

State why each claim is ready for proposal and what upstream concept/doctrine/source basis supports it.
