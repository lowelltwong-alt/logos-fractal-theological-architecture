---
id: translation.root
anchor: translation.root
title: Translations Layer
slug: translations
node_type: translation_root
system_role: translation_layer
artifact_tier: foundational_support

domain: christian_ai_theology
subdomain: translations
audience_tags:
  - theology
  - biblical_studies
  - ontology

tags:
  - translation.layer
  - ontology.core
  - biblical_studies
  - ai.retrieval

parents:
  - docs.root
children: []
related:
  - scripture.root
  - hermeneutic.root
  - manuscripts.root
  - original_language.root

authors:
  - id: author.lowell_t_wong
    roles: [conceptualization, writing]
coauthors: []
editors: []
reviewers: []
contributors: []
tradition_review: []

status: draft
review_status: unreviewed
review_cycle: quarterly
---

# Translations Layer

This folder is the entry point for Bible translations, ancient versions, and translation-level comparison in the repository.

## Why this layer exists

The project needs to know not only what verse is cited, but also:
- what translation is being used
- what textual base stands behind it
- what translation philosophy shaped it
- whether it is broadly trustworthy, limited, sectarian, or disputed

This layer exists to prevent translation-level confusion from silently shaping doctrine.

## Core rule

No translation should be treated as a primary doctrinal witness by default without at least minimal classification metadata.

See:
- `docs/governance/translation-trust-and-sectarian-classification.md`
- `docs/governance/textual-traditions-translation-and-noncanonical-sources.md`

## Recommended substructure

- `ancient-versions/`
- `mainstream-modern/`
- `sectarian-and-disputed/`

## Interpretation rule

This layer should help the repository distinguish between:
- responsible translation differences
- confessional tone and register
- textual-base limitations
- sectarian or doctrinally tendentious renderings
- disputed or misleading provenance claims
