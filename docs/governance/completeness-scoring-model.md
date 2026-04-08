---
id: governance.completeness_scoring_model
anchor: governance.completeness_scoring_model
title: Completeness Scoring Model
node_type: governance_node
status: active
review_status: draft
object_type: governance_scoring_policy
trust_zone: canonical
lifecycle_status: active
provenance_note: Created on 2026-04-08 to govern architectural completeness scoring and remediation prioritization.
reason_for_inclusion: Make recursive build quality measurable and trendable across governed graph nodes.
---

# Completeness Scoring Model

## Purpose

Define a single scoring model that quantifies how architecturally complete each governed node is.

The score exists to:
- measure recursive build quality
- target overnight remediation work
- provide a promotion gate from `proposed` into higher-trust zones
- show trend direction (improving or regressing) over time

## Scoring dimensions

Each node is scored on six dimensions:
1. **identity**: required identity fields are present
2. **provenance**: provenance and authorship traceability are present
3. **trust**: trust-zone value is present and allowed
4. **relation coverage**: required relationship structures and minimum typed edges exist
5. **retrieval neighborhood**: node participates in retrieval and cross-reference neighborhoods
6. **review posture**: review state is present and favors editor-reviewed posture

Default weights:
- identity: `0.20`
- provenance: `0.20`
- trust: `0.15`
- relation_coverage: `0.20`
- retrieval_neighborhood: `0.10`
- review_posture: `0.15`

Weighted score range: `0.00` to `1.00`.

## Per-node-type requirements

Requirements are declared in:
- `data/graph/completeness_requirements.json`

The registry defines:
- required identity fields
- required provenance fields
- accepted trust-zone values
- required relationship keys
- minimum typed-edge counts
- minimum retrieval-link expectations
- accepted and preferred review states

## Overnight prioritization

Priority queue logic is generated from:
- low weighted completeness score
- high graph centrality percentile

`remediation_priority_index = (1 - weighted_score) * (1 + centrality_percentile)`

Nodes are marked `needs_overnight_remediation: true` when:
- weighted score `< 0.75`
- centrality percentile `>= 0.60`

## Trend reporting

Each run writes a trend payload that includes:
- latest overview
- previous overview
- delta for average/median/under-threshold counts
- full run history from `reports/completeness/history.jsonl`

Trend output file:
- `reports/completeness/trend_latest.json`

## Promotion thresholds (proposed → higher trust)

Completeness scoring is a gate, not the only criterion.

Minimum recommended score gates:
- `proposed -> tradition-scoped`: `>= 0.78`
- `proposed -> canonical`: `>= 0.90`

Hard constraints before promotion:
- review posture must be `editor_reviewed`
- no missing required identity fields
- no missing required provenance fields
- relation coverage dimension score must be `>= 0.80`

## Script and outputs

Run:

```bash
python3 scripts/compute_completeness.py
```

Outputs:
- `reports/completeness/node_scores_<timestamp>.json`
- `reports/completeness/prioritized_remediation_<timestamp>.json`
- `reports/completeness/latest_node_scores.json`
- `reports/completeness/latest_prioritized_remediation.json`
- `reports/completeness/history.jsonl`
- `reports/completeness/trend_latest.json`

## Governance note

Completeness score should inform queueing and promotion decisions, but reviewers still own final promotion judgment where doctrinal or trust-boundary risk is non-trivial.
