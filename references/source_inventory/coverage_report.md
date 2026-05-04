# Source Inventory Coverage Report

Last checked: 2026-05-04

This inventory was assembled before promoting `sr-survey-prior-router` from a staged router to a substantive survey/SR prior. It records candidate canonical sources, method authorities, venue guidance, exemplar corpora, and backing databases. A first local corpus now exists at `../canonical_sources/`, with raw downloads and Markdown conversions for sources that could be retrieved.

## Bottom Line

The pack can now claim that it has a seed source inventory and a first local full-document corpus for survey/SR prior construction.

It must not yet claim complete knowledge-heavy coverage. Full coverage still requires validating each source row, resolving or documenting blocked official URLs, generating source cards for individual high-priority sources, and testing retrieval/evidence packets against real writing tasks.

## Local Corpus Status

Local corpus path: `docs/agent_capability_packs/sr-survey-prior-router/references/canonical_sources/`.

- `raw/`: downloaded HTML, PDF, DOCX, and other raw files.
- `md/`: Markdown conversions for downloaded readable documents.
- `download_manifest.jsonl`: source ID, URL, final URL, checksum, local raw path, Markdown path, conversion status, and failures.
- `source_inventory/local_corpus_index.md` and `.json`: source-level lazy-load index; 65 source IDs, 201 Markdown paths, with primary entry points capped for initial selection. One local capture, `state_of_art_review_2022`, is flagged `bad_capture` because the Markdown contains only a browser-check page.
- `corpus_index/document_index.jsonl`: 201 document locator rows.
- `corpus_index/section_index_manifest.jsonl` plus `corpus_index/sections/by_source/<source_id>.jsonl`: split section/page locator indexes for selected sources only.
- Current verified count after the 2026-05-04 augmentation plus subagent completion pass: 201 raw files and 201 Markdown files.
- `source_manifest.jsonl` now has local raw/Markdown documents for 63 of 65 source rows. The rows without local documents are `press` and `cacm_author_guidelines`, both blocked by official-site 403 responses from this environment. Of the 63 with local files, `state_of_art_review_2022` is not evidence-usable because the captured PMC page is a reCAPTCHA/browser-check response.
- PRISMA 2020 now includes the PRISMA site pages, checklist PDFs/DOCX, expanded checklist PDF, abstract checklist PDF/DOCX, flow diagram DOCX files, PLOS statement PDF, PLOS statement HTML, and PMC/BMJ printable full-text HTML for the statement and explanation/elaboration papers.
- Nickerson taxonomy method now has a publisher PDF from Springer converted to Markdown because the OPUS Augsburg mirror timed out from this environment.
- Previously skipped API/database rows now have official documentation snapshots where practical, including OpenAlex snapshot docs, Semantic Scholar API docs/OpenAPI JSON, CORE API docs, Lens API docs/swagger YAML, Dimensions DSL/API docs, Scite API docs/OpenAPI JSON, OpenCitations docs, and IEEE Xplore API docs. Bulk datasets and commercial data products were not mirrored.
- Venue/exemplar gaps were reduced by local official alternatives: ACM DL user guide, TransACL submission/formatting files, Computational Linguistics OJS/style files, Papers with Code GitHub data/client docs, IEEE ComSoc author kit, and ISCA Interspeech booklet.

## Current Coverage

### Strong Seed Coverage

- SR reporting and conduct authorities: PRISMA 2020, PRISMA extensions, PRISMA-S, PRISMA-P, PRISMA-ScR, Cochrane Handbook, MECIR, JBI Manual, Campbell Standards.
- SR certainty, appraisal, bias, and search QA with local evidence: GRADE, GRADE Handbook, CERQual, AMSTAR 2, ROBIS, RoB 2, ROBINS-I. PRESS remains a candidate search-QA authority, but it is blocked locally and cannot be treated as local canonical evidence.
- Survey/scoping/narrative/synthesis methods: JBI scoping/narrative guidance, SWiM, ENTREQ, RAMESES, Cochrane Handbook chapters 9 and 12, SANRA, and narrative synthesis guidance. `state_of_art_review_2022` is present as a source row but its local capture is a browser-check page, so it is not currently usable as local method evidence.
- Survey taxonomy and organization: Nickerson taxonomy method and Kundisch taxonomy update.
- NLP/speech/CS exemplar and metadata sources: ACL Anthology, TACL, Computational Linguistics, ISCA Archive, DBLP, Crossref, OpenAlex, arXiv.
- Backing databases/APIs and registry locators: PubMed/NCBI E-utilities, Europe PMC, ClinicalTrials.gov, WHO ICTRP, PROSPERO, EQUATOR PRISMA, OpenCitations, Semantic Scholar, CORE, Lens, Dimensions, Scite, ACM DL, IEEE Xplore.

