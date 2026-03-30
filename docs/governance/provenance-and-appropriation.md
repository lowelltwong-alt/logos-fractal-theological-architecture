# Provenance and Appropriation

## Purpose

This file defines how the Logos Fractal Theological Architecture repository should represent source lineage, synthesis, appropriation, adaptation, and translation burden.

The project is not only concerned with what a node says. It is also concerned with where the node comes from, how it was formed, whether it is directly derived or multi-source, and whether it carries categories borrowed from outside the Christian theological frame.

Because this repository is designed for:
- human-readable theological architecture
- semantic retrieval and RAG-style use
- recursive comparison across thinkers, doctrines, concepts, and traditions
- future ontology development
- explicit governance and vocabulary discipline

provenance is not optional metadata. It is part of the architecture itself.

## Core rule

Do not flatten source lineage into vague influence language.

When a node is meaningfully shaped by an upstream source, that relationship should be represented explicitly.

When a node is shaped by multiple sources, do not present it as if it came from only one.

When a node borrows, receives, or transforms categories from non-Christian philosophy or adjacent intellectual traditions, do not smuggle those categories in silently. Make the provenance visible.

## Why this matters

Theological architecture becomes less trustworthy when:
- synthesis is presented as if it came from a single thinker
- borrowed philosophical categories are treated as if they were native Christian doctrine without acknowledgment
- comparison assumes direct equivalence where translation is actually required
- the reader cannot tell whether a node is descriptive, synthetic, appropriated, or adaptive

This matters for both human readers and future machine use.

A retrieval system, ontology layer, or synthesis workflow can only preserve conceptual honesty if provenance has already been made explicit.

## Core provenance distinctions

The repository should distinguish at least the following forms of source relationship.

### 1. Direct derivation
Use when a node is substantially derived from one major source or one dominant upstream node.

Typical relationship verb:
- `derived_from`

Examples:
- a concept node mainly built from Augustine
- a crosswalk node substantially derived from a specific LAIRCA document
- a doctrine note strongly structured by one dominant source

Direct derivation does not mean perfect identity. It means the upstream lineage is strong enough that it should be named as primary.

### 2. Multi-source synthesis
Use when a node is intentionally built from several sources together and should not be represented as if it came from one alone.

Typical relationship verb:
- `synthesizes`

Examples:
- a synthesis node drawing from Augustine, Bavinck, and O'Donovan
- a governance application combining anthropology, prudence, and institutional accountability
- a doctrine node built from several canon figures rather than one dominant source

Synthesis should be named explicitly so the repository does not create false single-source claims.

### 3. Appropriation from outside the Christian theological frame
Use when a node borrows or receives categories, distinctions, or conceptual tools from non-Christian philosophy or adjacent intellectual traditions.

Typical relationship verb:
- `appropriates_from`

Examples:
- Augustine and Platonism
- Aquinas and Aristotelianism
- Christian theological reasoning using political or philosophical categories that did not originate inside Christian doctrine

Appropriation does not necessarily imply agreement or dependency in every respect. It means the source is materially present enough that the repository should make the borrowing visible.

### 4. Adaptation
Use when a borrowed or inherited category is not simply repeated, but revised, redirected, transformed, or theologized within a new frame.

Typical relationship verb:
- `adapts`

Examples:
- a Christian thinker revising a philosophical category for theological use
- a synthesis node taking an inherited distinction and redirecting it toward governance or AI application
- a doctrine file using an older conceptual tool in a transformed way

Adaptation should be distinguished from direct derivation because the category is not merely being carried over unchanged.

### 5. Translation burden
Use when two nodes can be compared only after translating assumptions, vocabulary, conceptual structure, or doctrinal frames.

Typical relationship verb:
- `requires_translation_to_compare`

Examples:
- Christian doctrine compared with non-Christian philosophy
- two traditions using similar terms with different metaphysical assumptions
- apparently parallel governance concepts that are not actually equivalent without interpretive work

Translation burden is especially important where superficial similarity may otherwise mislead the reader.

### 6. Alignment and misalignment
Use when the main issue is degree of conceptual or structural compatibility rather than simple derivation.

Typical relationship verbs:
- `aligns_with`
- `partially_aligns_with`
- `misaligns_with`
- `tensions_with`
- `contradicts`
- `corrects`
- `sharpens`

