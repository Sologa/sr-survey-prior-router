---
artifact_type: validation_snapshot
snapshot_date: "2026-05-04"
snapshot_status: superseded
current_status_source: validation/source_integrity_tracker.md
superseded_by:
  - validation/source_integrity_tracker.md
  - validation/README.md
stale_status_notice: "Historical snapshot; do not treat dated audit findings, source states, or status text as current live state."
frontmatter_added: "2026-05-06"
---

# Source Alignment Audit: Organized Pack vs Canonical Corpus

Date: 2026-05-04

## Publication Note

Historical snapshot. Current live status is tracked in `validation/source_integrity_tracker.md`. Superseded points: PRESS/CACM manual captures now exist, `state_of_art_review_2022` was recaptured, and graphify outputs were refreshed where relevant.

## Scope

This audit checks whether the organized `sr-survey-prior-router` files align with the local canonical source corpus under:

- `references/canonical_sources/md/`
- `references/canonical_sources/raw/`

The organized layer checked here includes:

- `SKILL.md`
- `references/route-registry.md`
- `references/route-source-index.yaml`
- `references/evidence-rules.md`
- `references/source-map.md`
- `references/source_inventory/source_registry.yaml`
- `references/source_inventory/source_manifest.jsonl`
- `references/source_inventory/local_corpus_index.md`
- `references/source_inventory/local_corpus_index.json`
- `references/source_inventory/coverage_report.md`
- `references/source_inventory/source_cards/*.md`
- `references/corpus_index/*.jsonl`

## Method

The main audit process did not bulk-read the long canonical Markdown corpus. It performed structural checks over indexes, manifests, and file paths, then delegated long-source semantic checks to read-only subagents and one isolated OMX read-only audit.

Subagent split:

- Structural alignment: source IDs, counts, path existence, orphan checks, and route/source-index membership.
- SR method authority alignment: PRISMA, Cochrane, MECIR, JBI, Campbell, GRADE/CERQual, AMSTAR 2, ROBIS, RoB 2, ROBINS-I, PRESS, PROSPERO, EQUATOR PRISMA.
- Survey-writing and taxonomy alignment: PRISMA-ScR, JBI, SWiM, ENTREQ, RAMESES, Cochrane chapters 9/12, SANRA, narrative synthesis, state-of-art review, taxonomy methods, and venue guidance.
- Scholarly database/API, NLP/speech/CS exemplar, and Codex packaging alignment.
- OMX read-only audit: independent sampled check for source-card/evidence-boundary overclaims.

## Verdict

The two layers are **not completely aligned**.

They are **structurally aligned** and **mostly semantically aligned**, but there are several important supportability gaps. The most serious one is `state_of_art_review_2022`: it is treated as a locally retrieved method source in the organized metadata, but its local canonical Markdown is only a reCAPTCHA/browser-check page and does not contain the article body.

## Structurally Aligned

Mechanical checks passed:

- `source_manifest.jsonl`: 65 unique `source_id` rows.
- `source_registry.yaml`: 65 source IDs across 6 family blocks.
- `local_corpus_index.json`: 65 top-level source IDs.
- `document_index.jsonl`: 201 document rows for 63 source IDs.
- `section_index_manifest.jsonl`: 63 source rows.
- Local file counts: 201 raw files and 201 Markdown files.
- All `raw_path` and `md_path` values in `source_manifest.jsonl` exist.
- No orphan raw/Markdown files were found outside the manifest/index path sets.
- The only source IDs without local documents are `press` and `cacm_author_guidelines`, matching the blocked-source status.

Evidence:

- `coverage_report.md:20-24` states 65 source IDs, 201 Markdown paths, 201 raw/Markdown files, and 63/65 source rows with local docs.
- `local_corpus_index.json:149-161` marks `cacm_author_guidelines` blocked with zero docs.
- `local_corpus_index.json:1071-1083` marks `press` blocked with zero docs.
- `route-source-index.yaml:80-82` marks `cacm_author_guidelines` as blocked/partial for `survey_writing_prior`.
- `route-source-index.yaml:112-114` marks `press` as blocked/partial for `sr_writing_prior`.

## Semantically Aligned

The core router/evidence design is aligned with the corpus boundary:

- `SKILL.md:14-16` says the local corpus is not proof of exhaustive coverage and requires route-by-route checks before substantive claims.
- `SKILL.md:32-39` requires route selection, lazy indexes, document/section locators, and only then opening selected canonical Markdown.
- `evidence-rules.md:31-36` says index rows are locators and direct support requires verification against selected canonical Markdown/raw sources.
- `evidence-rules.md:40-43` keeps PRISMA/Cochrane/JBI/GRADE/etc. as authority candidates, PROSPERO as a registry, and source cards/indexes as derivative aids.
- `source_cards/codex-skill-packaging.md:9-22` correctly limits Codex docs to packaging architecture, not SR/survey methodology.

