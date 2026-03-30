# Concordance Implementation Roadmap

## Purpose

This roadmap explains how the concordance should be built in phases, in what order, and why that order matters.

This document is intentionally opinionated.

The concordance should not be built by immediately importing everything, linking everything, and hoping structure can be added later.
That is the fastest path to an untrustworthy graph.

The right path is:
- stabilize the architecture first
- build the immutable reference layer early
- introduce graph relationships in a controlled way
- add interpretation and imported data later under explicit provenance and review controls

## Build philosophy

The concordance should be built under this principle:

**make the base layer boring, stable, and hard to corrupt; let the richer layers grow on top of it**

That means the order of build is not arbitrary. It is defensive.

## Phase 0. Governance first

### Goal
Create the rule set before large-scale content enters the system.

### What should exist
- concordance branch README
- node-type registry
- relationship-type registry
- review and trust model
- design decisions document
- roadmap
- schema template

### Why first
If this phase is skipped, contributors will begin inventing structure by habit and convenience, and later cleanup will be expensive.

### Outcome
A contributor should be able to read the docs and know:
- what kinds of nodes exist
- what relationships are allowed
- how trust states work
- what kinds of claims require stronger review

## Phase 1. Canonical reference layer

### Goal
Establish the stable scripture identity layer.

### What to build
- verse node pattern
- passage node pattern
- canonical verse and passage identifiers
- book/chapter/verse normalization rules
- translation witness conventions

### Why now
Everything else depends on stable identity.
If the verse layer is unstable, all later links become brittle.

### Strong opinion
Do not start with doctrines, themes, or interpretive systems before the verse identity layer is stable.

## Phase 2. Minimal machine-readable schema and starter nodes

### Goal
Make the branch real with working examples.

### What to build
- canonical concordance node template
- a few sample verse nodes
- a few sample passage nodes
- a few sample translation witness nodes
- starter validation assumptions

### Why now
Contributors need concrete examples, not just theory.

### Success condition
A new contributor should be able to open a sample verse node and understand immediately how the structure works.

## Phase 3. Entity and concept seed layer

### Goal
Introduce the first reusable non-verse objects.

### What to build
- first entity nodes such as Abraham, Jerusalem, Israel
- first concept nodes such as imago Dei, covenant, kingdom of God
- first topic nodes where broader navigation is needed
- first motif nodes where repetition is literary-theological rather than doctrinal

### Why this order
Entities and concepts are more stable and less controversial than full doctrinal or tradition-specific claims.
They are the best next layer for controlled expansion.

### Strong opinion
This phase should come before large doctrine imports.

## Phase 4. Typed relationships on low-risk objects

### Goal
Build the graph carefully before introducing doctrinal volatility.

### What to build
- mentions_entity
- centers_on_entity
- contains_lemma
- relates_to_concept
- parallel_to
- quotes
n- alludes_to
- echoes

### Why this order
These relationships are often easier to review and easier to validate than full doctrinal or interpretive assertions.

### Strong opinion
The graph should first get good at saying what kind of relationship exists before it gets ambitious about theology.

## Phase 5. Doctrine and interpretation layer

### Goal
Introduce theological depth under explicit review control.

### What to build
- doctrine nodes
- interpretive/tradition nodes
- doctrine support relationships
- contested-doctrine relationships
- translation-required comparison notes

### Why later
This is where poisoning, overclaim, and hidden ideology become much more likely.

### Strong opinion
Do not allow doctrine-support claims to become the first major layer of the concordance. That invites premature dogmatic capture.

## Phase 6. Philosophy and external source intersections

### Goal
Make external conceptual influence explicit.

### What to build
- philosophy nodes such as Platonism, Aristotelianism, Stoicism
- appropriation and adaptation relationships
- misalignment and translation-status fields where needed

### Why this matters
This is one of the key intellectual strengths of the larger repo and should be visible here too.

### Strong opinion
Keep this as a separate branch and do not hide it inside Christian canon or doctrine nodes.

## Phase 7. Imported concordances and external datasets

### Goal
Bring in scale without losing control.

### What to build
- import staging area
- source-specific import documentation
- normalization rules
- review workflow for imported edges
- provenance requirements for imported assertions

### Why now
Once the architecture exists, imports become useful rather than destabilizing.

### Strong opinion
Never import directly into canonical locked graph objects.
Always stage, normalize, review, and then promote.

## Phase 8. Review, audit, and locking workflows

### Goal
Make the concordance safe for many contributors and long-term machine use.

### What to build
- trust state workflow
- editor and scholar review roles
- review event records
- supersession logic
- conflict resolution notes
- audit dashboards or summaries if later tooling supports them

### Why this matters
A large graph without review infrastructure eventually becomes hard to trust.

### Strong opinion
Trust state should be visible at the node or assertion level, not just inferred from branch location.

## Phase 9. Validation and shape rules

### Goal
Prevent structural drift automatically.

### What to build
- schema validation rules
- shape constraints for major node families
- required field checks for high-trust assertions
- controlled vocabulary validation

### Why this matters
Human review alone does not scale forever.
Validation should catch structure problems before reviewers have to.

### Strong opinion
Validation should protect structure first; theological judgment remains a human task.

## Phase 10. Publication and snapshot strategy

### Goal
Make the concordance safely reusable.

### What to build
- canonical snapshots
- release notes for trusted graph states
- clear distinction between latest working data and stable published data
- provenance-preserving exports

### Why this matters
People and systems need to know what version they are querying.

### Strong opinion
A published concordance snapshot should be harder to mutate than a working branch.

## Folder and data layout recommendation

The long-term build should likely grow toward this shape:

```text
/docs
  /concordance
/data
  /sources
    /bible
    /imported
  /graph
    /verses
    /passages
    /translations
    /lemmas
    /entities
    /topics
    /concepts
    /doctrines
    /philosophy
    /interpretations
    /relationships
  /provenance
  /shapes
  /snapshots
```

The exact layout may evolve, but the main principle should remain:

**separate source inputs, approved graph objects, provenance, and validation artifacts**

## What should be done first in practice

The very next practical tasks should be:
1. add the concordance schema template
2. add three example verse nodes
3. add one passage node
4. add one translation witness example
5. add three concept/entity examples
6. add sample typed relationships among them

That will prove the architecture before scale arrives.

## Summary principle

The concordance should be built in the order that minimizes future corruption and maximizes future reuse.

That means:
- governance before scale
- stable identifiers before rich meaning
- low-risk graph edges before doctrinal overbuild
- provenance before mass import
- review discipline before canonical status

If the project follows that order, it can become both large and trustworthy.
If it ignores that order, it may become large faster, but it will be harder to trust.
