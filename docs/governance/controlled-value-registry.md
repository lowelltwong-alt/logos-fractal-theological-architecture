---
id: governance.controlled_value_registry
anchor: governance-controlled-value-registry
title: Controlled value registry
node_type: governance_policy
status: active
review_status: review_pending
address: docs.governance.controlled-value-registry
trust_zone: canonical
lifecycle_state: active
ai_usage_posture: ai_assist_human_review
object_type: repository_governance_contract
lifecycle_status: active
provenance_note: "Created on 2026-04-08 during controlled-vocabulary normalization pass."
reason_for_inclusion: "Define canonical bounded vocabularies and migration aliases so validators and templates enforce the same value spaces."
---

# Controlled Value Registry

This registry is the canonical bounded-value source for governance-controlled fields.

## Controlled fields

### `trust_zone`
Allowed values:
- `canonical`
- `tradition-scoped`
- `proposed`
- `inferred`
- `deprecated`
- `learning-sidecar`

Migration aliases (must be normalized before validation):
- `core_trusted` -> `canonical`
- `reviewed_specialized` -> `tradition-scoped`
- `working_proposed` -> `proposed`
- `boundary_restricted` -> `learning-sidecar`
- `experimental_graph` -> `inferred`

### `lifecycle_status`
Allowed values:
- `draft`
- `active`
- `deprecated`
- `superseded`
- `archived`

## Enforcement scope

Validators must enforce membership for:
- Markdown frontmatter across the `docs` tree
- YAML governed records under `data` and `examples`
- JSON templates under `data/graph/templates`

## CI requirement

Controlled-value violations are merge-blocking and must emit a machine-readable report with `path`, `field`, `value`, and `message` for each violation.
