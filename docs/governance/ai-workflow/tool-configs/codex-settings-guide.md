---
object_type: tool_settings_guide
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: contributor_guidance_only
tool: codex
---

# Codex Settings Guide

## Default settings

- Reasoning effort: match route risk.
- Internet: off unless route requires current official docs or source/license verification.
- Permissions: conservative.
- Detail level: coding or detailed when available.
- Prevent sleep or long-running task option: on for large repo tasks when available.

## Reasoning effort

- medium: maps, staged research, route docs, roadmap updates.
- high: governance bridges, concepts, profile cards, policy docs.
- xhigh: schemas, validators, source registries, claim objects, graph objects, ingestion, runtime planning, CI.

## Required startup

Paste the universal prompt header or equivalent. Codex must follow `AGENTS.md`, `AI_WORK_START_HERE.md`, and the route table before editing.

## Internet use

Codex should not browse by default. Enable internet only for official tool docs, source/license status, or current facts needed for the task.

## Stop posture

Codex should stop rather than repair automatically when local state is dirty, a branch is divergent, validation fails unexpectedly, source rights are unclear, or the route is ambiguous.
