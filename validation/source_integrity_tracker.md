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
| `current_omx_native_audit_2026_05_05` | Fresh native-subagent plus isolated-OMX audit found no current source-content blocker in the tracked pack. Derivative cards/indexes align with checked canonical Markdown at draft-router scope. | `SKILL.md`; `agents/openai.yaml`; `references/source_inventory/source_cards_v2/`; `references/canonical_sources/md/`; `references/corpus_index/`; `validation/source_integrity_tracker.md` | `validated` | 2026-05-05 | No source-content repair required from this audit. Keep draft/seed-corpus limitations visible and do not claim final knowledge-heavy coverage. | `validation/source_integrity_tracker.md` |
| `validation_snapshot_supersession_headers` | Fresh tracker audit found older validation snapshot files still contain stale blocked/bad-capture/not-ready conclusions without in-file supersession headers. The tracker is current, but a reviewer opening old notes directly can be misled. | `validation/agent_qa_validation_2026-05-04.md`; `validation/source_alignment_audit_2026-05-04.md`; `validation/source_alignment_fix_validation_2026-05-04.md`; `validation/live_recapture_2026-05-05.md`; `validation/README.md` | `validated` | 2026-05-05 | Supersession banners were added to the four stale snapshots, and `validation/README.md` now points reviewers to the current tracker before dated notes. | `validation/source_integrity_tracker.md` |
| `omx_validation_environment` | Isolated OMX worker used an environment with `networkx 3.3`, below this pack's `networkx>=3.4,<4` requirement, so graphify validation failed only in that OMX environment. Pack-local Python had `networkx 3.6.1` and passed graphify validation. | `requirements.txt`; `validation/validate_graphify_navigation.py`; `validation/source_integrity_tracker.md` | `deferred` | 2026-05-05 | Install this pack's requirements in the OMX lab before treating OMX as a green validation environment, or make the graphify validator compatible with `networkx 3.3` if that environment must be supported. | `validation/source_integrity_tracker.md` |
| `remote_publish_state` | Fresh publish audit found the nested pack repo clean but local `main` is ahead of `origin/main` by four commits, so content is local-only until pushed. | `.git/`; `git status --branch --short`; `git branch -vv` | `todo` | 2026-05-05 | Push the nested repo when the goal is actual GitHub publication rather than local readiness review. | `validation/source_integrity_tracker.md` |
| `archive_publish_sidecars` | Native publish-readiness audit found 15 AppleDouble files inside nested `.git`. They are not Git-push blockers, but would matter if the whole directory is zipped or handed off. | `.git/._index`; `.git/gk/._config`; `.git/objects/*/._*`; `.git/refs/heads/._main` | `deferred` | 2026-05-05 | For archive-based handoff, exclude `.git/` or remove sidecars before packaging. Not needed for normal Git publication. | `validation/source_integrity_tracker.md` |
| `validation_publication_entrypoint` | Publication-surface audit recommended a tracked validation entry point so reviewers see current status before historical snapshots. | `validation/README.md`; `validation/source_integrity_tracker.md` | `validated` | 2026-05-05 | `validation/README.md` is the publication-facing entry point; `source_integrity_tracker.md` remains the live source of truth. | `validation/README.md` |
| `canonical_md_metadata_drift` | First-round blocker repair recomputed all existing Markdown `md_sha256` values and refreshed current `bytes` metadata in document and section indexes. Rows without `md_sha256` were intentionally left unchanged under a present-field-only checksum policy. | `references/source_inventory/source_manifest.jsonl`; `references/canonical_sources/download_manifest.jsonl`; `references/corpus_index/document_index.jsonl`; `references/corpus_index/section_index_manifest.jsonl`; `references/canonical_sources/md/` | `validated` | 2026-05-06 | No current md_sha256/bytes drift remains for fields updated in this round. Preserve the present-field-only checksum policy unless a later schema migration is requested. | `validation/source_integrity_tracker.md` |
| `route_refresh_sensitive_coverage` | `route-source-index.yaml` now surfaces the four audited high freshness-risk source IDs: `core_api` and `paperswithcode` under `general_domain_prior`, and `tacl_submission` and `computational_linguistics` under `survey_writing_prior`. | `references/route-source-index.yaml`; `references/source_inventory/source_cards_v2/*.md` | `validated` | 2026-05-06 | Keep these route entries as freshness-visible locator/venue/API sources, not methodology authorities. | `validation/source_integrity_tracker.md` |
| `cacm_manifest_browser_verified_url` | Added the CACM-specific canonical URL to `cacm_author_guidelines.browser_verified_urls` while preserving the existing ACM fallback URLs. | `references/source_inventory/source_manifest.jsonl` | `validated` | 2026-05-06 | No live refresh was performed; the URL records the existing manual browser-capture provenance. | `validation/source_integrity_tracker.md` |
| `chatgpt_deep_review_bundle_supersession` | Added an in-file supersession banner near the top of the imported ChatGPT deep-review snapshot pointing direct readers to `../source_integrity_tracker.md` and `../README.md` for current status. | `validation/chatgpt_deep_review_2026-05-04/review.md`; `validation/README.md`; `validation/source_integrity_tracker.md` | `validated` | 2026-05-06 | Preserve this review as a dated imported snapshot, not current publication truth. | `validation/source_integrity_tracker.md` |
| `source_card_keypoint_yaml_parseability` | Quoted the three colon-bearing `claim` scalars that blocked strict PyYAML parsing in `narrative_synthesis_york_2006.md`, `prisma_2020.md`, and `robis.md`; factual wording was unchanged. | `references/source_inventory/source_cards_v2/narrative_synthesis_york_2006.md`; `references/source_inventory/source_cards_v2/prisma_2020.md`; `references/source_inventory/source_cards_v2/robis.md`; `references/source_inventory/source_cards_v2/README.md`; `validation/validate_source_cards_v2.py` | `validated` | 2026-05-06 | All 65 source-card-v2 key-point YAML blocks now parse under strict PyYAML. | `validation/source_integrity_tracker.md` |
| `non_git_appledouble_sidecars` | Required validators initially failed after external-drive edits created non-`.git` AppleDouble files, plus one pre-existing validation sidecar. These non-`.git` sidecars were removed; nested `.git` sidecars were not touched. | `find . -path './.git' -prune -o -name '._*' -type f -print`; `validation/validate_source_cards_v2.py`; `validation/validate_graphify_navigation.py` | `validated` | 2026-05-06 | Continue running `COPYFILE_DISABLE=1` and the non-`.git` sidecar scan before publish/archive handoff. | `validation/source_integrity_tracker.md` |

## 2026-05-05 First-round native subagent audit

Task: first-round source-integrity and publish-readiness audit for `sr-survey-prior-router`, including `SKILL.md`, `agents/openai.yaml`, route/index/source-card/validation docs, and local canonical Markdown under `references/canonical_sources/md/`.

Verdict: not ready to publish as a standalone reusable pack yet. The local canonical Markdown is broadly present and targeted source-card claims mostly align with the checked canonical files, but publish/use readiness is blocked by locator portability and state-label consistency defects.

Second-level worker:

```sh
codex exec --ephemeral --cd "/Volumes/My Book/NLP_PRISMA_Reviews" --sandbox read-only --skip-git-repo-check 'You are a second-level read-only audit worker. Task: audit docs/agent_capability_packs/sr-survey-prior-router for source integrity and publish readiness. You MUST NOT write files. You MUST NOT spawn native subagents. You MUST NOT run codex exec or any other nested worker. Inspect SKILL.md, agents/openai.yaml, references route/index/source cards/validation docs, references/canonical_sources/md, and docs/agent_capability_packs/sr-survey-prior-router/validation/source_integrity_tracker.md. Compare derivative markdown/cards/routes/validation claims against canonical markdown content, not just filenames. Find content errors, omissions, incorrect source-state labels, refresh-sensitive/blocking inconsistencies, and publish-time misleading claims. Return: (1) task, (2) exact shell commands you ran with exit codes, (3) concise output summary, (4) ready-to-publish verdict: ready/not ready/conditional ready, (5) blockers and non-blockers with file paths, (6) limitations, (7) whether you wrote files. Keep the audit focused and evidence-based. Final answer in Chinese.'
```

Worker exit code: 0.

