---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: source_registry
---

# Source Registry Template

## Settings

- Reasoning effort: xhigh
- Internet: on only for source or license verification
- Permissions: conservative
- Mode: Edit

## Required scope

Use this route for source registries, source templates, Bible source metadata, public-domain/open-license candidates, or private connector manifest policy.

## Required prompt fields

- Target branch:
- PR title:
- Source category:
- Registry files touched:
- Rights or license status:
- Source verification plan:
- Non-goals:
- Validation expected:

## Required work

Create metadata and registry structures before any ingestion. Mark candidates as review-required unless the source status is already verified in the repo.

## Forbidden

Do not add source text, chunks, embeddings, protected modern translations, modern theology text, or proprietary lexicon material.

## Required PR note

State whether the PR adds metadata only or changes a source-use boundary. State that no source text was ingested unless explicitly routed as ingestion.
