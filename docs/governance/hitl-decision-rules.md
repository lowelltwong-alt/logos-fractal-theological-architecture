# Human-in-the-Loop Decision Rules

## Purpose

This file defines how human-in-the-loop discipline should function inside the Logos architecture.

The repository already distinguishes between:
- upstream theological source architecture
- tradition composition profiles
- downstream decision architecture
- machine inference from governed local structure

This file makes explicit how human judgment, review, escalation, and accountability should remain visible when downstream systems use AI-assisted support.

It should be read together with:
- `tradition-composition-profile.md`
- `institution-overlay.md`
- `build-priority-policy.md`
- `commit-mutation-protocol.md`
- `inference-policy.md`
- `trust-zones.md`
- `schema-compatibility-policy.md`

## Core principle

Human-in-the-loop should not be treated as a decorative slogan.

Within this repository's logic, human-in-the-loop means that meaningful moral, institutional, doctrinal, and mission-shaped judgment remains:
- visible
- attributable
- reviewable
- non-silent

AI may assist.
AI may inform.
AI may help narrow, compare, or summarize.

But accountable human commitment should remain explicit where the decision materially affects doctrine, mission, governance, persons, or public action.

## Why this layer matters

Without explicit HITL rules, several failures become likely:
- moral responsibility appears human while real judgment has drifted into defaults or automation
- institutional translation happens too fast for review
- convenient outputs begin to overtake upstream constraints
- repeated AI assistance silently reshapes doctrine, governance, or mission practice without deliberate authorization

This file exists to prevent that drift.

## Basic HITL distinction

The repository should distinguish clearly between:

### 1. AI-assisted support
Examples:
- retrieval
- summarization
- structured comparison
- candidate ranking
- draft generation
- concordance expansion from governed local assertions

### 2. Human commitment
Examples:
- approving a doctrinally meaningful synthesis
- promoting repeated structure into a reusable governed object
- changing trust-zone status
- approving downstream institutional rules
- making a mission-significant recommendation actionable

These are not equivalent.

## Rule families

### Rule 1. Human accountability must remain visible
Where a downstream system makes a meaningful decision recommendation, a human owner or review role should remain explicit.

A system should not rely on vague claims like:
- reviewed by team
- accepted by workflow
- aligned by model

It should be possible to identify who:
- approved
- escalated
- overrode
- deferred
- constrained
- rejected

### Rule 2. AI may assist before commitment, not erase commitment
AI may assist in:
- architecting option space
- surfacing inputs
- summarizing evidence
- comparing alternatives
- generating first-draft structures

AI should not be treated as silently equivalent to:
- accountable approval
- doctrinal judgment
- institutional authorization
- moral commitment

### Rule 3. Escalation should be explicit where stakes rise
Escalation is required when a downstream decision materially affects one or more of the following:
- doctrinal meaning
- trust-zone classification
- canonical or boundary handling
- institution-facing governance
- public-positioning consequences
- use of AI in high-impact human decisions
- irreversible or hard-to-reverse structural commitments

### Rule 4. Review depth should match decision class
Not every decision needs the same level of review.

A contributor or downstream system should distinguish among:
- routine low-risk assistance
- governed but reversible local changes
- cross-branch structural changes
- doctrine- or mission-sensitive decisions
- institution-shaping decisions

The greater the impact, the more explicit the human review must become.

### Rule 5. Silent inference must not outrun governed structure
Machines may infer larger recursive structure from governed local assertions.

They should not silently:
- invent doctrine
- reclassify trust zones
- create new moral non-negotiables
- create new institutional permissions
- merge boundary-sensitive materials into core logic

Such moves require deliberate human review.

## Suggested decision classes

The following classes can help determine the required HITL depth.

### `assist_only`
AI may help, but the action remains low-risk and reversible.

Examples:
- retrieval assistance
- note summarization
- initial comparison drafts

### `review_required`
A human should review before adoption, but the impact remains mostly local.

Examples:
- new local node drafts
- local synthesis edits
- machine-proposed structure promotion candidates

### `escalation_required`
A named human reviewer or authority should approve before adoption because the impact reaches beyond one local node or has trust consequences.

Examples:
- schema changes
- trust-zone changes
- new branch proposals
- institution-overlay changes

### `authority_commit_required`
A clearly attributable human authority should approve because the decision materially affects doctrine, mission, governance, or downstream decision use.

Examples:
- formal tradition profile adoption
- institution-overlay approval
- downstream high-impact decision rules
- public or mission-shaping operating constraints

## Suggested reviewer roles

A downstream implementation may use coded reviewer roles such as:
- `review.local`
- `review.structural`
- `review.tradition`
- `review.institution`
- `review.authority`

The repository does not need to hard-code one organizational chart now.
It does need explicit role grammar for later implementation.

## Relation to institution overlays

Institution overlays should specify which decision classes require:
- local review only
- escalation
- authority commit

That means HITL rules are not merely general ethics language. They should become institution-specific downstream constraints.

## Relation to AIRCA / LAIRCA

This repository's HITL rules align naturally with AIRCA-style logic.

A rough mapping is:
- AI may assist heavily in Inform and Rank
- human responsibility must remain especially visible in Commit
- Architect and Act may also require explicit human control where upstream constraints or mission risk are high

This should remain visible in later LAIRCA and institutional builds.

## Minimal review questions

Before a downstream AI-assisted action is accepted, a reviewer should be able to ask:
- what is being decided?
- what kind of decision class is this?
- what upstream theological or trust constraints apply?
- what human role is accountable here?
- what would this affect downstream?
- is this reversible?
- does this require escalation?

## Summary principle

Human-in-the-loop means more than leaving a person somewhere near the workflow.

It means preserving visible human accountability at the points where theology, mission, governance, trust, or institutional action could otherwise be silently displaced by convenience, automation, or machine suggestion.
