---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: ingestion_pilot
---

# Ingestion Pilot Template

## Settings

- Reasoning effort: xhigh
- Internet: on only for source and license verification
- Permissions: conservative
- Mode: Plan first, then Edit only if source policy permits

## Required scope

Use this route for public-domain or open-license source ingestion pilots.

## Required prompt fields

- Target branch:
- PR title:
- Source registry entry:
- License or rights status:
- Text scope:
- Chunking scope:
- Metadata sidecars:
- Non-goals:
- Validation expected:

## Required work

Verify source-use status before adding text. Start with a small pilot. Include source registry metadata, provenance, and chunk/sidecar rules before ingestion.

## Forbidden

Do not add protected modern Bible translations, modern theology book text, proprietary lexicon entries, private chunks, or embeddings without reviewed permission.

## Required PR note

State the source-use basis, exact corpus scope, whether text was added, and what ingestion gates were satisfied.
