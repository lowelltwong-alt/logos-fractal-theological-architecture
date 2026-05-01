---
object_type: edge_vocabulary
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: agent_skill_edge_vocabulary_guidance
provenance_note: "Created 2026-05-01 as the initial typed edge vocabulary for future agent/skill graph relationships."
reason_for_inclusion: "Prevent generic or ambiguous agent/skill relationships by defining typed edges before registry graph data is created."
---

# Agent / Skill Edge Vocabulary

## Candidate edges

| Edge | Meaning |
|---|---|
| depends_on | Skill requires another skill or route. |
| supersedes | Skill replaces an older skill. |
| improves | Skill makes another skill better or safer. |
| composes_with | Skill can combine with another skill after review. |
| conflicts_with | Skill should not be used together with another skill. |
| requires_review_by | Skill requires owner or role review. |
| routes_to | Skill supports a route. |
| monitors | Skill watches a signal, source, or process. |
| generates | Skill produces a defined output. |
| validates | Skill checks or validates an output. |
| duplicate_candidate | Skill may duplicate another skill. |
| merge_candidate | Skill may be merged with another skill. |
| derivative_of | Skill derives from another skill. |
| theological_drift_risk_with | Skill combination may drift from declared theological profile. |
| unsafe_composition_with | Skill combination may create unsafe behavior. |

## Forbidden edge

Do not use generic `related_to` for agent/skill graph relationships.
