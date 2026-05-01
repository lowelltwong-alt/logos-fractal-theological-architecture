---
object_type: route_template
trust_zone: governance_instructions
lifecycle_status: draft
review_status: unreviewed
ai_usage_posture: reusable_route_template
route: ai_run_ledger
---

# AI Run Ledger Template

## Settings

- Reasoning effort: xhigh
- Internet: off unless official tool documentation is required
- Permissions: conservative
- Mode: Plan first

## Required scope

Use this route for AI prompt, input, output, settings, and run-ledger audit policy.

## Required prompt fields

- Target branch:
- PR title:
- Capture level:
- Data sensitivity:
- Redaction policy:
- Storage path, if any:
- Schema path, if any:
- Non-goals:
- Validation expected:

## Required work

Define what AI input/output should be captured, summarized, redacted, hashed, or excluded.

Start with PR disclosure and redacted summaries before adding full run-ledger storage.

## Forbidden

Do not capture secrets, credentials, private source text, protected modern Bible/theology text, proprietary lexicons, privileged material, sensitive personal data, or raw private chats without redaction and approval.

## Required PR note

State the capture level, excluded content classes, redaction posture, and whether this PR creates only policy or also storage/schema infrastructure.
