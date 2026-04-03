# Build Priority Policy

## Purpose

This file defines how contributors should prioritize work in the current stage of the Logos repository.

The repository already contains several governed branches and future-oriented extensions. That breadth is useful, but it also creates a recurring risk: contributors may expand the architecture sideways faster than the current primary build is stabilized.

This file exists to reduce that drift.

It should be read together with:
- `README.md`
- `docs/governance/README.md`
- `docs/governance/ontology-discipline.md`
- `docs/governance/fractal-rules.md`
- `docs/governance/inference-policy.md`
- `docs/roadmap/theological-buildout-roadmap.md`
- `docs/roadmap/repository-integration-map.md`

## Core principle

Not every valuable branch should receive equal build priority at the same time.

The repository should preserve a distinction between:
- the current primary architecture
- important supporting layers
- future governed expansions

A contributor should not assume that because a branch is legitimate, it is therefore the current center of gravity.

## Current priority rule

At the present stage, contributors should prioritize work that directly strengthens the repository's upstream theological-decision architecture.

That current primary build includes:
- theological source architecture
- canon, doctrine, concept, comparison, and synthesis buildout
- ordering and weighting logic
- LAIRCA-facing theological translation
- ontology discipline and recursive governance rules
- identity, anchor, schema, and trust discipline
- institution-facing translation paths into downstream decision architecture

This means contributors should currently favor work that makes the repository more usable as:
- a theological upstream layer
- a governed source architecture
- a decision-shaping architecture
- a later tradition-composition and institutional-instantiation engine

## Current primary build focus

In practical terms, the strongest current priorities are:

### 1. Theological source buildout
Examples:
- canon thinker nodes
- doctrine nodes
- concept nodes
- comparison nodes
- synthesis nodes

### 2. Ordering, weighting, and derivation logic
Examples:
- explicit ordering profiles
- explicit weighting profiles
- doctrine-to-governance derivation patterns
- theology-to-LAIRCA translation paths

### 3. Ontology and governance discipline
Examples:
- stable IDs
- controlled vocabularies
- trust-zone discipline
- promotion discipline
- schema compatibility discipline
- commit and mutation discipline

### 4. Institutional translation and instantiation readiness
Examples:
- crosswalk nodes
- institution-facing overlays
- tradition-composition profiles
- downstream use constraints for AI-assisted decision support

## Supporting but non-primary work

Some work is legitimate and useful without being the current center of gravity.

Examples may include:
- scripture-layer enrichment that clearly grounds doctrine or concept work
- original-language enrichment tied to active doctrine or concept questions
- graph or concordance work needed to stabilize recurring theological relationships
- machine-readable sidecars where the prose architecture is already mature enough

This work is allowed when it directly strengthens the current primary build.

## Future-governed expansion rule

Some branches are real parts of the repository but should currently be treated primarily as governed future shells unless they are needed by the active build.

Examples include:
- larger manuscript and witness buildout
- fragment and reconstruction corpora
- large-scale translation comparison expansion
- broad corpus ingestion
- advanced graph-domain expansion beyond current governed need

These branches are not excluded because they are unimportant.
They are deferred because premature expansion can dilute the repository's current architectural center.

## Deferred-but-governed principle

A branch may be:
- legitimate
- well designed
- architecturally compatible
- still not a current build priority

That distinction should remain explicit.

A contributor who touches a future-facing branch should normally ask:
1. does this directly strengthen the current primary architecture?
2. does this solve a present ontology, derivation, or instantiation problem?
3. is this strengthening the core, or simply expanding the horizon?

If the answer is mainly horizon expansion, the work should usually be deferred.

## Build-class guidance

The repository should informally distinguish between three build classes.

### `primary_current`
Use for work that directly strengthens the current center of gravity.

Typical examples:
- canon, doctrine, concept, comparison, and synthesis growth
- ordering and weighting work
- derivation logic
- ontology discipline
- trust, ID, schema, and commit governance
- institution-instantiation readiness

### `supporting_current`
Use for work that supports the primary build without replacing it as the center of gravity.

Typical examples:
- scripture or lexical grounding for active doctrine work
- limited graph support for repeated governed relationships
- machine-readable sidecars for mature structures

### `future_governed`
Use for well-governed work that belongs in the architecture but is not yet the main build priority.

Typical examples:
- manuscript corpora
- fragment corpora
- larger translation comparison layers
- broader data-import surfaces
- expansive graph-domain growth beyond present governed need

## Contributor decision rule

Before beginning substantial work, a contributor should be able to say:
- what build class the work belongs to
- why it belongs there
- whether it strengthens the current primary build
- what current node, branch, or problem it directly serves

If that cannot be stated clearly, the work likely needs to be narrowed or deferred.

## Fractal rule

Build priority should itself remain fractal.

That means the same question should recur at multiple levels:
- is this branch primary now, supporting now, or future-governed?
- is this node strengthening the current shell or merely expanding optional surface area?
- is this local addition feeding the present architecture or distracting from it?

## Summary principle

A governed repository still needs sequencing.

The current Logos build should prioritize the theological and decision-shaping core first, allow supporting work where it directly strengthens that core, and keep larger source-corpus and expansion work in a governed future horizon unless the present architecture truly requires it.
