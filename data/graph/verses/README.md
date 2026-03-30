# Verse Nodes

## Purpose

This folder holds the canonical verse-node layer for the concordance graph.

These files should represent stable scripture reference identity, not one specific translation rendering.

## Core rule

A verse node is a canonical reference object.

It may point to:
- translation witness nodes
- concept nodes
- doctrine nodes
- entity nodes
- cross-reference edge objects

But it should not collapse all of those layers into itself.

## What belongs here

- stable verse identifiers
- canonical reference metadata
- low-risk graph relationships from verse to other node families
- provenance and review state for meaningful typed edges

## What does not belong here

- uncontrolled doctrinal over-claims
- translation-specific text as if it were the verse identity itself
- hidden philosophical or interpretive conclusions without provenance

## Summary principle

Keep the verse layer stable.
Let richer meaning accumulate around it through governed links.
