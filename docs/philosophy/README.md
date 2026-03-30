# Philosophy and External Source Traditions

## Purpose

This folder defines the philosophy layer for the Logos Fractal Theological Architecture repository.

The philosophy layer exists to house non-Christian philosophical sources, schools, conceptual traditions, and adjacent intellectual frameworks that materially intersect with the theological architecture of the project.

This branch does not exist to replace the Christian canon layer. It exists to make non-Christian influence, appropriation, adaptation, comparison, and misalignment explicit rather than leaving them hidden inside Christian nodes.

This is therefore not a generic philosophy survey and not a loose collection of background influences. It is a governed source architecture for external conceptual traditions.

The philosophy branch should help answer questions such as:
- which non-Christian philosophical traditions materially influence Christian thinkers or doctrine nodes in the repository
- where Christian theology appropriates, adapts, corrects, or misaligns with external philosophical systems
- which philosophical categories are repeatedly useful enough to deserve stable treatment
- where comparison requires translation rather than simple alignment language
- which concepts belong as reusable philosophy or concept nodes rather than remaining buried inside canon thinker pages

## Why this branch matters

A theological architecture becomes less intellectually honest when non-Christian philosophical influence is left implicit.

Christian thinkers often interact deeply with philosophical traditions without simply collapsing into them. If the repository wants to preserve lineage, synthesis, translation burden, and conceptual honesty, it needs a clean structural place for those external source traditions.

Because this repository is designed for:
- human-readable theological architecture
- semantic retrieval and RAG-style use
- recursive comparison across thinkers, doctrines, concepts, and traditions
- future ontology development
- governed provenance and vocabulary discipline

the philosophy branch is not optional background. It is part of the repository’s larger source architecture.

## Dominant node type

The dominant node type in this folder should be:

- `philosophy_node`

This node family should be used for major non-Christian philosophical source systems, schools, or recurring external conceptual traditions that materially affect the project.

Examples may include:
- Platonism
- Aristotelianism
- Stoicism
- Neoplatonism
- modern political liberalism
- utilitarianism
- existentialism
- secular humanism

A philosophy node should normally explain:
- what the philosophical source is
- why it matters for this repository
- where it intersects with Christian theology
- where it is appropriated, adapted, corrected, or resisted
- where comparison is direct and where translation is required
- which canon thinkers, doctrine nodes, or synthesis nodes most strongly interact with it

If a recurring category appears across several philosophy nodes and Christian files, it should eventually be considered for promotion into a `concept_node`.

## Philosophy inclusion logic

Do not treat external philosophy as automatically opposed to Christian theology, and do not treat it as automatically harmonious.

A philosophy node may function as:
- a major external source tradition
- a recurring conceptual background
- an appropriated category source
- a comparative framework
- a tension-producing or misaligned system
- a historical bridge requiring careful translation

That distinction should be made explicit in the file itself or through controlled tags.

## Why this branch should remain separate from canon

Christian canon thinkers and non-Christian philosophical traditions are not the same kind of architectural object in this repository.

The canon branch names Christian theological source anchors internal to the project’s theological architecture.
The philosophy branch names external intellectual traditions that may influence, challenge, structure, or illuminate parts of that architecture.

Keeping these branches distinct allows the repository to say things like:
- Augustine `appropriates_from` Platonism
- Augustine `adapts` Platonic categories
- Augustine `misaligns_with` some Platonic assumptions
- Aquinas `appropriates_from` Aristotelianism
- a doctrine node `requires_translation_to_compare` with Stoic or liberal categories

That is much cleaner than forcing all of those relationships into the canon layer.

## Anchor conventions for philosophy nodes

Philosophy files should follow a philosophy anchor family.

Preferred pattern:
- `philosophy.<tradition_or_system>`
- `philosophy.<tradition_or_system>.<subconcept>`

Examples:
- `philosophy.platonism`
- `philosophy.platonism.forms`
- `philosophy.aristotelianism`
- `philosophy.stoicism`
- `philosophy.utilitarianism`

These anchors should remain:
- lowercase
- dot-delimited
- stable
- semantically meaningful

Do not improvise alternative anchor families casually.

## Tag conventions for philosophy nodes

