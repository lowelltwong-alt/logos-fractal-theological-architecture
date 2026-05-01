---
object_type: threat_model
trust_zone: incoming_research
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: staged_threat_model_only
provenance_note: "Created 2026-05-01 as a staged threat model for misaligned agents and theological-profile drift."
reason_for_inclusion: "Capture risks from intentionally misaligned agents, accidental composition failures, hidden source-profile shifts, and unapproved theological drift."
---

# Anti-Drift Threat Model

## Threats

- intentionally misaligned agent;
- hidden prompt injection in a skill;
- overly broad tool inheritance;
- unreviewed source hierarchy change;
- hidden theological profile change;
- unsafe composition of two individually acceptable skills;
- agent-generated agent with no card;
- local model producing unreviewed theological default;
- prompt/output capture leaking protected material;
- runtime skill changing route behavior.

## Mitigations

- card metadata required;
- owner required;
- model policy required;
- allowed/forbidden tools required;
- doctrinal profile boundary required;
- audit capture level required;
- composition review required;
- orchestrator impact assessment required;
- no hidden runtime agent creation;
- no tool-specific implementation before registry review.
