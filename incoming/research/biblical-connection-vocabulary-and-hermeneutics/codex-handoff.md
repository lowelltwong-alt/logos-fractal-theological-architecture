---
id: codex_handoff.biblical_connection_vocabulary_and_hermeneutics
anchor: codex_handoff.biblical_connection_vocabulary_and_hermeneutics
title: Codex Handoff for Biblical Connection Vocabulary and Hermeneutics Seed
node_type: codex_handoff
trust_zone: incoming_research
lifecycle_state: draft
review_status: unreviewed
epistemic_status: procedural
created: 2026-04-29
created_by: ChatGPT
ai_usage_posture: implementation_guidance_only
---

# Codex Handoff: Biblical Connection Vocabulary and Hermeneutics

## Mission

Create a small governed reference bridge from this incoming research packet. The bridge should introduce the first approved subset of biblical connection vocabulary without changing validators, importing Bible text, or creating graph objects.

## Read first

Read every file in this seed packet before editing, especially relationship vocabulary, hermeneutics vocabulary, prophecy vocabulary, textual evidence vocabulary, archaeology and context vocabulary, Bible text ingestion policy, and GraphRAG needs note.

## Primary implementation target

Create a new governed reference document for biblical connection vocabulary. The document should live under the governance docs area and should use the filename biblical-connection-vocabulary.md.

Avoid writing planned paths as live links in this research packet unless the target exists.

## Suggested first approved subset

Start with no more than 12 relationship types:

- quotes
- alludes_to
- echoes
- typologically_corresponds_to
- claims_fulfillment_of
- translated_as
- has_lemma
- has_reading
- attested_by_witness
- interpreted_by
- archaeologically_contextualized_by
- grounds_doctrine
- constrains_application

If this feels too many, split `grounds_doctrine` and `constrains_application` into a later application subset.

## Required content in the bridge

The bridge should explain:

1. why biblical scholarship needs more precise graph relation language than generic GraphRAG;
2. why Bible text import should wait;
3. why prophecy vocabulary needs caution;
4. why typology is not the same as direct prediction;
5. why textual criticism needs witness / reading / variant terminology;
6. why archaeology contextualizes but does not automatically prove doctrine;
7. how AI should render relation confidence and method;
8. how this vocabulary can later become schema and validator work.

## Guardrails

Do not import Bible text, paste copyrighted translations or commentaries, create claim objects, create graph relationship objects, change validators, create a full prophecy system, create a full original-language corpus, invent fringe prophecy categories, use generic `related_to` for meaningful biblical-theological edges, or make this packet canonical.

## Validation expectations

Run normal repo validation after implementation. Also run all-markdown link validation because planned path notes often cause false live-link failures.

## Done definition

The next Codex pass is done when the repo contains one reviewable governed reference document introducing the first subset of biblical connection vocabulary, while this research packet remains staged and unpromoted.
