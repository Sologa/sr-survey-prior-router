---
artifact_type: validation_snapshot
snapshot_date: "2026-05-04"
snapshot_status: superseded
current_status_source: validation/source_integrity_tracker.md
superseded_by:
  - validation/source_integrity_tracker.md
  - validation/README.md
stale_status_notice: "Historical snapshot; do not treat dated questions, results, or status text as current live state."
frontmatter_added: "2026-05-06"
---

# Agent QA Validation: sr-survey-prior-router

Date: 2026-05-04

## Publication Note

Historical snapshot. Current live status is tracked in `validation/source_integrity_tracker.md`. Superseded points: PRESS/CACM manual captures now exist, `state_of_art_review_2022` was recaptured, and graphify outputs were refreshed where relevant.

Scope: validate that `sr-survey-prior-router` works as a thin route-first skill with lazy-loaded source/document/section indexes, rather than encouraging agents to bulk-load the downloaded full-document corpus.

Agents:

- Questioner: `019def44-e138-7c43-9ca7-de226a4b124f`
- Answerer: `019def45-f012-77c3-8544-e4f993a11277`
- Orchestrator: main Codex agent, reviewed the exchange and performed local consistency checks.

## Method

The questioner was instructed to read only skill/router docs and produce validation questions. It was forbidden from reading the full canonical corpus under `references/canonical_sources/raw/` or `references/canonical_sources/md/`.

The answerer was instructed to answer the questioner's questions by following:

1. `SKILL.md`
2. `references/route-registry.md`
3. `references/route-source-index.yaml`
4. `references/source_inventory/local_corpus_index.*`
5. `references/corpus_index/document_index.jsonl`
6. Selected `references/corpus_index/sections/by_source/<source_id>.jsonl` only when a selected source needed a locator

The answerer was explicitly forbidden from bulk-loading `canonical_sources/raw/`, `canonical_sources/md/`, or all split section indexes.

## Questions And Results

### Q1. SR Writing Prior Boundary

Question: For an SR methods-writing task, how should an agent decide whether to use PRISMA 2020, Cochrane Handbook, JBI Manual, GRADE, PRESS, and PROSPERO as sources? Answer with authority roles and what should not be treated as methodology authority.

Expected route: `sr_writing_prior`, optionally `source_audit`.

Answerer result:

- Used `sr_writing_prior`.
- Treated `prisma_2020` as reporting authority for completed systematic reviews.
- Treated `cochrane_handbook` and `jbi_manual_2024` as conduct/manual authorities within scope.
- Treated GRADE/CERQual as certainty/confidence authorities, not search/screening/prose authorities.
- Treated `press` as search strategy peer-review/search-QA authority, with local retrieval blocked.
- Treated `prospero` as a registry/database source, not methodology authority.
- Explicitly rejected PROSPERO, PubMed, OpenAlex, workflow tools, source cards, and corpus indexes as methodology authorities.

Pass: yes.

Reason: authority boundaries match the skill's SR route and evidence rules. The answerer did not open canonical Markdown.

### Q2. Survey Writing Prior Routing

Question: A user wants to build prior knowledge for writing an NLP/speech literature survey with taxonomy, related-work structure, and source cards. Which route and source families should be used first, and how should venue guidance differ from method guidance?

Expected route: `survey_writing_prior`.

Answerer result:

- Used `survey_writing_prior`.
- Started with `survey_writing_methods`, `nlp_speech_cs_exemplar_sources`, and `scholarly_databases_and_apis`.
- Correctly separated method guidance from venue guidance.
- Did not collapse survey writing into formal SR writing.
- Did not promote ACL/ISCA/CACM/IEEE/Nature venue material into universal methodology authority.

Pass: yes.

Reason: the answer follows `route-source-index.yaml` and the survey route's authority boundary.

### Q3. Evidence Locator Use

Question: Support or reject this claim using the skill: "For a grounded answer about synthesis without meta-analysis, the agent can cite a source card or index row directly without opening a selected canonical Markdown section." Provide the evidence packet shape the answer should require.

Expected route: `evidence_grounding`.

Answerer result:

- Rejected the claim for direct grounded support.
- Treated source cards, `local_corpus_index`, `document_index`, and section index rows as locators or derivative aids only.
- Required canonical Markdown/raw verification before marking support as `direct`.
- Included evidence-packet fields: `source_id`, `doc_id`, `section_id`, `source_path`, `section`, `span_or_page`, `quote_or_summary`, `support_type`, `confidence`, `freshness`, `claim_type`, and `canonical_verification`.

Pass: yes.

Reason: the answer matches `evidence-rules.md` and the local corpus boundary. It did not treat index rows as evidence.

