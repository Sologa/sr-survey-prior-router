---
note_id: source-grounding-audit
version: 0.1.0
source_of_truth: ../references/source-map.md
status: optional_background_note
future_domain: source-grounding-audit
use_boundary:
  - read only when source-audit tasks need a checklist
  - do not treat as a required execution workflow
---

# Source Grounding Audit Note

This optional note helps reason about source roles and authority. It is not a required workflow for every route.

Useful checks:

- Read the source list or registry without modifying it.
- Classify each source by role, authority level, scope, and not-for boundary.
- Check version/date/freshness fields where the claim is time-sensitive.
- Separate canonical sources from derivative aids.
- Report gaps, stale sources, and overclaimed authority.
- Recommend the next smallest evidence or registry correction.

Common mistakes:

- Treating workflow tools as methodology authorities.
- Treating registry records as conduct guidance.
- Ignoring version/date or not-for boundaries.
