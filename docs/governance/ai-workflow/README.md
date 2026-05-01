---
object_type: governance_reference
trust_zone: proposed
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: contributor_guidance_only
provenance_note: "Created 2026-04-30 as the index for the AI-assisted work routing control plane."
---

# AI Workflow Governance

This folder defines how AI-assisted work is routed, scoped, validated, and submitted in this repository.

It is the control-plane layer for tools such as Codex, Claude Code, ChatGPT, Claude chat, Cursor, Copilot-style tools, and future agentic systems.

## Start here

All AI-assisted work begins at the root file:

- `AI_WORK_START_HERE.md`

Then use:

- `ai-work-cycle.md` for the required cycle.
- `ai-routing-algorithm.md` for route selection.
- `ai-task-route-table.yaml` for task-to-template mapping.
- `ai-tool-settings-matrix.md` for reasoning, internet, and permission settings.
- `universal-prompt-header.md` for reusable prompt headers.
- `stop-conditions.md` for mandatory stop rules.
- `validation-and-pr-requirements.md` for PR expectations.
- `clean-room-and-source-boundaries.md` for source-use boundaries.
- `templates/` for route-specific prompt templates.
- `tool-configs/` for tool-specific guidance.

## Core rule

AI work must be routed before it edits files.

The route determines:

- work mode;
- allowed paths;
- forbidden actions;
- reasoning effort;
- internet posture;
- permission posture;
- validation requirements;
- PR governance content.

## Router update rule

This router is a living artifact. If a PR changes how AI work should be done, the router must be reviewed and updated in the same PR or a listed follow-up PR.