### Q4. Blocked Source Handling

Question: The user asks whether PRESS and CACM author guidelines are locally available and usable. How should the answerer report blocked or partial source state without guessing or substituting unsupported sources?

Expected route: `source_audit`, optionally `sr_writing_prior` or `survey_writing_prior`.

Answerer result:

- Reported `press` as an inventory row with search-QA role but locally blocked.
- Reported `cacm_author_guidelines` as a venue-guidance row but locally blocked.
- Refused to fabricate local PRESS/CACM evidence.
- Refused to substitute ACM DL user-guide material as CACM author guidelines.
- Stated both are unresolved audit targets unless access-approved browser/manual retrieval supplies canonical text.

Pass: yes.

Reason: this matches `coverage_report.md`, `local_corpus_index`, `canonical_sources/README.md`, and `download_manifest.jsonl`.

Orchestrator check:

```text
press status=blocked md=0 raw=0 blocked=6
cacm_author_guidelines status=blocked md=0 raw=0 blocked=5
```

### Q5. GitHub / Full-Corpus Boundary

Question: If this staged skill is prepared for GitHub review, which parts should be treated as portable review surface, and which parts should remain local backing corpus or use a large-file channel?

Expected route: `general_domain_prior` and `source_audit`.

Answerer result:

- Treated router docs, source registries, source cards, coverage reports, lazy indexes, `canonical_sources/README.md`, `download_manifest.jsonl`, and `.gitignore` as the portable review surface.
- Treated `references/canonical_sources/raw/`, `references/canonical_sources/md/`, `._*`, scratch logs, and full corpus mirrors as excluded from normal PR/review surface unless Git LFS, release assets, object storage, or another large-file channel is chosen.

Pass: yes.

Reason: the answer matches `source-map.md`, `canonical_sources/README.md`, `corpus_index/README.md`, and the skill-local `.gitignore`.

## Answerer Read Log

The answerer reported:

- Q1: `SKILL.md`, `references/route-registry.md`, `references/task-routing.md`, `references/route-source-index.yaml`, `references/evidence-rules.md`, `references/source-map.md`, `references/source_inventory/source_cards/sr-method-authorities.md`, `references/source_inventory/coverage_report.md`, `references/source_inventory/local_corpus_index.md`; canonical Markdown opened: no.
- Q2: `SKILL.md`, `references/route-registry.md`, `references/task-routing.md`, `references/route-source-index.yaml`, `references/source_inventory/source_cards/survey-writing-methods.md`, `references/source_inventory/source_cards/nlp-speech-cs-exemplars.md`, `references/source_inventory/coverage_report.md`, `references/source_inventory/local_corpus_index.md`; canonical Markdown opened: no.
- Q3: `references/evidence-rules.md`, `references/source-map.md`, `references/route-source-index.yaml`, `references/corpus_index/README.md`, selected rows from `references/corpus_index/document_index.jsonl`, selected rows from `references/corpus_index/section_index_manifest.jsonl`; canonical Markdown opened: no.
- Q4: `references/source-map.md`, `references/source_inventory/coverage_report.md`, `references/source_inventory/local_corpus_index.md`, selected `press`/`cacm_author_guidelines` rows from `references/source_inventory/source_manifest.jsonl`, `references/canonical_sources/README.md`, selected failed records from `references/canonical_sources/download_manifest.jsonl`; canonical Markdown opened: no.
- Q5: `SKILL.md`, `references/route-registry.md`, `references/source-map.md`, `references/canonical_sources/README.md`, `references/corpus_index/README.md`, `references/source_inventory/local_corpus_index.md`, `.gitignore`; canonical Markdown opened: no.

## Orchestrator Consistency Checks

```text
section_index_files 63
canonical_md_files 201
canonical_raw_files 201
```

Additional checks from the local corpus index:

```text
press status=blocked md=0 raw=0 blocked=6
cacm_author_guidelines status=blocked md=0 raw=0 blocked=5
prisma_2020 status=partial md=24 raw=24 blocked=2
cochrane_handbook status=partial md=27 raw=27 blocked=2
prisma_scr status=available md=5 raw=5 blocked=0
swim status=available md=3 raw=3 blocked=0
```

## Verdict

Pass.

This two-agent validation exercised route selection, source-family selection, evidence locator rules, blocked-source handling, and the GitHub/full-corpus boundary. The answerer followed the intended progressive-disclosure path and did not bulk-load canonical Markdown/raw files.

Residual risk: this validates navigation behavior and source-boundary logic, not factual correctness of every canonical source. Claim-level factual validation still requires selected canonical Markdown/raw spans for the specific claim being answered.
