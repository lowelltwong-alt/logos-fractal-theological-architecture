# Promotion Thresholds

## Purpose

This file defines when repeated material should remain local and when it should be promoted into a more reusable governed object.

A fractal repository grows by promotion, not by uncontrolled duplication.

The goal of this file is to help contributors decide when to:
- keep material inside a parent node
- create a child node
- create a shared concept node
- create a scripture or text node
- create a relationship object
- create a graph or concordance object

## Core principle

Do not promote too early.
Do not duplicate too long.

A good threshold protects the repository from both:
- fragmentation through premature object creation
- incoherence through repeated ungoverned copy-paste structure

## Default promotion sequence

When new material appears, use this order of judgment:

1. keep it local if it is still mostly useful inside one parent node
2. create a child node if it becomes independently meaningful within that branch
3. promote it to a shared reusable node if it recurs across branches or domains
4. create a relationship object if the edge itself becomes important enough to govern
5. create a graph or concordance object when machine-readable reuse becomes structurally important

## Concept promotion thresholds

A repeated concept should usually be promoted into a shared concept node when one or more of the following becomes true:
- it appears meaningfully in 3 or more parent nodes
- it is carrying important theological work across multiple thinkers or traditions
- contributors would otherwise define it repeatedly in slightly different ways
- retrieval would be improved by making it independently addressable
- later doctrine, comparison, or graph work will likely depend on it

Typical examples:
- imago Dei
- vocation
- institutions
- ordered love
- public reason

## Child-node thresholds

A local section should usually become a child node when:
- it has enough internal structure to deserve its own heading map
- it is likely to be linked directly from elsewhere
- it contains multiple subarguments or subthemes
- it is starting to dominate the parent file

Typical examples:
- `canon.augustine.two_cities`
- `canon.aquinas.natural_law`
- a chapter-specific or doctrine-specific expansion within a thinker folder

## Scripture and text-node thresholds

A passage or verse cluster should usually become a governed scripture or text node when:
- it is cited across multiple doctrine, concept, or theme nodes
- it is carrying major lexical or interpretive load
- translation or manuscript differences matter for understanding it
- multiple traditions interpret it differently in ways the repository needs to track
- it is becoming a reusable reference point in graph or concordance work

Typical examples:
- Genesis 1:26–28
- Genesis 3:1–19
- Genesis 11:1–9
- Jeremiah 31:31–34

## Biblical-theme thresholds

A theme should usually become a biblical-theme node when:
- it draws together multiple passages
- it bridges text, doctrine, and concept layers
- several thinkers or traditions use it differently
- it is shaping downstream governance or AI reasoning

Typical examples:
- image of God
- stewardship
- covenant
- Babel
- wisdom

## Lexical-node thresholds

A term should usually become an original-language node when:
- the original-language wording carries doctrinal or interpretive weight
- one modern-language gloss is insufficient
- multiple translations render the term differently in meaningful ways
- the term appears centrally in a high-value passage or theme cluster

Typical examples:
- `tselem`
- `demut`
- `radah`
- `logos`

## Translation-note thresholds

A translation witness or translation-specific note should usually become its own governed object when:
- the translation is cited repeatedly
- its rendering choices affect doctrine, theme, or interpretation
- trust or sectarian-boundary questions matter
- provenance or textual-base questions need to be preserved clearly

## Manuscript and text-critical thresholds

A witness or text-critical note should usually become a governed node when:
- a variant affects interpretation significantly
- a manuscript tradition is repeatedly used as support
- provenance claims need explicit handling
- contributors would otherwise repeatedly restate the same witness logic

## Boundary-source thresholds

A noncanonical, pseudepigraphal, forged, or heretical source should usually get its own node when:
- it is being mentioned more than once
- contributors might misunderstand its status without a stable classification node
- background or comparative use needs explicit limitations
- doctrinal contamination risk increases if the source remains an ungoverned mention

## Relationship-object thresholds

A simple typed edge should usually remain local unless one or more of the following is true:
- the relationship is reused across multiple nodes
- the relationship is contested
- the relationship needs provenance or rationale
- the relationship has doctrinal, boundary, or interpretive significance
- the relationship may later be superseded or revised
- a graph system will likely reuse the edge as a governed object

Typical examples:
- major verse-to-verse intertextual claims
- verse-to-concept grounding claims
- doctrine-support links with real interpretive controversy

## Graph/concordance-object thresholds

Create a graph or concordance object when:
- machine-readable traversal requires a stable reusable object
- the object aggregates multiple controlled references
- the object belongs to a graph domain that will grow through repetition
- the object has enough metadata, provenance, or boundary logic that plain prose is no longer sufficient

## Anti-fragmentation rule

Do not promote something only because:
- it sounds important
- the label is attractive
- it might be useful someday
- a contributor prefers more objects instead of more discipline

If the object is not yet recurrent, reusable, or structurally meaningful, keep it local.

## Anti-duplication rule

Do not leave something unpromoted when:
- the same explanation is being copied into multiple nodes
- different contributors are already drifting in wording
- machines would gain significant clarity from a stable reusable object
- the concept is already acting like a shared node in practice

## Review rule

Promotion decisions should be treated as governance-relevant decisions.

A reviewer should ask:
- is this object genuinely reusable?
- is the threshold met?
- is a child node enough, or is a shared node needed?
- would promotion reduce duplication and improve retrieval?
- would promotion create unnecessary fragmentation?

## Summary principle

Promote repeated structure when reuse becomes real.
Keep material local when independence is still weak.

Fractal growth should make the repository clearer, not merely larger.

## Completeness-score gate for trust-zone promotion

Promotion from `proposed` into higher trust zones should include an architectural completeness gate.

Use the generated completeness reports in `reports/completeness` as an explicit threshold check:

- proposed -> tradition-scoped: weighted completeness score >= 0.78
- proposed -> canonical: weighted completeness score >= 0.90

Before promotion, verify the node also has:
- review posture at `editor_reviewed`
- no missing required identity fields
- no missing required provenance fields
- relation coverage dimension score >= 0.80

These thresholds should be treated as governance defaults and can be tightened for sensitive doctrine or boundary-source material.
