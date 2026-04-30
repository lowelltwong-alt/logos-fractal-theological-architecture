---
id: research_packet.biblical_connection_vocabulary_and_hermeneutics.main
anchor: research.biblical_connection_vocabulary_and_hermeneutics.main
title: Biblical Connection Vocabulary and Hermeneutics GraphRAG Research Packet
node_type: research_packet
trust_zone: incoming_research
lifecycle_state: draft
review_status: unreviewed
epistemic_status: proposed
created: 2026-04-29
created_by: ChatGPT
requested_by: Lowell T. Wong
ai_usage_posture: staging_only_not_auto_promote
---

# Biblical Connection Vocabulary and Hermeneutics GraphRAG Research Packet

## 1. Research question

What vocabulary of relationship types, hermeneutical methods, textual evidence types, prophecy categories, and contextual evidence terms is needed for a scholar-recognizable biblical-theological graph that can also support AI retrieval and GraphRAG without flattening meaning?

## 2. Core conclusion

Before adding full Bible text, translation corpora, commentary corpora, or large original-language datasets, the repository should first define a biblical connection vocabulary.

The connection vocabulary should be recognizable to biblical scholars, theologians, Hebrew Bible scholars, Jewish studies scholars, textual critics, and archaeologists; precise enough for AI retrieval and graph traversal; governed enough to prevent drift; and flexible enough to support future original-language, translation, commentary, archaeology, and science-adjacent layers.

## 3. Why full Bible Markdown files should wait

Full Bible-text import is not the next step.

Reasons:

1. Many modern translations are copyrighted and not compatible with a public CC BY repository.
2. Large text imports create retrieval surfaces before the authority and relationship vocabulary is ready.
3. The repo needs canonical reference discipline before it needs complete verse text.
4. Translation comparison requires licensing, attribution, language, edition, and quotation-boundary policy.
5. Original-language data requires morphology, lemma, token, witness, and text-form rules before bulk ingestion.

The near-term pattern should be reference anchor -> source policy -> relation vocabulary -> selected open original-language data or external licensed API -> translation comparison notes -> future text objects.

## 4. Source spine for review

This packet proposes the source-spine categories that should govern later promotion:

- OSIS / Open Scripture Information Standard for Bible markup and canonical reference discipline.
- TEI critical apparatus guidance for apparatus entries, readings, witnesses, variants, and fragmentary witnesses.
- SBL Handbook of Style for biblical studies citation, abbreviations, transliteration, ancient languages, and archaeological site-name conventions.
- SBL Greek New Testament as a likely open-license Greek text option.
- Open Scriptures Hebrew Bible / morphhb-style morphology and lemma data after license verification.
- Public-domain translations such as KJV or World English Bible as possible examples after source verification.
- Copyright-sensitive translations such as ESV and NASB as reference-only unless permission is obtained.

## 5. Fractal design principle

The same repeated structure should apply at each level.

A relationship type should always ask:

- What is the source object?
- What is the target object?
- What kind of connection is claimed?
- Is the connection asserted, inferred, proposed, contested, or rejected?
- What evidence supports it?
- What discipline does the evidence come from?
- What hermeneutical method is used?
- What authority or tradition scope applies?
- What confidence or review status applies?
- How should AI render this connection?

That is the fractal DNA of the vocabulary.

## 6. Relationship families to seed

Seed these families first:

- Canon, reference, and structure.
- Intertextuality.
- Typology and figural relations.
- Prophecy and fulfillment.
- Covenant and redemptive-historical development.
- Lexical, semantic, and syntactic relations.
- Textual criticism and witness relations.
- Translation and reception.
- Archaeology and historical context.
- Theology and doctrine.

## 7. Hermeneutical categories to seed

Hermeneutical vocabulary should include scholar-recognizable terms: grammatical-historical interpretation, literary context, canonical reading, theological interpretation of Scripture, historical-critical method, source criticism, form criticism, redaction criticism, narrative criticism, discourse analysis, intertextuality, typology, figural reading, sensus plenior, reception history, Second Temple context, rabbinic reception, patristic reception, covenantal reading, and archaeological contextualization.

Each method should have a definition, what it is good for, what it must not overclaim, what evidence it requires, and how AI should signal it in generated answers.

## 8. Prophecy caution

Prophecy needs special governance because it can attract fringe claims, overconfident fulfillment claims, and speculative modern-event mapping.

The vocabulary should distinguish prophetic oracle, prediction, promise, covenant curse/blessing, symbolic vision, apocalyptic vision, sign-act, messianic expectation, typological fulfillment, direct fulfillment claim, pesher-style interpretation, sensus plenior, eschatological horizon, and contested fulfillment.

AI outputs should not treat a claimed fulfillment model as settled unless the authority scope and interpretive tradition are explicitly given.

## 9. Archaeology and science-adjacent caution

Archaeological and scientific evidence can contextualize texts, challenge assumptions, confirm settings, or illuminate material culture. It should not be made to do more than it can.

The vocabulary should distinguish material artifact, inscription, site, stratum, locus, provenance, provenience, paleography, epigraphy, ceramic chronology, radiocarbon dating, archaeobotany, archaeozoology, comparative ancient Near Eastern parallel, historical geography, environmental context, and genetic evidence.

AI should not turn archaeological correlation into theological proof without an explicit intermediate argument.

## 10. Near-term build recommendation

The next implementation after this seed should be a governed bridge or reference document that defines the first approved subset of biblical connection vocabulary.

Start small with: quotes, alludes_to, echoes, typologically_corresponds_to, claims_fulfillment_of, translated_as, has_lemma, has_reading, attested_by_witness, interpreted_by, archaeologically_contextualized_by, grounds_doctrine, and constrains_application.

## 11. What this packet should prevent

This packet should prevent importing Bible text before relationship vocabulary is ready, building a graph of generic `related_to` edges, flattening prophecy into prediction-only categories, confusing typology with direct prediction, confusing archaeology with doctrinal proof, confusing translation choice with original-language meaning, and treating inferred GraphRAG edges as asserted scholarly relations.
