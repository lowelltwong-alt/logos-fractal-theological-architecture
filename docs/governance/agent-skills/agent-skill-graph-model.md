---
object_type: graph_model
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: agent_skill_graph_guidance
provenance_note: "Created 2026-05-01 as the graph model for future agent and skill relationships."
reason_for_inclusion: "Define how agent/skill relationships should be represented and reviewed before graph data or runtime orchestration exists."
---

# Agent / Skill Graph Model

## Purpose

The skill graph helps discover, compose, audit, and govern many capabilities.

## Edge families

- dependency edges;
- improvement edges;
- composition edges;
- conflict edges;
- orchestration edges;
- review edges;
- drift-risk edges;
- duplicate and merge candidate edges.

## Important rule

Skill graph edges are not permission grants.

A graph edge may recommend discovery or review, but tool permissions and runtime behavior require separate approval.

## Composition risk

Two individually aligned skills may compose into a misaligned behavior.

Any new composed agent/skill must be treated as a new object requiring review.

Composition must check:

- source boundaries;
- doctrinal profile boundary;
- side-effect level;
- tool permissions;
- audit capture level;
- orchestrator routing;
- owner approval.
