# Edge Shapes

## Purpose

This file defines the expected validation shape for governed relationship and edge objects in the graph and concordance layer.

It exists to keep important links machine-readable, reviewable, and semantically disciplined.

## Core principle

An important edge is not just a line between two nodes.

When an edge becomes governed, it should be treated as an object with its own identity, relation type, provenance, confidence, and review expectations.

## Minimum expected shape

A governed edge object should normally include:
- edge ID
- from
- relation
- to
- provenance

It may also include:
- confidence
- evidence
- warning or trust fields
- review status
- supersession history

## Minimum validation expectations

A governed edge object should normally have:
- a stable deterministic edge identifier
- a valid controlled relation type
- valid source and target references
- provenance or assertion metadata

## Higher-governance expectations

Additional validation should usually be required when an edge is:
- doctrinally significant
- contested
- translation-sensitive
- boundary-sensitive
- likely to be reused across many contexts

## Example specialized expectations

### Doctrinal support edges
Should normally include:
- evidence or source refs
- confidence
- review expectation where appropriate

### Boundary-sensitive edges
Should normally include:
- warning logic where appropriate
- use-case limits where relevant
- stronger provenance expectations

### Supersedable edges
Should normally include:
- supersedes or superseded-by handling
- review notes if a prior edge is being replaced or narrowed

## Validation rule

When a contributor creates a governed edge object, they should ask:
- is the relation type controlled and precise?
- is this edge important enough to justify first-class treatment?
- does the edge carry enough provenance to be trusted?
- is the object still following the repository's common edge grammar?

## Summary principle

A fractal ontology needs repeatable edge grammar as well as repeatable node grammar.

That is how important connections remain governable instead of becoming hidden ad hoc links.
