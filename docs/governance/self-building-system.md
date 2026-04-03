# Self-Building System

## Purpose

This file defines how the Logos repository should become a governed self-building system rather than a static document collection.

The goal is not autonomous theological authority.
The goal is a disciplined architecture in which:
- humans define the ontology, trust boundaries, and doctrinal constraints
- AI systems accelerate drafting, linking, validation, and growth
- feedback loops improve the repository over time
- automation expands only inside governed limits

This file should be read together with:
- `fractal-rules.md`
- `inference-policy.md`
- `trust-zones.md`
- `deterministic-id-policy.md`
- `promotion-thresholds.md`
- `eight-layer-address-system.md`
- `human-in-the-loop-ai-build-loop.md`
- `feedback-and-learning-loops.md`

## Core principle

Logos may become self-building in workflow, but not self-authorizing in theology.

That means the repository may increasingly automate:
- candidate node discovery
- candidate edge discovery
- address assignment
- metadata normalization
- validation
- review queues
- retrieval packaging
- gap detection
- drift detection

But the repository should not allow machines to silently:
- define doctrine
- redefine trust zones
- promote speculative claims into core status
- create new canonical authorities
- flatten canonical and noncanonical material
- erase lineage or provenance

## What self-building means here

A self-building repository is one in which governed rules help the system extend itself through recurring cycles.

The cycle is:
1. detect gap
2. generate candidate object
3. assign identity and address
4. validate structure
5. route for review
6. approve, revise, reject, or quarantine
7. update graph and retrieval surfaces
8. measure downstream performance and feedback

## Required layers for self-building

### 1. Governance layer
Defines what kinds of objects may exist and how they may be trusted.

### 2. Schema and validation layer
Defines machine-checkable structure for governed node families.

### 3. Proposal layer
Allows AI or humans to generate candidate nodes, edges, notes, or comparisons in a controlled state.

### 4. Review layer
Routes candidates to human review with explicit review status and confidence markers.

### 5. Promotion layer
Defines how proposals become governed repository objects.

### 6. Retrieval and feedback layer
Measures whether additions actually improve search, traversal, coherence, and downstream usability.

## Self-building object states

Recommended high-level lifecycle:
- `proposed`
- `draft`
- `review_pending`
- `reviewed_specialized`
- `core_trusted`
- `boundary_restricted`
- `deprecated`
- `superseded`

These states should interact with trust zones but should not be collapsed into them.

## Candidate generation sources

Candidate buildout may be triggered by:
- repeated concepts appearing across nodes
- missing child nodes in high-value branches
- repeated interpretive references to the same passage
- repeated lexical references needing governed term nodes
- repeated doctrinal dependencies needing explicit concept nodes
- graph-edge reuse that justifies a governed relationship object
- retrieval failures showing a missing explanatory node
- human review notes requesting normalization

## Safe automation zones

The repository may safely automate more aggressively in areas such as:
- frontmatter completion
- address normalization
- schema routing
- tag suggestion
- broken-link detection
- unresolved reference detection
- duplicate-candidate detection
- review-queue generation
- migration-record generation

## Restricted automation zones

The repository should require human approval for:
- doctrinal classification changes
- trust-zone promotion
- noncanonical boundary classification
- relationship-verb expansion
- canonical status assertions
- major comparison claims
- synthesis claims with downstream governance force

## Proposal rule

AI-generated objects should normally enter through a proposal state rather than appearing as silently accepted repository truth.

Every substantial proposal should preserve:
- source basis
- generation method
- confidence note
- review target
- timestamp
- proposer identity or system identity

## Self-replication rule

The repository should be able to reproduce its own grammar in a new branch or domain.

That means every serious branch should eventually carry a recognizable shell including:
- identity
- address
- node type
- trust zone
- lifecycle state
- local relationships
- provenance
- review state
- machine-readable validation route

## Self-instruction rule

The repository should explicitly teach future AI sessions how to extend it.

That instruction should live in governed files, not only in ephemeral chat context.

At minimum, the repository should maintain:
- a continuation guide for future AI sessions
- a repo reading order
- a build-order policy
- a proposal-to-promotion workflow
- a validation and CI policy
- a drift detection policy

## Summary principle

The Logos repository should become self-building by making more of its growth process explicit, validated, and reviewable.

It should grow faster through automation without surrendering theological authority, provenance, or trust discipline.
