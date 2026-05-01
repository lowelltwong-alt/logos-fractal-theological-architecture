---
object_type: card_model
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: agent_skill_card_guidance
provenance_note: "Created 2026-05-01 as the required future metadata model for agent and skill cards."
reason_for_inclusion: "Define mandatory fields for future agent/skill cards before creating real registry data, schemas, or runtime agents."
---

# Agent / Skill Card Model

## Required fields

- skill_id
- name
- type
- status
- trust_zone
- owner
- model_policy
- doctrinal_profile_boundary
- inputs
- outputs
- allowed_tools
- forbidden_tools
- side_effect_level
- required_permissions
- source_boundaries
- reasoning_effort_default
- internet_default
- validation_required
- routes_supported
- related_skills
- depends_on
- improves
- supersedes
- risk_level
- audit_capture_level
- last_reviewed

## Type values

Candidate types:

- prompt_template
- codex_workflow
- claude_skill
- claude_subagent
- openai_agent
- local_model_runner
- monitoring_agent
- orchestrator
- validator
- retrieval_route
- renderer
- source_monitor
- governance_reviewer

## Status values

- proposed
- experimental
- active
- deprecated
- retired

## Model policy

Each card should specify:

- allowed_model_classes;
- disallowed_model_classes;
- local_model_allowed;
- frontier_model_required;
- human_review_required;
- model_vendor_binding, if any.

Default should be model-agnostic.

## Doctrinal profile boundary

Every theological or source-facing skill must say which profile it operates under.

Examples:

- conservative_evangelical_primary
- source_policy_only
- tradition_scoped_comparison
- historical_contrast_only
- no_theological_assertion

Hidden profile drift is a stop condition.
