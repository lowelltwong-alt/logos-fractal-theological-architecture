# Weighting Profiles

Weighting profiles assign relative force, priority, and practical influence to theological considerations within a given use case.

This branch exists because sequence alone does not explain judgment. Ordering tells us what comes first. Weighting tells us what carries the greatest force when tradeoffs, tensions, or conflicts arise in practical decision contexts.

## Why weighting matters

Two systems may consult the same doctrines in the same order and still make different decisions because they assign different levels of practical importance to truthfulness, dignity, accountability, stewardship, speed, or institutional control.

In AI governance and institutional design, weighting is often where the real moral architecture shows itself.

Examples:
- a system may say dignity matters, but give speed and scale more practical force
- a system may affirm accountability, but weight automation convenience more heavily than human review
- a system may invoke stewardship, while quietly treating efficiency as the deciding value in every conflict

Weighting makes those choices explicit.

## What weighting is not

Weighting is not doctrine.
Doctrine identifies what is affirmed.

Weighting is not ordering.
Ordering explains sequence.

Weighting is the assignment of comparative practical force within a defined context.

## Design rules

1. Make the weighting profile explicit.
2. Link weightings to use cases rather than pretending one profile fits all contexts.
3. Preserve upstream theological constraints even when weights change.
4. Distinguish hard constraints from adjustable priorities.
5. Record known risks created by each weighting profile.
6. Treat weighting as reviewable rather than final.

## Types of weighting to distinguish

### Hard constraints
These are not simply high priorities. They are boundaries the system should not cross.

Examples:
- intentional deception
- coercive manipulation
- denial of human moral standing
- removal of accountable human oversight in morally consequential contexts

### Very high weight
These are considerations that should normally override convenience or local optimization.

Examples:
- truthfulness
- human dignity
- responsibility and answerability
- protection against domination or abuse

### High weight
These carry strong force but may require prudential balancing.

Examples:
- justice
- prudence
- stewardship
- transparency of lineage and review

### Moderate weight
These matter significantly but should often remain downstream of more fundamental commitments.

Examples:
- consistency
- timeliness
- process simplicity
- moderate efficiency gains

### Conditional weight
These may be useful in narrow settings but should not be treated as universally governing.

Examples:
- personalization
- aggressive optimization
- autonomous execution
- black-box ranking

## Why this branch matters for AI governance

Most unhealthy AI governance frameworks fail because they leave weighting implicit. They say many noble things, but when real tradeoffs appear, the true weights emerge:
- speed over truth
- risk reduction over dignity
- output volume over judgment
- automation over accountability

This repository rejects that hidden architecture. Weighting must be named.

## Baseline theological weighting intuition

The default logic of this repository is that considerations grounded in truth, personhood, moral responsibility, and neighbor-love should generally outrank considerations grounded only in local optimization.

That means:
- truth outranks convenience
- dignity outranks throughput
- accountability outranks frictionless automation
- prudence outranks blind scale
- stewardship is real, but not ultimate

## Recommended starter profiles

- default AI governance weighting
- nonprofit governance weighting
- ministry leadership weighting
- comparative weighting analysis

## Machine-readable implications

Each weighting profile should eventually store:
- weighting id
- related ordering profile
- use case
- hard constraints
- weight categories
- explicit rationales
- known failure modes
- review cadence
- approval state

## What to build next

1. a full AI governance weighting profile
2. a nonprofit governance weighting profile
3. a comparison file showing how different weights change downstream decisions
4. a crosswalk tying weightings to derivation examples
