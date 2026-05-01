---
object_type: scoring_model
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: signal_scoring_guidance
provenance_note: "Created 2026-05-01 as a draft scoring model for frontier signals."
reason_for_inclusion: "Create a consistent way to rank frontier signals by relevance, risk, urgency, and impact before routing them into repo work."
---

# Signal Scoring Model

## Score fields

Use 0-5 unless otherwise specified.

| Field | Meaning |
|---|---|
| novelty | How new or unexpected the signal is. |
| relevance_to_logos | How directly it affects Logos architecture, theology, source policy, graph/RAG, or governance. |
| verification_quality | Whether the signal is supported by official sources, peer review, formal proof, replication, or trusted evidence. |
| source_quality | Quality of the source channel. |
| impact_radius | Number and importance of repo surfaces affected. |
| urgency | How quickly action is needed. |
| risk_if_wrong | Harm if the signal is false or misapplied. |
| rights_or_license_risk | Copyright, license, privacy, or source boundary risk. |
| theological_profile_risk | Risk of drifting from declared theological profile or source hierarchy. |
| agentic_risk | Risk if implemented as an agent/skill/tool/runtime workflow. |

## Derived classification

| Total posture | Recommended action |
|---|---|
| low signal / high uncertainty | watch |
| medium signal / bounded impact | staged research |
| high signal / high impact | governance bridge or roadmap |
| high signal / source-rights impact | source registry review |
| high signal / validation impact | validation infra follow-up |
| high signal / agentic risk | agent-skill review and threat model |

## Required output

Every scored signal should produce:

- score summary;
- reasoning;
- recommended route;
- impacted files/surfaces;
- owner role;
- next action;
- stop conditions.
