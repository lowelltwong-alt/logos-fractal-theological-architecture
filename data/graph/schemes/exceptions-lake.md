# Exceptions Lake Scheme

## Purpose

This scheme defines the graph domain for exception-capture and learning-loop objects.

It allows exception pressure to be represented in governed machine-readable form without mutating ontology or taxonomy directly.

## Core object families

- expectation objects
- exception-event objects
- adaptation proposal objects
- promotion-decision relationship objects

## Address grammar

Exception-domain objects should carry the nine-layer address:

`root.domain.capability.entity.instance.state.expectation.exception.adaptation`

The address is structural placement. Semantic identity should still be stable and separate.

## Required distinctions

This scheme keeps separate object identities for:

- expectation
- exception
- adaptation

Do not flatten these into one field or one object.

## AIRCA stage linkage

Typical stage linkage:

- Architect -> expectation objects
- Inform -> exception capture objects
- Rank -> priority and severity scoring objects/fields
- Commit -> review and approval decision objects
- Act -> relationship links to rule/taxonomy/ontology/governance updates

## Pressure vectors

Exception objects may include one or more pressure vectors:

- theological
- psychological
- moral
- political
- economic
- cultural

These vectors support routing and analysis, not doctrinal authority by themselves.

## Lineage rule

Exception events are append-only records.
Any adaptation or promotion decision should link back to source exceptions using explicit graph relationships.
