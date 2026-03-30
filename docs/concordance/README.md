# Concordance Architecture

## Purpose

This branch defines the concordance layer for the Logos Fractal Theological Architecture repository.

The concordance layer exists to create a large, durable, machine-readable, audit-friendly cross-reference system connecting:
- verses
- passages
- lemmas
- topics
- concepts
- doctrines
- entities such as people and places
- translation notes
- theological and philosophical interpretations
- cross-reference relationships

This is not meant to be a flat index of “related verses.”

It is meant to become a governed, recursive, ontology-ready concordance system that can grow over time through many contributors without collapsing into ambiguity, uncontrolled drift, or silent poisoning.

## Why this branch exists

A normal concordance is useful for lookup.
A serious machine-readable concordance must do more.

It must preserve:
- stable reference identity
- typed relationships
- source lineage
- review and auditability
- translation burden where direct equivalence is misleading
- distinction between canonical source text and interpretive layer

This branch exists so that scriptural cross-reference work is built as a governed architecture rather than as a growing pile of disconnected notes.

## Core principle

The concordance should be built as a layered graph, not as a single giant document.

That means:
- the verse layer should remain stable
- the translation layer should remain distinguishable from the canonical verse identity layer
- the concept and doctrine layers should remain distinguishable from the verse layer
- the interpretive layer should remain distinguishable from the source-text layer
- all meaningful links should carry provenance and review state

## What this branch should produce over time

A mature concordance branch should make it possible to:
- map stable canonical references to reusable verse nodes
- attach translation witnesses without confusing them with verse identity
- attach topics, concepts, doctrines, and entities through typed relationships
- compare theological and philosophical readings without flattening them
- import external concordance or biblical datasets without automatically canonizing them
- support machine retrieval, ontology buildout, and human review at scale

## Main build logic

The concordance should be built in layers.

### Layer 1. Canonical reference layer
Stable verse and passage identity.

### Layer 2. Translation and language layer
Translation witnesses, lemmas, morphology, semantic notes.

### Layer 3. Conceptual layer
Topics, themes, concepts, doctrines, motifs.

### Layer 4. Interpretive layer
Tradition-specific notes, theological arguments, philosophical intersections, contested readings.

### Layer 5. Provenance and trust layer
Who added the claim, what source justified it, what review status it has, what confidence it deserves, and what can or cannot be treated as canonical.

## Why this is better than a normal concordance

A normal concordance often assumes that if two verses are related, the relationship is obvious and stable.

This branch assumes the opposite:
- relationship type matters
- provenance matters
- review status matters
- translation burden matters
- theology and philosophy must not be silently mixed without explanation

That is why this branch is built as governed ontology work rather than only as Bible-study convenience.

## What should live here

This branch should hold:
- concordance branch governance docs
- node-type and relationship-type registries specific to the concordance
- review and trust rules
- the implementation roadmap
- contributor design decisions and rationale
- starter schemas and templates for machine-readable nodes

## Summary principle

The concordance should grow like the rest of the repository:
- node-first
- recursively
- under controlled vocabulary
- with explicit provenance
- with strong review discipline
- with enough machine readability that future AI systems can traverse it safely

The goal is not just more links.
The goal is trustworthy link architecture.
