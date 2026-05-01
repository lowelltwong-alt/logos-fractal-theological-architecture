---
object_type: governance_reference
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: agent_skill_registry_guidance
provenance_note: "Created 2026-05-01 as the index for Agent/Skill Capability Registry governance."
reason_for_inclusion: "Define the governance entry point for future agents, skills, subagents, monitors, orchestrators, capability tags, graph edges, ownership, cadence, audit, and anti-drift review."
---

# Agent / Skill Capability Registry

This folder governs future agents, subagents, skills, monitors, orchestrators, prompt workflows, and model-specific implementations.

## Core rule

The registry is the source of truth. Tool-specific files are adapters.

Examples of tool-specific adapters:

- Claude Code project subagents;
- Claude Skills;
- Codex prompts/workflows;
- OpenAI-style agents;
- other frontier-model agents;
- local/free model task runners.

Do not create tool-specific runtime agent files before registry and review policy exist.

## Why this exists

If the system eventually has thousands of agents or skills, a prompt folder will become chaotic.

The registry should support:

- discovery;
- ownership;
- allowed/forbidden tools;
- source boundaries;
- doctrinal profile boundaries;
- theological drift review;
- composition safety;
- duplicate detection;
- skill merging;
- orchestrator notification;
- audit and trace requirements;
- generated derived indexes and GraphRAG summaries.

## Theological drift boundary

Agents and skills must preserve the declared theological/source profile of Logos.

This is not a ban on studying other traditions. It is a ban on hidden or unapproved drift from the declared profile, source hierarchy, and review gates.

Tradition-scoped or contrastive work must be labeled as such.

## Hardening surfaces

These docs harden specific failure surfaces and apply to every card, adapter, monitor, orchestrator, or composed skill:

- `safety-controls-floor.md` — minimum non-negotiable safety controls.
- `theological-profile-drift-review-checklist.md` — diff-of-defaults and drift cadence.
- `local-and-free-model-boundary-policy.md` — what local and free-tier models may not do alone.
- `unsafe-composition-review-checklist.md` — review checklist for composed skills.
- `swarm-scale-failure-modes.md` — failure modes that emerge at registry scale.

If any hardening doc imposes a stricter rule than another file, the stricter rule wins.
