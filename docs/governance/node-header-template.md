# Node Header Template

## Purpose

This file defines the standard top-of-file header pattern for governed nodes in the Logos Fractal Theological Architecture repository.

The goal is not to make every file look rigid or mechanical. The goal is to make each node structurally legible to:
- human readers
- semantic retrieval systems
- future RAG-style workflows
- future ontology promotion
- future contributors working inside the same shell

A good node header should make the file easier to classify, retrieve, compare, and extend.

## Core rule

Use the smallest header that gives the node a stable identity, but default to the fuller governed form for most serious nodes in this repository.

Do not add unnecessary metadata.
Do not invent uncontrolled header fields casually.
Use the approved vocabulary from the governance folder whenever possible.

## Standard default header

Most governed nodes in this repository should begin with this fuller header:

```markdown
**Node type:** canon_thinker  
**Anchor:** canon.augustine  
**Tags:** thinker.augustine, tradition.patristic, era.patristic, canon.primary, concept.creation_order, concept.ordered_love, concept.two_cities, ai.governance  
**Key relationships:** grounds, sharpens, constrains, translates_into  
**Status:** working  
**Parent:** docs/canon/README.md  
**Related nodes:** doctrine.anthropology, doctrine.sin, concept.ordered_love, concept.institutions  