The main SR authority roles are also mostly source-faithful:

- PRISMA-family sources are handled as reporting guidance.
- Cochrane, MECIR, JBI, and Campbell are handled as conduct/manual or standards sources.
- GRADE/CERQual, AMSTAR 2, ROBIS, RoB 2, and ROBINS-I are separated by certainty, appraisal, review bias, and primary-study bias roles.
- PROSPERO is treated as a registry, not methodology truth.

Survey/venue/API boundaries are mostly aligned:

- `survey-writing-methods.md:7-17` correctly frames survey-writing prior as a layered stack, not a universal official rulebook or automatic survey-generation pipeline.
- `source_registry.yaml:77-103` keeps survey-writing methods as mixed methodology and venue guidance.
- `scholarly-databases.md:11-24` correctly states that databases/APIs are discovery/state infrastructure, not writing methodology, and that commercial/restricted sources need access checks.
- `nlp-speech-cs-exemplars.md:11-25` correctly says venue/exemplar sources are not methodology authorities and need license/provenance checks.

## Gaps And Mismatches

### 1. `state_of_art_review_2022` is not locally usable as a method source

`source_manifest.jsonl:36` marks `state_of_art_review_2022` as:

- `authority_class: peer_reviewed_method_paper`
- `source_type: state_of_the_art_review_methodology`
- `retrieval_fit: yes`
- `local_bundle_status: downloaded_and_converted`

But the canonical Markdown contains only a browser-check page:

- `canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md:1-10`

Impact: organized docs should not treat this source as locally verified method content until the article body is recaptured or the row is downgraded to blocked/bad conversion.

### 2. `equator_prisma` has a registry-vs-method family mismatch

`source_registry.yaml:57-72` places `equator_prisma` inside `sr_certainty_appraisal_bias_search`, whose family-level `authority_type` is `methodology_guideline`.

`source_manifest.jsonl:20` describes `equator_prisma` as:

- `authority_class: registry_database`
- `source_type: reporting_guideline_registry_record`
- `not_for: Replacing PRISMA, Cochrane, or JBI as method authority`

Impact: EQUATOR PRISMA is useful as a locator/update-monitoring record, but the family placement can make it look like a method authority unless an explicit per-source override is surfaced.

### 3. PRESS is listed in strong SR coverage but has no local canonical content

`coverage_report.md:35` includes PRESS under "Strong Seed Coverage" for SR certainty/appraisal/bias/search QA, while:

- `coverage_report.md:24` says `press` has no local documents.
- `coverage_report.md:50` says CDA-AMC PRESS pages were blocked by 403.
- `local_corpus_index.json:1071-1083` marks `press` blocked with zero docs.

Impact: PRESS should be phrased as a candidate/known authority row that is blocked locally, not as locally source-backed coverage.

### 4. Some source-card summaries mention cross-family sources not listed in that card's `source_ids`

`nlp-speech-cs-exemplars.md:7` mentions Crossref, OpenAlex, IEEE COMST, and ACM/CACM as part of the broader NLP/speech/CS prior context, but its `source_ids` list is limited to NLP/speech/CS exemplar and venue/archive sources. The referenced Crossref/OpenAlex/API and ACM/CACM/IEEE rows live in other families.

Impact: not a false claim, but it weakens one-hop traceability from a source card to its backing rows.

### 5. Some API canonical Markdown files are entry-point stubs, not full capability evidence

Examples flagged by subagent audit:

- `canonical_sources/md/core_api/official_api_root_official_api_root.md:1-8`
- `canonical_sources/md/core_api/official_api_v3_docs_v3.md:1-6`
- `canonical_sources/md/scite_api/official_api_docs_docs_7da8d680.md:1-6`

Impact: the organized docs correctly gate API claims through canonical verification, but these local Markdown files are too shallow to support detailed API capability claims by themselves.

## Recommended Fixes

1. Downgrade `state_of_art_review_2022` in `source_manifest.jsonl`, `local_corpus_index.*`, and coverage prose until the real article body is captured.
2. Move `equator_prisma` to a registry/locator family or add an explicit per-source caveat in `source_registry.yaml`.
3. Reword the PRESS part of `coverage_report.md` so it is not grouped with locally backed "Strong Seed Coverage" without a blocked-source caveat in the same bullet.
4. Add "cross-family mentions" caveats to `nlp-speech-cs-exemplars.md` and `scholarly-databases.md`, or list the external source IDs in a separate `related_source_ids` field.
5. Add a conversion-depth flag for short/stub API Markdown files, especially when the source is only an entry point and not a full local doc.

## Current Conclusion

The pack is safe to treat as a **router plus seed corpus index**. It is not yet safe to claim that the organized summaries are **fully and completely aligned** with the canonical source content.

The main source corpus/index mechanics are sound. The remaining work is semantic cleanup of a small number of rows and coverage phrases before claiming complete alignment.
