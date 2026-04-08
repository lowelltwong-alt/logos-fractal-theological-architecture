---
id: governance.trust_zone_normalization_migration_rule
anchor: governance-trust-zone-normalization-migration-rule
title: Trust-zone normalization migration rule
node_type: governance_policy_note
status: active
review_status: review_pending
address: docs.governance.trust-zone-normalization-migration-rule
trust_zone: canonical
lifecycle_state: active
ai_usage_posture: ai_assist_human_review
object_type: governance_migration_note
lifecycle_status: active
provenance_note: "Created on 2026-04-08 during trust-zone controlled-vocabulary normalization across docs, claims, and retrieval records."
reason_for_inclusion: "Document deterministic migration behavior for invalid trust_zone values so future normalization is consistent and reviewable."
---

# Trust-zone normalization migration rule

## Rule

When a record contains a non-enum `trust_zone` value, normalize it to the nearest allowed trust zone.

Default mapping rule:
- `working_proposed` -> `proposed`

Use a stricter zone only when there is explicit governance justification in the change set.

## Rationale

The repository uses a controlled trust-zone vocabulary to preserve retrieval consistency, graph integrity, and governance legibility.

Legacy aliases such as `working_proposed` create vocabulary drift and must be normalized before validation and CI checks run.

## Scope

This migration rule applies to:
- markdown frontmatter under `docs/`
- YAML claim records under `data/claims/`
- YAML retrieval neighborhood records under `data/retrieval/`
