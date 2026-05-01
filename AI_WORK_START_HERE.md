---
object_type: ai_work_entry_point
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: mandatory_routing_entry_point
provenance_note: "Created 2026-04-30 as the operational entry point for AI-assisted repository work."
---

# AI Work Start Here

This is the required operational entry point for Codex, Claude Code, ChatGPT, Claude chat, Cursor, Copilot-style tools, and future AI-assisted contributors working on this repository.

## Required reading order

1. Read `AGENTS.md`.
2. Read this file.
3. Read `docs/governance/ai-workflow/ai-routing-algorithm.md`.
4. Select the route from `docs/governance/ai-workflow/ai-task-route-table.yaml`.
5. Use the matching route template in `docs/governance/ai-workflow/templates/`.
6. Use the tool settings guidance in `docs/governance/ai-workflow/ai-tool-settings-matrix.md`.

## Mandatory cycle

Every AI-assisted task follows this cycle:

1. Orient.
2. Sync safely.
3. Classify the task.
4. Choose mode: Explore, Plan, Edit, or Execute.
5. Choose tool settings.
6. Choose the route template.
7. Work only inside the declared scope.
8. Run validation.
9. Open a PR with required governance sections.
10. Report outcome.
11. Check whether the router itself needs updating.

## Live-main rule

Treat live `origin/main` as the source of truth for new work. Fetch, fast-forward local `main` only, and branch from updated `main`.

If local state is dirty, divergent, ambiguous, or the target branch already exists, stop and report before editing.

Never reset, rebase, force-push, delete, discard, or overwrite local work unless explicitly instructed.

## Default posture

Default to read-only Explore or Plan unless the task explicitly authorizes edits.

Default internet access to off unless the task requires source, license, legal, public documentation, or current tool-behavior verification.

Default permissions to conservative.

## Router update check

Every PR must answer whether it affects AI work routing. If it changes trust zones, source policies, schemas, validators, claim objects, graph objects, ingestion policy, tool settings, templates, or PR governance, the router must be reviewed and updated in the same PR or a listed follow-up PR.

## Hard boundaries

Do not ingest protected modern Bible translations, modern theology books, proprietary lexicons, private source chunks, private embeddings, leaked code, private prompts, or leak-derived repositories.

Allowed clean-room lessons include mode separation, permissions, hooks, approval gates, auditability, source boundaries, and trust zones.
