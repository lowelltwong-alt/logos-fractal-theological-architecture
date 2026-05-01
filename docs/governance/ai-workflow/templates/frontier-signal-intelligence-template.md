---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: frontier_signal_intelligence
provenance_note: "Created 2026-05-01 as the AI work route template for Frontier Signal Intelligence tasks."
reason_for_inclusion: "Define how AI tools should stage, score, and route high-leverage external signals without direct mutation."
---

# Frontier Signal Intelligence Template

## Settings

- Reasoning effort: high
- Internet: on only for official/public source verification
- Permissions: conservative
- Mode: Plan/Edit

## Required prompt fields

- Target branch:
- PR title:
- Signal classes:
- Sources to inspect:
- Expected output:
- Non-goals:
- Validation expected:

## Required work

Create or update docs-only signal monitoring, scoring, and routing surfaces.

## Forbidden

Do not create runtime monitors, schedulers, source ingestion, claim objects, graph objects, schemas, validators, autonomous repo mutation, or copyrighted source ingestion.

## Required PR note

State that this PR adds monitoring/routing governance only and does not grant runtime monitoring or mutation powers.
