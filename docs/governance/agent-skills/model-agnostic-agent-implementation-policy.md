---
object_type: implementation_policy
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: model_agnostic_agent_guidance
provenance_note: "Created 2026-05-01 as a draft model-agnostic implementation policy for future agents and skills."
reason_for_inclusion: "Ensure future agents and skills are governed by capabilities, routes, permissions, and audit requirements rather than being locked to a single model vendor or tool ecosystem."
---

# Model-Agnostic Agent Implementation Policy

## Principle

Define capabilities first. Bind to tools later.

The same registry card may later map to:

- Claude Code subagent;
- Claude Skill;
- Codex workflow;
- OpenAI-style agent;
- Cursor/Copilot-style assistant;
- local model runner;
- future frontier model agent.

## Model routing

| Risk class | Model posture |
|---|---|
| trivial formatting | local/free/small model allowed |
| read-only summary | local/cheap model allowed if source boundaries are safe |
| source-sensitive research | stronger model or human review recommended |
| theology/governance | stronger model and human review |
| claims/graphs/schemas/validators | strongest available model and human review |
| runtime side effects | explicit approval, regardless of model |

## Local/free model lane

Local or free models are useful for:

- formatting;
- file classification;
- tag suggestions;
- duplicate detection candidates;
- summarization drafts;
- non-sensitive outline generation.

They should not autonomously decide doctrine, claims, graph edges, source licensing, or runtime permissions.

## Tool-specific adapters

Tool-specific implementations must preserve the registry card's constraints.

If a tool cannot express the required constraints, it should not implement that skill without a wrapper or additional review.
