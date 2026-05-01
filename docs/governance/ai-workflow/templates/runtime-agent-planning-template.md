---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: runtime_agent_planning
---

# Runtime Agent Planning Template

## Settings

- Reasoning effort: xhigh
- Internet: off unless official tool documentation is required
- Permissions: conservative
- Mode: Plan

## Required scope

Use this route for planning future agents, tool registries, hooks, approval gates, run ledgers, connector boundaries, and execution controls.

## Required prompt fields

- Target branch:
- PR title:
- Runtime/control-plane topic:
- Planning-only boundary:
- Source materials inspected:
- Non-goals:
- Validation expected:

## Required work

Create planning documents or staged research only. Keep knowledge plane, control plane, and execution plane separated.

## Forbidden

Do not create executable agents, `.claude/agents`, external side effects, runtime tool registries, approval runtime code, or connector code unless explicitly authorized in a separate execution route.

## Required PR note

State that the PR is planning-only and does not create active runtime behavior.
