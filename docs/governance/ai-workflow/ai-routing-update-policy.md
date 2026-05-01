---
object_type: routing_update_policy
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: mandatory_router_maintenance_policy
provenance_note: "Created 2026-04-30 to require updates to AI routing whenever repository process or trust boundaries change."
reason_for_inclusion: "Require the AI routing algorithm, route table, templates, and settings guidance to be reviewed whenever repository changes affect AI-assisted work classification, prompting, validation, source boundaries, or governance process."
---

# AI Routing Update Policy

The AI routing algorithm is a living control-plane artifact.

Any change that affects how AI-assisted work should be classified, scoped, validated, prompted, or submitted must update the router in the same PR or identify a follow-up PR.

## Mandatory PR question

Every PR should answer:

Does this PR affect AI work routing?

- No.
- Yes, updated AI_WORK_START_HERE.md, route table, settings matrix, or templates.
- Yes, follow-up PR required and listed.

## Path triggers

Review the router when a PR changes any of these paths:

- `AGENTS.md`
- `AI_WORK_START_HERE.md`
- `AI_FRONT_DOOR.md`
- `docs/governance/**`
- `docs/roadmap/**`
- `docs/governance/ai-workflow/**`
- `.github/workflows/**`
- `.github/pull_request_template.md`
- `schemas/**`
- `scripts/**`
- `data/claims/**`
- `data/graph/**`
- `data/relationships/**`
- `data/source-registry/**`
- `docs/concepts/**`
- `docs/doctrine/**`
- `incoming/research/**` when a new source family or task route is introduced

## Semantic triggers

Review the router when a PR introduces or changes:

- trust zones;
- lifecycle statuses;
- source types;
- source-ingestion policy;
- validation rules;
- schemas;
- claim object types;
- graph relationship types;
- route templates;
- AI tool settings;
- internet-use rules;
- copyright or source boundaries;
- PR governance requirements;
- branch protection expectations;
- CODEOWNERS expectations;
- counseling workflows;
- agent workflows;
- Bible workflows;
- source-registry workflows;
- claim workflows;
- graph workflows.

## Update surfaces

If routing is affected, update one or more of:

- `AI_WORK_START_HERE.md`
- `docs/governance/ai-workflow/ai-routing-algorithm.md`
- `docs/governance/ai-workflow/ai-task-route-table.yaml`
- `docs/governance/ai-workflow/ai-tool-settings-matrix.md`
- relevant route templates under `docs/governance/ai-workflow/templates/`
- relevant tool guide under `docs/governance/ai-workflow/tool-configs/`

## Same PR vs follow-up PR

Update in the same PR when the route impact is small and obvious.

Use a follow-up PR when the route impact is broad, cross-cutting, or would distract from a risky schema/claim/graph/ingestion change.

If a follow-up PR is required, the original PR must name the follow-up branch and scope.

## Non-bypass rule

Do not bypass the router because the change is urgent. If the work changes AI process, record the process impact.