Worker output summary: validators pass (`validate_source_cards_v2.py`, `validate_graphify_navigation.py`, and `validate_graphify_navigation.py --require-generated`), nested repo status was clean, and targeted checks of high-risk/manual-capture sources mostly supported the current card claims. The worker found three publish-readiness issues: pack-root path portability, source-state labels that conflict with the index's own status vocabulary, and one `core_api` card locator/supporting-path mismatch.

Worker limitations: read-only local audit only; no live web refresh; no full semantic verification of every card claim; some broad `rg` output was truncated. Worker wrote files: no.

Controller verification:

- `python3 validation/validate_source_cards_v2.py`: pass; 65 cards for 65 manifest sources.
- `python3 validation/validate_graphify_navigation.py`: pass; generated graph present.
- `python3 validation/validate_graphify_navigation.py --require-generated`: pass; generated graph present.
- `git -C docs/agent_capability_packs/sr-survey-prior-router status --short`: clean before this tracker append.
- Pack-root locator portability audit: `source_manifest.jsonl` has 212/212 locator paths missing from the nested pack root but resolvable after stripping `docs/agent_capability_packs/sr-survey-prior-router/`; `download_manifest.jsonl` has 212/212; `document_index.jsonl` has 212/212; `section_index_manifest.jsonl` has 65/65; `local_corpus_index.json` has 380/380.
- Source-status audit: `cacm_author_guidelines` is `available` with 5 blocked attempts and `press` is `available` with 6 blocked attempts, contradicting `local_corpus_index.md` line 8 semantics. `clinicaltrials_api` is `partial` with 0 blocked attempts, but this is explainable by sparse/SPA human docs plus richer OpenAPI/version captures.
- Source-card locator audit: checked 338 `quote_or_locator` Markdown line references; found 2 issues in `references/source_inventory/source_cards_v2/core_api.md`, where `official_api_root_official_api_root.md` and `official_api_v3_docs_v3.md` appear in the locator string but not in that key point's `supporting_canonical_paths`.

Blockers:

1. `references/source_inventory/source_manifest.jsonl`, `references/canonical_sources/download_manifest.jsonl`, `references/corpus_index/document_index.jsonl`, `references/corpus_index/section_index_manifest.jsonl`, `references/source_inventory/local_corpus_index.json`, and `references/source_inventory/local_corpus_index.md` use parent-repo-prefixed locator paths. These work from `/Volumes/My Book/NLP_PRISMA_Reviews` but break from the nested pack root and would mislead a standalone GitHub reviewer or installed skill.
2. `references/source_inventory/local_corpus_index.md` and `.json` mark `press` and `cacm_author_guidelines` as `available` despite retained blocked scripted-fetch attempts. Either the rows should use a state such as `partial`/`accepted_manual`, or the status vocabulary should explicitly separate local evidence availability from refresh/retrieval blockage.

Non-blockers:

- `references/source_inventory/source_cards_v2/core_api.md` should add the two cited stub files to the affected key point's `supporting_canonical_paths`, or remove them from that key point's locator string.
- `agents/openai.yaml` sets `allow_implicit_invocation: true`; this is not a source-integrity error, but should be explicitly confirmed before publishing a broad router.
- Manual browser captures for PRESS and CACM have navigation/footer/cookie noise and reuse caveats. These are documented and do not currently hide source limits.
- `graphify-out/` and split by-source section locators are ignored local/rebuildable artifacts. Current docs describe fallback behavior, so this is acceptable if the public pack does not require them.

Next smallest action for the repair round: normalize locator paths to the pack root or teach every consumer/validator to resolve both parent-prefixed and pack-root-relative paths, then fix the `available` status semantics for manual-capture-with-blocked-refresh rows and repair the `core_api` card locator mismatch.

## 2026-05-05 Second-round repair

Task: linearly repair the first-round publish blockers/non-blocker for `sr-survey-prior-router`, using a first-level controller plus foreground read-only `codex exec` workers for patch review.

Files repaired:

- `references/source_inventory/source_manifest.jsonl`
- `references/canonical_sources/download_manifest.jsonl`
- `references/corpus_index/document_index.jsonl`
- `references/corpus_index/section_index_manifest.jsonl`
- `references/corpus_index/sections/by_source/*.jsonl`
- `references/source_inventory/local_corpus_index.json`
- `references/source_inventory/local_corpus_index.md`
- `references/source_inventory/source_cards_v2/core_api.md`
- `graphify-out/` regenerated as ignored locator-only local output
- `validation/source_integrity_tracker.md`

Repair summary:

- Normalized public locator paths from parent-repo-prefixed `docs/agent_capability_packs/sr-survey-prior-router/...` to pack-root-relative `references/...` paths.
- Included split section locators under `references/corpus_index/sections/by_source/*.jsonl` after the first second-level patch review found 4647 remaining parent-prefixed `md_path` values.
- Kept `press` and `cacm_author_guidelines` as locally `available` because manual browser Markdown evidence exists, but changed the status rule to separate local evidence availability from blocked scripted-refresh attempts.
- Added `refresh_status=scripted_fetch_blocked_manual_browser_refresh_required` to the `press` and `cacm_author_guidelines` rows in `local_corpus_index.json`.
- Added the two CORE entry-stub Markdown files cited by the last `core_api` key point to that key point's `supporting_canonical_paths`.
- Rebuilt `graphify-out/` after index changes; graph output remains locator-only and contains no canonical raw/md or split-section paths.

Second-level worker 1:

```sh
codex exec --ephemeral --cd "/Volumes/My Book/NLP_PRISMA_Reviews" --sandbox read-only --skip-git-repo-check 'You are a second-level read-only patch-review worker for docs/agent_capability_packs/sr-survey-prior-router. You MUST NOT write files. You MUST NOT spawn native subagents. You MUST NOT run codex exec or any nested worker. Review the current second-round repair patch against this spec: path portability must remove parent prefix docs/agent_capability_packs/sr-survey-prior-router/ from locator artifacts while keeping referenced files resolvable from the pack root; status semantics must make press and cacm_author_guidelines available/manual evidence compatible with blocked scripted refresh attempts; core_api.md must not cite quote locator files absent from supporting_canonical_paths; graphify generated artifacts may be refreshed but must remain locator-only. Inspect git -C docs/agent_capability_packs/sr-survey-prior-router diff, run read-only validation or audit commands as needed from the pack root, and report in Chinese: task, exact commands you ran with exit codes, output summary, whether blockers remain, ready-to-publish verdict, limitations, and whether you wrote files.'
```

Worker 1 exit code: 0.

Worker 1 output summary: source-card and graphify validators passed, the six top-level locator artifacts had zero parent prefixes and all checked JSON path values resolved from the pack root, `press`/`cacm_author_guidelines` status semantics were acceptable, `core_api` had no remaining locator/supporting-path mismatch, and `graphify-out/` stayed locator-only. The worker found one remaining same-class blocker: all 65 split by-source section index files still had parent-prefixed `md_path` values, 4647 path values total, all resolvable after stripping the prefix.

Worker 1 limitations: read-only local audit only; no live web refresh; no graph or section-index regeneration; no full semantic re-review of all source-card claims; some exploratory output was truncated. Worker 1 wrote files: no.

Second-level worker 2:

```sh
codex exec --ephemeral --cd "/Volumes/My Book/NLP_PRISMA_Reviews" --sandbox read-only --skip-git-repo-check 'You are a second-level final read-only patch-review worker for docs/agent_capability_packs/sr-survey-prior-router. You MUST NOT write files. You MUST NOT spawn native subagents. You MUST NOT run codex exec or any nested worker. Keep output small and avoid broad diff or broad rg output. Review the final second-round repair after the controller also normalized references/corpus_index/sections/by_source/*.jsonl. From the pack root, run concise read-only checks only: git status short and diff stat; validate_source_cards_v2.py; validate_graphify_navigation.py; validate_graphify_navigation.py --require-generated; a concise parent-prefix/path-resolution count covering the six top-level locator artifacts plus references/corpus_index/sections/by_source/*.jsonl; a concise check of press and cacm_author_guidelines status/local manual availability/blocked refresh fields; a concise core_api quote_or_locator versus supporting_canonical_paths check; and graphify-out forbidden path check. Report in Chinese: task, exact commands you ran with exit codes, output summary, remaining blockers if any, ready-to-publish verdict, limitations, and whether you wrote files.'
```

