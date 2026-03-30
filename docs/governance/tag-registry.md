# Tag Registry

## Purpose

Tags support retrieval, comparison, clustering, and future ontology promotion.

They should be controlled, reusable, and semantically clear.

Tags are not a place for casual variation.

## General rules

Tags should:
- use consistent family prefixes
- prefer existing controlled terms
- be semantically meaningful
- avoid redundant synonyms
- be broad enough to reuse and narrow enough to matter

## Approved tag families

### Thinker tags
- `thinker.augustine`
- `thinker.aquinas`
- `thinker.calvin`
- `thinker.athanasius`

### Tradition tags
- `tradition.patristic`
- `tradition.catholic`
- `tradition.reformed`
- `tradition.evangelical`
- `tradition.methodist`
- `tradition.orthodox`

### Era tags
- `era.patristic`
- `era.medieval`
- `era.reformation`
- `era.modern`
- `era.contemporary`

### Concept tags
- `concept.creation_order`
- `concept.imago_dei`
- `concept.anthropology`
- `concept.sin`
- `concept.pride`
- `concept.grace`
- `concept.redemption`
- `concept.vocation`
- `concept.work`
- `concept.institutions`
- `concept.governance`
- `concept.public_theology`
- `concept.public_reason`
- `concept.natural_law`
- `concept.sanctification`
- `concept.theosis`
- `concept.ordered_love`
- `concept.two_cities`

### AI-project tags
- `ai.anthropology`
- `ai.governance`
- `ai.agency`
- `ai.power`
- `ai.work`
- `ai.translation_layer`
- `ai.public_theology`
- `ai.formation`
- `ai.institutional_limits`
- `ai.retrieval`
- `ai.rag`

### Node-role tags
- `canon.primary`
- `canon.secondary`
- `comparison.core`
- `concept.core`
- `doctrine.core`
- `synthesis.core`

### Stance tags
- `stance.high_alignment`
- `stance.partial_alignment`
- `stance.strong_tension`
- `stance.requires_translation`

## Tagging rule

Prefer the smallest set of tags that makes the node retrievable and comparable.

Do not over-tag.

Good tagging should improve findability and conceptual mapping, not create noise.

## Synonym rule

Do not introduce synonyms casually.

Examples:
- prefer `concept.imago_dei` over parallel alternatives unless there is a real distinction
- prefer `concept.public_theology` over multiple near-equivalent public-facing labels
- prefer `ai.governance` over several competing AI governance variants unless a real subdivision exists

## When to add a new tag

Add a new tag only when:
- the idea recurs across multiple nodes
- existing tags do not fit cleanly
- the new tag can be defined clearly
- the distinction is useful for retrieval or comparison

## Documentation rule

Before using a new tag broadly:
1. add it here
2. define the family it belongs to
3. use it consistently thereafter

## Summary principle

Tags should help the architecture converge, not drift.

Every new tag should make the system more searchable, more comparable, or more reusable.
