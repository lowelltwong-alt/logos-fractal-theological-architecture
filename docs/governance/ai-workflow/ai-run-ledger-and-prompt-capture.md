---
object_type: governance_policy
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: prompt_audit_and_run_ledger_policy
provenance_note: "Created 2026-04-30 to define future prompt/input/output capture expectations for AI-assisted contributors."
---

# AI Run Ledger and Prompt Capture Policy

## Purpose

AI-assisted contributions should be auditable.

The repository should eventually be able to answer:

- which AI tool was used;
- which model and settings were used;
- what prompt or instruction started the work;
- what files or sources the AI inspected;
- what output or patch the AI produced;
- what validations ran;
- what human reviewed or approved;
- what source boundaries applied;
- whether any private or protected material was excluded.

## Current status

This is a draft governance policy. It does not create runtime logging, telemetry, or mandatory prompt upload infrastructure.

## Capture levels

### Level 0: PR disclosure

Minimum expected today.

Record in the PR body or comment:

- AI tool used;
- model, if known;
- reasoning effort or equivalent setting;
- internet setting;
- permission mode;
- route selected;
- validation run;
- whether AI routing was affected.

### Level 1: Prompt summary

Recommended for normal AI-assisted PRs.

Record a short summary of:

- starting prompt;
- task scope;
- non-goals;
- sources inspected;
- generated artifacts;
- human edits after generation.

Do not include secrets, credentials, private data, protected source text, or full private chats.

### Level 2: Prompt and output artifact

Use for high-risk work such as schemas, validators, claims, graph objects, source registry, ingestion, or runtime planning.

Store a redacted prompt/output artifact under a future governed path such as:

- `data/ai-runs/`
- `incoming/ai-runs/`
- or another approved run-ledger location.

This path must not be created for sensitive or protected content until the repo has a validated schema and privacy policy for AI run capture.

### Level 3: Full run ledger

Future state only.

A full run ledger may include:

- run_id;
- task_id;
- PR number;
- tool;
- model;
- model version;
- reasoning effort;
- internet setting;
- permission mode;
- route selected;
- prompt hash;
- redacted prompt text;
- output hash;
- files read;
- files modified;
- sources cited;
- validations run;
- approvals;
- stop conditions triggered;
- human reviewer;
- merge outcome.

## What must not be captured

Do not capture:

- secrets;
- API keys;
- credentials;
- private keys;
- private licensed source text;
- full protected Bible translations;
- full modern copyrighted theology text;
- proprietary lexicon entries;
- confidential third-party data;
- sensitive personal data;
- attorney-client or privileged material;
- private chats unless intentionally redacted and approved.

## Prompt hash option

If the full prompt cannot be stored, store a hash and summary.

This preserves auditability without exposing sensitive content.

## PR question

For high-risk AI-assisted PRs, answer:

Was AI input/output captured for audit?

- No, not required for this route.
- Yes, summarized in PR.
- Yes, redacted prompt/output artifact added.
- Deferred, run-ledger schema needed first.

## Future implementation route

A full prompt/run-ledger implementation should use the `validation_infra` or a future `ai_run_ledger` route. It should be treated as xhigh risk because it may affect privacy, source boundaries, and contributor governance.
