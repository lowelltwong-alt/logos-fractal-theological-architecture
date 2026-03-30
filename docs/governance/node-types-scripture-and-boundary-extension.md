# Node Types Extension: Scripture, Translation, Manuscript, and Boundary Layers

## Purpose

This file extends the main node type registry for the scripture, interpretation, hermeneutic, translation, manuscript, original-language, and noncanonical boundary-source layers.

It should be read together with:
- `docs/governance/node-types.md`
- `docs/governance/scripture-taxonomy-and-ontology.md`
- `docs/governance/textual-traditions-translation-and-noncanonical-sources.md`

## Approved extension node types

### `scripture_root`
Use for the entry node of the scripture layer.

### `scripture_book`
Use for a biblical book as a whole.

### `scripture_chapter`
Use for chapter-level nodes.

### `pericope_node`
Use for meaningful interpretive units larger than one verse.

### `scripture_text`
Use for an exact passage or verse cluster.

### `interpretation_node`
Use for a particular reading of a passage.

### `hermeneutic_root`
Use for the entry node of the hermeneutic layer.

### `hermeneutic_node`
Use for a hermeneutic method or interpretive approach.

### `biblical_theme_root`
Use for the entry node of the biblical themes layer.

### `biblical_theme_node`
Use for recurring themes that connect multiple texts.

### `translation_root`
Use for the entry node of the translation layer.

### `translation_subroot`
Use for subfolders such as ancient versions, mainstream modern, or sectarian and disputed.

### `translation_witness`
Use for a specific Bible translation or version.

### `original_language_root`
Use for the entry node of the original-language layer.

### `original_language_term`
Use for lexical nodes in Hebrew, Aramaic, or Greek.

### `manuscripts_root`
Use for the entry node of the manuscript layer.

### `manuscript_witness`
Use for manuscript or textual-tradition witnesses.

### `text_critical_note`
Use for textual variants and text-critical notes.

### `noncanonical_root`
Use for the entry node of the noncanonical boundary layer.

### `noncanonical_subroot`
Use for deuterocanonical, pseudepigraphal, or forged/heretical subfolders.

### `noncanonical_text`
Use for a specific noncanonical text node.

## Summary principle

These node types should be preferred over improvised local labels whenever the repository is handling biblical text, interpretation, translation, manuscript tradition, or noncanonical boundary material.
