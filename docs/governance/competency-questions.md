# Competency Questions

## Purpose

This file defines the kinds of questions the repository's ontology and concordance system should be able to answer.

A strong ontology should not only look well structured. It should be able to support meaningful retrieval, comparison, traversal, and reasoning.

Competency questions help test whether the architecture is doing its job.

This file should be read together with:
- `fractal-rules.md`
- `promotion-thresholds.md`
- `schema-compatibility-policy.md`
- `scripture-taxonomy-and-ontology.md`
- `repository-integration-map.md`

## Core principle

An ontology should be judged not only by elegance, but by usefulness.

If the repository cannot answer the kinds of questions it is meant to support, then the structure still needs work.

## Main question families

### 1. Identity and location questions
These test whether a node can be found and placed clearly.

Examples:
- What kind of object is this node?
- What branch or domain does this node belong to?
- What is directly above it?
- What is directly below it?
- What related nodes exist across the graph?

### 2. Scripture and grounding questions
These test whether theology can be traced to text.

Examples:
- Which passages ground the image of God theme?
- Which scripture nodes connect to covenant?
- Which passages are central to Babel as a theme?
- Which doctrine nodes have explicit scriptural grounding?

### 3. Lexical and translation questions
These test whether the repository preserves important language distinctions.

Examples:
- Which Hebrew terms are central to Genesis 1:26–28?
- Which modern-language renderings are used for `tselem`?
- Which translation witnesses are acceptable as primary doctrinal witnesses?
- Which translation objects are caution-required or boundary-sensitive?

### 4. Manuscript and witness questions
These test whether text-critical context is preserved.

Examples:
- Which manuscript witnesses matter for a given passage?
- Where do translation notes depend on Masoretic Text versus Septuagint?
- Which witness objects are relevant to a disputed reading?

### 5. Doctrine and concept questions
These test whether repeated theological objects are reusable and traversable.

Examples:
- Which concepts recur across Augustine, Aquinas, and Calvin?
- Which doctrine nodes are grounded by Genesis 1 and Genesis 3?
- Which concepts should be promoted because they recur across multiple branches?

### 6. Boundary and trust questions
These test whether dangerous or disputed materials are controlled.

Examples:
- Which noncanonical sources are usable only for background context?
- Which boundary-sensitive nodes require warning blocks?
- Which translations are not acceptable as primary doctrinal witnesses?
- Which sources are doctrinally contradictory or heretical by tradition?

### 7. Provenance and review questions
These test whether the system preserves authorship, review, and change logic.

Examples:
- Who asserted this edge?
- Who reviewed this node?
- What source or evidence grounds this classification?
- Which objects remain community-proposed rather than reviewed?

### 8. Graph and concordance questions
These test whether machine-readable traversal is actually working.

Examples:
- Which edges connect Genesis 1:26–28 to concept.imago_dei?
- Which relationship objects are reused across multiple domains?
- Which graph objects belong to the concepts domain?
- Which nodes are linked by a governed doctrinal-support edge?

## Design rule

When adding a new branch, schema, or object family, ask:
- what competency questions should this new layer help answer?
- what questions become easier because this layer exists?
- what ambiguity does this layer reduce?

If no meaningful question becomes easier to answer, the new structure may not yet be justified.

## Review rule

Contributors and reviewers should periodically ask:
- can the repository answer the questions it was built to answer?
- are the answers clear enough for both humans and machines?
- do the current node and edge patterns support real traversal?
- are important trust and provenance questions answerable?

## Summary principle

Competency questions keep the ontology honest.

A repository becomes world-class not only when it is well organized, but when it can answer the right questions reliably.
