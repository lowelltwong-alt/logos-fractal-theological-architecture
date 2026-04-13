# Graph Templates

## Purpose

This folder holds reusable template patterns for governed graph and concordance objects.

These templates exist to help contributors create new machine-readable objects that follow the repository's common grammar rather than inventing a new local structure each time.

## Why this layer exists

A strong ontology should not only have rules. It should also provide reusable shapes for common object families.

Templates reduce:
- schema drift
- inconsistent field naming
- missing provenance
- ad hoc graph object design

## Typical template families

Examples include:
- concept object templates
- doctrine object templates
- passage object templates
- relationship object templates
- external mapping object templates
- translation witness templates
- boundary-source templates
- exception event object templates

## Relation to the rest of the repository

This folder should be read together with:
- `docs/governance/interface-patterns.md`
- `docs/governance/shared-properties.md`
- `docs/governance/schema-compatibility-policy.md`
- `data/graph/shapes/README.md`

## Summary principle

Templates help the graph layer become operational by turning governance guidance into repeatable object patterns.
