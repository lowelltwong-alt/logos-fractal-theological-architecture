---
object_type: watch_policy
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: ai_capability_watch_guidance
provenance_note: "Created 2026-05-01 as a draft policy for monitoring AI capability and tool changes."
reason_for_inclusion: "Define how model/tool capability shifts should be tracked and routed while preserving model-agnostic governance and conservative permissions."
---

# AI Capability Watch Policy

## Purpose

Track AI tool and model changes that may affect Logos work.

Examples:

- Codex-style coding agents;
- Claude Code subagents and Skills;
- OpenAI-style agents and handoffs;
- local or free models for low-risk tasks;
- new context windows;
- new tool-use capabilities;
- new retrieval or graph reasoning;
- new safety or permission mechanisms.

## Model-agnostic rule

The repo should define capabilities, routes, trust zones, owners, tools, permissions, and audit requirements independently of any one model vendor.

Tool-specific implementation files should be adapters, not source of truth.

## Model routing posture

| Work type | Default model posture |
|---|---|
| low-risk formatting / summarization | small/local/cheap model allowed |
| staged research summary | medium model allowed, source-sensitive |
| governance, doctrine, source policy | strong model + human review |
| claims, graph objects, schemas, validators | strongest available model + human review |
| runtime agents / side effects | plan-first, approval-gated, no autonomous mutation |

## Hard boundary

Do not grant tools or mutate repo policies merely because a new model can do more.
