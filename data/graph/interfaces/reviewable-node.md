# Reviewable Node Interface

## Purpose

This file describes the reviewable-node interface pattern for graph and concordance objects.

A reviewable object is one that should carry meaningful review state, review cadence, or reviewer attribution rather than being treated as permanently trustworthy by default.

## Why this interface exists

Different object types may still share the same review expectations.

For example:
- concept objects
- doctrine objects
- relationship objects
- translation witnesses
- boundary-source objects

may all require review, even though they are not the same node type.

## Typical expectations

A reviewable object should usually carry fields such as:
- `review_status`
- `review_cycle`
- `reviewed_by`
- `last_reviewed`
- review notes where needed

## Use rule

Use this interface when an object's trust should depend in part on whether it has been reviewed, not only on what kind of object it is.

## Summary principle

Reviewability is a reusable governance pattern, not only a local note.
