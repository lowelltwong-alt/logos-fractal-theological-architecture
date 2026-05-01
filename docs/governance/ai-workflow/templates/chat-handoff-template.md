---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: chat_handoff
---

# Chat Handoff Template

## Settings

- Reasoning effort: medium
- Internet: off unless source verification is required
- Permissions: conservative
- Mode: Plan

## Required scope

Use this route when turning chat output, assistant-generated research, or conversation planning into repo-safe instructions or staged packets.

## Required prompt fields

- Target branch:
- PR title:
- Chat/source material summarized:
- Intended repo destination:
- Trust zone:
- Non-goals:
- Validation expected:

## Required work

Convert chat material into a scoped handoff, staged research packet, prompt, or roadmap. Preserve uncertainty and source boundaries.

## Forbidden

Do not silently promote chat output into doctrine, claims, graph objects, source registry truth, or ingestion outputs. Do not include private or protected source text.

## Required PR note

State that the PR converts chat material into staged or planning form and does not promote it into higher-trust repo surfaces unless separately routed.
