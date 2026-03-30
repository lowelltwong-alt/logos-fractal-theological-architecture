# Anchor Conventions

## Purpose

Anchors make the repository traversable for both humans and machines.

They should be stable, predictable, and semantically meaningful.

Anchors are not decorative labels. They are part of the retrieval and ontology architecture.

## General rules

Anchors should be:
- lowercase
- dot-delimited
- stable over time
- short enough to remain usable
- descriptive enough to remain clear

Avoid:
- spaces
- random abbreviations
- inconsistent separators
- casual renaming after a node becomes established

## Anchor families

Use these anchor families as defaults.

### Canon thinker nodes
- `canon.<thinker>`
- `canon.<thinker>.<concept>`

Examples:
- `canon.augustine`
- `canon.augustine.creation_order`
- `canon.aquinas.natural_law`

### Doctrine nodes
- `doctrine.<doctrine_name>`
- `doctrine.<doctrine_name>.<subconcept>`

Examples:
- `doctrine.anthropology`
- `doctrine.anthropology.imago_dei`

### Concept nodes
- `concept.<concept_name>`
- `concept.<concept_name>.<subconcept>`

Examples:
- `concept.grace`
- `concept.institutions`
- `concept.public_reason`

### Comparison nodes
- `comparison.<node1>_<node2>.<topic>`

Examples:
- `comparison.augustine_aquinas.order`
- `comparison.calvin_wesley.formation`

### Tradition nodes
- `tradition.<tradition_name>`
- `tradition.<tradition_name>.<topic>`

Examples:
- `tradition.reformed`
- `tradition.orthodox.theosis`

### Synthesis nodes
- `synthesis.<theme>`
- `synthesis.<theme>.<subtheme>`

Examples:
- `synthesis.christian_ai_anthropology`
- `synthesis.ai_governance_limits`

## Stability rule

Once an anchor is established and linked elsewhere, it should be treated as stable.

Do not rename anchors casually.

If a change is absolutely necessary, update all known references at the same time.

## Granularity rule

Make anchors specific enough to support retrieval, but not so narrow that they become noise.

Good:
- `canon.augustine.sin`
- `canon.augustine.two_cities`

Too broad:
- `canon.augustine.stuff`

Too narrow unless truly needed:
- `canon.augustine.sin.paragraph3.line2`

## Extension rule

When in doubt:
1. use an existing family
2. create a stable node-level anchor
3. add subanchors only if the concept is likely to recur or be retrieved separately

## Summary principle

Anchors should make the structure more legible, not more improvised.

They are part of the recursive skeleton of the project.
