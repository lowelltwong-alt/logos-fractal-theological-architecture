---
object_type: roadmap_note
trust_zone: proposed
lifecycle_status: draft
provenance_note: "Created on 2026-04-30 to classify live and planned source-document families after the cleaned-baseline normalization and Bridge Pack v1 work."
reason_for_inclusion: "Give contributors one governed map for deciding which source packets actively inform work now, which remain future or parked inputs, and how each may or may not be promoted."
---

# Source Document Integration Map

## Purpose

This note classifies the major source-document families currently visible in the repository so contributors can tell:

- which inputs are active now;
- which inputs are future-facing only;
- which inputs are parked side routes;
- which inputs govern control-plane behavior;
- which inputs exist mainly to control licensing or source-policy risk.

This file is a routing map, not a promotion event.

It does not promote new claims, doctrine, graph objects, or Bible-text ingestion.

## Classification rule

Use the lightest trustworthy path:

```text
incoming research
-> draft bridge or governed note
-> reviewed doctrine / concept / application patch
-> later claim or graph work only if clearly needed
```

If a source family is marked `future input` or `parked side-route input`, treat it as planning guidance rather than an active build lane.

## Active input

### Doctrine layer

- Source family name: Doctrine layer
- Repo location: `docs/doctrine/`
- What it informs: stable doctrine topics that upstream concept, application, and later claim work may depend on
- What it must not be used for: auto-promoting unreviewed research packets, flattening tradition differences, or treating one draft doctrine file as final authority for all downstream work
- Promotion path: focused doctrine patch -> steward review -> later claim or graph extraction only where the prose path is already accepted
- Trust zone: proposed
- Next recommended action: continue small doctrine buildout only where incoming research or bridge files already show a narrow, reviewable need

### Concept layer

- Source family name: Concept layer
- Repo location: `docs/concepts/`
- What it informs: reusable cross-branch concepts such as `imago-dei`, `stewardship`, and `vocation`
- What it must not be used for: replacing doctrine topics, absorbing whole research packets unchanged, or bypassing source-basis review for repeated ideas
- Promotion path: narrow concept patch from existing doctrine, Scripture, or reviewed bridge work -> steward review -> later claim or graph reuse if the concept becomes machine-relevant
- Trust zone: proposed
- Next recommended action: keep promoting only repeated cross-branch concepts, not one-off applications

### AI governance bridge pack

- Source family name: AI Governance Bridge Pack v1
- Repo location: `docs/applications/ai-governance/`
- What it informs: prudential governance applications derived from reviewed theological source paths
- What it must not be used for: canonical doctrine, final policy, Scripture replacement, or proof that a downstream AI-governance conclusion is settled
- Promotion path: incoming research packet -> draft bridge -> theology and governance review -> later claim or graph work if the prose derivation is accepted
- Trust zone: proposed
- Next recommended action: use these bridge files as the preferred copyable pattern for new application work before any claim-object promotion

### Trinity, anthropology, and AI governance packet

- Source family name: Trinity, Anthropology, and AI Governance research packet
- Repo location: `incoming/research/trinity-anthropology-ai-governance/`
- What it informs: the Trinity -> personhood -> anthropology -> human agency -> AI-governance bridge path
- What it must not be used for: direct doctrine promotion, direct graph-object creation, or unreviewed claims about personhood becoming canonical
- Promotion path: packet review -> bridge refinement -> targeted doctrine or concept patch only after review
- Trust zone: incoming_research
- Next recommended action: use it to strengthen review questions and source-basis notes for the existing Trinity bridge rather than widening scope

### Scripture, authority, and retrieval governance packet

- Source family name: Scripture, Authority, and AI Retrieval Governance research packet
- Repo location: `incoming/research/scripture-authority-ai-retrieval-governance/`
- What it informs: retrieval ordering, authority-scope caution, and source-type differentiation in AI-governance work
- What it must not be used for: declaring a settled source hierarchy, importing Bible text, or turning retrieval guidance into canonical doctrine
- Promotion path: packet review -> application bridge refinement -> later source-policy or claim work only after authority distinctions are reviewed
- Trust zone: incoming_research
- Next recommended action: keep refining bridge-level distinctions between direct theological claims and prudential retrieval controls

### Fallenness, institutional drift, and AI safety packet

- Source family name: Fallenness, Institutional Drift, and AI Safety research packet
- Repo location: `incoming/research/fallenness-institutional-drift-ai-safety/`
- What it informs: auditability, exception capture, drift review, and anti-rationalization constraints for AI governance
- What it must not be used for: treating safety heuristics as doctrine, bypassing governance review, or promoting exceptions-lake structures directly into graph data
- Promotion path: packet review -> bridge refinement -> governance note or claim work only where the reviewed prose path is clear
- Trust zone: incoming_research
- Next recommended action: keep it coupled to existing exceptions-lake governance docs instead of creating a separate AI-safety doctrine lane

### Christology, incarnation, and AI mediation packet

- Source family name: Christology, Incarnation, and AI Mediation research packet
- Repo location: `incoming/research/christology-incarnation-ai-mediation/`
- What it informs: mediated presence constraints, disclosure posture, and anti-impersonation cautions for AI-assisted settings
- What it must not be used for: canonical Christology, sacramental claims, pastoral automation, or final ecclesial policy
- Promotion path: packet review -> bridge refinement -> later doctrine or application patch only after tradition-scope cautions are reviewed
- Trust zone: incoming_research
- Next recommended action: keep the bridge draft narrow and explicitly downstream from future Christology source work

