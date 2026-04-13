---
id: scripture.root
anchor: scripture.root
title: Scripture Layer
slug: scripture
node_type: scripture_root
system_role: scripture_layer
artifact_tier: foundational_support
address: christian_ai_theology.scripture.core.root.layer.scripture_root.scripture_root.primary
trust_zone: proposed
lifecycle_state: draft
epistemic_status: asserted

domain: christian_ai_theology
subdomain: scripture
overlay_scope: shared_core
shared_core_status: intended_shared_core
audience_tags:
  - theology
  - biblical_studies
  - ontology
  - ai_governance

tags:
  - scripture.layer
  - ontology.core
  - biblical_studies
  - ai.retrieval

parents:
  - docs.root
children: []
related:
  - doctrine.root
  - canon.root
  - concept.root
  - hermeneutic.root

source_basis:
  - scripture
  - governance_architecture
ai_usage_posture: retrieval_ok_not_auto_promote

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

# Scripture Layer

This folder is the entry point for the repository's biblical text layer.

Its purpose is to let the project move from broad theological architecture down into:
- biblical books
- chapters
- pericopes
- verse clusters
- interpretive questions
- hermeneutic methods
- competing readings
- doctrinal implications
- downstream governance and AI implications

## Why this layer exists

The project should not treat biblical references as only citations buried inside thinker pages or doctrine summaries.

Instead, the repository should be able to preserve the distinction between:
- the biblical text itself
- a specific interpretation of that text
- the doctrine drawn from it
- the downstream application built from that doctrine

That distinction matters for biblical scholarship, theological rigor, and ontology development.

## Recommended substructure

As this layer grows, it may include:
- `genesis/`
- `romans/`
- `matthew/`
- other biblical book folders as needed

Each book folder may later contain:
- a book-level README
- chapter-level nodes
- pericope nodes
- text nodes
- links to interpretation nodes and theme nodes

## Key companion layers

This folder should be read together with:
- `docs/hermeneutics/README.md`
- `docs/biblical-themes/README.md`
- `docs/governance/scripture-taxonomy-and-ontology.md`

## Build priority

The first recommended scripture buildout for this repository is:
- Genesis 1
- Genesis 3
- image of God
- fall
- stewardship
- vocation

Those are the strongest starting points for connecting biblical text to anthropology, labor, sin, institutions, and AI governance.
