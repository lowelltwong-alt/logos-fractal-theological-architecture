---
id: manuscripts.root
anchor: manuscripts.root
title: Manuscripts Layer
slug: manuscripts
node_type: manuscripts_root
system_role: manuscript_layer
artifact_tier: foundational_support

domain: christian_ai_theology
subdomain: manuscripts
audience_tags:
  - theology
  - biblical_studies
  - ontology
  - textual_history

tags:
  - manuscripts.layer
  - manuscript.witness
  - textual_history
  - ontology.core

parents:
  - docs.root
children: []
related:
  - scripture.root
  - translation.root
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

# Manuscripts Layer

This folder is the entry point for manuscript witnesses, textual traditions, and text-critical notes in the repository.

## Why this layer exists

The project should be able to note not only what a passage says and how it is translated, but also:
- what manuscript or textual tradition stands behind it
- whether the reading is associated with the Masoretic Text, Septuagint, Dead Sea Scrolls, papyri, codices, or another witness
- whether there are major textual variants that affect interpretation
- whether claims about antiquity or textual priority are well supported or misleading

## Relation to the rest of the project

This layer connects directly to:
- scripture text nodes
- translation witness nodes
- original-language term nodes
- text-critical notes
- interpretation nodes

## Recommended future substructure

- `dss/`
- `mt.md`
- `lxx.md`
- papyri and codex nodes as needed

## First recommended manuscript buildout

The strongest early witnesses for this repository include:
- Masoretic Text
- Septuagint
- Dead Sea Scrolls witness notes relevant to Genesis and Isaiah
- major New Testament papyri and codices where needed later
