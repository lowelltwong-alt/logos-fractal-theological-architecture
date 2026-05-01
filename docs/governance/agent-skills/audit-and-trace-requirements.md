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
