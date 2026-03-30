# Concordance Node Types

## Purpose

This file defines the main node families for the concordance layer.

The goal is to prevent contributor drift by making clear that not every biblical object is the same kind of thing.

A verse is not a concept.
A doctrine is not a translation witness.
A person is not a topic.
A philosophical reading is not a canonical verse.

That distinction is necessary both for intellectual honesty and for machine readability.

## Core rule

When modeling something new, identify its node type before adding content.

Do not flatten unlike things into one generic bucket such as “entry,” “idea,” or “reference.”

## Canonical text and reference nodes

### `verse_node`
A stable canonical verse reference.

Examples:
- `verse.gen.1.1`
- `verse.jhn.1.1`

A verse node should identify the canonical reference, not one specific translation rendering.

### `passage_node`
A stable multi-verse unit used when a larger textual unit is the correct semantic object.

Examples:
- `passage.gen.1.1-2.3`
- `passage.rom.8.18-25`

Use a passage node when the meaning or relationship depends on the larger textual block.

## Language and witness nodes

### `translation_witness_node`
A specific rendering of a verse or passage in a specific translation.

Examples:
- `translation.esv.jhn.1.1`
- `translation.niv.rom.8.28`

This node should remain distinct from the canonical verse node.

### `lemma_node`
A lexical node for an original-language lemma.

Examples:
- `lemma.agape.g26`
- `lemma.logos.g3056`

Use where lexical relationships are stable and reusable.

### `morphology_node`
A grammatical or morphological feature node when grammatical analysis must be explicitly modeled.

Use sparingly unless the project grows into a deeper language-analysis layer.

## Conceptual nodes

### `topic_node`
A broad retrieval-oriented category.

Examples:
- prayer
- covenant
- exile

Topic nodes are useful for navigation, but they are usually broader and looser than concept or doctrine nodes.

### `concept_node`
A more precise reusable conceptual object.

Examples:
- `concept.imago_dei`
- `concept.ordered_love`
- `concept.kingdom_of_god`

Use concept nodes when the object is reusable across verses, doctrines, and thinkers.

### `motif_node`
A recurring literary or theological motif.

Examples:
- temple
- wilderness
- new exodus
- bridegroom

Use motifs when the recurrence is pattern-based rather than doctrine-centered.

### `doctrine_node`
A stable theological object that may draw on multiple texts and traditions.

Examples:
- `doctrine.creation`
- `doctrine.justification`
- `doctrine.resurrection`

Do not confuse doctrine nodes with verses or with broad topics.

## Entity nodes

### `entity_person_node`
A stable biblical or theological person node.

Examples:
- Abraham
- Moses
- Mary
- Paul

### `entity_place_node`
A stable place node.

Examples:
- Jerusalem
- Babylon
- Sinai

### `entity_group_node`
A stable people-group or corporate entity node.

Examples:
- Israel
- Pharisees
- Church

## Interpretive and comparison nodes

### `tradition_interpretation_node`
A node representing a distinct tradition-specific or historically situated reading.

Examples:
- Augustinian reading of Romans 5
- Reformed reading of election in Ephesians 1

Use when the interpretive layer must be explicit rather than hidden.

### `comparison_node`
A node used to compare readings, concepts, doctrines, or source systems.

Use when the main purpose is comparative rather than descriptive.

### `cross_reference_node`
A node used for a stabilized cross-reference claim when the relationship itself becomes important enough to stand as a reusable object.

Use when the edge needs its own provenance, rationale, and review history.

## External source nodes

### `philosophy_node`
A non-Christian philosophical source system or conceptual tradition.

Examples:
- `philosophy.platonism`
- `philosophy.aristotelianism`

This node type is essential so that Christian and non-Christian source systems are not collapsed together.

### `external_source_node`
A broader non-biblical source node when the object is external but not best modeled as philosophy.

Examples might include:
- concordance dataset source
- commentary tradition source
- reference lexicon source

## Governance nodes

### `assertion_node`
A node representing a specific reviewed or proposed claim, especially when a verse-to-concept or verse-to-doctrine relationship requires explicit provenance and may be contested.

### `review_node`
A node representing a review event, correction, dispute resolution step, or audit trail object.

Use these when the concordance becomes large enough that assertions and review history must be modeled as first-class objects.

## Design rule

Prefer the most semantically precise node type that can be reused across the repository.

Do not create a new node type unless the current families cannot represent the object without distortion.

## Summary principle

The concordance should remain intelligible by preserving the differences among:
- source text
- translation witness
- language object
- concept
- doctrine
- entity
- interpretation
- external source
- governance object

That distinction is what keeps the concordance both fractal and trustworthy.