Worker 2 exit code: 0.

Worker 2 output summary: `git status --short` showed only modified tracked pack files; `git diff --stat` reported 8 modified tracked files before this tracker append; `validate_source_cards_v2.py`, `validate_graphify_navigation.py`, and `validate_graphify_navigation.py --require-generated` passed. Parent-prefix/path-resolution count passed for the six top-level locator files and the split by-source section locators: top-level `rows=662`, `path_values=1574`, `bad_prefix=0`, `missing=0`, `parent_mismatch=0`; by-source `files=65`, `section_rows=4647`, `path_values=4647`, `bad_prefix=0`, `missing=0`, `parent_mismatch=0`, `filename_source_mismatch=0`. `press` had 3 manual downloads and 6 failed scripted refresh attempts; `cacm_author_guidelines` had 4 manual downloads and 5 failed scripted refresh attempts; both were locally available with manual-capture validation. `core_api` had `claims=4`, `locator_doc_refs=6`, `unmatched_locator_docs=0`, and `missing_support_paths=0`. Forbidden graphify path counts were all zero for canonical raw, canonical md, split section paths, `refs_old/`, and `upstream_repo/`.

Worker 2 limitations: read-only local audit only; no live network refresh; no full diff expansion; no full-text semantic re-review. Worker 2 wrote files: no.

Controller verification after repairs:

- `python3 validation/validate_source_cards_v2.py`: pass; 65 cards for 65 manifest sources.
- `python3 validation/validate_graphify_navigation.py`: pass; generated graph present.
- `python3 validation/validate_graphify_navigation.py --require-generated`: pass; generated graph present.
- Targeted path portability check: pass; 5837 path references checked across the six top-level locator artifacts plus 65 by-source section index files; parent-prefixed strings: 0.
- Targeted status semantics check: pass; `press` and `cacm_author_guidelines` are locally `available`, manual-browser converted, refresh-sensitive, and explicitly marked `scripted_fetch_blocked_manual_browser_refresh_required`.
- Targeted `core_api` locator/support check: pass; 4 claim blocks checked; no quote locator references missing from supporting paths.
- macOS metadata check: pass; no pack `._*` files outside ignored `.git`/`.omx` metadata remained after edits.

Remaining limitations:

- No live web refresh was performed.
- Manual browser captures for `press` and `cacm_author_guidelines` remain refresh-sensitive and should be recaptured manually or with browser automation if exact current wording is needed later.
- The ready-to-publish judgment covers this source-integrity and locator-portability repair scope; it does not certify every substantive claim in every source card against full canonical text.

Verdict: ready to publish for the second-round source-integrity scope.

## 2026-05-05 Third-round zero-known-issues audit

Task: zero-known-issues local publish/readiness audit for `sr-survey-prior-router` after the second-round repair. This round intentionally did not repair content. The only intended write is this tracker section.

Second-level worker:

```sh
codex exec --ephemeral --cd "/Volumes/My Book/NLP_PRISMA_Reviews" --sandbox read-only --skip-git-repo-check 'You are a second-level read-only audit worker for docs/agent_capability_packs/sr-survey-prior-router. You MUST NOT write files. You MUST NOT spawn native subagents. You MUST NOT run codex exec or any nested worker. Task: perform a zero-known-issues local publish/readiness audit after previous repairs. Inspect SKILL.md, agents/openai.yaml, requirements, .gitignore, .graphifyignore, README-like docs, references route/index/source inventory/source cards v2/canonical_sources/corpus_index, validation notes/scripts/validators, tracked diff/status, and behavior when ignored generated files are absent. Check for any remaining problem that would affect complete publication and use: stale wording, misleading status semantics, parent-prefixed or absolute paths, validator gaps, ignored/rebuildable artifact dependency, GitHub checkout portability, allow_implicit_invocation risk, source-card versus canonical markdown alignment, manifest/local corpus/document index consistency. Do not do live web refresh. Run validators and focused read-only scripts as needed. Return in Chinese: task, exact shell commands run with exit codes, concise output summary, limitations, whether you wrote files, and final verdict. If any issue exists, do not say ready; list severity, exact file(s), evidence, and smallest recommended fix. If no issues, say no known issues within local audit scope and state limitations.'
```

Worker exit code: 0.

Worker output summary: not ready. The worker found that the local validators and main locator indexes pass, but zero-known-issues is not met because canonical Markdown headers still expose non-portable local raw paths, the nested pack repo is not in a clean publish state, `coverage_report.md` still has a parent-prefixed corpus path, and `allow_implicit_invocation: true` remains a publish policy risk for a broad router.

Worker command/result summary:

- `git status --branch --short`: exit 0; branch `main...origin/main [ahead 1]` with 8 modified tracked files.
- `python3 validation/validate_source_cards_v2.py`: exit 0; pass, 65 cards / 65 manifest sources.
- `python3 validation/validate_graphify_navigation.py`: exit 0; pass, generated graph present.
- `python3 validation/validate_graphify_navigation.py --require-generated`: exit 0; pass.
- Simulated absent `graphify-out` default validation: exit 0; pass as `absent_optional_rebuildable`.
- Simulated absent `graphify-out --require-generated`: exit 1 as expected; missing generated graph artifacts reported.
- JSON/JSONL parse and manifest/index consistency checks: exit 0; 65 source IDs, 65 local corpus sources, 65 source cards, 212 document rows, 254 download rows, 65 section manifests, and no missing source/card/index sets.
- Top-level locator portability check: exit 0; 1125 path values, 0 parent-prefixed paths, 0 local absolute paths, 0 missing pack-root paths.
- Split `sections/by_source` check: exit 0; 65 files and 4647 rows, with 0 parent/absolute/missing/source-mismatch issues.
- Source-card keypoint locator/support check: exit 0; 308 claims, 338 locator doc refs, 0 unmatched locator docs, 0 missing support paths.
- Canonical Markdown raw-header portability check: exit 0 but found 212 `Local raw file:` headers; 109 absolute local paths, 100 parent-prefixed paths, 3 pack-root-relative paths.
- `git diff --check`: exit 0.
- Requirements import check (`networkx`, `yaml`, `graphify`): exit 0.
- Two here-doc probes failed in the read-only worker because the sandbox could not create shell temp files; no files were written.

Worker limitations: read-only local audit only; no live web refresh; no full semantic re-review of all 308 source-card claims; raw corpus, split section, and graphify absence were simulated rather than physically deleting ignored artifacts; outer `/Volumes/My Book/NLP_PRISMA_Reviews` is not a Git repo, so Git state is from the nested pack repo.

Worker wrote files: no.

Controller checks:

- `git status --branch --short`: exit 0; nested pack repo is `main...origin/main [ahead 1]` with the same 8 modified tracked files.
- `python3 validation/validate_source_cards_v2.py`: exit 0; pass, 65 cards for 65 manifest sources.
- `python3 validation/validate_graphify_navigation.py`: exit 0; pass, generated graph present.
- `python3 validation/validate_graphify_navigation.py --require-generated`: exit 0; pass, generated graph present.
- `git diff --check`: exit 0.
- `python3 -m json.tool references/source_inventory/local_corpus_index.json` plus JSONL parse check: exit 0.
- Requirements import check for `networkx`, `yaml`, and `graphify`: exit 0.
- Manifest/index consistency check: exit 0; `source_manifest_ids=65`, `unique_source_ids=65`, `local_corpus_sources=65`, `source_cards_v2=65`, `document_index_rows=212`, `download_manifest_rows=254`, `section_manifest_rows=65`, `doc_sources=65`, `section_sources=65`; all missing/delta lists empty.
- Top-level locator portability check across `source_manifest`, `download_manifest`, `document_index`, `section_index_manifest`, and `local_corpus_index`: exit 0; `rows=596`, `path_values=1125`, `parent_prefix=0`, `absolute_local=0`, `missing_pack_root=0`.
- Source-card keypoint locator/support check: exit 0; `claims=308`, `locator_doc_refs=338`, `unmatched_locator_docs=0`, `missing_support_paths=0`.
- Canonical Markdown raw-header portability check: exit 0 but confirms the worker issue: `md_files=212`, `local_raw_headers=212`, `absolute=109`, `parent_prefixed=100`, `pack_relative=3`, `other=0`.
- Simulated absent `graphify-out` with `PYTHONDONTWRITEBYTECODE=1`: default validation exit 0 (`generated_graph: absent_optional_rebuildable`); `--require-generated` exit 1 as expected with three missing generated graph artifacts.
- Controller cleanup note: an initial Python import simulation created `validation/__pycache__` and AppleDouble metadata; these controller-created temp files were removed, and final `find validation -maxdepth 2 \( -name '__pycache__' -o -name '._*' \) -print` returned no paths.