## Future input

### Biblical connection vocabulary and hermeneutics packet

- Source family name: Biblical Connection Vocabulary and Hermeneutics research packet
- Repo location: `incoming/research/biblical-connection-vocabulary-and-hermeneutics/`
- What it informs: future relationship vocabulary, hermeneutic method labels, textual-evidence language, and GraphRAG-facing source distinctions
- What it must not be used for: Bible-text ingestion, immediate schema changes, direct graph-object rollout, or collapsing quotation, allusion, typology, and fulfillment into one live relation family
- Promotion path: vocabulary review -> governance/reference bridge -> small governed subset -> later schema or validator work only after review
- Trust zone: incoming_research
- Next recommended action: treat this as vocabulary and source-policy groundwork, not as an active graph-expansion license

### Biblical primary-sources framework

- Source family name: Biblical primary-sources future framework
- Repo location: `docs/roadmap/biblical-primary-sources-future-framework.md`; related planned branch `docs/primary-sources/`
- What it informs: future witness, fragment, transcription, lexical-evidence, and translation-comparison architecture
- What it must not be used for: activating a corpus import, storing copyrighted Bible text, or implying that the future branch is already live
- Promotion path: policy and license review -> reference-anchor and source-registry work -> limited open-license examples later if explicitly approved
- Trust zone: proposed
- Next recommended action: keep this as planning guidance until source-policy, licensing, and vocabulary controls are stronger

## Parked side-route input

### Christian counseling side-quest roadmap

- Source family name: Christian counseling side-quest roadmap
- Repo location: `docs/roadmap/christian-counseling-side-quest-roadmap.md`
- What it informs: future safety boundaries and contributor-lane thinking for a possible counseling-adjacent domain
- What it must not be used for: activating counseling work, creating client-facing content, ingesting sensitive case material, or launching AI counselor behavior
- Promotion path: remain parked -> if activated later, start with safety and role-boundary seed work in planned paths rather than application content
- Trust zone: proposed
- Next recommended action: leave this lane parked until the main research-to-bridge workflow is more mature and qualified reviewers are available

## Governance/control-plane input

### Repository architecture and sequencing docs

- Source family name: Repository architecture and sequencing docs
- Repo location: `README.md`; `docs/roadmap/README.md`; `docs/roadmap/repository-integration-map.md`; `docs/roadmap/theological-buildout-roadmap.md`
- What it informs: repo reading order, build sequence, layer integration, and contributor orientation
- What it must not be used for: claiming doctrinal finality, bypassing file-level review status, or treating roadmap prose as machine-contract authority
- Promotion path: narrow wording updates through governance-aware PRs; downstream files still need their own governed metadata and review posture
- Trust zone: mixed, currently active orientation surface
- Next recommended action: use these docs to keep new work in sequence, especially before opening new source families

### Front door and governance surface

- Source family name: AI front door and governance surface
- Repo location: `AI_FRONT_DOOR.md`; `docs/governance/`
- What it informs: contribution lanes, source-basis discipline, trust-zone posture, validation rules, and promotion boundaries
- What it must not be used for: replacing doctrine review, silently approving AI-generated content, or authorizing graph or validator changes without explicit review
- Promotion path: governance-note updates -> review -> downstream contributor behavior changes where accepted
- Trust zone: mixed canonical and proposed governance surface
- Next recommended action: keep pointing new contributors here first so incoming research stays staged and reviewable

### Agent stewardship control-plane seed

- Source family name: Logos agent stewardship control-plane seed
- Repo location: `incoming/research/logos-agent-stewardship-control-plane/`; `docs/roadmap/logos-agent-stewardship-roadmap.md`
- What it informs: future specialist-agent limits, approval gates, run-ledger expectations, and separation between knowledge plane, control plane, and execution plane
- What it must not be used for: activating agents, building a runtime, granting autonomous merge authority, or loosening current human-review requirements
- Promotion path: keep as governance/control-plane planning -> later governed control-plane notes only if explicitly activated
- Trust zone: incoming_research plus proposed roadmap guidance
- Next recommended action: preserve this as a safety-planning lane and do not activate agent workflows yet

## Licensing/source-policy input

### Bible text ingestion and translation policy seed

- Source family name: Bible text ingestion and translation policy seed
- Repo location: `incoming/research/biblical-connection-vocabulary-and-hermeneutics/bible-text-ingestion-policy.md`
- What it informs: licensing caution, translation-source handling, reference-first ingestion posture, and limits on public-repo text storage
- What it must not be used for: bulk Bible import, commentary text dumping, or implying that current source-policy review is complete
- Promotion path: policy review -> source-license registry and reference-anchor work -> later open-license examples only if explicitly approved
- Trust zone: incoming_research
- Next recommended action: treat this as the current boundary note for why Bible-text ingestion stays off until license and source-policy work is stronger

## Bottom line

Active source work should stay concentrated in:

- governed doctrine and concept files;
- draft AI-governance bridges;
- narrowly staged incoming research packets that already have a clear next bridge or review step.

Future, parked, control-plane, and source-policy inputs should remain explicit without being mistaken for live promotion authority.
