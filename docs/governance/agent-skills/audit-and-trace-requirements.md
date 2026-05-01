---
object_type: audit_policy
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: agent_skill_audit_guidance
provenance_note: "Created 2026-05-01 as the audit and trace policy for future agent and skill usage."
reason_for_inclusion: "Define audit expectations for future agent/skill prompts, outputs, model settings, tool use, approvals, and review results."
---

# Audit and Trace Requirements

## Audit levels

| Level | Use |
|---|---|
| 0 | PR disclosure only. |
| 1 | Prompt summary and output summary. |
| 2 | Redacted prompt/output artifact. |
| 3 | Full governed run ledger after schema/privacy policy approval. |

## Minimum audit floor by capability class

The level below is a floor. A card may declare a higher level. It may not declare a lower one.

| Capability class | Minimum audit level |
|---|---|
| trivial formatting / shape-only edits | 0 |
| read-only summarization of repo-internal content | 1 |
| staged research / source monitoring | 1 |
| frontier signal monitoring / scoring | 1 |
| concept or doctrine support | 2 |
| source license review | 2 |
| claim candidate review | 2 |
| graph relationship review | 2 |
| validator or schema support | 2 |
| theological drift detection | 2 |
| prompt-injection or security review | 2 |
| orchestrator support | 2 |
| runtime planning | 2 |
| runtime execution / side effects (future) | 3 |

Composition raises the floor to the maximum of its parts (see `unsafe-composition-review-checklist.md`).

High-risk classes cannot be downsampled or aggregated below their floor (see `swarm-scale-failure-modes.md`).

## High-risk usage

High-risk skills require stronger audit when they touch:

- doctrine;
- concepts;
- claims;
- graph objects;
- source registry;
- Bible/source licensing;
- schemas/validators;
- tool permissions;
- runtime agents;
- theological profile boundaries.

## Do not capture

Do not capture secrets, credentials, private licensed source text, protected Bible/theology text, proprietary lexicons, privileged material, sensitive personal data, or raw private chats without redaction and approval.

## Tamper-evidence and retention

Audit records are append-only at the docs/governance level. Edits to past records require a new entry and a pointer to the prior entry rather than in-place rewrite.

Retention follows the run-ledger policy and source/privacy boundaries. Retention shorter than the policy floor requires owner approval; retention longer than the floor must respect privacy and source-rights boundaries.

Audit silencing, sampling below the floor, or aggregation that hides high-risk events is forbidden (see `swarm-scale-failure-modes.md`).
