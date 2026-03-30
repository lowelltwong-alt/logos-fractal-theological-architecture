# Deterministic ID Policy

## Purpose

This file defines how stable identifiers should work across the repository.

A world-class ontology depends on deterministic identity.
If IDs drift, collide, depend on incidental file position, or change with naming whims, then links, graph objects, provenance trails, and machine traversal all become weaker.

This file should be read together with:
- `anchor-conventions.md`
- `anchor-conventions-scripture-and-graph-extension.md`
- `schema-compatibility-policy.md`
- `fractal-rules.md`
- `inference-policy.md`

## Core principle

Identity should be stable, deliberate, and derived from semantic structure rather than incidental workflow details.

An ID should not depend on:
- row order
- file order
- temporary working titles
- who created it first
- whether a contributor reorganized a folder visually

## Preferred ID pattern

The repository should prefer IDs that are:
- deterministic
- semantically meaningful
- stable across reuse
- readable enough for human debugging
- specific enough to avoid collision

Typical examples:
- `canon.augustine`
- `scripture.genesis.1`
- `text.genesis.1.26-28`
- `term.hebrew.tselem`
- `translation.esv`
- `witness.mt`
- `noncanonical.1_enoch`

## ID rule for governed nodes

Every governed node should normally have:
- one stable canonical ID
- one stable anchor closely aligned to that ID
- one title that may be more human-readable but should not control identity

Where possible, title changes should not require ID changes.

## ID rule for graph and concordance objects

Graph and concordance objects should also use deterministic identity.

That means their IDs should be derived from:
- object domain
- object type
- semantic content
- stable source references where relevant

Not from:
- import order
- temporary filenames
- auto-numbered sequence only

## Edge ID rule

A governed edge object should normally use a deterministic ID based on:
- source node
- relation type
- target node

Optional suffixes may be added when multiple distinct governed edges exist between the same nodes.

Example pattern:
- `edge.term.hebrew.tselem.grounds.biblical_theme.image_of_god`

## Renaming rule

Do not change IDs casually.

If a title, description, or file location changes, the first preference should usually be:
- keep the same ID
- keep the same anchor
- update human-readable labels only

If an ID must change, treat it as a governance-significant event and update references deliberately.

## Collision rule

Before creating a new governed ID, a contributor should check whether:
- the object already exists
- the same concept is already modeled elsewhere
- a local section should be promoted rather than duplicated under a new ID

## Fractal rule

Deterministic identity should recur across scales.

That means the same identity discipline should apply to:
- documentation nodes
- scripture nodes
- lexical nodes
- graph objects
- edge objects
- boundary objects
- schemes and validation shapes

## Machine-readability rule

AI and graph tooling should be able to rely on IDs as stable references.

That means IDs should function as durable handles, not disposable labels.

## Summary principle

Stable identity is one of the deepest structural commitments in a serious ontology.

If the IDs are unstable, the structure is only pretending to be governed.
