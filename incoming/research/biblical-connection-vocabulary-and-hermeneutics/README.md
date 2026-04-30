---
id: research_packet.biblical_connection_vocabulary_and_hermeneutics
anchor: research.biblical_connection_vocabulary_and_hermeneutics
title: Biblical Connection Vocabulary and Hermeneutics GraphRAG Research Seed
node_type: research_seed_packet
trust_zone: incoming_research
lifecycle_state: draft
review_status: unreviewed
epistemic_status: proposed
created: 2026-04-29
created_by: ChatGPT
requested_by: Lowell T. Wong
ai_usage_posture: staging_only_not_auto_promote
---

# Biblical Connection Vocabulary and Hermeneutics GraphRAG Research Seed

## Purpose

This packet stages the next vocabulary layer for the Logos repository: a scholar-recognizable biblical connection vocabulary for original-language work, translations, textual criticism, intertextuality, hermeneutics, prophecy, archaeology, historical context, and AI / GraphRAG retrieval.

The purpose is not to import Bible text yet. The purpose is to define the connection language that will eventually govern Bible text, source witnesses, translation notes, commentary, doctrine, and graph traversal.

## Status

Incoming research only. Not canonical doctrine, not a promoted graph vocabulary, not a Bible text import policy, and not production retrieval behavior.

## Why this packet exists

Standard graph vocabularies are usually too generic for biblical and theological scholarship. Biblical studies needs more precise relationship language than `related_to`, `supports`, or `references`.

A scholarly graph needs to distinguish quotation from allusion, allusion from echo, typological correspondence from direct prediction, prophecy from apocalyptic, lexical relation from theological relation, manuscript witness from translation witness, archaeological contextualization from doctrinal grounding, and asserted source relation from inferred retrieval relation.

## Files in this packet

- `research-packet.md` — overview, research question, source spine, and build logic.
- `bible-text-ingestion-policy.md` — why not to import full copyrighted modern translations yet.
- `relationship-vocabulary.yaml` — proposed relationship families and scholarly labels.
- `hermeneutics-vocabulary.yaml` — proposed hermeneutical method and interpretation vocabulary.
- `prophecy-vocabulary.yaml` — controlled prophecy and fulfillment vocabulary with caution flags.
- `textual-evidence-vocabulary.yaml` — textual criticism, witness, variant, Hebrew/Greek evidence vocabulary.
- `archaeology-and-context-vocabulary.yaml` — archaeology, historical context, inscription, geography, and science-adjacent evidence terms.
- `graph-rag-needs.md` — what AI / GraphRAG needs that standard graph relation labels often lack.
- `codex-handoff.md` — implementation handoff for a future bridge or governance vocabulary pass.

## Promotion posture

Do not auto-promote this vocabulary. Promotion should happen in small steps: review terms for scholarly recognizability, align term names with existing governance vocabulary, define a first subset for graph use, create a governance/reference bridge, then create schema, validator, or graph-object updates.

## Short answer to the Bible text question

Do not add full Bible Markdown files yet. Start with canonical references, source policies, licensing rules, original-language anchor options, translation-scope rules, and connection vocabulary. Full text ingestion should come later and only from license-compatible sources or external licensed APIs.
