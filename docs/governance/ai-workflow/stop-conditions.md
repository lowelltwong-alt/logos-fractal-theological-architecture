---
object_type: governance_guardrail
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: mandatory_stop_conditions
provenance_note: "Created 2026-04-30 as mandatory stop conditions for AI-assisted repository work."
---

# Stop Conditions

AI-assisted tools must stop and report instead of improvising when any stop condition is triggered.

## Git and local-state stops

Stop if:

- the worktree is dirty;
- untracked files may be overwritten;
- local `main` cannot fast-forward from `origin/main`;
- the target branch already exists and its state is unclear;
- local and remote branch states diverge;
- the task requires reset, rebase, force-push, delete, discard, or overwrite.

## Scope stops

Stop if:

- required changes fall outside declared scope;
- the task spans multiple high-risk routes and should be split;
- the task would modify doctrine, claim, graph, schema, ingestion, or runtime surfaces unexpectedly;
- the task would require a new source policy or trust zone not yet defined.

## Source and copyright stops

Stop if:

- the work requires protected modern Bible text;
- the work requires full modern theology book text;
- the work requires proprietary lexicon material;
- source license or public-domain status is unclear;
- copyrighted material would be embedded, chunked, indexed, or committed;
- private source text, chunks, or embeddings would be added to the public repository.

## Theology and graph stops

Stop if:

- a claim lacks source basis;
- a concept lacks upstream doctrine/source basis;
- a graph edge lacks approved relationship vocabulary;
- inferred material would be represented as asserted material;
- staged research would be silently promoted to doctrine, claim, or graph truth.

## Runtime and agent stops

Stop if:

- a task would create executable agents without explicit authorization;
- a tool registry, action gateway, approval runtime, or external connector would be created outside a planning route;
- a side-effecting action would be performed without approval;
- secrets, credentials, private data, or sensitive local files would be accessed.

## Validation stops

Stop if:

- validation fails for an unclear reason;
- validation failure appears unrelated to the PR;
- fixing validation would require broad scope expansion;
- the repo's validation commands or workflow expectations are unclear.

## Required report when stopped

Report:

- current branch;
- local status;
- remote state if known;
- files implicated;
- route selected;
- stop condition triggered;
- safe next options.
