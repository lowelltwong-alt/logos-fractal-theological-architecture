# Commit Mutation Protocol

## Purpose

This file defines how contributors should describe meaningful repository changes when those changes affect structure, ontology, governance, schemas, or reusable theological architecture.

The repository already contains strong rules for anchors, IDs, relationships, trust zones, inference, and schema compatibility. This file adds a parallel discipline for mutation itself.

Its purpose is not to force bureaucratic overhead onto every tiny wording edit. Its purpose is to make meaningful structural change more legible, reviewable, and traceable.

This file should be read together with:
- `ontology-discipline.md`
- `fractal-rules.md`
- `deterministic-id-policy.md`
- `schema-compatibility-policy.md`
- `trust-zones.md`
- `promotion-thresholds.md`
- `inference-policy.md`

## Core principle

A meaningful commit is not only a code or file event.
It is a mutation of the repository's governed architecture.

When the change affects stable structure, contributors should be able to say:
- what changed
- what object or branch changed
- where the change belongs in the ontology
- whether the change affects identity, schema, trust, inference, or downstream reuse
- whether the change strengthens the current primary build

## When this protocol applies

Use this protocol especially when a commit does one or more of the following:
- adds a new governed node family
- changes a schema or machine-readable object shape
- adds or changes controlled vocabulary
- changes a trust-zone expectation
- introduces a new branch or structural surface
- promotes repeated material into a reusable governed object
- changes inference expectations
- changes how downstream users may rely on a branch or node family

This protocol may also be used for major synthesis or tradition-architecture commits when the content meaningfully changes the reusable structure of the project.

## Commit-mutation dimensions

A meaningful repository change should be describable through the following dimensions.

### 1. Build class
What current build class does the mutation belong to?

Suggested values:
- `primary_current`
- `supporting_current`
- `future_governed`

See:
- `build-priority-policy.md`

### 2. Mutation class
What kind of mutation is this?

Suggested values:
- `identity`
- `schema`
- `vocabulary`
- `relationship`
- `trust`
- `inference`
- `promotion`
- `instantiation`
- `content`
- `integration`

### 3. Target surface
What branch, node family, or artifact surface is being changed?

Examples:
- canon
- doctrine
- concept
- scripture
- translation
- graph
- governance
- roadmap
- tradition
- institution overlay

### 4. Local address
What is the nearest governed address for the change?

The repository should continue to prefer local deterministic identity over bloated hand-authored global maps.

That means a contributor should usually name:
- the local file or node
- the local anchor or canonical ID
- the immediate parent branch or governing file family

Do not force contributors to hand-author total ancestor chains when governed local structure already exists.

### 5. Governance impact
What kind of downstream effect does this mutation have?

Examples:
- no governance impact
- local structural impact only
- cross-branch reuse impact
- schema compatibility impact
- trust-zone impact
- inference impact
- downstream decision-support impact

## Preferred commit header pattern

For meaningful structural commits, prefer a commit message that makes at least three things visible:
- mutation class
- target surface
- actual change

Examples:
- `Add build-priority policy for current primary architecture`
- `Add commit mutation protocol for governed structural changes`
- `Extend node types with tradition composition profile`
- `Clarify trust-zone expectations for experimental graph objects`

A contributor may optionally use a more explicit governed pattern such as:

`[schema][governance] add compatibility rule for governed edge objects`

or

`[promotion][concept] promote repeated vocation material into shared concept node`

The repository does not need one single decorative format. It does need semantic clarity.

## Preferred commit body pattern for major changes

When the change is structural enough to deserve a fuller explanation, the commit body or accompanying PR note should ideally answer:

### What changed?
What was added, revised, promoted, constrained, or integrated?

### Why now?
Why does this mutation strengthen the present repository rather than merely expanding optional surface area?

### Where does it belong?
What local node, branch, or governance family does it belong to?

### What does it affect downstream?
Does it affect:
- schema compatibility
- trust
- inference
- promotion
- machine-readable reuse
- downstream decision architecture

### What was intentionally not done?
What nearby but non-primary expansion was deferred?

This last question is especially important for preventing premature sideways growth.

## Local-over-global rule

This protocol should follow the same fractal discipline as the rest of the repository.

That means contributors should describe:
- the local mutation
- the immediate governed context
- the relevant downstream effects

They should not be forced to manually encode the entire global graph of consequences inside every commit.

Humans record the meaningful local mutation.
Machines and later review can infer broader recursive structure from governed local assertions.

## Promotion rule

When a mutation promotes repeated material into a reusable governed object, the commit or review note should make that visible.

Typical examples:
- section -> child node
- repeated local concept -> shared concept node
- repeated edge pattern -> relationship object
- branch-local structure -> reusable schema family

This makes promotion legible as an architectural event rather than a cosmetic reorganization.

## Trust and schema rule

If a mutation changes:
- trust zone behavior
- schema meaning
- inference assumptions
- deterministic identity behavior

then the change should be treated as governance-significant, not as a casual refactor.

Such changes should usually be easy for a later reviewer to find and understand.

## Tradition and institution rule

When the repository begins adding formal tradition-composition profiles or institution-overlay objects, contributors should use this protocol to make clear whether a commit is:
- extending reusable tradition architecture
- adding one local instantiation
- changing downstream application logic only
- changing the core upstream grammar

This will matter because not every new institution-specific build should be mistaken for a mutation of the shared theological core.

## Fractal rule

Commit discipline should itself remain fractal.

That means the same general mutation questions should recur across levels:
- what changed locally?
- what governed object or branch changed?
- what type of mutation is this?
- what downstream reliance may be affected?
- is this strengthening the current shell or just expanding optional horizon?

## Summary principle

A serious repository needs governed mutation, not only governed structure.

The goal of this protocol is to make meaningful changes traceable enough that future humans and machines can understand not only what the repository is, but how it changed and why.
