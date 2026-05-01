---
object_type: composition_review_checklist
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: unsafe_composition_review
provenance_note: "Created 2026-05-01 as a docs-level checklist for reviewing skill composition risk."
reason_for_inclusion: "Two individually safe skills can compose into unsafe behavior. Define an explicit composition review checklist before any composed agent, subagent, orchestrator, or chained skill is approved."
---

# Unsafe Composition Review Checklist

This checklist hardens the composition rule in `agent-misalignment-and-theological-drift-policy.md` and the composition risk note in `agent-skill-graph-model.md`.

A composed skill, subagent chain, or orchestrator is a new object. It must be reviewed as a new card with its own owner, risks, model policy, source boundary, audit level, and stop conditions.

## When to run this review

Run this review when any of the following exists or is proposed:

- a `composes_with` edge between two cards;
- an orchestrator that chains two or more skills;
- a subagent that delegates to another subagent;
- a workflow that pipes one card's output into another card's input;
- a tool-use sequence that spans multiple cards in one run.

## Per-pair questions

For each pair of composed cards, answer:

- What is the union of allowed tools? Does the union exceed any single card's intent?
- What is the union of side-effect levels? Does it cross from `read_only` to `draft_only`, `repo_edit`, `external_side_effect`, or `runtime_mutation`?
- What is the union of source boundaries? Does the chain see sources neither card alone is allowed to see?
- What is the union of doctrinal profile boundaries? Does the chain change the active profile, hermeneutic, or assertion posture?
- What is the union of model policies? Does the chain run a forbidden route on a local/free model?
- What is the union of audit capture levels? Is the chain's audit level at least the maximum of its parts?
- What is the union of owners and approvals? Are all required reviewers covered?

## Forbidden compositions

Reject the composition if it would, even briefly:

- give a card tools it does not declare;
- elevate side-effect level beyond what is approved on each card;
- bypass a stop condition declared on either card;
- merge a tradition-scoped or contrastive card into a canonical-asserting chain without a profile-change review;
- combine retrieval, rendering, and claim or graph creation in one run without claim/graph route review;
- combine a frontier-required step with a local-only adapter for that step;
- chain skills in a loop without a declared termination condition;
- chain skills that produce inputs for each other without a declared trust zone for intermediate outputs.

## Required outputs

A composition review must produce:

- a composition card naming both parents and the union of properties;
- a `composes_with` edge with rationale and risk;
- a `theological_drift_risk_with` or `unsafe_composition_with` edge if any drift or unsafe property is detected;
- a list of required reviewers, including any added by the union;
- a recorded decision: approved, approved-with-changes, deferred, or rejected.

Composition reviews follow `audit-and-trace-requirements.md`.

## Examples of suspected unsafe composition

These are illustrative, not exhaustive:

- summarization skill plus claim-writer skill, without doctrine or source basis;
- retrieval skill plus graph-edge writer skill, without vocabulary review;
- source-monitor skill plus ingestion-pilot skill, without licensing review;
- read-only review skill plus a tool-permission editor skill;
- tradition-scoped explainer skill plus canonical concept promoter skill;
- a local/free summarizer feeding a frontier-required claim review without re-grounding.

When a composition resembles any of the above, default to `unsafe_composition_with` and require explicit review.
