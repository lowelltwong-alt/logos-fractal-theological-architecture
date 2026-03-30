# Graph Interfaces

## Purpose

This folder is the entry point for interface-like patterns in the graph and concordance layer.

Interfaces help different graph object families share reusable structure, capabilities, or governance expectations without collapsing into one flat object type.

## Why this layer exists

A strong graph ontology should be able to say not only what an object is, but also what reusable patterns it participates in.

That helps with:
- validation
- reuse
- tooling
- governance
- cross-domain consistency

## Typical interface families

Examples may include:
- reviewable objects
- boundary-sensitive objects
- scripture-grounded objects
- machine-readable objects

## Relation to the rest of the repository

This layer should be read together with:
- `docs/governance/interface-patterns.md`
- `docs/governance/shared-properties.md`
- `data/graph/shapes/README.md`

## Summary principle

Interfaces help graph domains share repeatable structural grammar without erasing meaningful type differences.
