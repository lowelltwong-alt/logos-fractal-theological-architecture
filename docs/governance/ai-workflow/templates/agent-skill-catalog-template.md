---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: agent_skill_catalog
provenance_note: "Created 2026-05-01 as the AI work route template for Agent/Skill Catalog tasks."
reason_for_inclusion: "Define how AI tools should plan or update the agent/skill registry, capability graph, tags, owners, model policies, and anti-drift review surfaces."
---

# Agent / Skill Catalog Template

## Settings

- Reasoning effort: high
- Internet: off unless official tool documentation is required
- Permissions: conservative
- Mode: Plan/Edit

## Required prompt fields

- Target branch:
- PR title:
- Agent/skill scope:
- Model/tool ecosystem:
- Registry surfaces touched:
- Theological profile boundary:
- Non-goals:
- Validation expected:

## Required work

Create or update docs-only registry, card models, tag policies, edge vocabulary, owner routing, audit, and anti-drift policies.

## Model-agnostic rule

Do not bind governance to Claude, Codex, OpenAI, Anthropic, local models, or any single vendor.

Tool-specific files are adapters and require later review.

## Forbidden

Do not create runtime agents, `.claude/agents`, `.claude/skills`, schedulers, autonomous repo rewriting, unrestricted tool access, or tool-specific implementation files unless explicitly routed later.

## Required PR note

State whether this PR changes AI routing and whether it affects agent/skill governance, model policy, or theological drift safeguards.
