# Relationship Registry

## Purpose

Relationship verbs make the ontology legible.

They should be controlled, stable, and semantically distinct.

Do not casually vary them in prose or metadata when the project is trying to make comparison explicit.

## Core relationship verbs

### Structural relationships
- `parent`
- `children`
- `depends_on`
- `enables`
- `derived_from`
- `related_to`

### Comparison relationships
- `aligns_with`
- `partially_aligns_with`
- `tensions_with`
- `contradicts`
- `corrects`
- `sharpens`
- `requires_translation_to_compare`

### Canon and concept development relationships
- `promotes_to`
- `instantiates`
- `extends`
- `constrains`
- `grounds`
- `translates_into`

## Definitions

### `aligns_with`
Use when two thinkers, concepts, or nodes substantially converge on a point.

### `partially_aligns_with`
Use when there is meaningful overlap, but not full convergence.

### `tensions_with`
Use when two nodes are not outright contradictory, but exert pressure against one another.

### `contradicts`
Use when the disagreement is strong enough that both claims cannot be carried together without substantial qualification.

### `corrects`
Use when one thinker or node is being used as a substantive correction to another.

### `sharpens`
Use when one thinker or node clarifies, intensifies, or gives more precision to another without fundamentally opposing it.

### `requires_translation_to_compare`
Use when two nodes can be compared, but only after translating categories, assumptions, or vocabulary.

### `grounds`
Use when one node provides a deeper basis for another.

### `translates_into`
Use when one node moves into a downstream expression, such as theology translating into governance language.

### `constrains`
Use when one node sets a limit on another.

### `instantiates`
Use when a downstream node is a concrete instantiation of a broader source logic.

## Synonym rule

Do not casually introduce parallel verbs such as:
- `agrees_with`
- `fits_with`
- `matches`
- `influences`
- `kind_of_opposes`

If an existing controlled verb already fits, use it.

## Usage rule

Choose the strongest accurate relationship, but do not overstate.

For example:
- use `partially_aligns_with` instead of `aligns_with` when the agreement is real but bounded
- use `tensions_with` instead of `contradicts` if the difference is serious but not absolute

## Documentation rule

If a new relationship verb becomes necessary, define it here before using it broadly.

## Summary principle

Relationship verbs are part of the ontology, not just descriptive prose.

Use them carefully enough that a human or machine could reliably infer the intended shape of comparison.
