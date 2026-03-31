# Controlled Schemes and Vocabularies Policy

## Purpose

This file defines how controlled schemes, concept vocabularies, and governed value spaces should work in the repository.

This file should be read together with:
- `tag-registry.md`
- `anchor-conventions.md`
- `node-types.md`
- `noncanonical-and-heresy-classification.md`
- `translation-trust-and-sectarian-classification.md`

## Core principle

Not every category name, trust label, doctrinal grouping, or canon status should be invented locally each time it is needed.

A mature ontology increasingly relies on controlled schemes and governed vocabularies.

## What a controlled scheme does

A controlled scheme defines a bounded value space that can be reused across many nodes or assertions.

Examples include:
- trust-zone vocabularies
- canonicality schemes
- translation-status schemes
- concept families
- doctrinal classification families
- manuscript or witness classification families

## Why schemes matter

Controlled schemes help:
- reduce vocabulary drift
- improve machine-legibility
- support cleaner filtering and retrieval
- preserve cross-branch consistency
- support future graph exports and validation

## Preferred rule

When the repository repeatedly uses a category family, contributors should consider whether it should become a governed scheme rather than remain an informal repeated phrase.

## Examples of good candidates for schemes

Examples include:
- canonical / deuterocanonical / apocryphal / pseudepigraphal / forged / heretical classifications
- trusted / reviewed / proposed / restricted status families
- translation trust classes
- doctrinal domain families
- hermeneutic method families
- tradition-family labels

## Scheme rule

A controlled scheme should normally have:
- a stable name or identifier
- a clear purpose
- a bounded set of values or members
- guidance on scope and use
- clear relation to trust and review logic where relevant

## Vocabulary rule

Labels inside a controlled scheme should not drift casually.

That means contributors should avoid:
- making near-duplicate labels casually
- introducing slightly different wording for the same governed category
- using repository-wide terms with inconsistent meanings across branches

## Expansion rule

A new scheme should not be created lightly.

Preferred order:
1. reuse an existing scheme if it fits
2. extend an existing scheme if the concept belongs inside it
3. create a new scheme only when the repository genuinely needs a distinct bounded value space

## Validation rule

As the repository matures, controlled schemes should increasingly become validation targets.

That means objects may eventually be checked for:
- valid scheme membership
- valid scheme labels
- required scope markers
- conflict with forbidden values in certain trust zones

## Retrieval rule

Controlled schemes are one of the most important tools for future retrieval and AI use.

They make it easier for a system to:
- filter by status or trust
- group similar objects
- compare traditions
- preserve boundary-sensitive distinctions

## Fractal rule

Scheme logic should recur across scales.

That means controlled vocabularies may govern:
- a small local branch
- a scripture subdomain
- a doctrinal family
- a boundary-source family
- a repo-wide trust grammar

## Summary principle

A serious ontology does not leave important value spaces to casual improvisation.

It increasingly stabilizes them as governed schemes.
