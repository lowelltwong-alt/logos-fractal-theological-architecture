---
object_type: roadmap_scorecard
trust_zone: canonical
lifecycle_status: active
provenance_note: "Added on 2026-04-13 while salvaging the durable merge-alignment scorecard idea from old PR #18 onto the cleaned baseline."
reason_for_inclusion: "Give maintainers and agents one additive comparison frame for selective salvage, supersession, and merge decisions across competing branches."
---

# Codex Merge Alignment Scorecard

## Purpose

This file gives maintainers and future agents a single place to compare competing architectural additions without forcing an immediate rewrite.

The goal is not to crown one branch prematurely. The goal is to make competing changes easy to evaluate, merge selectively, keep in parallel for a time, or retire cleanly.

Use this scorecard when multiple branches, PRs, or generated artifacts are all trying to improve repository structure, governance, retrieval, validation, or ontology operations.

## How to use this

For each incoming branch or proposal:

1. Identify what it changes.
2. Map it to one or more capability areas below.
3. Classify the change using `docs/governance/change-taxonomy.yaml` when that helps.
4. Score it against the criteria.
5. Record whether it should be:
   - adopted
   - merged selectively
   - kept as alternative
   - superseded
   - retired

## Capability areas to compare

### 1. Deterministic identity
- Does it preserve immutable IDs?
- Does it separate labels from IDs?
- Does it define recomputation rules for generated IDs?
- Does it avoid hidden identity drift?

### 2. Validation discipline
- Does it add or strengthen machine-checkable contracts?
- Does it improve schema, metadata, or structural validation rather than relying on prose only?
- Does it fit the shared validation suite instead of creating sidecar runner logic?

### 3. Asserted vs inferred separation
- Does it keep asserted data separate from inferred or generated artifacts?
- Does it preserve provenance for derived material?
- Does it avoid silently writing inference back into source truth?

### 4. Governance and lifecycle
- Does it clarify proposal, experimental, active, deprecated, and retired states?
- Does it define deprecate-over-delete behavior?
- Does it improve migration readability for future maintainers?

### 5. Retrieval and rendering support
- Does it help retrieval, graph neighborhood generation, evidence bundles, or output contracts?
- Does it reduce view drift across renderers?
- Does it make confidence and scope easier to inspect?

### 6. AI quarantine and reviewability
- Does it isolate AI-generated or speculative material?
- Does it create cleaner review lanes?
- Does it reduce contamination of canonical layers?

### 7. Merge safety
- Is the change additive instead of destructive?
- Can it coexist with other agent work long enough to compare outcomes?
- Are rollback and selective adoption easy?

### 8. Human maintainability
- Is the structure discoverable?
- Are file names, paths, and responsibilities obvious?
- Would a new maintainer understand what to trust and where to edit?

## Comparison rubric

Score each area from 0 to 3.

- 0 = does not help or creates confusion
- 1 = partial improvement but incomplete or fragile
- 2 = strong improvement with manageable tradeoffs
- 3 = strong improvement and clearly reusable

## Decision frame

After scoring, tag the proposal with one of the following dispositions.

- `adopt`: strong enough to become part of the main operational spine
- `merge-selectively`: keep only the strongest files or patterns
- `parallel-track`: keep beside another approach until downstream testing decides
- `supersede`: archive older approach after migration path is clear
- `retire`: preserve history but stop routing new work through it

## Merge notes template

```md
### Candidate
- branch/pr:
- author/agent:
- date reviewed:

### What it changes
- 

### Strengths
- 

### Weaknesses
- 

### Scores
- deterministic identity:
- validation discipline:
- asserted vs inferred separation:
- governance and lifecycle:
- retrieval and rendering support:
- AI quarantine and reviewability:
- merge safety:
- human maintainability:

### Disposition
- adopt / merge-selectively / parallel-track / supersede / retire

### Notes for Codex
- 
```

## Current default recommendation

Until a more complete merge framework exists, prefer changes that are:

1. additive
2. file-local
3. reversible
4. machine-validated
5. provenance-aware
6. explicit about confidence and lifecycle

That bias should help maintainers compare branches by operational quality instead of surface complexity alone.