Remaining issues:

1. Severity: medium-high. Tracked canonical Markdown headers still expose non-portable raw paths. All 212 tracked files under `references/canonical_sources/md/**/*.md` have `Local raw file:` headers; 109 are local absolute paths such as `/Volumes/My Book/...`, and 100 are parent-repo-prefixed `docs/agent_capability_packs/sr-survey-prior-router/...` paths. Example: `references/canonical_sources/md/acl_anthology/canonical_api.md:4`. Smallest fix: normalize these headers to pack-root-relative `references/canonical_sources/raw/...` paths, or use an explicit placeholder such as `${RAW_CORPUS_ROOT}/...` plus wording that raw backing files may be absent from a public checkout. Add a validator so this cannot recur.
2. Severity: medium. The nested pack repo is not in a clean publish state. `git status --branch --short` shows `main...origin/main [ahead 1]` and 8 modified tracked files: `references/canonical_sources/download_manifest.jsonl`, `references/corpus_index/document_index.jsonl`, `references/corpus_index/section_index_manifest.jsonl`, `references/source_inventory/local_corpus_index.json`, `references/source_inventory/local_corpus_index.md`, `references/source_inventory/source_cards_v2/core_api.md`, `references/source_inventory/source_manifest.jsonl`, and `validation/source_integrity_tracker.md`. This also conflicts with the tracker row that says validated pack changes are committed and clean before publishing. Smallest fix: either commit the validated repair files before publishing, or mark the publish state as pending commit and keep the release gate at a clean `git status`.
3. Severity: low. `references/source_inventory/coverage_report.md:15` still says the local corpus path is `docs/agent_capability_packs/sr-survey-prior-router/references/canonical_sources/`, which is parent-prefixed from the pack root. Smallest fix: change it to `references/canonical_sources/`.
4. Severity: low / publish policy decision. `agents/openai.yaml:6` sets `allow_implicit_invocation: true` for a broad router whose skill description covers prepared resources, domain prior, literature corpora, survey/SR writing prior, evidence grounding, source audit, and source-grounded synthesis. `SKILL.md` has useful route boundaries, but the publish policy should still be explicit. Smallest fix: set it to `false` for draft/explicit-only publication, or keep `true` and document that implicit invocation is intentional.

Positive checks with no new issues found:

- Source-card v2 schema validation passes.
- Graphify navigation validation passes with generated graph present, and default validation can tolerate absent ignored `graphify-out/`.
- Required generated graph validation fails when graphify artifacts are absent, as intended.
- Main manifest/index locator paths are now pack-root-relative and resolvable.
- Source-card keypoint quote locators match supporting canonical paths in the checked pattern.
- JSON/JSONL files parse.
- Requirements imports are available in the current environment.

Verdict: not ready for zero-known-issues publication. The stopping criterion "no known issues" is not met. Next repair round should fix the four remaining issues above, then rerun the same zero-known-issues audit.

## 2026-05-05 Fourth-round repair

Task: repair the four third-round zero-known-issues blockers for `sr-survey-prior-router`, verify the pack, and prepare a clean nested-repo publish state.

Repairs:

- Normalized all `references/canonical_sources/md/**/*.md` `Local raw file:` headers to pack-root-relative `references/canonical_sources/raw/...` paths. Body text was not intentionally changed.
- Changed `references/source_inventory/coverage_report.md` local corpus path from the parent-repo-prefixed path to `references/canonical_sources/`.
- Changed `agents/openai.yaml` from broad implicit invocation to explicit-only: `allow_implicit_invocation: false`, with description/capabilities scoped to explicit prepared SR/survey prior routing.
- Removed controller-created AppleDouble `._*` metadata files after the first validator run exposed them as publish blockers.

Second-level read-only worker:

```sh
COPYFILE_DISABLE=1 codex exec --ephemeral --cd "/Volumes/My Book/NLP_PRISMA_Reviews" --sandbox read-only --skip-git-repo-check 'You are a second-level read-only patch/audit reviewer for the fourth-round repair of docs/agent_capability_packs/sr-survey-prior-router. You MUST NOT write files. You MUST NOT spawn native subagents. You MUST NOT run codex exec or any other nested worker. Inspect the current pack state and dirty diff only within docs/agent_capability_packs/sr-survey-prior-router. Review the four known issues from the third-round audit: (1) Local raw file headers under references/canonical_sources/md/**/*.md must be pack-root-relative references/canonical_sources/raw/... with no /Volumes or docs/agent_capability_packs/sr-survey-prior-router prefix and existing local raw paths; (2) coverage_report.md must not contain parent-prefixed corpus path; (3) agents/openai.yaml must be explicit-only and no broad implicit invocation risk; (4) nested pack tracked changes should be publish-readiness-only and committable, with final clean state expected after commit. Run read-only checks as needed, including validators if feasible. Return in Chinese: task, exact shell commands you ran with exit codes, concise output summary, verdict ready/not ready/no-known-issues or blockers, limitations, and whether you wrote files. Keep it evidence-based and mention any remaining issue explicitly.'
```

Worker exit code: 0.

Worker output summary: no known issues within the fourth-round local audit scope. It verified 212/212 canonical Markdown raw headers are pack-root-relative and point to existing raw files, no `/Volumes` or parent-prefixed pack paths remain in the checked locator surfaces, `coverage_report.md` has no parent-prefixed corpus path, `agents/openai.yaml` is explicit-only, source-card and graphify validators pass, `git diff --check` passes, and all dirty tracked files are within expected publish-readiness surfaces. It found no remaining blocker; the only pre-commit condition was that the nested pack repo remained dirty until the repair is committed.

Worker limitations: read-only local audit only; no live web refresh; no full semantic re-review of all source-card claims; one read-only here-doc probe failed because the read-only sandbox could not create a shell temp file, and one quoted `python3 -c` probe failed before the worker reran an equivalent raw-header check successfully. Worker wrote files: no.

Controller command/result summary:

- Initial mechanical header rewrite with default locale: exit 9 due missing `C.UTF-8`; no useful output indicated a completed rewrite.
- Retried header rewrite with `LC_ALL=C LANG=C`: exit 0.
- `python3` targeted raw-header check: exit 0; `headers=212`, `bad_prefix=0`, `missing_raw_paths=0`, `non_pack_relative_local_raw_values=0`.
- `python3` targeted coverage report check: exit 0; `coverage_parent_prefixed_refs=0`.
- `python3` targeted `openai.yaml` invocation-policy check: exit 0; `allow_implicit_invocation_false=True`, `allow_implicit_invocation_true_absent=True`, explicit-only description and capabilities present.
- `git diff --check`: exit 0.
- First `python3 validation/validate_source_cards_v2.py`: exit 1 because pack AppleDouble `._*` metadata files were present.
- `find docs/agent_capability_packs/sr-survey-prior-router -name '._*' -type f -print -delete | wc -l`: exit 0; removed 216 pack metadata files.
- `COPYFILE_DISABLE=1 python3 validation/validate_source_cards_v2.py`: exit 0; pass, 65 cards for 65 manifest sources.
- `COPYFILE_DISABLE=1 python3 validation/validate_graphify_navigation.py`: exit 0; pass, generated graph present.
- `COPYFILE_DISABLE=1 python3 validation/validate_graphify_navigation.py --require-generated`: exit 0; pass, generated graph present.
- Final metadata check before commit: exit 0; no pack `._*` files remained.
- Second-level `codex exec` worker command above: exit 0; no known issues within scope.

Commit: pending at the time this section was written; a post-commit addendum records the repair commit hash after Git creates it.

Remaining limitations:

- No live web refresh was performed.
- No full semantic re-review of every source-card claim was performed.
- `press` and `cacm_author_guidelines` remain refresh-sensitive manual captures for future current-wording checks, but this is no longer a local publish-readiness blocker.

