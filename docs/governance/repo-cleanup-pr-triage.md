# Logos open PR triage note

Use this as a review sheet while building `cleanup/repo-consolidation`.

| PR | Title | Recommended cleanup handling |
|---|---|---|
| #28 | Normalize layer and node metadata: add address, trust, lifecycle, epistemic, and governance fields | Review first. Cherry-pick only the pieces that fit your final canonical path/schema decisions. Do **not** merge directly into `main` before cleanup. |
| #18 | Add Codex merge-alignment spine for governance and repo comparison | Review as documentation/supporting alignment notes. Cherry-pick selectively if it clarifies cleanup rules. |
| #17 | Reinforce exceptions-lake and governed learning as architecture DNA | Keep out of the core cleanup unless you want exceptions-lake in this wave. Otherwise close as superseded and revisit later. |
| #13 | Add canonical external mapping grammar and ingestion validator | Review after you decide the single canonical schema folder and ontology boundary. Cherry-pick only if it aligns cleanly. |
| #5 | Add exceptions lake import pack | Same as #17: useful only if exceptions-lake remains an active priority in the cleanup wave. |
| #4 (draft) | feat: add trinity network layer and phased build architecture | Leave for after cleanup. This is content expansion and should not be mixed into a structural normalization PR. |

## Simple decision rule
- If a PR helps normalize paths, validation, link integrity, or branch/rules governance, it belongs in the cleanup wave.
- If a PR adds new doctrinal/network content, it should wait until after cleanup is merged.
- If two PRs solve the same problem differently, keep the simpler one and close the other as superseded.
