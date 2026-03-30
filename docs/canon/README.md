# Canon and Source Map

## Purpose

This folder defines the canon layer for the Logos Fractal Theological Architecture repository.

The canon layer identifies the major theological voices, traditions, and source figures that shape the rest of the project. It exists to clarify which thinkers are functioning as upstream sources for doctrine, concept formation, comparison, derivation, governance reasoning, and downstream AI- and institution-related applications.

This is not a general reading list and not a loose historical survey. It is a governed source architecture.

The canon branch should help answer questions such as:
- which thinkers belong in the shared core of the project
- which thinkers belong in optional overlays or comparative branches
- which doctrine areas are most shaped by each thinker
- where major alignments, tensions, and translation problems appear
- which recurring concepts should remain embedded in thinker nodes and which should eventually become reusable concept nodes

## Why this branch matters

The rest of the repository depends on upstream theological sources. Doctrine nodes, synthesis files, comparisons, ordering profiles, weighting profiles, and application examples all become weaker if the canon layer is vague, unstable, or casually expanded.

Because this repository is designed for:
- human-readable theological architecture
- semantic retrieval and RAG-style use
- recursive buildout
- future ontology promotion

the canon branch must remain structurally disciplined.

Canon is not just background. It is part of the repository’s governing architecture.

## Dominant node type

The dominant node type in this folder is:

- `canon_thinker`

Use `canon_thinker` for major source figures whose thought significantly shapes the project.

Examples:
- Augustine
- Athanasius
- Aquinas
- Calvin
- Bavinck
- Kuyper

A canon thinker node should normally explain:
- why the thinker belongs in the project
- what theological contributions make the thinker important here
- which doctrine areas are most influenced by the thinker
- what governance, institutional, or AI-era implications may follow
- what strengths the thinker brings
- what tensions or cautions matter in using the thinker

If a recurring concept appears across multiple thinker files, it should eventually be considered for promotion into a `concept_node` rather than remaining buried only inside thinker pages.

## Canon inclusion logic

Do not confuse source inclusion with equal authority or equal usefulness.

A thinker may be included as:
- shared core
- foundational but non-core
- major supporting
- optional overlay
- comparative only

That distinction should be made explicit in the file itself or through controlled tags.

The canon branch should remain broad enough for serious Christian reuse while still being disciplined enough to support comparison and downstream reasoning.

## Recommended shared core

The default shared core should remain broad, serious, and reusable across the main architecture of the project.

These are the figures that should function as the primary canon anchors unless and until the project formally revises the core:

- Irenaeus
- Athanasius
- Augustine
- Thomas Aquinas
- John Calvin
- Herman Bavinck
- Abraham Kuyper
- John Stott
- J. I. Packer
- Francis Schaeffer
- Tim Keller
- Oliver O'Donovan
- Dallas Willard
- Henri Nouwen

These figures should normally carry the greatest weight in the shared canon layer because they are the most likely to shape doctrine nodes, synthesis work, derivations, governance reasoning, and downstream project architecture across multiple branches.

## Important non-core or overlay figures

The following figures may still be highly important to the project, but should not automatically be treated as shared-core anchors unless a specific branch, tradition, comparison, or use case requires it.

These figures may function as:
- supporting voices
- optional overlays
- comparative figures
- branch-specific anchors
- use-case-specific theological contributors

Examples include:
- Jonathan Edwards
- C. S. Lewis
- Lesslie Newbigin
- John Piper
- Wayne Grudem
- N. T. Wright

These figures may become very important in particular parts of the repository, but they should be tagged or framed as non-core, overlay, or comparative unless the project explicitly promotes them into the shared core later.

## Optional overlays

Optional overlays may be used for:
- Reformed emphasis
- evangelical emphasis
- Anglican emphasis
- patristic retrieval emphasis
- ministry or nonprofit emphasis
- institution-specific doctrinal commitments
- comparative traditions not intended to function as shared-core anchors

Overlay use should be explicit rather than implied.

## Anchor conventions for canon nodes

Canon files should follow the canon anchor family defined in `docs/governance/anchor-conventions.md`.

