# Logos Governed Node Schema

## Purpose

This document defines the current reference shape for a governed machine-readable node in the Logos Fractal Theological Architecture repository.

It translates the repository’s current governance logic into schema language. It is not meant to be a full JSON Schema specification in the technical-validator sense. It is a governed structural reference for how sidecars and machine-readable companions should be shaped.

## Why this schema exists

Earlier project work developed a strong recursive decision artifact structure with identity, classification, system, relationships, logic, execution, governance, evidence, persistence, content, lifecycle, inheritance, interpretation rules, provenance, validation, and entity-model fields. That structure remains valuable. However, the current repository has moved further toward:
- governed node types
- ontology discipline
- explicit provenance distinctions
- translation-status visibility
- philosophy and external-source handling
- more precise semantic relationship logic

This schema keeps the recursive strength of the earlier artifact model while aligning it with the current repository architecture.

## Governing principles

A governed node schema in this repository should:
- preserve a stable recursive shell
- support typed nodes rather than one generic node type alone
- make provenance visible
- support synthesis and appropriation explicitly
- preserve translation burden where direct comparison is misleading
- allow theology, philosophy, governance, comparison, and application nodes to coexist inside one machine-readable family

## Required top-level field families

A governed node should normally support the following field families:

- `node_type`
- `identity`
- `classification`
- `system`
- `relationships`
- `logic`
- `execution`
- `governance`
- `evidence`
- `content`
- `lifecycle`
- `permissions`
- `provenance`
- `validation`
- `entity_model`
- `inheritance`
- `interpretation_rules`
- `subnodes`

Not every node must populate every field deeply. Some fields may remain behaviorally dormant when blank, following the interpretation rules.

## Recommended node type family

The schema should allow multiple governed node types, including at minimum:
- `canon_thinker`
- `doctrine_node`
- `concept_node`
- `comparison_node`
- `synthesis_node`
- `governance_node`
- `application_node`
- `crosswalk_node`
- `philosophy_node`

This is a major difference from the earlier generic `decision_node` framing. The older model was useful, but the repository now needs richer typed-node expressiveness.

## Identity family

The identity family should preserve:
- stable id
- anchor
- title
- slug
- version
- status

Anchors should follow the current anchor conventions of the repo, using stable, lowercase, dot-delimited patterns.

## Classification family

The classification family should preserve:
- document type
- primary use
- domain
- subdomain
- object type
- tags
- audience tags
- source domains

This family should increasingly align with controlled tags and ontology-ready vocabulary rather than freeform drift.

## System family

The system family should preserve:
- system role
- intent
- author logic
- AI compatibility
- interaction mode
- requires human judgment

This allows both theological and operational artifacts to remain intelligible to future AI systems.

## Relationships family

The relationships family should preserve the structural graph logic of the earlier schema, but it should also align more tightly with the current relationship registry.

It should support at least:
- parent
- parents
- children
- depends_on
- enables
- related_to
- supersedes
- superseded_by

Where relevant, relationship metadata may also be used to capture dependency strength or criticality.

For semantically stronger relationship claims, the content layer or structured sidecar notes should use governed verbs such as:
- aligns_with
- partially_aligns_with
- misaligns_with
- tensions_with
- contradicts
- corrects
- sharpens
- requires_translation_to_compare
- grounds
- constrains
- translates_into
- derived_from
- synthesizes
- appropriates_from
- adapts

## Logic family

The logic family should preserve:
- inputs
- outputs
- decision type
- output type
- constraints
- assumptions
- tradeoffs
- evaluation criteria
- success metrics

This remains especially important for AIRCA, governance, and application-side nodes.

## Governance family

The governance family should preserve:
- owner
- reviewers
- decision rights
- approval required
- review cycle
- sensitivity
- retention guidance

This is especially important for long-term machine use and protected artifacts.

## Evidence family

The evidence family should preserve:
- citations
- data sources
- confidence
- confidence notes
- a decomposed confidence model where useful

This family is also where biblical references, translation references, and theology references may be represented as evidence objects or cited sources.

## Provenance family

The provenance family is one of the most important current upgrade areas.

A governed node should support at least:
- source refs
- derived from
- synthesizes
- appropriates from
- adapts
- created by
- last modified by
- transformation history
- derivation method
- process refs
- authoring mix
- translation status
- alignment strength

This extends the older provenance pattern so the repository can distinguish:
- direct derivation from one source
- multi-source synthesis
- appropriation from non-Christian philosophy
- active adaptation of borrowed categories
- direct comparison versus translation-required comparison

## Entity model family

The entity model should preserve:
- entity type
- entity subtype
- canonical id
- lifecycle state
- canonical status
- source of truth ref
- aliases

This family supports future ontology work.

## Lifecycle, inheritance, and interpretation rules

The newer v2 template already makes a major advance here. Those families should remain.

They are important because:
- lifecycle allows per-node review, protection, and disposition logic
- inheritance allows recursive defaults without uncontrolled duplication
- interpretation rules prevent blank fields from being misread as active permission

Those features remain aligned with the latest governance logic and should be retained.

## New alignment fields

To better fit the current governance layer, governed nodes should increasingly support:
- `translation_status`
- `alignment_strength`

Suggested values for `translation_status`:
- `directly_comparable`
- `partially_translatable`
- `requires_translation_to_compare`
- `not_yet_clear`

Suggested values for `alignment_strength`:
- `high`
- `moderate`
- `low`
- `mixed`
- `not_applicable`

The repository should not use decimal pseudo-precision unless it later formalizes a scoring model.

## New provenance distinctions

To better fit the current governance layer, the schema should increasingly represent:
- `derived_from`
- `synthesizes`
- `appropriates_from`
- `adapts`

These should not be flattened into generic influence language.

## Non-Christian philosophy support

The schema should support philosophy nodes and external-source traditions explicitly.

Examples include:
- `philosophy.platonism`
- `philosophy.aristotelianism`
- `philosophy.stoicism`
- `philosophy.neoplatonism`

This allows the repository to model:
- Christian appropriation of philosophical categories
- Christian adaptation of external concepts
- misalignment between theology and philosophy
- translation burden in cross-tradition comparison

## Migration guidance from older decision-node templates

If an older artifact uses a generic `decision_node` structure, it does not need to be discarded.

Instead, migrate it by:
1. identifying the stronger governed node type
2. preserving the recursive shell
3. expanding provenance fields
4. adding translation-status and alignment fields where needed
5. keeping lifecycle, inheritance, and interpretation rules intact
6. distinguishing philosophy-source lineage from Christian canon lineage where relevant

## Summary principle

The governed schema should remain recursive, stable, provenance-aware, ontology-ready, and aligned with the current branch governance.

It should not merely describe a document.
It should make the document machine-legible in a way that remains faithful to the project’s latest architecture.
