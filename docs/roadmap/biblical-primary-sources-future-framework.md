# Biblical Primary Sources Future Framework

## Purpose

This file defines a long-range framework for how the repository could one day expand into a governed primary-sources layer for biblical manuscripts, fragments, witness traditions, and translation analysis.

The goal is not to flatten all witnesses into one reconstructed text. The goal is to preserve:
- the fragment or witness itself
- manuscript-level provenance and confidence
- passage-level reconstruction and comparison
- lexical and translation analysis from original languages
- machine-readable linkage into the wider ontology and concordance system

## Core principle

Do not collapse these into one object:
- fragment image
- manuscript witness record
- transcription
- normalized reconstruction
- lexical analysis
- translation analysis
- doctrinal implication

These layers should connect, but remain distinguishable.

## Future architecture layers

### 1. Witness layer
This layer holds manuscript witness objects.

Examples:
- papyrus witnesses
- codex witnesses
- Dead Sea Scrolls witnesses
- major textual traditions such as MT or LXX where modeled as witness-tradition objects

### 2. Fragment layer
This layer holds fragment-level objects where a witness survives in pieces.

Examples:
- one fragment image
- one fragment transcription
- one fragment's identified passage coverage

### 3. Passage reconstruction layer
This layer assembles fragment and witness evidence into a governed passage-level comparison object.

Examples:
- all known witnesses for a passage
- variant lists for a passage span
- confidence-aware reconstruction summaries

### 4. Lexical and phrase analysis layer
This layer connects original-language terms and phrase-level meaning to passage evidence.

### 5. Translation layer
This layer models how passages or terms are rendered into target languages and how those renderings differ.

## Recommended object families

- `fragment_object`
- `witness_object`
- `transcription_object`
- `passage_reconstruction_object`
- `lexical_evidence_object`
- `translation_comparison_object`

## Standards and external alignment

This future layer should align as much as possible with real scholarly and digital-humanities practice.

- TEI manuscript description for manuscript and fragment description
- IIIF image and presentation models for images and manifests
- manuscript-workspace style systems for cataloging, transcription, collation, and annotation
- public fragment-library patterns for fragment-level browsing and search

## Recommended future field groups

### Witness metadata
- stable witness ID
- holding institution
- shelfmark
- language
- script
- approximate date or date range
- material
- coverage
- confidence notes

### Fragment metadata
- fragment ID
- parent witness ID
- image reference
- IIIF links where available
- passage coverage estimate
- transcription status
- damage or lacuna notes
- reconstruction confidence

### Passage reconstruction metadata
- passage ID
- linked witnesses
- linked fragments
- diplomatic text layers
- normalized comparison layer
- variant list
- confidence summary

### Lexical metadata
- term ID
- lemma
- passage occurrences
- witness-sensitive variation notes
- semantic-range notes
- comparison with non-biblical contemporaneous usage where appropriate

### Translation metadata
- target language
- translation philosophy
- likely rendering options
- high-confidence renderings
- lower-confidence or context-sensitive renderings
- doctrinally sensitive rendering notes

## Confidence model

This future system should preserve confidence explicitly rather than forcing false certainty.

Suggested confidence dimensions:
- witness authenticity confidence
- dating confidence
- reading confidence
- reconstruction confidence
- lexical-confidence level
- translation-confidence level

## Why this future layer should fit the current ontology

This future project is not separate from the current ontology. It extends it.

It would connect naturally to:
- scripture nodes
- lexical nodes
- translation witness nodes
- manuscript witness nodes
- biblical themes
- doctrine nodes
- graph and concordance objects

## Recommended phased buildout

### Phase 1: metadata-ready shell
- define object families
- define IDs and trust rules
- define witness and fragment metadata expectations

### Phase 2: sample witness clusters
- create a few sample witness objects
- create a few sample fragment objects
- create one or two passage reconstruction objects
- test one lexical evidence object

### Phase 3: image integration
- add IIIF-compatible image references where available
- support fragment-to-image linking
- support page-order and fragment-order representation where relevant

### Phase 4: lexical and translation expansion
- connect terms to occurrences
- connect occurrences to witnesses and passages
- add target-language comparison objects

### Phase 5: larger corpus import
- selectively ingest larger trusted corpora
- preserve provenance and licensing constraints
- add validation and anti-poisoning checks before broad imports

## Summary principle

One day this repository could grow into a governed theological and textual knowledge system that lets a user move from:
- fragment
- to witness
- to passage
- to lexical analysis
- to translation analysis
- to doctrine and theology

without losing provenance, confidence, or context.