Preferred pattern:
- `canon.<thinker>`
- `canon.<thinker>.<concept>`

Examples:
- `canon.augustine`
- `canon.augustine.creation_order`
- `canon.augustine.two_cities`
- `canon.bavinck.creation`
- `canon.kuyper.common_grace`

Do not invent alternative anchor patterns casually.

## Tag conventions for canon nodes

Canon nodes should use controlled tags from `docs/governance/tag-registry.md`.

Typical canon node tags may include:
- thinker tags, such as `thinker.augustine`
- tradition tags, such as `tradition.patristic`
- era tags, such as `era.patristic`
- node-role tags, such as `canon.primary`
- concept tags, such as `concept.creation_order`, `concept.ordered_love`, or `concept.two_cities`
- AI-project tags where relevant, such as `ai.governance` or `ai.work`

Do not over-tag. Use the smallest meaningful set of tags that improves retrieval and comparison.

## Relationship conventions for canon nodes

Canon files should prefer approved relationship verbs from `docs/governance/relationship-registry.md`.

Most common relationship verbs for canon work will likely be:
- `grounds`
- `sharpens`
- `constrains`
- `aligns_with`
- `partially_aligns_with`
- `tensions_with`
- `corrects`
- `requires_translation_to_compare`
- `translates_into`

Do not casually substitute uncontrolled synonyms like:
- agrees with
- fits with
- kind of opposes
- influences

If an approved relationship verb fits, use it.

## Canon node architecture

Canon nodes should begin as strong single-file nodes.

Preferred live pattern:
- `docs/canon/<name>.md`

Examples:
- `docs/canon/augustine.md`
- `docs/canon/bavinck.md`
- `docs/canon/kuyper.md`

A canon node should stay as a single file as long as it remains one coherent retrieval object.

If a thinker becomes dense enough to justify recursive expansion, the node may be promoted into a folder using the canon architecture pattern documented in:
- `docs/canon/NODE_ARCHITECTURE.md`

Typical promoted form:
- `docs/canon/<name>/README.md`
- `docs/canon/<name>/artifact.json`
- `docs/canon/<name>/sources-and-lineage.md`
- `docs/canon/<name>/core-theology.md`
- `docs/canon/<name>/creation-fall-redemption.md`
- `docs/canon/<name>/governance-and-institutions.md`
- `docs/canon/<name>/ai-governance-implications.md`
- `docs/canon/<name>/notes.md`

The rule is:
**let complexity earn structure**

## When a recurring concept should become its own node

A repeated concept should be considered for promotion into a `concept_node` when:
- it recurs across multiple thinkers
- it matters to the architecture
- it supports comparison or derivation
- keeping it buried in thinker pages makes retrieval or comparison harder

Examples of concepts likely to deserve promotion over time:
- imago Dei
- ordered love
- institutions
- vocation
- grace
- public theology
- creation order
- two cities
- prudence

## Design rule for contributors

When adding a new thinker or expanding an existing one, follow this order:

1. model the new source as a canon thinker node first  
2. fit it into existing anchor, tag, and relationship vocabulary where possible  
3. promote repeated concepts into reusable concept nodes only when recurrence justifies it  
4. promote a thinker into a recursive folder only when density and reuse justify it  
5. avoid structural redesign unless the current shell cannot represent the material without distortion  

## What this folder should produce over time

A mature canon branch should make it possible to:
- identify core thinkers quickly
- compare thinkers cleanly
- surface repeated concepts across thinkers
- support doctrine and synthesis branches with stable upstream sources
- prepare selected concepts for ontology promotion
- support retrieval without uncontrolled naming drift

## Related governance files

This branch should be read alongside:
- `docs/governance/README.md`
- `docs/governance/ontology-discipline.md`
- `docs/governance/anchor-conventions.md`
- `docs/governance/tag-registry.md`
- `docs/governance/relationship-registry.md`
- `docs/governance/node-types.md`
- `docs/canon/NODE_ARCHITECTURE.md`

## Summary principle

The canon branch should stay theologically rich, structurally disciplined, and ontologically extensible.

The shell should stay stable.
The thinker nodes can grow.
Repeated concepts can become reusable trunks of their own.
