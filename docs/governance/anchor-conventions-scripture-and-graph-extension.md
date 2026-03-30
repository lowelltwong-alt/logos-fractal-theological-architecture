# Anchor Conventions Extension: Scripture, Boundary, and Graph Layers

## Purpose

This file extends the main anchor conventions for the newer scripture, original-language, manuscript, translation, noncanonical, and graph/concordance layers.

It should be read together with:
- `docs/governance/anchor-conventions.md`
- `docs/governance/scripture-taxonomy-and-ontology.md`
- `docs/governance/textual-traditions-translation-and-noncanonical-sources.md`
- `docs/governance/noncanonical-and-heresy-classification.md`
- `docs/governance/translation-trust-and-sectarian-classification.md`

## Additional anchor families

### Scripture layer
- `scripture.<book>`
- `scripture.<book>.<chapter>`
- `pericope.<book>.<unit>`
- `text.<book>.<chapter>.<verse_span>`

Examples:
- `scripture.genesis`
- `scripture.genesis.1`
- `text.genesis.1.26-28`
- `text.genesis.11.1-9`

### Biblical themes layer
- `biblical_theme.<theme>`

Examples:
- `biblical_theme.image_of_god`
- `biblical_theme.stewardship`
- `biblical_theme.babel`
- `biblical_theme.covenant`

### Original-language layer
- `term.<language>.<lemma_or_key_term>`

Examples:
- `term.hebrew.tselem`
- `term.hebrew.demut`
- `term.hebrew.radah`

### Translation layer
- `translation.<translation_id>`
- `translation.<subroot>.<translation_id>` where needed for internal grouping

Examples:
- `translation.esv`
- `translation.mainstream_modern.root`

### Manuscript and textual-witness layer
- `witness.<witness_id>`
- `variant.<book>.<chapter>.<topic>` where text-critical notes need their own node

Examples:
- `witness.mt`
- `witness.lxx`
- `variant.isaiah.7.14.translation_issue`

### Noncanonical and boundary layer
- `noncanonical.<text_name>`
- `noncanonical.<subclass>.<text_name>` where the folder-level grouping needs explicit representation

Examples:
- `noncanonical.1_enoch`
- `noncanonical.pseudepigrapha.root`
- `noncanonical.forgeries_and_heretical.root`

### Graph and concordance layer
- `graph.<dataset_or_domain>`
- `graph.edge.<from>.<relation>.<to>` for governed edge objects where needed

Examples:
- `graph.verses`
- `graph.relationships`
- `graph.edge.john_1_1.echoes.genesis_1_1`

## Summary principle

The newer layers should follow the same stable, dot-delimited, semantically meaningful anchor logic as the original canon, doctrine, concept, comparison, and synthesis layers.

The goal is not to create a second anchor system. The goal is to extend the same recursive address logic across the newer ontology and graph surfaces.