This repository should treat alignment language carefully. The question is not only whether two nodes look similar, but whether they actually share structure, direction, assumptions, and downstream implications.

## Recommended provenance logic in node headers

Major nodes should increasingly preserve provenance in their node headers.

Recommended fields include:
- `Derived from`
- `Synthesizes`
- `Appropriates from`
- `Translation status`
- `Alignment strength`

Example:

```markdown
**Derived from:** canon.augustine
**Synthesizes:** canon.bavinck, canon.odonovan
**Appropriates from:** philosophy.platonism
**Translation status:** requires_translation_to_compare
**Alignment strength:** moderate
```

Not every field must appear in every small node, but major nodes should increasingly carry enough provenance information to remain traceable.

## Provenance and philosophy nodes

The repository should not force non-Christian philosophy into the Christian canon branch as if it were the same kind of source object.

Instead, the architecture should support a parallel source family for non-Christian philosophical systems and traditions.

Examples of future philosophy nodes:
- `philosophy.platonism`
- `philosophy.aristotelianism`
- `philosophy.stoicism`
- `philosophy.neoplatonism`

These should be represented separately from canon thinkers so the repository can show both intersection and distinction clearly.

This allows the project to represent cases such as:
- Augustine `appropriates_from` Platonism
- Augustine `adapts` Platonic categories
- Augustine `misaligns_with` some Platonic assumptions
- comparison between Christian theology and philosophy that `requires_translation_to_compare`

## Provenance and Christian canon thinkers

Christian canon thinkers should not be treated as isolated or contextless.

Where relevant, the repository should explicitly note:
- when a thinker is deeply shaped by earlier Christian tradition
- when a thinker synthesizes several sources internally
- when a thinker appropriates from non-Christian philosophy
- when a thinker adapts or transforms inherited categories
- when the relationship to an external source is partial, corrective, or misaligned rather than simply derivative

This is especially important for major anchor figures whose work is often described too simplistically.

## Provenance and doctrine nodes

Doctrine nodes should also preserve provenance where meaningful.

A doctrine node may be:
- strongly derived from one source tradition
- synthesized from several theologians
- indebted to categories partly shaped by philosophy
- comparable across traditions only with translation

Do not assume doctrine nodes are self-originating just because they are stable objects in the repository.

## Provenance and synthesis nodes

Synthesis nodes are the most likely place for provenance confusion, because synthesis often combines several thinkers, doctrines, and concepts into one repository-level argument.

Because of that, synthesis nodes should be especially careful to:
- name their major upstream sources
- distinguish direct derivation from synthesis
- identify non-Christian appropriations where relevant
- disclose translation burden where conceptual vocabulary does not carry over directly

A synthesis node should never be allowed to masquerade as a pure single-source artifact when it is actually multi-source.

## What not to do

Avoid:
- vague language such as “influenced by” when a more exact relationship is available
- pretending multi-source synthesis came from one thinker
- silently importing philosophy into theology without acknowledgment
- treating borrowed categories as native without explanation
- assuming comparison is direct when translation is actually required
- using provenance fields performatively without real explanatory value

## Decision rule for contributors

When working on a node, ask:

1. Is this mainly derived from one major source?
2. Is this actually synthesizing several sources?
3. Is this borrowing from non-Christian philosophy or another external framework?
4. Is the borrowed material merely received, or actively adapted?
5. Does comparison require translation before judgment can be made?
6. Would a future reader or AI system misunderstand the lineage if I leave it implicit?

If the answer to any of those questions is yes, make the provenance explicit.

## Relationship to the rest of governance

This file should be read together with:
- `docs/governance/README.md`
- `docs/governance/ontology-discipline.md`
- `docs/governance/anchor-conventions.md`
- `docs/governance/tag-registry.md`
- `docs/governance/relationship-registry.md`
- `docs/governance/node-types.md`
- `docs/governance/node-header-template.md`

## Summary principle

The repository should preserve not only meaning, but lineage.

It should distinguish:
- derivation from synthesis
- synthesis from appropriation
- appropriation from adaptation
- alignment from misalignment
- direct comparison from translation-required comparison

That is the discipline required for a theological architecture that wants to remain honest, reusable, ontology-ready, and intellectually serious.
