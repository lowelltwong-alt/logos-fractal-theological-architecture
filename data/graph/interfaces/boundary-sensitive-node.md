# Boundary-Sensitive Node Interface

## Purpose

This file describes the boundary-sensitive-node interface pattern for graph and concordance objects.

A boundary-sensitive object is one whose use must be constrained by trust, doctrine, translation, or source-status limits.

## Why this interface exists

Different object types may still share the same boundary expectations.

For example:
- noncanonical source objects
- forged or heretical boundary objects
- disputed translations
- certain contested relationship objects

may all need warning logic, use-case limits, and stronger review expectations.

## Typical expectations

A boundary-sensitive object should usually carry fields such as:
- warning text where appropriate
- `use_case_limit`
- classification metadata
- trust-zone awareness
- stronger provenance and review expectations

## Use rule

Use this interface when an object's downstream use must be explicitly limited rather than assumed safe by default.

## Summary principle

Boundary sensitivity is a reusable governance pattern, not just a special case for one branch.
