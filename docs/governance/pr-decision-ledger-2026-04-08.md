---
object_type: decision_ledger
trust_zone: canonical
lifecycle_status: active
provenance_note: "Compiled on 2026-04-08 from merged PR history and current governance corpus; uncertain mappings are explicitly marked proposed."
reason_for_inclusion: "Create a durable architecture decision ledger linking merged PR intent to governing rules and present canonical state."
---

# PR Decision Ledger (2026-04-08)

Scope: major merged pull requests visible in `git log` through PR #22.

## Ledger

| Ledger ID | Merged PR | What changed | Why it was approved | Architecture rule touched | Trust zone status |
|---|---|---|---|---|---|
| DL-PR-0006 | [#6](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/6) | Integrated exceptions-lake concepts into architecture/governance surfaces. | Needed a governed path for exception handling instead of ad hoc side channels. | Fractal rule: trust and boundary recursion; layer integration rule. | canonical |
| DL-PR-0007 | [#7](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/7) | Added overnight maintenance automation and logging patterns. | Improved operational reliability and repeatability for solo-maintainer flow. | A1 trust-direction guardrails via validator usage (inferred linkage). | proposed (mapping inference pending validation) |
| DL-PR-0008 | [#8](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/8) | Expanded cross-reference ID resolution behavior. | Reduced unresolved references and improved graph legibility. | A3 identity vs label separation (stable reference behavior). | canonical |
| DL-PR-0009 | [#9](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/9) | Fixed README internal file references. | Addressed broken navigation and contributor friction. | Internal link conventions and integrity checks. | canonical |
| DL-PR-0010 | [#10](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/10) | Added trust-zone normalization pass and validator support. | Enforced consistent trust vocabulary and safer cross-layer behavior. | A1 trust-zone dependency direction. | canonical |
| DL-PR-0011 | [#11](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/11) | Auto-generated retrieval neighborhood bundles. | Increased retrieval consistency and machine legibility for downstream agents. | Retrieval neighborhood model and canonical->derived direction (inferred linkage). | proposed (mapping inference pending validation) |
| DL-PR-0012 | [#12](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/12) | Added node completeness scoring and trend reporting. | Supplied measurable quality gates for iterative promotion work. | Completeness scoring model; review queue governance. | canonical |
| DL-PR-0014 | [#14](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/14) | Packaged governance-aware automation and nightly pipeline controls. | Established safer AI-assisted maintenance with explicit policy hooks. | AI output quarantine lane; human-in-the-loop AI build loop. | canonical |
| DL-PR-0015 | [#15](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/15) | Added semantic merge pipeline and drift artifacts. | Created merge-time semantic conflict visibility to reduce silent drift. | Drift detection policy; deprecate-not-delete posture support (inferred linkage). | proposed (mapping inference pending validation) |
| DL-PR-0016 | [#16](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/16) | Normalized controlled vocabularies and enforced validation. | Needed deterministic vocabulary for governance and schema compatibility. | Controlled vocabularies policy; A1 trust-zone vocabulary consistency. | canonical |
| DL-PR-0019 | [#19](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/19) | Added branch cleanup runbook and CI validation controls. | Reduced branch sprawl risk while preserving reviewable history. | A4 deprecate-not-delete aligned process discipline. | canonical |
| DL-PR-0020 | [#20](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/20) | Authored dated alignment baseline and related normalization planning docs. | Needed an immutable checkpoint before structural normalization work. | Identity and placement discipline; migration-before-mutation posture. | canonical |
| DL-PR-0021 | [#21](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/21) | Added canonical branch ruleset with required checks. | Enforced governed merge controls directly in repository policy. | PR gate enforcement for A1-A4 via required CI. | canonical |
| DL-PR-0022 | [#22](https://github.com/lowelltwong-alt/logos-fractal-theological-architecture/pull/22) | Added architecture invariants and explicit PR checklist. | Converted implicit governance assumptions into explicit, testable invariants. | A1 trust direction, A2 doctrine role separation, A3 identity-label separation, A4 deprecate-not-delete. | canonical |

## Notes on uncertainty handling

Entries explicitly labeled `proposed` identify inferred mappings that should be validated against original PR discussions before promotion to canonical certainty.

## Canonical backlink targets

- `docs/governance/architecture-invariants.md` -> `DL-PR-0022`
- `docs/governance/pr-architecture-invariants-checklist.md` -> `DL-PR-0022`
- `docs/governance/branch-cleanup-and-protection-runbook.md` -> `DL-PR-0019`
- `docs/governance/alignment-baseline-2026-04-08.md` -> `DL-PR-0020`
