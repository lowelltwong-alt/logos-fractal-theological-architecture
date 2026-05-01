---
object_type: research_note
trust_zone: incoming_research
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: staged_research_only
provenance_note: "Created 2026-05-01 as staged research for model-agnostic agent routing."
reason_for_inclusion: "Capture how future agents and skills should map to Claude, Codex, OpenAI-style agents, other frontier models, and local/free models without vendor lock-in."
---

# Model-Agnostic Agent Routing

## Principle

Capabilities are governed before tools.

## Routes by risk

- local/free model: formatting, simple summaries, tag suggestions, duplicate candidates;
- mid-tier model: staged research drafts and low-risk analysis;
- frontier model: governance, theological synthesis, source policy, claims, graphs, validators;
- human review: all high-impact outputs.

## Adapter families

- Claude Code subagent;
- Claude Skill;
- Codex workflow;
- OpenAI-style agent;
- local model runner;
- future frontier model runner.

Adapters must preserve registry constraints.
