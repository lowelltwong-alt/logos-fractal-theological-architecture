# Source-Boundary-Object Interface

## Purpose

This file describes the source-boundary-object interface pattern for graph and concordance objects.

A source-boundary object is one whose use must be constrained because it belongs to a boundary-sensitive source family such as noncanonical, forged, heretical, sectarian, or otherwise restricted material.

## Why this interface exists

Different source families may still share the same boundary-governance expectations.

For example:
- noncanonical texts
- pseudepigraphal works
- forged or heretical materials
- disputed source objects

may all need explicit limits, warnings, provenance, and review expectations.

## Typical expectations

A source-boundary object should usually carry fields such as:
- canonical status
- confessional status
- historical authenticity
- doctrinal alignment
- use-case limit
- warning text where appropriate

## Use rule

Use this interface when an object's main challenge is not only what it is, but how strictly its use must be constrained.

## Summary principle

Boundary-sensitive source handling is a reusable ontology pattern, not merely an exception case.
