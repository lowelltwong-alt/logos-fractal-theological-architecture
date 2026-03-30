# Concordance Design Decisions

## Purpose

This document explains the major design decisions behind the concordance architecture and why those decisions were chosen.

It exists so future contributors do not merely copy the structure, but understand the reasoning behind it.

The goal is consistency of judgment, not only consistency of formatting.

## Decision 1. Build a graph, not a giant concordance file

### Decision
The concordance should be built as a graph of typed nodes and typed relationships rather than as one flat master concordance.

### Why
A giant concordance file is easy to browse at first, but it becomes hard to:
- review
- audit
- diff
- validate
- extend semantically
- protect against poisoning

A graph architecture makes it easier to:
- reuse stable objects
- connect many object types
- preserve provenance edge by edge
- review claims at a finer grain

### Strong opinion
This is the most important design decision in the whole concordance branch.

If the project gets this wrong, everything else becomes much harder later.

## Decision 2. Separate canonical verse identity from translation witnesses

### Decision
A verse node should represent a stable canonical verse reference, not one specific translation rendering.

### Why
A verse is not identical to one English wording.

If translation renderings are fused into the verse node, the system becomes much less useful for:
- cross-translation comparison
- language analysis
- translation burden notes
- import of multiple translation witnesses

### Strong opinion
This separation is non-negotiable if the concordance is meant to be machine-readable and durable.

## Decision 3. Separate concepts, doctrines, topics, and entities

### Decision
Concept nodes, doctrine nodes, topic nodes, and entity nodes should remain distinct.

### Why
A broad topic is not the same thing as a reusable concept.
A doctrine is not the same thing as a theme.
A person is not the same thing as an interpretive category.

If these are collapsed, the ontology becomes muddy and the machine cannot tell what kind of thing it is traversing.

### Strong opinion
The temptation to flatten should be resisted early.
Flattening feels simpler only until the graph becomes large.
Then it becomes a major cleanup problem.

## Decision 4. Treat interpretation as a separate layer, not as invisible truth

### Decision
Tradition-specific readings, doctrinal claims, and theological interpretations should be modeled as interpretive objects or claims, not silently baked into the source-text layer.

### Why
A verse node should not quietly carry one theological conclusion as if it were the only reading.

Interpretation may be strong, ancient, persuasive, and central. It still needs to be represented as interpretation rather than hidden as neutral fact when appropriate.

### Strong opinion
This distinction is essential both for accuracy and for trust. It makes the system more honest and less vulnerable to ideological capture.

## Decision 5. Keep non-Christian philosophy structurally distinct from Christian source architecture

### Decision
Non-Christian philosophy should live in its own branch and node family rather than being folded into Christian canon by default.

### Why
Christian theology often appropriates, adapts, corrects, or misaligns with philosophy. Those are not the same relationship.

If philosophy is hidden inside Christian nodes without clear provenance, the architecture becomes less truthful and less reusable.

### Strong opinion
This is one of the most intellectually important decisions in the whole repository.
It protects the project from quietly baptizing borrowed categories without explanation.

## Decision 6. Require provenance on meaningful assertions

### Decision
The concordance should preserve provenance not only for source texts, but for major conceptual and interpretive assertions.

### Why
Without provenance, the graph becomes hard to trust.
A user or machine should be able to ask:
- where did this link come from
- who asserted it
- what source supported it
- whether it was imported, proposed, reviewed, or stabilized

### Strong opinion
Provenance is not metadata garnish. It is part of the truthfulness of the system.

## Decision 7. Use trust layers explicitly

### Decision
The graph should explicitly separate imported, proposed, reviewed, and canonical states.

### Why
A multi-contributor concordance will eventually contain bad links, naive links, overstated doctrinal claims, and possibly malicious edits.

Trust status makes it possible to:
- grow quickly without pretending unreviewed material is settled
- welcome contribution without surrendering quality
- let machines see confidence and review state explicitly

### Strong opinion
This is not bureaucracy. It is the minimum architecture needed for scale without corruption.

## Decision 8. Prefer qualitative trust and alignment scales before numeric scoring

### Decision
Use governed qualitative values such as high, moderate, low, mixed, or not applicable before introducing numeric agreement or confidence scores.

### Why
Numeric scoring looks precise, but often creates false exactness too early.
The project is better served first by:
- explicit relationship type
- explicit provenance
- explicit translation burden
- explicit review state
- explicit alignment strength

### Strong opinion
Do not rush into decimals. Most projects that do this too early build a fake sense of rigor.

## Decision 9. Separate imported source data from approved graph data

### Decision
External concordances, lexicons, or datasets should be imported into source or staging layers before being normalized into approved graph objects.

### Why
An imported dataset is useful, but it is not automatically canonical.
This separation allows:
- bulk ingestion
- controlled review
- source comparison
- rollback if needed

### Strong opinion
Imported data should be treated as candidate input, not as trusted final structure.

## Decision 10. Let complexity earn structure

### Decision
Start with strong single-node files and promote to deeper recursive folders only when density, reuse, or metadata burden justifies it.

### Why
Premature folder complexity creates empty architecture.
No structure creates chaos.

The repository’s fractal rule is the right middle path:
keep the shell stable, then deepen only when needed.

### Strong opinion
This rule should govern the concordance branch just as strongly as the theology branches.

## Decision 11. Optimize for future AI traversal, not only present human reading

### Decision
The concordance should be easy for a machine to traverse safely, not only pleasant for a person to browse.

### Why
This project is explicitly aiming for machine readability, semantic retrieval, ontology growth, and future AI use.
That means the structure must support:
- stable ids
- typed relationships
- explicit provenance
- review state
- machine-meaningful distinctions among object kinds

### Strong opinion
If forced to choose, prioritize machine-safe clarity over casual human convenience. Human readability still matters, but the machine layer is the harder thing to retrofit later.

## Decision 12. Use the concordance as an ontology seed, not just an index

### Decision
The concordance should be designed so repeated concepts, motifs, entities, and interpretive patterns can later become reusable ontology objects.

### Why
A well-built concordance is not just an index of verses. It becomes a map of the conceptual universe the repository is building.

### Strong opinion
This is the highest long-term value of the branch. The concordance is one of the best possible places to grow a serious Christian knowledge graph over time.

## Summary principle

The concordance should not be built for short-term convenience alone.

It should be built as if:
- many contributors will use it
- machines will query it
- errors will accumulate unless constrained
- bad actors may try to poison it
- future ontology growth will depend on what is done now

That means the architecture should favor:
- typed nodes
- typed relationships
- explicit provenance
- strong trust layers
- clear separation of source text, interpretation, philosophy, and doctrine
- stable recursive structure
