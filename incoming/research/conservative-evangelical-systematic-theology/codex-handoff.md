---
object_type: codex_handoff
trust_zone: incoming_research
lifecycle_status: draft
provenance_note: "Created 2026-04-30 for Codex to stage conservative evangelical source-spine and Bible licensing policy work."
reason_for_inclusion: "Give Codex an exact implementation sequence without allowing copyrighted source ingestion."
review_status: unreviewed
ai_usage_posture: staging_only_not_auto_promote
---

# Codex Handoff: Conservative Evangelical Source Spine

## Branch

Use `docs/conservative-evangelical-source-spine`.

Start from live `main` after the standard AGENTS.md live-main sync protocol.

## Goal

Stage a conservative evangelical source spine and Bible ingestion policy without importing copyrighted source text.

## Files added

- `docs/roadmap/conservative-evangelical-source-spine.md`
- `docs/governance/bible-source-and-licensing-policy.md`
- `incoming/research/conservative-evangelical-systematic-theology/README.md`
- `incoming/research/conservative-evangelical-systematic-theology/grudem-source-profile.md`
- `incoming/research/conservative-evangelical-systematic-theology/conservative-theologian-anchor-map.md`
- `incoming/research/conservative-evangelical-systematic-theology/bible-ingestion-raggraph-plan.md`
- `incoming/research/conservative-evangelical-systematic-theology/licensing-boundary-notes.md`
- `incoming/research/conservative-evangelical-systematic-theology/copyright-safe-source-options.md`
- `incoming/research/conservative-evangelical-systematic-theology/codex-handoff.md`

## Do not add

- full Bible text;
- full Grudem text;
- full modern theology books;
- protected modern Bible chunks;
- protected-source embeddings;
- proprietary lexicon data;
- claim objects;
- graph objects;
- validators;
- runtime agents.

## Key rule

This PR is a governance and planning PR. It prepares a future source registry and ingestion path. It does not ingest a corpus.

## PR title

`Seed conservative evangelical source spine and Bible licensing policy`

## Validation

Run the existing repo validation workflows or the scripts referenced in the repo workflows.
