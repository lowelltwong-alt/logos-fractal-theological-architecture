# Action Types and Governed Changes

## Purpose

This file defines the repository's action-type model.

An action type is a governed category of change that helps the repository evolve through recognizable, reviewable operations rather than ad hoc edits.

This file should be read together with:
- `operational-ontology-model.md`
- `schema-compatibility-policy.md`
- `deterministic-id-policy.md`
- `research-synthesis-ai-era-ontology-takeaways.md`

## Core principle

A serious ontology should not only govern what objects exist.
It should also govern how changes happen.

That means major edits should become more recognizable as action families.

## Why action types matter

Action types help:
- reduce ad hoc structural drift
- make contributor intent clearer
- improve review quality
- support future automation and audit trails
- make AI-assisted workflows safer

## Common action families

### Add object
Use when introducing a new governed node or object.

Examples:
- add thinker
- add doctrine
- add concept
- add scripture node
- add witness object
- add graph object

### Add relationship object
Use when introducing a governed edge or relation that needs explicit provenance, trust, or review logic.

Examples:
- add thinker-doctrine relation
- add doctrine-scripture grounding relation
- add witness-to-reconstruction relation

### Add or revise witness evidence
Use when adding or revising manuscript, fragment, transcription, or translation evidence.

Examples:
- add witness
- add fragment
- add transcription
- add variant reading note

### Add or revise controlled scheme membership
Use when placing an object inside a scheme or controlled vocabulary structure.

Examples:
- place a text in a canonical-status scheme
- place a doctrine in a concept scheme
- place a translation in a trust classification scheme

### Promote object
Use when a working or repeated structure should become more stable.

Examples:
- promote a repeated concept into a governed concept node
- promote a recurring relation into a formal relationship object
- promote a prototype graph domain into a stable graph scheme

### Deprecate object
Use when an object should no longer be treated as preferred but must remain traceable.

Examples:
- deprecate a duplicate node
- deprecate a weak or replaced relation
- deprecate an outdated scheme pattern

### Merge or split object
Use when one object should be divided or multiple overlapping objects should be consolidated.

Examples:
- merge overlapping concepts
- split lexical senses
- split over-broad doctrine nodes

## Required governance expectations

An important action should normally make clear:
- what changed
- why the change is needed
- what IDs are affected
- what trust or compatibility impact exists
- whether promotion or deprecation is involved
- what references or evidence support the change

## Action-type rule

Not every tiny edit needs a heavy process.

But the more an edit affects:
- stable identity
- schema shape
- trust status
- cross-branch structure
- downstream retrieval
- doctrinal or boundary significance

the more useful it becomes to think of that edit as a governed action type.

## Review rule

Action types can imply different review expectations.

Examples:
- add a small local node may need light review
- change a canonicality classification may need heavy review
- deprecate a stable identifier may need explicit compatibility review
- add a new relationship verb may require central governance review

## AI-assisted rule

Future AI systems should not invent action semantics ad hoc.

They should be able to recognize and follow governed action families when suggesting or preparing changes.

That means action types should remain legible, stable, and documented.

## Fractal rule

Action-type logic should recur across scales.

That means similar governance grammar may apply whether the action affects:
- a single node
- a relationship object
- a graph domain
- a scheme family
- a larger architectural branch

## Summary principle

A strong ontology is not only governed by static rules.
It is also governed by recognizable, reviewable patterns of change.