Verdict before commit: no known issues within the fourth-round local publish-readiness audit scope except the expected dirty tracked state, to be closed by committing the nested pack repair.

Post-commit addendum:

- Fourth-round repair commit: `2801500c04ffd824c7136c76f50514e1f7c2edca` (`Fix sr-survey prior publish readiness`).
- The commit hash could not be known until after the tracker section itself was committed, so this addendum records the repair commit in a tracker-only follow-up commit.

## 2026-05-05 Fifth-round OMX/native subagent audit

Task: answer whether the current `sr-survey-prior-router` Markdown and index
content aligns with the canonical Markdown corpus under
`references/canonical_sources/md/`, and whether the staged skill is ready to
publish as a draft. This round used three native read-only subagents plus one
isolated read-only OMX worker. The only intended write is this tracker section.

Review paths:

- Native subagent A: canonical/source-card alignment, focused on high-risk
  manual/partial sources.
- Native subagent B: publish-readiness, path portability, Git state, ignored
  artifacts, and policy boundaries.
- Native subagent C: tracker and validation-note consistency.
- Isolated OMX worker: independent read-only audit of alignment and draft
  publish readiness.

Direct answers:

1. Alignment with canonical Markdown: qualified yes. No reviewer found a current
   blocker where a checked derivative card/index/route claim contradicted the
   canonical Markdown. The strongest evidence is structural plus targeted
   semantic: 65/65 source-card-v2 files validate against 65 manifest sources,
   338 source-card locator document references all match their supporting
   canonical paths, 212 canonical Markdown headers point to existing
   pack-root-relative raw files, and targeted deep checks for `press`,
   `cacm_author_guidelines`, `state_of_art_review_2022`, `clinicaltrials_api`,
   `paperswithcode`, `prisma_2020`, `computational_linguistics`,
   `tacl_submission`, `grade_working_group`, `core_api`, and `equator_prisma`
   matched the current canonical Markdown within their stated scopes.
2. Ready to publish: conditional ready for a tracked draft capability pack, not
   ready to claim final knowledge-heavy coverage, not confirmed remote-published,
   and not ideal as a whole-folder zip. Draft publication is content-ready if
   reviewers use the nested Git repo surface, respect ignored/local generated
   artifacts, and read this tracker as the current status. Remaining publication
   caveats are the stale wording in older validation snapshots, local branch
   `ahead 3`, archive-only `.git` AppleDouble sidecars, no live web refresh, and
   the isolated OMX environment not satisfying `requirements.txt`.

Controller verification:

- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_source_cards_v2.py`: pass; 65 cards for 65 manifest sources.
- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_graphify_navigation.py`: pass; generated graph present.
- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_graphify_navigation.py --require-generated`: pass; generated graph present.
- `git diff --check`: pass.
- `find . -path './.git' -prune -o -name '._*' -type f -print`: pass; no tracked-surface AppleDouble files.
- Path portability check across `source_manifest`, `download_manifest`,
  `document_index`, `section_index_manifest`, `local_corpus_index`, and 65 split
  by-source section indexes: pass; 661 top-level rows, 1125 top-level path
  values, 4647 split-section path values, 0 parent-prefixed paths, 0 absolute
  local paths, 0 missing pack-root paths.
- Canonical Markdown raw-header check: pass; 212 Markdown files, 212 `Local raw
  file:` headers, 0 bad prefixes, 0 missing raw files.
- Source-set consistency check: pass; 65 manifest IDs, 65 local corpus IDs, 65
  source cards, 65 document-index source IDs, 65 section-index source IDs; no
  missing source sets.
- Source-card locator/support check: pass; 308 claim blocks, 338 locator
  document references, 0 unmatched locator documents, 0 missing support paths.
- Publish-surface stale path/policy scan over `SKILL.md`, `agents/openai.yaml`,
  and `references/`: pass; 0 `/Volumes/My Book`, parent-prefixed pack paths, or
  `allow_implicit_invocation: true` matches.
- Pack-local Python dependency check: `/opt/homebrew/opt/python@3.13/bin/python3.13`
  with `networkx 3.6.1`; satisfies `requirements.txt`.
- `git status --branch --short`: clean working tree before this tracker append,
  `main...origin/main [ahead 3]`. After this section is written, this tracker
  file itself is the expected working-tree modification until committed.

Native subagent synthesis:

- Alignment worker verdict: qualified alignment. It found no current high-risk
  source where derivative claims contradicted canonical Markdown. It emphasized
  that this is a draft router plus local canonical corpus, not a mature complete
  knowledge base. It also noted that PRESS/CACM remain manual browser captures;
  API/registry/stub sources must stay within their locator/API/partial-source
  boundaries.
- Publish worker verdict: conditional ready. It treated local draft publication
  as acceptable from the nested Git repo surface, but identified three practical
  conditions: push the nested repo for remote GitHub publication, exclude `.git`
  sidecars for archive handoff, and avoid final knowledge-heavy or license-clean
  claims.
- Tracker worker verdict: tracker is current for live tracked state, but
  qualified insufficient as standalone publish evidence because old snapshot
  files still contain stale blocked/not-ready/bad-capture statements without
  in-file supersession banners.

OMX worker synthesis:

- The isolated OMX worker agreed that targeted high-risk source-card content was
  broadly aligned with canonical Markdown and that source-card-v2 validation
  passed.
- It reported graphify validation failures in the isolated OMX environment:
  `node_link_graph() got an unexpected keyword argument 'edges'`.
- Controller follow-up showed this was an environment mismatch: the OMX worker
  had `networkx 3.3`, while this pack requires `networkx>=3.4,<4`; the
  pack-local environment had `networkx 3.6.1` and graphify validators passed.
  Therefore this is not evidence of canonical-content misalignment, but it is a
  real validation-environment caveat for future OMX-based audits.

Content findings:

- No current source-content blocker was found in the checked runtime/review
  surfaces.
- The current pack still must not claim final knowledge-heavy coverage. It can
  claim a seed source inventory, first local canonical Markdown corpus, complete
  v2 source-card coverage for the 65 manifest sources, and route/index/source
  boundaries.
- Manual browser captures for `press` and `cacm_author_guidelines` are locally
  usable and correctly disclosed, but remain refresh-sensitive and not clean
  publisher XML/HTML.
- Older validation snapshots remain useful provenance, but several need explicit
  supersession headers before the validation folder can stand alone as reviewer
  evidence.

Remaining limitations:

- No live web refresh was performed.
- No full semantic re-review of all 308 source-card claims was performed; the
  semantic review was targeted to high-risk/manual/partial sources plus
  structural validators.
- Remote GitHub publication was not performed or verified in this round.
- Archive-based handoff was not prepared; normal Git publication and folder zip
  publication have different cleanliness requirements.

Verdict: conditional ready for draft Git publication of the tracked nested pack
surface, with no current canonical-alignment blocker found. Not final
knowledge-heavy; not remote-published until the `ahead 3` commits are pushed;
and not a fully standalone validation evidence bundle until stale snapshot files
get supersession banners or a current validation-status README.

## 2026-05-05 Sixth-round publication prep

Task: close the operational publication-readiness gaps found after the fifth
round by native subagents. This round used one write worker for supersession
banners and two read-only subagents for publication-surface review.

Changes made:

- Added publication/supersession banners to these historical snapshots:
  `validation/agent_qa_validation_2026-05-04.md`,
  `validation/source_alignment_audit_2026-05-04.md`,
  `validation/source_alignment_fix_validation_2026-05-04.md`, and
  `validation/live_recapture_2026-05-05.md`.
- Added `validation/README.md` as the publication-facing validation entry point.
  It tells reviewers to start with this tracker and warns that dated notes are
  snapshots that may be superseded.
- Removed non-`.git` AppleDouble sidecars generated while editing validation
  files.
- Updated the live item table to mark `validation_snapshot_supersession_headers`
  as `validated` and added `validation_publication_entrypoint`.

Subagent findings integrated:

- Supersession-banner worker: added concise banners without deleting historical
  findings.
- Current-status entrypoint auditor: recommended tracking `validation/README.md`
  rather than adding a separate `CURRENT_VALIDATION_STATUS.md`.
- Publication-surface auditor: identified the final blockers as validation
  AppleDouble sidecars, dirty/untracked validation edits, the tracker row still
  saying `todo`, and the unpushed local branch.

Expected remaining state after this prep is committed:

- The nested Git working tree should be clean.
- Source-card and graphify validators should pass.
- The tracked publication/review surface should have a clear validation entry
  point and explicit supersession banners for stale snapshots.
- Local `main` will still be ahead of `origin/main` until pushed; that is the
  remaining remote-publication step, not a local content/readiness defect.

Archive caveat:

- Normal Git publication excludes ignored raw corpus, split section dumps,
  graphify output, and `.git` sidecars. Whole-folder zip/archive handoff should
  explicitly exclude `.git/`, `references/canonical_sources/raw/`,
  `references/corpus_index/sections/`, and `graphify-out/`.

## 2026-05-05 Seventh-round OMX/native source-integrity audit

Task: answer the user's two current questions after inspecting this tracker and
the full staged pack:

1. Do the derivative Markdown/source-card/index contents align with the canonical
   Markdown corpus under `references/canonical_sources/md/`?
2. Is the staged skill ready to publish, aside from necessary operational steps,
   and are there content errors or missing pieces?

This round used three native read-only subagents, one isolated read-only OMX
worker, and controller-side checks. The only intended write is this tracker
update.

Direct answers:

1. Content alignment: qualified yes for the substantive claims checked. Native
   and OMX audits found no high-risk source-card or route claim that directly
   contradicted the current canonical Markdown. The cards and indexes correctly
   preserve the known boundaries for `press`, `cacm_author_guidelines`,
   `clinicaltrials_api`, `state_of_art_review_2022`, `paperswithcode`,
   `prisma_2020`, `tacl_submission`, `computational_linguistics`,
   `grade_working_group`, `core_api`, and `equator_prisma`.
2. Ready-to-publish: not yet if the publication claim is
   "canonical-content aligned and provenance-clean." The pack is structurally
   close and still conditionally suitable for draft review from the nested Git
   repo surface, but this audit found unfixed metadata/provenance drift and a
   few publication-evidence omissions. It should not be published as clean until
   the open live items from this round are repaired or explicitly scoped out.

Controller verification:

- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_source_cards_v2.py`:
  pass; 65 cards for 65 manifest sources.
- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_graphify_navigation.py`:
  pass in the pack-local environment; generated graph present.
- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_graphify_navigation.py --require-generated`:
  pass in the pack-local environment.
- `git status --branch --short`: clean tracked working tree before this tracker
  update; `main...origin/main [ahead 4]`.
- `git diff --check`: pass before this tracker update.
- Non-`.git` AppleDouble scan: pass; no `._*` files outside `.git`.
- Path portability check: pass; 597 top-level rows, 1125 top-level path values,
  65 split-section files, 4647 split-section path values, 0 parent-prefixed
  paths, 0 absolute local paths, 0 missing pack-root paths, and 0 source/file
  mismatches.
- Source-set consistency: pass; 65 manifest IDs, 65 local corpus IDs, 65 source
  cards, 65 document-index source IDs, and 65 section-manifest source IDs.
- Canonical Markdown raw-header check: pass; 212 Markdown files, 212
  `Local raw file:` headers, 0 bad prefixes, and 0 missing raw files.
- Source-card locator/support check: pass; 308 claim blocks, 338 locator
  document references, 0 unmatched locator documents, 0 missing support paths.
- Source-card locator line-range check: pass; 446 referenced line ranges, 0
  out-of-range references.
- Metadata drift check: fail for provenance-clean publication; 16 checked
  `md_sha256` entries mismatch 8 unique current Markdown files, 405 local
  document/download rows have no `md_sha256`, `document_index.jsonl` has 209
  stale `bytes` values while all line counts still match, and
  `section_index_manifest.jsonl` has 65 stale `bytes` values while all section
  counts still match.

Native subagent synthesis:

- Canonical-alignment worker: no direct contradiction was found between checked
  high-risk source-card claims and canonical Markdown. It found the blocking
  issue for a provenance-clean claim: stale `md_sha256` in `source_manifest` and
  `download_manifest`, plus stale `bytes` metadata in the document and section
  indexes.
- Publish-readiness worker: the tracked nested repo surface is conditionally
  ready for draft Git review, not final knowledge-heavy publication. The repo is
  clean but ahead of `origin/main` by 4 commits; archive/zip handoff must exclude
  `.git/`, ignored raw corpus, split section dumps, and graphify output.
- Validation-history worker: `validation/README.md` and this tracker are the
  right current entry points, and the four earlier stale snapshots have
  supersession banners. The imported
  `validation/chatgpt_deep_review_2026-05-04/review.md` still lacks an in-file
  supersession banner despite containing old blocked/bad-capture/201-document
  statements.

OMX worker synthesis:

- The isolated OMX worker agreed that substantive checked content is aligned and
  that the remaining issues are operational/metadata rather than new source-card
  contradictions.
- OMX graphify validation failed in that isolated environment with
  `node_link_graph() got an unexpected keyword argument 'edges'` because the OMX
  environment had `networkx 3.3`, below this pack's `networkx>=3.4,<4`
  requirement. The pack-local environment used by the controller passed graphify
  validation, so this remains an OMX environment caveat, not a pack-content
  failure.

Open issues from this round:

1. `canonical_md_metadata_drift`: update stale `md_sha256` values for the 8
   affected Markdown files, decide whether missing checksums should be filled or
   intentionally omitted, and regenerate/update stale `bytes` metadata in
   `document_index.jsonl` and `section_index_manifest.jsonl`.
2. `route_refresh_sensitive_coverage`: surface or justify route-level freshness
   sensitivity for high-risk sources already flagged in cards, especially
   `paperswithcode`, `tacl_submission`, `computational_linguistics`, and
   `core_api`.
3. `cacm_manifest_browser_verified_url`: add the CACM-specific canonical URL to
   `browser_verified_urls` or document why it is excluded.
4. `chatgpt_deep_review_bundle_supersession`: add a supersession banner to the
   imported ChatGPT deep-review bundle before treating validation as a standalone
   public evidence package.
5. `remote_publish_state`: push the four local commits when the goal is actual
   GitHub publication.
6. `archive_publish_sidecars`: exclude `.git/` or remove the 15 `.git` AppleDouble
   files before any whole-folder zip/archive handoff.

Remaining limitations:

- No live web refresh or browser recapture was performed.
- No full semantic re-review of all 308 source-card claims was performed; the
  semantic review focused on high-risk/manual/partial sources plus structural
  validators.
- No clean fresh-clone rebuild was performed.
- Remote GitHub publication was not performed.

Verdict: derivative content is substantively aligned with canonical Markdown
within the checked draft-router scope, but the pack is not ready for a
provenance-clean publish claim until metadata drift and the listed publication
evidence omissions are repaired. It remains usable for local draft review if the
limitations above are stated explicitly.

## 2026-05-06 First-level delegated read-only audit

Task: as a first-level subagent, inspect this tracker plus the full staged
`sr-survey-prior-router` pack and answer whether derivative Markdown, source
cards, indexes, and validation notes align with canonical Markdown under
`references/canonical_sources/md/`, and whether the pack is ready to publish/use.

Delegation model:

- Main agent -> native first-level subagent -> foreground `codex exec` worker.
- No native subagent was spawned by this first-level subagent.
- No OMX wrapper was executed; the requested OMX/subagent review was represented
  by this native subagent plus one foreground read-only `codex exec` worker.
- The only file written by this first-level subagent in this round is this
  tracker.

Second-level worker command:

```sh
codex exec --ephemeral --cd "/Volumes/My Book/NLP_PRISMA_Reviews" --sandbox read-only --skip-git-repo-check -
```

The prompt was passed on stdin and explicitly prohibited writes, native
subagents, `codex exec`, OMX/omx-lab/codex-omx-exec, live web refresh, package
installation, and environment mutation. It required reporting task, commands,
exit codes, output summary, findings, publish-readiness conclusion, limitations,
and whether files were written.

Worker exit code: 0.

Worker output summary:

- Source-card and graphify validators passed:
  `validate_source_cards_v2.py`, `validate_graphify_navigation.py`, and
  `validate_graphify_navigation.py --require-generated`.
- Corpus/index sets align structurally: 65 source IDs, 212 canonical Markdown
  files, 212 document-index rows, 254 download rows, 65 section-manifest rows,
  and 65 split by-source section files; no source-ID set gaps were reported.
