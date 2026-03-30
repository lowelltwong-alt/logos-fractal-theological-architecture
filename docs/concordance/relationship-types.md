# Concordance Relationship Types

## Purpose

This file defines the approved relationship types for the concordance layer.

The central rule is simple:

A concordance should not just say that two things are “related.”
It should say how they are related.

That is one of the main differences between a convenience concordance and a machine-readable, ontology-ready concordance.

## Core rule

Use typed relationships whenever possible.

Do not collapse all connections into vague labels such as:
- related
- similar
- connected
- linked

Those may be acceptable for lightweight navigation, but they are not sufficient for serious ontology work, auditability, or future AI use.

## Relationship families

### Textual and literary relationships

#### `quotes`
Use when one verse or passage directly quotes another text.

#### `alludes_to`
Use when one verse or passage likely alludes to another without direct quotation.

#### `echoes`
Use when the relationship is literary or thematic resonance rather than formal quotation.

#### `parallel_to`
Use when two passages function as textual or narrative parallels.

#### `fulfills`
Use when one text is interpreted as fulfillment of another.

#### `recapitulates`
Use when one passage repeats or replays an earlier pattern at a larger theological level.

### Linguistic relationships

#### `contains_lemma`
Use when a verse or translation witness contains a given lemma.

#### `uses_morphology`
Use when a verse or witness should be linked to a grammatical or morphological feature node.

#### `translates_as`
Use when a translation witness renders a lemma or phrase in a particular way.

### Conceptual relationships

#### `relates_to_concept`
Use when a verse, passage, or entity materially bears on a concept.

#### `supports_concept`
Use when the verse is a strong support text for the concept.

#### `partially_supports_concept`
Use when the verse contributes but is not a strong standalone support.

#### `is_often_grouped_with`
Use when the relationship is common in concordance practice but weaker than doctrinal or conceptual support.

### Doctrinal relationships

#### `supports_doctrine`
Use when a verse or passage is a strong support text for a doctrine.

#### `is_contested_for_doctrine`
Use when the verse is commonly used in doctrinal debate and should not be represented as straightforward support without qualification.

#### `is_classic_for_doctrine`
Use when a verse is historically central in a doctrine’s reception history.

### Entity relationships

#### `mentions_entity`
Use when a verse or passage mentions a person, place, or group.

#### `centers_on_entity`
Use when the entity is central rather than incidental.

#### `occurs_in_place`
Use when a narrative or event is located in a place.

### Interpretive relationships

#### `interpreted_by`
Use when a verse, passage, or concept is linked to a specific interpretive tradition or thinker.

#### `interpreted_as`
Use when a text receives a specific theological or conceptual reading.

#### `requires_translation_to_compare`
Use when the comparison is not direct and needs conceptual translation.

#### `aligns_with`
Use when an interpretation or concept meaningfully aligns with another node.

#### `partially_aligns_with`
Use when the overlap is real but bounded.

#### `misaligns_with`
Use when the relation is meaningfully out of alignment rather than merely different.

#### `tensions_with`
Use when the relation is under real pressure but not best described as contradiction.

#### `corrects`
Use when one interpretive node is functioning as a correction of another.

### Provenance and governance relationships

#### `derived_from`
Use when an assertion or node is directly derived from one major source.

#### `synthesizes`
Use when a claim or interpretation is built from several sources together.

#### `appropriates_from`
Use when a Christian reading or concept borrows from an external philosophical or conceptual tradition.

#### `adapts`
Use when a borrowed category is revised or redirected into a new frame.

#### `reviewed_by`
Use when an assertion or edge has been reviewed by a specific editor or reviewer.

#### `supersedes`
Use when a newer reviewed claim replaces an earlier one.

#### `flags`
Use when a review node flags a problem or risk in an assertion.

## Strength and status guidance

Not every relationship should be treated as equally strong.

The concordance should increasingly support qualitative relationship strength fields such as:
- `high`
- `moderate`
- `low`
- `mixed`
- `not_applicable`

It should also support review status such as:
- `imported_unreviewed`
- `community_proposed`
- `editor_reviewed`
- `scholar_reviewed`
- `canonical_locked`

The relationship type and the review state should remain distinct.

## What not to do

Avoid:
- vague “related verse” claims without typed relation
- doctrinal claims presented as neutral cross-references without provenance
- imported concordance edges promoted directly into canonical status
- relationship inflation where every weak resonance is given strong support language

## Summary principle

The concordance should preserve not only connection, but connection type.

That is what makes the graph reusable, reviewable, and machine-legible.
