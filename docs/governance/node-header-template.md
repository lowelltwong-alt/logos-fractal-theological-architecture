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

Use the smallest header that gives the node a stable identity.

Do not add unnecessary metadata.
Do not invent uncontrolled header fields casually.
Use the approved vocabulary from the governance folder whenever possible.

## Standard minimal header

Most governed nodes should begin with a compact block like this:

```markdown
**Node type:** doctrine_node  
**Anchor:** doctrine.prudence  
**Tags:** doctrine.core, concept.governance, ai.governance  
**Key relationships:** grounds, constrains, translates_into
