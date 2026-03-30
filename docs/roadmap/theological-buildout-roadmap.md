# Theological Buildout Roadmap

## Purpose

This file gives contributors a practical roadmap for building out the theological architecture of the repository.

It answers three questions:

1. Which thinkers and traditions should be built first?
2. In what order should they be added?
3. What should each thinker page include so the project stays recursive, comparable, and ontology-ready?

This file should be read alongside:
- `README.md`
- `docs/governance/README.md`
- `docs/governance/ontology-discipline.md`
- `docs/governance/anchor-conventions.md`
- `docs/governance/tag-registry.md`
- `docs/governance/relationship-registry.md`
- `docs/governance/node-types.md`
- `docs/roadmap/repository-integration-map.md`

## Important scope note
This repository also now includes a future primary-sources expansion for witnesses, fragments, transcriptions, passage reconstructions, lexical evidence, and translation comparison. That future branch runs alongside the theological buildout and is meant to support deeper textual, lexical, and translation-aware grounding for later doctrine, concept, and synthesis work.

This roadmap is primarily about the theological buildout of:
- canon thinkers
- doctrine nodes
- concept nodes
- comparison nodes
- synthesis nodes

It now sits inside a wider repository that also includes:
- scripture-layer nodes
- original-language nodes
- translation and manuscript control layers
- biblical themes
- noncanonical boundary handling
- graph and concordance surfaces

Those wider layers do not replace this roadmap. They support and extend it.

For the repo-wide relationship between those layers, see:

- `docs/roadmap/repository-integration-map.md`

## Guiding principle

The project should not grow as a random collection of theologian notes.

It should grow as a structured theological architecture in which:
- major thinkers become canon nodes
- repeated concepts become concept nodes
- traditions become tradition nodes
- alignments and tensions become comparison nodes
- synthesis pages integrate multiple upstream nodes into project-level arguments

## Recommended build order

The build order should balance four needs:
- theological depth
- cross-tradition usefulness
- relevance to AI, governance, anthropology, and institutions
- future ontology value

## Phase 1: first-ring foundational thinkers

These are the strongest starting pillars because they provide major architectural categories for the project.

### 1. Augustine
Why first:
- anthropology
- interiority
- sin and disordered love
- grace
- institutions
- the two cities
- limits of earthly systems

### 2. Aquinas
Why early:
- creation as intelligible order
- reason and revelation
- natural law
- metaphysics
- public moral reasoning

### 3. Athanasius
Why early:
- Christological precision
- incarnation
- doctrinal coherence
- theological stability at the source level

### 4. Calvin
Why early:
- Protestant system-building
- sovereignty
- institutions
- discipline
- vocation
- governance seriousness

## Phase 2: second-ring expansion thinkers

These deepen the architecture and widen denominational usefulness.

### 5. Wesley
Why:
- sanctification
- method and formation
- disciplined spiritual growth
- practical system-building

### 6. Jonathan Edwards
Why:
- will
- affections
- philosophical theology
- evangelical rigor
- moral psychology

### 7. Luther
Why:
- vocation
- bondage of the will
- critique of self-justifying systems
- limits of moral self-repair

### 8. Gregory of Nyssa or Maximus the Confessor
Why:
- stronger Orthodox depth
- personhood
- participation
- transformation
- desire and sanctification/theosis themes

## Phase 3: third-ring comparative and public-theology buildout

These deepen the ontology and help with pluralism, institutions, and modern translation.

### 9. Turretin
Why:
- precision
- scholastic clarity
- formal distinctions
- Reformed conceptual discipline

### 10. Irenaeus
Why:
- recapitulation
- formation
- embodied humanity
- anti-reductionism

### 11. Barth
Why:
- Christ-centered revelation
- limits of natural theology
- critique of human systems claiming too much

### 12. Kuyper
Why:
- sphere sovereignty
- institutions
- pluralism
- public theology

### 13. O'Donovan
Why:
- moral order
- political theology
- authority and public reasoning

### 14. Ellul or Niebuhr
Why:
- technology critique
- power
- modern systems
- realism about institutions

## Phase 4: tradition-bridge and modern translator layer

These do not replace the core canon, but they help connect the architecture to modern institutional questions.

Possible additions:
- Tim Keller
- Dallas Willard
- Henri Nouwen
- Oliver O'Donovan if not already built earlier
- Jacques Ellul if not already built earlier
- modern Orthodox or Catholic translators where needed

## Suggested first practical sequence

If contributors need a concrete first queue, use this order:

1. Augustine
2. Aquinas
3. Athanasius
4. Calvin
5. concept.imago_dei
6. concept.grace
7. concept.institutions
8. concept.work
9. Wesley
10. Edwards
11. Luther
12. Gregory of Nyssa or Maximus
13. first comparison nodes
14. first synthesis nodes

## Scripture and source-control interaction

The repository now also includes a wider supporting buildout in:
- scripture
- original-language terms
- translations
- manuscripts
- biblical themes
- noncanonical and heresy boundary layers
- graph and concordance work

