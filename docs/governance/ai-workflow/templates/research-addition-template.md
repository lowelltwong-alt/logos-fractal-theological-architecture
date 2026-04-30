---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: research_addition
---

# Research Addition Template

## Settings

- Reasoning effort: medium
- Internet: off unless source verification is required
- Permissions: conservative
- Mode: Edit

## Required scope

Use this route for staged research additions from chat, uploaded files, public source synthesis, or internal planning notes.

Default allowed path: `incoming/research/`.

## Required prompt fields

- Target branch:
- PR title:
- Source family:
- Source status:
- Trust zone: incoming_research
- Non-goals:
- Validation expected:

## Required work

Create a staged research packet with metadata/provenance. Keep the material draft, unreviewed, and not automatically promoted.

## Forbidden

Do not create doctrine nodes, concept nodes, claim objects, graph objects, schemas, validators, runtime agents, or source ingestion outputs.

Do not add protected modern source text or private corpus material.

## Required PR note

State that the PR adds staged incoming research only and does not promote the material into governed doctrine, concepts, claims, graphs, or ingestion outputs.
