---
object_type: decision_ledger_inference_sidecar
trust_zone: proposed
lifecycle_status: active
provenance_note: "Split from the canonical PR decision ledger on 2026-04-08 to quarantine inferred architecture-rule mappings pending review."
reason_for_inclusion: "Preserve uncertain PR-to-rule mappings while preventing inferred claims from remaining in canonical governance records."
---

# PR Decision Ledger Inferred Mappings (2026-04-08)

This sidecar contains inferred PR-to-rule mappings that require reviewer confirmation before promotion into canonical governance records.

## Inferred mapping queue

| Ledger ID | Merged PR | What changed | Inferred architecture rule touched | Current status |
|---|---|---|---|---|
| DL-PR-0007 | [#7](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/7) | Added overnight maintenance automation and logging patterns. | A1 trust-direction guardrails via validator usage. | proposed (mapping inference pending validation) |
| DL-PR-0011 | [#11](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/11) | Auto-generated retrieval neighborhood bundles. | Retrieval neighborhood model and canonical->derived direction. | proposed (mapping inference pending validation) |
| DL-PR-0015 | [#15](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/15) | Added semantic merge pipeline and drift artifacts. | Drift detection policy; deprecate-not-delete posture support. | proposed (mapping inference pending validation) |

## Promotion criteria

Promote an inferred mapping to canonical only after all are present:
- reviewer identity
- review timestamp
- explicit evidence from PR discussion or merged diff
- rationale that links evidence to a specific governance rule
- update to canonical ledger with sidecar reference retired or marked deprecated