Those layers should increasingly support this theological buildout by:
- grounding doctrine in text
- preserving lexical nuance
- clarifying translation and manuscript assumptions
- distinguishing canonical from noncanonical authority
- making important connections machine-readable

This roadmap does not try to sequence every one of those supporting layers in detail. It focuses on the theological buildout proper while acknowledging that the repository now has a broader ontological surface.

## What each thinker page should include

Every thinker page should follow a repeatable pattern so comparison and retrieval stay strong.

## Required sections for each thinker node

### 1. Why this thinker belongs in the project
Explain why the thinker matters specifically for this repository.

### 2. Core works most relevant to this project
List the primary texts most useful for the node.

### 3. Creation / metaphysics / order
What does this thinker say about reality, order, intelligibility, or creation?

### 4. Human person / anthropology / imago Dei
What is a human being in this thinker’s framework?

### 5. Sin / fallenness / pride / corruption
What goes wrong in persons and institutions?

### 6. Grace / redemption / transformation
What restores, heals, or reorders?

### 7. Work / vocation / labor / participation
How should human work, responsibility, and creaturely action be understood?

### 8. Institutions / governance / power / public order
What does the thinker contribute to institutional reasoning?

### 9. Public theology / translation / pluralism
How does this thinker help or resist public-facing translation?

### 10. AI / governance relevance
What does this thinker especially help the project see?

### 11. Alignment map
Explicitly list:
- aligns_with
- partially_aligns_with
- tensions_with
- contradicts
- corrects
- sharpens
- requires_translation_to_compare

### 12. Retrieval map
Break the thinker into semantic chunks appropriate for retrieval and recursive reuse.

### 13. Gaps / limitations
Where is this thinker less useful, weaker, or in need of supplementation?

### 14. Suggested child nodes
List the likely subnodes if the thinker needs deeper buildout.

## Recommended semantic chunking pattern for thinker pages

To support RAG, retrieval, and recursive ontology growth, thinker pages should be chunked into semantically meaningful sub-sections such as:
- creation_order
- anthropology
- sin_and_pride
- grace_and_redemption
- work_and_vocation
- institutions_and_power
- public_theology

If a concept becomes dense enough to deserve reuse across the project, promote it into a child node or shared concept node.

## What to add when more information becomes necessary

When new information or connections become necessary, use this order:

1. add detail inside the existing thinker section if the concept remains local
2. create a child node if the concept becomes independently meaningful
3. create or reuse a concept node if the concept appears across multiple thinkers
4. create a comparison node if the new material is mainly about alignment or tension
5. create a synthesis node if the new material integrates multiple upstream nodes into a project-level claim

## Contributor checklist for each thinker page

Use this checklist before considering a thinker page mature.

### Minimum completeness checklist
- [ ] thinker has a stable anchor
- [ ] thinker has approved tags
- [ ] thinker has a clear inclusion rationale
- [ ] thinker has core texts listed
- [ ] thinker has sections for order, anthropology, sin, grace, work, institutions, public theology, and AI relevance
- [ ] thinker has at least one explicit alignment or tension mapping
- [ ] thinker has retrieval chunks identified
- [ ] thinker has at least one stated limitation or gap
- [ ] thinker has likely child nodes named

### Stronger completeness checklist
- [ ] thinker is linked to at least two shared concept nodes
- [ ] thinker is linked to at least one comparison node
- [ ] repeated concepts have been promoted where appropriate
- [ ] public theology or translation implications are named explicitly
- [ ] downstream AI or governance relevance is stated clearly rather than implied

## Concept promotion rule

If a concept appears in multiple thinker pages and remains important across the project, it should usually become a shared concept node.

Examples:
- imago Dei
- grace
- institutions
- ordered love
- natural law
- vocation
- public reason
- two cities
- theosis

## Comparison roadmap

Once the first 4 to 6 major thinkers are built, begin adding explicit comparison nodes.

Recommended early comparison pages:
- Augustine vs Aquinas on order
- Augustine vs Calvin on sin and grace
- Calvin vs Wesley on formation and sanctification
- Augustine, Calvin, and Edwards on the will
- Aquinas vs Barth on reason and revelation

## Synthesis roadmap

Once several thinker and concept nodes exist, begin building synthesis pages.

Recommended early synthesis pages:
- Christian AI anthropology map
- Theology of institutions for AI governance
- Christian account of work, labor, and participation under automation
- Translation layer: theology to public governance language

## Where this file fits in the ontology

This file is a roadmap and contributor guide, not a canon node.

Recommended node type:
- `governance_node`

Recommended role:
- stabilize build order
- guide contributors
- reduce improvisation
- support recursive theological expansion without drift

## Summary principle

Build the architecture in layers.  
Do not flatten thinkers into slogans.  
Do not bury comparisons in prose.  
Promote repeated concepts into reusable nodes.  
Keep the shell stable while the theological map grows.
