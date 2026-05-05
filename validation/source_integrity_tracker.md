# Source Integrity Tracker

Stable live tracker for `sr-survey-prior-router` source-integrity repair work.
Dated validation notes remain evidence snapshots; this file is the progress board.

Created: 2026-05-05

## Tracking Method

The GitHub/subagent review recommended a repo-local tracker as the source of truth.
GitHub Issues or Projects should only mirror this file if cross-person or remote
notification workflow becomes necessary. The nested pack repo is the tracked unit:
`docs/agent_capability_packs/sr-survey-prior-router`.

Status vocabulary:

- `todo`: known item, not started.
- `investigating`: being inspected or repaired.
- `fixed_pending_validation`: edits made; validation not complete.
- `validated`: edits and validation complete.
- `accepted_manual`: manual capture is the correct provenance, no automated repair planned.
- `blocked_external`: blocked by upstream access or server behavior.
- `deferred`: intentionally postponed until prerequisite work completes.

## Live Items

| source_id | integrity_problem | canonical_artifact | status | last_checked | next_smallest_action | validation_artifact |
| --- | --- | --- | --- | --- | --- | --- |
| `prisma_2020` | Earlier audit found two failed BMJ PDF rows and three linked PMC `*.pdf` HTML stubs; all five rows are now real local PDF captures with explicit provenance. | `references/canonical_sources/download_manifest.jsonl`; `references/corpus_index/document_index.jsonl`; `references/source_inventory/source_cards_v2/prisma_2020.md` | `validated` | 2026-05-05 | No missing PRISMA manifest PDFs remain. Keep BMJ White Rose and PMC OA Cloud provenance caveats visible. | `validation/prisma_2020_pdf_recapture_validation_2026-05-05.md` |
| `paperswithcode` | `canonical_about` and `canonical_sota` local captures redirected to Hugging Face Trending Papers. | `references/canonical_sources/download_manifest.jsonl`; `references/corpus_index/document_index.jsonl`; `references/source_inventory/source_cards_v2/paperswithcode.md` | `validated` | 2026-05-05 | Keep redirected captures as provenance only; use official GitHub data/client artifacts for local evidence. | `validation/source_integrity_repair_validation_2026-05-05.md` |
| `tacl_submission` | Direct MIT Press canonical locator failed with 403; usable local evidence is the official TransACL fallback. | `references/source_inventory/source_manifest.jsonl`; `references/corpus_index/document_index.jsonl`; `references/source_inventory/source_cards_v2/tacl_submission.md` | `validated` | 2026-05-05 | Use official TransACL fallback Markdown/final_url rows; keep MIT Press URL as blocked publisher locator. | `validation/source_integrity_repair_validation_2026-05-05.md` |
| `computational_linguistics` | Direct MIT Press canonical locator failed with 403; usable local evidence is the official CL Journal OJS fallback. | `references/source_inventory/source_manifest.jsonl`; `references/corpus_index/document_index.jsonl`; `references/source_inventory/source_cards_v2/computational_linguistics.md` | `validated` | 2026-05-05 | Use official CL Journal OJS fallback Markdown/final_url rows; keep MIT Press URL as blocked publisher locator. | `validation/source_integrity_repair_validation_2026-05-05.md` |
| `press` | PRESS local capture was made manually in browser because automated retrieval did not produce a usable file; all three manual PDFs now have page-level Markdown and section locators. | `validation/manual_browser_capture_2026-05-05.md`; `references/source_inventory/source_cards_v2/press.md`; `references/corpus_index/sections/by_source/press.jsonl` | `accepted_manual` | 2026-05-05 | Preserve manual-browser provenance; do not automate unless user requests a fresh recapture. | `validation/pdf_md_locator_completeness_audit_2026-05-05.md` |
| `cacm_author_guidelines` | CACM local capture was made manually in browser because automated retrieval did not produce a usable file; all four manual PDFs now have page-level Markdown and section locators. | `validation/manual_browser_capture_2026-05-05.md`; `references/source_inventory/source_cards_v2/cacm_author_guidelines.md`; `references/corpus_index/sections/by_source/cacm_author_guidelines.jsonl` | `accepted_manual` | 2026-05-05 | Preserve manual-browser provenance; do not automate unless user requests a fresh recapture. | `validation/pdf_md_locator_completeness_audit_2026-05-05.md` |
| `grade_working_group` | The linked 2024 newsletter local `.pdf.pdf` file was a Dropbox HTML preview capture, not a real PDF; it was recaptured from Dropbox `dl=1` as a 6-page PDF and converted to page-level Markdown. | `references/canonical_sources/raw/grade_working_group/linked_2_grade-working-group-newsletter-202409.pdf.pdf`; `references/canonical_sources/md/grade_working_group/linked_2_grade-working-group-newsletter-202409.pdf.md`; `references/source_inventory/source_cards_v2/grade_working_group.md` | `validated` | 2026-05-05 | No remaining GRADE Working Group PDF/Markdown locator gap. | `validation/pdf_md_locator_completeness_audit_2026-05-05.md` |
| `graphify` | Graph/navigation refresh was deferred until source-integrity repairs were complete; the scoped router/index graph is now refreshed and validated. | `graphify-out/`; `validation/validate_graphify_navigation.py`; `scripts/build_graphify_index_graph.py` | `validated` | 2026-05-05 | No remaining graphify source-integrity action. Keep graph output locator-only and rebuild after route/source/document/section index changes. | `validation/graphify_refresh_validation_2026-05-05.md` |
| `validation_notes` | Subagent review found stale validation-note statements: `chatgpt_deep_review_alignment_2026-05-05.md` reported 210 document rows instead of 212, and two same-day notes still described graphify as deferred/stale after a later refresh. | `validation/chatgpt_deep_review_alignment_2026-05-05.md`; `validation/source_integrity_repair_validation_2026-05-05.md`; `validation/pdf_md_locator_completeness_audit_2026-05-05.md`; `validation/graphify_refresh_validation_2026-05-05.md` | `validated` | 2026-05-05 | Count corrected and explicit supersession/current-status notes added. | `validation/source_integrity_tracker.md` |
| `graphify_publish_boundary` | Subagent review found that `validate_graphify_navigation.py` required ignored `graphify-out/` files, making fresh-checkout validation depend on local rebuildable artifacts. | `validation/validate_graphify_navigation.py`; `.gitignore`; `references/graphify-navigation.md`; `validation/graphify_refresh_validation_2026-05-05.md` | `validated` | 2026-05-05 | Generated graph files are optional by default; `--require-generated` covers local refresh validation. | `validation/source_integrity_tracker.md` |
| `graphify_requirements` | Subagent review found graph builder imports beyond `networkx`: `yaml` and the `graphify` module provided by the `graphifyy` package. | `requirements.txt`; `scripts/build_graphify_index_graph.py`; `validation/graphify_navigation_validation_2026-05-04.md` | `validated` | 2026-05-05 | Added `PyYAML` and `graphifyy` to requirements and updated the validation note to use `--require-generated`. | `validation/source_integrity_tracker.md` |
| `source_cards_v2_schema` | Subagent review found source-card `authority_level` values outside the README's recommended list even though the cards validate and the values are intentional. | `references/source_inventory/source_cards_v2/README.md`; `references/source_inventory/source_cards_v2/*.md`; `validation/validate_source_cards_v2.py` | `validated` | 2026-05-05 | Documented the current intentional authority-level values in the source-card-v2 schema. | `validation/source_integrity_tracker.md` |
| `nested_repo_publish_state` | Subagent review found the nested pack repo still had modified and untracked publish artifacts after content validation passed. | `.git/`; `git status --short`; `validation/source_integrity_tracker.md` | `validated` | 2026-05-05 | Validated pack changes are committed in the nested repo; verify `git status --short` remains clean before publishing. | `validation/source_integrity_tracker.md` |