### Partial Coverage

- Venue-specific survey writing norms are only seed-level. IEEE Communications Surveys & Tutorials, Nature Reviews, Scientific Reviews, CACM/ACM, IEEE Access, and publisher guidance are useful, but venue-specific and not universal methods authorities.
- NLP/speech survey conventions are represented by venue/corpus sources, not by a dedicated NLP/speech survey-writing methodology standard.
- Commercial/proprietary sources such as Dimensions, Lens, Scite, ACM DL, IEEE Xplore, and Semantic Scholar require explicit license/access checks before use as a retrieval corpus.

### Not Covered Or Still Blocked

- Exhaustive local mirrors of broad APIs, commercial databases, or bulk snapshots.
- Blocked official pages that returned 403 from this environment, especially CDA-AMC PRESS and CACM author guideline pages.
- Bad local captures, especially `state_of_art_review_2022`, whose current local Markdown contains only a PMC browser-check page rather than article content.
- MIT Press canonical pages for TACL and Computational Linguistics returned 403, but official TransACL and Computational Linguistics OJS/style-file alternatives are locally captured.
- Direct BMJ PDF endpoints for PRISMA 2020 statement and explanation/elaboration returned 403 after repeated attempts; equivalent/open full-text local fallbacks are captured from PRISMA/PLOS/PMC where available.
- Exhaustive source cards for every source row.
- Domain-specific NLP/speech taxonomy exemplars and worked paper-to-taxonomy ledgers.
- Bibliometric-review-specific methods as a full workflow.
- Automatic survey generation pipelines.

## Authority Rules

- Reporting guidelines, conduct manuals, and method papers are methodology authorities only within their declared scope.
- Registry/database sources such as PROSPERO, EQUATOR PRISMA, PubMed, ClinicalTrials.gov, WHO ICTRP, OpenAlex, DBLP, and Crossref support discovery, state checking, and metadata. They do not by themselves define how to write or conduct a review.
- Venue guidance supports style, positioning, article type, and reader expectations. It is not a cross-domain methodology standard.
- Derivative artifacts such as source cards, RAG chunks, prior chat summaries, and this coverage report can locate evidence but cannot support final claims unless traced back to canonical sources.

## Promotion Gate

Before this pack is described as knowledge-heavy for a route, require:

1. `source_manifest.jsonl` rows for the route's canonical sources are validated.
2. Local `canonical_sources/md/<source_id>/` files are checked first when available.
3. `source_registry.yaml` assigns authority class, scope, not-for boundary, freshness, and load mode.
4. At least one source card exists for each claimed source family.
5. Retrieval or manual lookup can produce evidence packets with source ID, URL/path, section or locator, support type, and freshness.
6. Coverage gaps remain visible in the answer rather than hidden by synthesis prose.
7. Agents use the lazy-load indexes before opening canonical Markdown, and do not bulk-load `canonical_sources/md/` as route context.

## Validation

- `../../validation/agent_qa_validation_2026-05-04.md`: two-agent Q/A validation passed for route-first behavior, SR authority boundaries, survey-writing routing, evidence locator rules, blocked-source handling, and GitHub/full-corpus boundaries.

## Recommended First Priority

For `sr_writing_prior`, validate and card these first: PRISMA 2020, PRISMA-S, Cochrane Handbook, MECIR, JBI Manual, Campbell Standards, GRADE/CERQual, AMSTAR 2, ROBIS, RoB 2, ROBINS-I, PROSPERO, and PRESS only after browser/manual or access-approved retrieval succeeds.

For `survey_writing_prior`, validate and card these first: PRISMA-ScR, JBI scoping/narrative chapters, SWiM, ENTREQ, RAMESES, Cochrane chapters 9 and 12, SANRA, narrative synthesis guidance, Nickerson taxonomy method, Kundisch taxonomy update, IEEE Communications Surveys & Tutorials, ACL Anthology, ISCA Archive, DBLP, OpenAlex, Crossref. Do not use `state_of_art_review_2022` until the article body is recaptured.
