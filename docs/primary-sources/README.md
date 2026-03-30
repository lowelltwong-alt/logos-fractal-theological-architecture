# Primary Sources Branch

## Purpose

This branch defines the future primary-sources expansion of the repository.

Its purpose is to give a future lead and team a governed architectural shell for building a manuscript, witness, fragment, transcription, lexical, reconstruction, and translation corpus that fits the rest of the Logos ontology instead of becoming a separate side project.

## What this future project is

This is not merely a collection of Bible quotations or a flat archive of manuscript images.

It is a future governed knowledge system for:
- manuscript witnesses, including fuller witnesses such as codices, books, letters, or substantial continuous-text objects
- fragments where a witness survives in pieces
- transcriptions
- passage reconstructions
- lexical evidence
- translation comparison
- confidence-aware provenance
- downstream linkage into doctrine, concepts, themes, and theology

## Why it belongs inside this repository

The wider repository already models:
- scripture nodes
- lexical nodes
- translation witnesses
- manuscript witnesses
- noncanonical and boundary-source controls
- graph and concordance objects

A future primary-sources corpus should therefore extend the current ontology rather than replace it.

## Long-range user outcomes

If built well, this branch could one day support workflows such as:
- showing the earliest extant witnesses for a passage
- comparing all known witnesses for a verse or passage span
- tracing where a word appears across scripture
- examining likely meanings in context from the original language
- comparing translation possibilities into many current languages
- showing where confidence is high and where uncertainty remains

## Important architectural rule

Do not collapse these layers:
- witness
- fragment
- image
- transcription
- reconstruction
- lexical analysis
- translation analysis
- doctrinal implication

They must connect, but remain distinct.

## Relation to scholarly practice

This future branch should align as much as possible with real digital-humanities and manuscript standards such as:
- TEI manuscript description for manuscript, manuscript-part, and fragment description
- IIIF for image delivery and manifests
- manuscript-workspace patterns for cataloging, transcription, and collation

## Recommended local reading order

A future lead for this branch should start with:
- `docs/roadmap/biblical-primary-sources-future-framework.md`
- `docs/primary-sources/ontology-and-taxonomy.md`
- `docs/governance/fractal-rules.md`
- `docs/governance/inference-policy.md`
- `docs/governance/trust-zones.md`
- `docs/governance/deterministic-id-policy.md`

## Summary principle

This branch is the future shell for a confidence-aware biblical primary-sources corpus that remains fractal, governable, and machine-legible.