Philosophy nodes should use controlled tags from `docs/governance/tag-registry.md`, and the tag registry should eventually expand to include philosophy-tag families where needed.

Typical tags may include:
- `concept.*` tags where recurring concepts are already governed
- future `philosophy.*` tags where the registry formally adds them
- comparison-oriented tags where useful
- AI-project tags where a philosophy node is especially important for governance, agency, or work

Examples of likely future tags:
- `philosophy.platonism`
- `philosophy.aristotelianism`
- `philosophy.stoicism`
- `ai.governance`
- `ai.agency`
- `concept.public_reason`
- `concept.institutions`

Do not over-tag. Use the smallest set of tags that improves retrieval and comparison.

## Relationship conventions for philosophy nodes

Philosophy files should prefer approved relationship verbs from `docs/governance/relationship-registry.md`.

Most important relationship verbs for this branch will likely include:
- `aligns_with`
- `partially_aligns_with`
- `misaligns_with`
- `tensions_with`
- `corrects`
- `sharpens`
- `requires_translation_to_compare`
- `appropriates_from`
- `adapts`
- `related_to`

Typical uses:
- a canon thinker may `appropriates_from` a philosophy node
- a doctrine node may `requires_translation_to_compare` with a philosophy node
- a synthesis node may `adapts` an inherited philosophical distinction
- a Christian node may `corrects` or `misaligns_with` an external source where the overlap is partial rather than total

## Node header requirement

Philosophy nodes should normally use the governed node header pattern documented in:

- `docs/governance/node-header-template.md`

A typical philosophy node should begin with a block such as:

```markdown
**Node type:** philosophy_node  
**Anchor:** philosophy.platonism  
**Tags:** concept.creation_order, concept.public_reason, ai.governance  
**Key relationships:** appropriates_from, adapts, requires_translation_to_compare, misaligns_with  
**Status:** working  
**Parent:** docs/philosophy/README.md  
**Related nodes:** canon.augustine, doctrine.anthropology, concept.ordered_love  
**Derived from:** none  
**Synthesizes:** none  
**Appropriates from:** none  
**Translation status:** requires_translation_to_compare  
**Alignment strength:** mixed
```

## Philosophy node architecture

Philosophy nodes should begin as strong single-file nodes.

Preferred live pattern:
- `docs/philosophy/<name>.md`

Examples:
- `docs/philosophy/platonism.md`
- `docs/philosophy/aristotelianism.md`
- `docs/philosophy/stoicism.md`

A philosophy node should stay as a single file as long as it remains one coherent retrieval object.

If a philosophical source becomes dense enough to justify recursive expansion, it may later be promoted into a folder using a stable recursive shell such as:

- `docs/philosophy/<name>/README.md`
- `docs/philosophy/<name>/artifact.json`
- `docs/philosophy/<name>/sources-and-lineage.md`
- `docs/philosophy/<name>/core-claims.md`
- `docs/philosophy/<name>/christian-intersections.md`
- `docs/philosophy/<name>/appropriation-and-adaptation.md`
- `docs/philosophy/<name>/ai-governance-implications.md`
- `docs/philosophy/<name>/notes.md`

The rule is:

**let complexity earn structure**

## What this folder should produce over time

A mature philosophy branch should make it possible to:
- represent non-Christian influence honestly
- compare philosophical and theological systems without flattening them
- preserve translation burden where direct comparison is misleading
- identify where Christian thinkers borrow, adapt, or resist external categories
- support retrieval and ontology work without forcing all conceptual lineage into the canon branch

## Related governance files

This branch should be read alongside:
- `docs/governance/README.md`
- `docs/governance/ontology-discipline.md`
- `docs/governance/relationship-registry.md`
- `docs/governance/node-types.md`
- `docs/governance/node-header-template.md`
- `docs/governance/provenance-and-appropriation.md`

## Summary principle

The philosophy branch should remain structurally distinct from the Christian canon branch while still being tightly integrated into the repository’s provenance, comparison, and ontology logic.

Christian theology should not silently absorb philosophy.
Philosophy should not be treated as identical to Christian source architecture.
The relationship should be made explicit, governed, and reusable.
