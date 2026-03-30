# Passages Scheme

## Purpose

This file describes the passages domain within the graph and concordance layer.

A passages scheme groups machine-readable passage objects that function as reusable scripture spans larger than a single verse and smaller than a whole book.

## Why this scheme exists

Passage objects often carry more usable theological and concordance value than isolated verses because interpretation, doctrine, and thematic reasoning frequently operate on meaningful clusters.

A scheme gives those objects:
- bounded domain identity
- cleaner governance
- better traversal
- easier validation and reuse

## What belongs here

Typical objects in this scheme include passage or span objects such as:
- Genesis 1:1–2:3
- Genesis 1:26–28
- Genesis 3:1–19
- Genesis 11:1–9
- Romans 8:18–25

## Relation to the rest of the repository

Passage objects in this scheme should connect strongly to:
- verse objects
- biblical theme nodes
- doctrine nodes
- lexical nodes
- manuscript and translation witnesses
- relationship objects

## Summary principle

A passages scheme helps the repository treat scripture spans as a governed graph domain rather than only as prose citations or ad hoc references.
