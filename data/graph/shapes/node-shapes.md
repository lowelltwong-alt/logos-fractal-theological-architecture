# Node Shapes

## Purpose

This file defines the expected validation shape for governed graph and concordance node objects.

It is not a strict executable schema by itself. It is the repository's human-readable reference point for what a valid governed node object should minimally contain.

## Core principle

A governed node object should be recognizable as the same kind of object family wherever it appears.

That means node objects should not casually diverge into several incompatible local grammars.

## Minimum expected shape

A governed node object should normally include sections or fields covering:
- identity
- classification
- relationships
- content
- provenance

Depending on the object family, it may also include:
- concordance-specific metadata
- trust or boundary metadata
- review metadata
- schema/version metadata

## Minimum validation expectations

A governed node object should normally have:
- stable ID
- stable anchor
- title
- node type
- at least a basic relationship block
- at least a basic provenance block

## Higher-governance expectations

Additional validation should usually be required when a node is:
- boundary-sensitive
- doctrinally significant
- translation-sensitive
- repeatedly reused in graph traversals
- expected to support machine workflows

## Example specialized expectations

### Translation witness objects
Should normally include:
- translation philosophy
- textual base quality
- doctrinal tendency
- use-case limit

### Noncanonical or heretical boundary objects
Should normally include:
- canonical status
- doctrinal alignment
- use-case limit
- warning text where appropriate

### Reviewable objects
Should normally include:
- review status
- review cycle
- reviewers or reviewed-by history where available

## Validation rule

When a contributor creates a new governed object family, they should ask:
- does it follow the same base shape as other governed node objects?
- are required fields present?
- are trust and provenance expectations satisfied?
- is the object's grammar still recognizable as part of this repository?

## Summary principle

Node shapes exist to keep graph objects from becoming structurally inconsistent with one another.

A fractal ontology needs repeatable object grammar, not just repeatable folder structure.