- Path portability checks passed: no parent-prefixed pack paths, no local
  `/Volumes` or `/Users` absolute paths, and no missing pack-root paths in the
  checked locator surfaces.
- Targeted high-risk content checks found no direct contradiction between
  checked source-card claims and canonical Markdown for `press`,
  `cacm_author_guidelines`, `paperswithcode`, `core_api`,
  `clinicaltrials_api`, `state_of_art_review_2022`, `tacl_submission`, and
  `computational_linguistics`.
- The worker wrote no files.

Controller verification:

- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_source_cards_v2.py`:
  pass; 65 cards for 65 manifest sources.
- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_graphify_navigation.py`:
  pass.
- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_graphify_navigation.py --require-generated`:
  pass.
- `GIT_OPTIONAL_LOCKS=0 git status --branch --short`: `main...origin/main
  [ahead 4]` and `M validation/source_integrity_tracker.md`.
- `GIT_OPTIONAL_LOCKS=0 git diff --check`: pass.
- Non-`.git` AppleDouble scan: pass; no `._*` files printed.
- Metadata drift check reproduced the prior blocker: 19 `md_sha256` fields
  checked, 16 mismatched, 405 counted local document/download rows without
  `md_sha256`, 209 stale `document_index.jsonl` `bytes` values, 0 stale
  document line counts, and 65 stale `section_index_manifest.jsonl` `bytes`
  values.
- Strict source-card key-point YAML parse check: 62 cards parse, 3 fail:
  `narrative_synthesis_york_2006.md`, `prisma_2020.md`, and `robis.md`.
- `cacm_author_guidelines` manifest check: canonical URL is
  `https://cacm.acm.org/author-guidelines`, while `browser_verified_urls`
  lists only ACM fallback URLs.
- Imported ChatGPT deep-review bundle check: `review.md` still contains stale
  blocked/bad-capture/201-document statements without an in-file supersession
  banner.

Direct answers:

1. Content alignment: qualified yes for the checked draft-router scope. The
   derivative cards, route/index docs, and validation entrypoint preserve the
   current canonical-source boundaries for the high-risk sources checked. No
   direct canonical Markdown contradiction was found in this round.
2. Ready-to-publish/use: conditional for local draft use, not ready for a
   provenance-clean or zero-known-issues public publish claim. The pack can be
   used as a staged, explicit-only, lazy-load router if the seed-corpus and
   no-live-refresh limitations are stated. It should not be published as clean
   until the open blockers below are repaired or explicitly scoped out.

Open issues requiring the next repair round:

1. `canonical_md_metadata_drift`: recompute or intentionally standardize
   Markdown checksum policy, then update stale `bytes` metadata in document and
   section indexes.
2. `source_card_keypoint_yaml_parseability`: make the three failing source-card
   key-point YAML blocks parseable or change the schema/validator contract.
3. `chatgpt_deep_review_bundle_supersession`: add an in-file supersession banner
   to the imported ChatGPT deep-review bundle before treating it as standalone
   public evidence.
4. `route_refresh_sensitive_coverage`: add or explicitly justify route-level
   freshness visibility for high-risk sources already flagged in cards.
5. `cacm_manifest_browser_verified_url`: add the CACM-specific canonical URL to
   `browser_verified_urls` or document why only ACM fallback pages were
   browser-verified.
6. `remote_publish_state`: push the nested repo branch when actual GitHub
   publication is requested.
7. `archive_publish_sidecars`: exclude `.git/` or remove `.git` AppleDouble
   files before whole-folder archive handoff.

Remaining limitations:

- No live web refresh or browser recapture was performed.
- No full semantic re-review of all 308 source-card claims was performed.
- No clean fresh-clone rebuild was performed.
- Remote GitHub publication was not performed.

Verdict: conditionally usable as a local staged router, but not ready for a
clean publish claim. The next linear step should repair metadata drift,
source-card YAML parseability, and stale validation-bundle supersession, then
rerun the same read-only audit.

## 2026-05-06 First-round blocker repair

Task: repair the first-round review blockers for provenance-clean draft
publish/use readiness while staying inside the requested write scope.

Files changed:

- `references/source_inventory/source_manifest.jsonl`
- `references/canonical_sources/download_manifest.jsonl`
- `references/corpus_index/document_index.jsonl`
- `references/corpus_index/section_index_manifest.jsonl`
- `references/source_inventory/source_cards_v2/narrative_synthesis_york_2006.md`
- `references/source_inventory/source_cards_v2/prisma_2020.md`
- `references/source_inventory/source_cards_v2/robis.md`
- `references/route-source-index.yaml`
- `validation/chatgpt_deep_review_2026-05-04/review.md`
- `validation/source_integrity_tracker.md`

Non-`.git` AppleDouble metadata sidecars created by external-drive edits, plus
the pre-existing `validation/._source_integrity_tracker.md`, were removed so the
required validators could run. Nested `.git` sidecars were not touched.

Second-level worker:

Initial command without `--skip-git-repo-check` failed because the storage root
is outside a trusted Git repository:

```sh
codex exec --ephemeral --cd "/Volumes/My Book/NLP_PRISMA_Reviews" --sandbox read-only "<plan review prompt>"
```

Exit code: 1.

Successful foreground read-only worker command:

```sh
codex exec --ephemeral --skip-git-repo-check --cd "/Volumes/My Book/NLP_PRISMA_Reviews" --sandbox read-only "<plan review prompt>"
```

Exit code: 0.

Worker task: review the proposed repair plan before edits. The prompt explicitly
prohibited writes, native subagents, nested `codex exec`, live web refresh, and
package/environment mutation.

Worker output summary:

- Confirmed the plan matched the blocker set and allowed future write-file
  scope.
- Confirmed recursive `source_manifest.jsonl` handling was required because the
  relevant `md_sha256` fields live under `local_documents`.
- Reproduced 8 mismatched nested `source_manifest` `md_sha256` fields, 8
  mismatched `download_manifest` `md_sha256` fields, 209 stale
  `document_index.jsonl` `bytes` values, 65 stale
  `section_index_manifest.jsonl` `bytes` values, 3 strict PyYAML key-point
  failures, 0 route occurrences for the four high-risk IDs, and the missing CACM
  canonical URL in `browser_verified_urls`.
- Flagged non-`.git` AppleDouble sidecars as validator blockers if left in
  place.
- Limitations: read-only local inspection only; no live web refresh, browser
  recapture, full semantic review of all source-card claims, or clean fresh-clone
  test.
- Files written by worker: none.

Repair commands/results:

- JSONL metadata repair script: exit 0; updated 8 nested
  `source_manifest.jsonl` `md_sha256` values, 8 `download_manifest.jsonl`
  `md_sha256` values, 209 `document_index.jsonl` `bytes` values, 65
  `section_index_manifest.jsonl` `bytes` values, and inserted
  `https://cacm.acm.org/author-guidelines` into the CACM
  `browser_verified_urls` list.
- Source-card YAML patch: quoted the three colon-bearing `claim` strings only.
- Route patch: added route-visible freshness coverage for `core_api`,
  `paperswithcode`, `tacl_submission`, and `computational_linguistics`.
- ChatGPT deep-review patch: added an imported-snapshot supersession banner.
- Non-`.git` AppleDouble scan before cleanup listed 10 sidecars; cleanup removed
  those 10 sidecars and left `.git/` sidecars alone.

Validation results:

- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_source_cards_v2.py`:
  pass; 65 cards for 65 manifest sources.
- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_graphify_navigation.py`:
  pass; generated graph present.
- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_graphify_navigation.py --require-generated`:
  pass; generated graph present.
- `GIT_OPTIONAL_LOCKS=0 git diff --check`: pass.
- `find . -path './.git' -prune -o -name '._*' -type f -print`: pass; no
  non-`.git` sidecars printed after cleanup.
- Targeted metadata/YAML/route/CACM check: pass. Current state is
  `source_manifest_md_sha256=(8 present, 0 mismatched, 0 missing, 204 md_path
  objects without md_sha256 by existing policy)`,
  `download_manifest_md_sha256=(11 present, 0 mismatched, 0 missing, 201 md_path
  rows without md_sha256 by existing policy)`, `document_index_bytes=(212 rows,
  0 mismatched, 0 missing)`, `section_index_manifest_bytes=(65 rows, 0
  mismatched, 0 missing)`, `keypoint_yaml=(65 ok, 0 failures)`, and each of
  `paperswithcode`, `tacl_submission`, `computational_linguistics`, and
  `core_api` appears twice in `route-source-index.yaml`.

Notable failed/diagnostic attempts:

- The first post-repair validator run failed because external-drive sidecars were
  present; this was resolved by removing non-`.git` `._*` files.
- One combined targeted check failed after scanning a binary AppleDouble file;
  the corrected check excluded `._*` and passed.
- One targeted check rerun failed due to a path-join bug in the checker script;
  the corrected checker passed.

Remaining limitations:

- No live web refresh or browser recapture was performed.
- No full semantic re-review of all source-card claims was performed in this
  repair round.
- Remote publish remains a separate operational step.
- `.git` AppleDouble sidecars remain intentionally untouched; they matter for
  whole-folder archive handoff, not normal Git publication.
- `omx_validation_environment` remains deferred because the isolated OMX
  environment previously used an older `networkx` than this pack requires.

Readiness conclusion: the five first-round blockers repaired in this round are
validated for the local nested-pack surface. The pack is closer to
provenance-clean draft publish/use readiness. Another content-repair loop is not
needed for these blockers, but a separate publish loop is still needed for
remote push and any archive-specific `.git` sidecar policy.

## Independent first-level validation - 2026-05-06

Scope: independent validation of the repaired pack state for provenance-clean
draft Git publication/use. This pass used one required foreground read-only
second-level `codex exec` worker, then reran local validators and targeted
checks from the pack root. No live web refresh, browser recapture, package
install, OMX, native subagent, nested worker, commit, or push was performed.

Second-level worker:

```sh
codex exec --ephemeral --skip-git-repo-check --cd "/Volumes/My Book/NLP_PRISMA_Reviews" --sandbox read-only "<independent read-only audit prompt>"
```

Exit code: 0.

Worker task: independently audit
`docs/agent_capability_packs/sr-survey-prior-router/` for provenance-clean draft
Git publication/use, with explicit prohibitions on file writes, native
subagents, nested `codex exec`, OMX, live web refresh, package installs, and
background jobs.

Worker output summary:

- Required validators passed: `validate_source_cards_v2.py` reported 65 cards
  for 65 manifest sources; both graphify navigation commands passed with the
  generated graph present; `git diff --check` passed; the non-`.git`
  AppleDouble scan printed no files.
- Targeted worker audit passed: 65 manifest source-card files were checked with
  `source_cards_v2/README.md` excluded; 308 key-point YAML items parsed under
  strict PyYAML; present metadata checks found no `md_sha256`, byte, or section
  count drift; route refresh-sensitive coverage and the CACM browser-verified
  URL were present; imported ChatGPT deep-review supersession pointers were
  present.
- Git surface reported by worker: `main...origin/main [ahead 4]`, 10 modified
  tracked files, no staged changes, and no untracked publish-surface files.
- Worker limitations: read-only local audit only; no live web refresh, no OMX,
  no packages, no commit/push, no full semantic review of all claims. One
  heredoc-style inline audit attempt failed in the read-only sandbox with exit
  code 1 because zsh could not create a temporary heredoc file; it wrote no
  files, and the worker reran the same audit via `python3 -c` successfully.
- Files written by worker: none.

First-level command results:

- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_source_cards_v2.py`:
  exit 0; pass; 65 cards for 65 manifest sources.
- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_graphify_navigation.py`:
  exit 0; pass; generated graph present.
- `COPYFILE_DISABLE=1 PYTHONDONTWRITEBYTECODE=1 python3 validation/validate_graphify_navigation.py --require-generated`:
  exit 0; pass; generated graph present.
- `GIT_OPTIONAL_LOCKS=0 git diff --check`: exit 0; no output.
- `find . -path './.git' -prune -o -name '._*' -type f -print`: exit 0; no
  non-`.git` sidecars printed.
- Targeted metadata/YAML/CACM/route audit: exit 0; pass. It checked 65 source
  cards excluding `README.md`, 308 strict PyYAML key-point items, 11
  `download_manifest` `md_sha256` fields, 8 `source_manifest` `md_sha256`
  fields, 204 existing-policy `md_path` objects without `md_sha256`, 212
  `document_index` byte and line-count rows, and 65 `section_index_manifest`
  byte and section-count rows.
- `GIT_OPTIONAL_LOCKS=0 git status --short --branch`: exit 0; `main` is ahead
  of `origin/main` by 4 commits and has 10 modified tracked files.
- `GIT_OPTIONAL_LOCKS=0 git diff --name-status`: exit 0; modified tracked files
  are `references/canonical_sources/download_manifest.jsonl`,
  `references/corpus_index/document_index.jsonl`,
  `references/corpus_index/section_index_manifest.jsonl`,
  `references/route-source-index.yaml`,
  `references/source_inventory/source_cards_v2/narrative_synthesis_york_2006.md`,
  `references/source_inventory/source_cards_v2/prisma_2020.md`,
  `references/source_inventory/source_cards_v2/robis.md`,
  `references/source_inventory/source_manifest.jsonl`,
  `validation/chatgpt_deep_review_2026-05-04/review.md`, and
  `validation/source_integrity_tracker.md`.
- `GIT_OPTIONAL_LOCKS=0 git diff --stat`: exit 0; 10 files changed, 679
  insertions and 290 deletions before this validation append.
- `GIT_OPTIONAL_LOCKS=0 git diff --cached --name-status`: exit 0; no staged
  changes.
- `GIT_OPTIONAL_LOCKS=0 git ls-files --others --exclude-standard`: exit 0; no
  untracked files.

First-round blocker closure:

- `canonical_md_metadata_drift`: closed for the present-field policy. Current
  checks found no drift in present `md_sha256`, document byte/line-count, or
  section byte/count fields.
- `source_card_keypoint_yaml_parseability`: closed. Strict PyYAML parsed the 65
  manifest source-card files and did not treat `source_cards_v2/README.md` as a
  source card.
- `chatgpt_deep_review_bundle_supersession`: closed. The imported dated review
  snapshot has top-of-file supersession pointers to the current tracker and
  validation README.
- `route_refresh_sensitive_coverage`: closed. Route-level
  `refresh_sensitive_source_ids` include `core_api`, `paperswithcode`,
  `tacl_submission`, `computational_linguistics`, `cacm_author_guidelines`,
  `press`, and `clinicaltrials_api` in the expected route buckets.
- `cacm_manifest_browser_verified_url`: closed.
  `https://cacm.acm.org/author-guidelines` is present in
  `cacm_author_guidelines.browser_verified_urls`.
- Non-`.git` AppleDouble sidecars: closed. The current scan found none.

Git publication surface:

The tracked changes are coherent with the repair set: metadata hash/byte/count
refresh, route freshness visibility, three source-card YAML quoting fixes, CACM
browser-verified URL provenance, imported-review supersession, and validation
tracking. I found no content blocker in this local validation scope.

Remaining limitations:

- No live web refresh or browser recapture was performed.
- No full semantic review of every source-card claim was performed.
- No clean remote clone checkout was tested.
- Actual remote publication remains an operational step: current changes still
  need staging/commit, and the branch also needs push because `main` is ahead of
  `origin/main`.

Verdict: ready for provenance-clean draft Git publication/use from the local
content and provenance-validation perspective. Not yet remotely published;
commit and push are still required.

## Main-controller final sanity check - 2026-05-06

Scope: final controller-side check after the independent validation append.

Result:

- A fresh post-append validator run initially failed because the external drive
  generated `validation/._source_integrity_tracker.md`.
- The controller removed that non-`.git` AppleDouble sidecar only. Nested `.git`
  sidecars were not touched.
- After cleanup, the required checks passed again:
  `validate_source_cards_v2.py`, `validate_graphify_navigation.py
  --require-generated`, `git diff --check`, and the non-`.git` AppleDouble scan.
- The dirty tracked surface remains the intended 10-file repair set: metadata
  checksum/byte updates, route freshness visibility, three YAML quoting fixes,
  CACM URL provenance, imported-review supersession, and this tracker.

Readiness conclusion: local content/provenance validation is clean for draft Git
publication/use. The remaining step for actual remote publication is to commit
and push the nested repository.
