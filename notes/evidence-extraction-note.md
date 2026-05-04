---
note_id: evidence-extraction
version: 0.1.0
source_of_truth: ../references/evidence-rules.md
status: optional_background_note
future_domain: evidence-extraction
use_boundary:
  - read only when evidence-sensitive tasks need a checklist
  - do not treat as a required execution workflow
---

# Evidence Extraction Note

This optional note helps reason about evidence packets. It is not a required workflow for every route.

Useful checks:

- Identify the claim or extraction target.
- Confirm the allowed corpus scope and source role.
- Prefer the smallest relevant canonical source before derivative aids.
- Capture source id, path, section, locator, support type, confidence, and freshness when available.
- Label unsupported, conflicting, or stale evidence explicitly.
- Stop when the evidence is sufficient for the requested confidence, or report what is missing.

Common mistakes:

- Using derivative summaries as canonical evidence.
- Omitting page/span/source path when available.
- Converting weak inference into direct support.
