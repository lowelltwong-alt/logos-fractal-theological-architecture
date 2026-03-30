# Trust Zones

## Purpose

This file defines trust zones for the repository.

A trust zone is a governance concept that indicates how strongly a node, object, edge, or branch may be relied upon for doctrinal use, machine inference, reuse, or downstream decision support.

The repository does not need enterprise software permissioning to benefit from a trust-zone model. It still needs a disciplined way to distinguish highly trusted core material from experimental, disputed, or boundary-sensitive material.

This file should be read together with:
- `noncanonical-and-heresy-classification.md`
- `translation-trust-and-sectarian-classification.md`
- `fractal-rules.md`
- `schema-compatibility-policy.md`
- `inference-policy.md`

## Core principle

Not every part of the repository should carry the same trust weight.

Some materials belong to the stable core.
Some are reviewed but still specialized.
Some are working proposals.
Some are included mainly for comparison, warning, or boundary-setting.

A strong ontology preserves those differences explicitly.

## Recommended trust zones

### `core_trusted`
Use for highly trusted, repository-core materials.

Typical examples:
- mature governance files
- stable canon nodes
- reviewed doctrine nodes
- well-governed concept nodes

Typical expectations:
- stable IDs
- stable schema use
- clear provenance
- reviewed status
- safe for ordinary retrieval and traversal

### `reviewed_specialized`
Use for material that is reviewed and trusted within a more specialized domain, but not necessarily part of the broadest repository core.

Typical examples:
- manuscript notes
- translation witnesses
- lexical nodes with domain-specific detail
- advanced graph objects that have been reviewed

Typical expectations:
- strong provenance
- clear scope
- safe for qualified use
- still governed, but sometimes more domain-specific than the core layer

### `working_proposed`
Use for nodes or objects that are promising but not yet strongly stabilized.

Typical examples:
- newly proposed graph nodes
- newly promoted concept candidates
- community-proposed relationship objects
- early-stage doctrine expansions

Typical expectations:
- explicit status markers
- caution in reuse
- not yet assumed to be fully stable for downstream automation

### `boundary_restricted`
Use for materials that are intentionally present but limited in use.

Typical examples:
- noncanonical texts
- disputed translations
- high-risk comparative materials
- doctrinally mixed or weakly aligned sources

Typical expectations:
- warning text where relevant
- use-case limits
- stronger review expectations for downstream reuse
- no silent promotion into core doctrinal authority

### `experimental_graph`
Use for machine-readable or graph-oriented objects that are still being tested structurally or operationally.

Typical examples:
- prototype graph domains
- import-normalization objects
- provisional relationship-object patterns
- early scheme objects

Typical expectations:
- explicit schema/version awareness
- compatibility caution
- restricted inference assumptions until stabilized

## Trust-zone rule

A trust zone is not the same thing as a node type.

Node type answers: what kind of object is this?
Trust zone answers: how much reliance should the repository place on this object?

An object's trust zone may change over time.

## Promotion and trust

A trust-zone change is often a governance event.

Examples:
- moving from `working_proposed` to `core_trusted`
- moving from `experimental_graph` to `reviewed_specialized`
- moving from an unclear status into `boundary_restricted`

Such moves should not happen silently when they affect downstream reuse.

## Inference rule

Machine inference should respect trust zones.

That means machines should not treat:
- `boundary_restricted` objects as equivalent to `core_trusted` nodes
- `experimental_graph` objects as fully authoritative structure
- `working_proposed` nodes as if they were already canonical within the repo

Trust zones should constrain traversal, promotion, and automation assumptions.

## Fractal rule

Trust zones should recur across scales.

That means trust can apply to:
- a single node
- an edge object
- an entire branch
- a graph domain
- a schema family

The same governance grammar should recur whether the object is small or large.

## Summary principle

A strong ontology does not only classify what things are.
It also classifies how much they may be trusted and how far they may be used.
