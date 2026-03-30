# Graph Shapes

## Purpose

This folder holds shape and validation guidance for the graph and concordance layer.

Its purpose is to define what governed machine-readable objects should look like so the repository can grow without silent schema drift, broken assumptions, or poisoning through malformed objects.

## Why this layer exists

A strong ontology is not only a set of objects and links. It also needs rules for validating whether those objects and links are structurally acceptable.

This layer exists to support:
- validation
- consistency
- safer imports
- clearer automation
- anti-drift governance

## What belongs here

Examples of shape and validation artifacts include:
- node shapes
- edge shapes
- boundary-sensitive object shapes
- translation witness shapes
- manuscript witness shapes

## Relation to the rest of the repository

This layer should be read together with:
- `docs/governance/schema-compatibility-policy.md`
- `docs/governance/interface-patterns.md`
- `docs/governance/shared-properties.md`
- `docs/governance/noncanonical-and-heresy-classification.md`
- `docs/governance/translation-trust-and-sectarian-classification.md`

## Summary principle

A graph becomes much safer and more machine-legible when governed objects are validated against explicit expectations rather than only trusted by convention.
