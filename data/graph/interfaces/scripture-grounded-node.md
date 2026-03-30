# Scripture-Grounded Node Interface

## Purpose

This file describes the scripture-grounded-node interface pattern for graph and concordance objects.

A scripture-grounded object is one that should be explicitly traceable to scripture passages, scripture-derived evidence, or governed text clusters.

## Why this interface exists

Different object types may still share the same grounding expectation.

For example:
- doctrine objects
- biblical theme objects
- some concept objects
- passage-linked relationship objects

may all need explicit scripture grounding even though they are not the same node type.

## Typical expectations

A scripture-grounded object should usually carry fields such as:
- scripture refs or source refs
- passage-level links
- doctrinal grounding traceability
- relevant lexical or translation links where needed

## Use rule

Use this interface when an object's legitimacy or interpretive usefulness depends in part on explicit connection to scripture.

## Summary principle

Scripture grounding is a reusable ontology pattern, not only a local note inside one branch.
