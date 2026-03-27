# Anthropology to AI Governance Derivation Example

## Purpose

This worked example shows how a single doctrine node, Christian anthropology, can be traced downward into ethics, governance, LAIRCA configuration, and a practical institutional AI review workflow.

The purpose of the example is to demonstrate that the repository is not only a collection of theological writing. It is an architecture in which upstream commitments visibly shape downstream design.

## Starting doctrine

The starting doctrine is anthropology, understood here as a Christian account of the human person.

Core affirmations used in this example:
- the person possesses inherent dignity
- the person is a morally accountable agent
- the person is relational rather than merely individual or merely functional
- the person is finite and not exhaustively knowable through system representation
- the person is fallen, as are the institutions and tools that act upon persons

## Step 1. Theology to ethics

If those anthropological claims are true, several ethical implications follow.

### Ethical implication 1: persons must not be reduced to operational objects
A system may use representations, categories, or predictive markers for practical purposes, but it must not begin to treat those abstractions as the whole truth about the person.

### Ethical implication 2: dignity places limits on means
Even if an AI workflow improves speed or consistency, it should be questioned when it depersonalizes, manipulates, or obscures how persons are being judged.

### Ethical implication 3: accountable agency should be preserved
If the person is a real agent, then consequential decisions should not dissolve responsibility into opaque process. Institutions should be able to name who judged, who approved, and who is answerable.

### Ethical implication 4: fallenness requires caution
Neither human intuition nor machine output can be treated as morally neutral. Review, humility, and safeguards are required.

## Step 2. Ethics to governance

Those ethical implications generate governance requirements.

### Governance requirement 1: visible human ownership for consequential decisions
Where a decision affects dignity, vocation, discipline, exclusion, or access to important goods, a named human decision owner should remain visible.

### Governance requirement 2: bounded automation
Routine low-consequence tasks may be automated more freely. Consequential tasks require stronger oversight, review, and escalation.

### Governance requirement 3: explanation and challenge paths
Affected persons should not be trapped under a system they cannot understand or challenge, especially when the system influences meaningful outcomes.

### Governance requirement 4: category discipline
Institutions should examine whether their categories describe operational need or whether they are silently becoming judgments about worth, trustworthiness, or moral status.

### Governance requirement 5: audit and review
Because sin and distortion remain possible, the workflow should include auditability, periodic review, and review triggers for edge cases or harm signals.

## Step 3. Governance to LAIRCA

These governance requirements then configure each LAIRCA stage.

### L: Logos grounding
The architecture remains accountable to truth, dignity, and moral order rather than treating the AI workflow as self-justifying.

### A: Architect
System designers must define the workflow so that the AI is assisting judgment rather than quietly replacing the human moral owner in consequential contexts.

Architect implications:
- define decision categories by consequence level
- specify where human review is mandatory
- establish what cannot be fully automated
- define appeal and escalation thresholds

### I: Inform
The AI may surface summaries, patterns, comparisons, or candidate concerns, but it should also surface uncertainty, provenance, and relevant context so the human reviewer is not being steered blindly.

Inform implications:
- present source context, not only compressed conclusions
- identify uncertainty and low-confidence outputs
- distinguish facts, inferences, and recommendations

### R: Rank
The workflow may rank options or cases operationally, but ranking must not imply that the model is assigning moral worth to persons.

Rank implications:
- rank queues, not human value
- use ranking as triage support, not final moral judgment
- require review where ranking materially affects a person's treatment

### C: Commit
A named human decision owner remains responsible for consequential calls.

Commit implications:
- preserve named approval authority
- require justification for override or adoption of AI suggestion in sensitive cases
- log why the final decision was made

### A: Act
Execution may occur only after the above controls are satisfied.

Act implications:
- allow low-risk automated follow-through where appropriate
- block autonomous execution in morally significant cases without human commit
- preserve audit trail and appeal path

## Step 4. LAIRCA to institutional workflow

Now the architecture becomes a concrete institutional workflow.

### Example use case
Imagine a Christian nonprofit using AI to assist in reviewing sensitive internal reports, constituent concerns, or personnel-related triage.

The organization wants faster intake and pattern recognition, but does not want to treat people as tickets, risk labels, or output categories.

### Workflow design

#### Stage 1: intake
A human-defined intake structure receives reports, requests, or concerns.
AI may help summarize submissions and cluster similar themes.

#### Stage 2: assisted review
The system surfaces:
- summary of the issue
- relevant prior cases or policies
- uncertainty markers
- possible escalation category

It does not make the final consequential judgment.

#### Stage 3: human ranking review
A trained reviewer checks whether the suggested category reflects operational urgency without collapsing the person into the category.

#### Stage 4: human commit
Where the issue may affect dignity, discipline, access, or trust, a named accountable reviewer decides the next step and records the rationale.

#### Stage 5: bounded execution
Routine follow-up may be automated after approval, but consequential actions require explicit human authorization.

#### Stage 6: audit and reflection
The organization periodically reviews where the system may be distorting attention, encouraging category drift, or weakening responsibility.

## What this example prevents

This derivation is designed to prevent:
- treating AI output as moral judgment
- allowing ranking to harden into hidden valuation of persons
- hiding responsibility behind process language
- prioritizing speed at the expense of dignity
- using abstraction to avoid pastoral, managerial, or institutional accountability

## What this example allows

This example still allows:
- operational assistance
- retrieval and summarization
- triage support
- policy comparison
- pattern recognition
- routine automation after proper approval

It is not anti-tool. It is anti-deformation.

## Related files in this repo

This example should be read alongside:
- `docs/doctrines/anthropology.md`
- `docs/orderings/default-lairca-ordering.md`
- `docs/weightings/default-ai-governance-weighting.md`
- `docs/lairca/README.md`
- `docs/integrations/lairca/airca-companion-crosswalk.md`

## Why this example matters

This example is important because it shows the core method of the repository:

1. begin with theology
2. derive ethical implications
3. formalize governance requirements
4. configure decision architecture
5. translate into institutional design

That is the heart of the Logos project.
