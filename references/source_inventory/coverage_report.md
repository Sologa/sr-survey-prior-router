# Source Inventory Coverage Report

Last checked: 2026-05-05

This inventory was assembled before promoting `sr-survey-prior-router` from a staged router to a substantive survey/SR prior. It records candidate canonical sources, method authorities, venue guidance, exemplar corpora, and backing databases. A first local corpus now exists at `../canonical_sources/`, with raw downloads and Markdown conversions for sources that could be retrieved.

## Bottom Line

The pack can now claim that it has a seed source inventory, a first local full-document corpus, and a source-card-v2 file for every `source_manifest.jsonl` row.

It must not yet claim final knowledge-heavy coverage. Remaining work is no longer "missing source cards"; it is live recapture/currentness checks for blocked or freshness-sensitive sources, route-level evidence-packet testing, and real writing-task validation.

## Local Corpus Status

Local corpus path: `docs/agent_capability_packs/sr-survey-prior-router/references/canonical_sources/`.

- `raw/`: downloaded HTML, PDF, DOCX, and other raw files.
- `md/`: Markdown conversions for downloaded readable documents.
- `download_manifest.jsonl`: source ID, URL, final URL, checksum, local raw path, Markdown path, conversion status, and failures.
- `source_inventory/local_corpus_index.md` and `.json`: source-level lazy-load index; 65 source IDs, 203 Markdown paths, with primary entry points capped for initial selection. The former `state_of_art_review_2022` bad capture was repaired on 2026-05-05, and `clinicaltrials_api` now includes an official OpenAPI v2 snapshot plus a live version endpoint capture.
- `corpus_index/document_index.jsonl`: 203 document locator rows.
- `corpus_index/section_index_manifest.jsonl` plus `corpus_index/sections/by_source/<source_id>.jsonl`: split section/page locator indexes for selected sources only. The split by-source files are local/rebuildable backing locators and may be absent from a public GitHub checkout.
- `source_inventory/source_cards_v2/`: per-source derivative cards with canonical paths, support types, and fallback locators for public review. There is now one v2 card for each of the 65 `source_manifest.jsonl` source IDs.
- Current verified count after the 2026-05-04 augmentation plus 2026-05-05 live recapture pass: 203 raw files and 203 Markdown files.
- `source_manifest.jsonl` now has local raw/Markdown documents for 63 of 65 source rows. The rows without local documents are `press` and `cacm_author_guidelines`; both were browser-live checked on 2026-05-05, but simple local scripted fetches still returned Cloudflare/403-style blocks and no tracked local canonical content exists for their source claims.
- PRISMA 2020 now includes the PRISMA site pages, checklist PDFs/DOCX, expanded checklist PDF, abstract checklist PDF/DOCX, flow diagram DOCX files, PLOS statement PDF, PLOS statement HTML, and PMC/BMJ printable full-text HTML for the statement and explanation/elaboration papers.
- Nickerson taxonomy method now has a publisher PDF from Springer converted to Markdown because the OPUS Augsburg mirror timed out from this environment.
- Previously skipped API/database rows now have official documentation snapshots where practical, including OpenAlex snapshot docs, Semantic Scholar API docs/OpenAPI JSON, CORE API docs, Lens API docs/swagger YAML, Dimensions DSL/API docs, Scite API docs/OpenAPI JSON, OpenCitations docs, and IEEE Xplore API docs. Bulk datasets and commercial data products were not mirrored.
- Venue/exemplar gaps were reduced by local official alternatives: ACM DL user guide, TransACL submission/formatting files, Computational Linguistics OJS/style files, Papers with Code GitHub data/client docs, IEEE ComSoc author kit, and ISCA Interspeech booklet.

## Current Coverage

### Strong Seed Coverage

- SR reporting and conduct authorities: PRISMA 2020, PRISMA extensions, PRISMA-S, PRISMA-P, PRISMA-ScR, Cochrane Handbook, MECIR, JBI Manual, Campbell Standards.
- SR certainty, appraisal, bias, and search QA with local evidence: GRADE, GRADE Handbook, CERQual, AMSTAR 2, ROBIS, RoB 2, ROBINS-I. PRESS remains a candidate search-QA authority; browser-live access found current official locators, but the pack still lacks local PRESS Markdown and cannot use PRESS content as local canonical evidence.
- Survey/scoping/narrative/synthesis methods: JBI scoping/narrative guidance, SWiM, ENTREQ, RAMESES, Cochrane Handbook chapters 9 and 12, SANRA, state-of-the-art review methodology, and narrative synthesis guidance.
- Survey taxonomy and organization: Nickerson taxonomy method and Kundisch taxonomy update.
- NLP/speech/CS exemplar and metadata sources: ACL Anthology, TACL, Computational Linguistics, ISCA Archive, DBLP, Crossref, OpenAlex, arXiv.
- Backing databases/APIs and registry locators: PubMed/NCBI E-utilities, Europe PMC, ClinicalTrials.gov, WHO ICTRP, PROSPERO, EQUATOR PRISMA, OpenCitations, Semantic Scholar, CORE, Lens, Dimensions, Scite, ACM DL, IEEE Xplore.

### Partial Coverage

- Venue-specific survey writing norms are only seed-level. IEEE Communications Surveys & Tutorials, Nature Reviews, Scientific Reviews, CACM/ACM, IEEE Access, and publisher guidance are useful, but venue-specific and not universal methods authorities.
- NLP/speech survey conventions are represented by venue/corpus sources, not by a dedicated NLP/speech survey-writing methodology standard.
- Commercial/proprietary sources such as Dimensions, Lens, Scite, ACM DL, IEEE Xplore, and Semantic Scholar require explicit license/access checks before use as a retrieval corpus.

### Not Covered Or Still Blocked

- Exhaustive local mirrors of broad APIs, commercial databases, or bulk snapshots.
- Browser-live but locally uncaptured official pages, especially CDA-AMC PRESS and CACM/ACM author guidance. These need browser/manual or access-approved capture before local evidence use.
- ClinicalTrials.gov human docs remain SPA-rendered/partial in simple captures; use the local OpenAPI v2 and version endpoint snapshots for API-schema/currentness locators, with live verification before automation.
- MIT Press canonical pages for TACL and Computational Linguistics returned 403, but official TransACL and Computational Linguistics OJS/style-file alternatives are locally captured.
- Direct BMJ PDF endpoints for PRISMA 2020 statement and explanation/elaboration returned 403 after repeated attempts; equivalent/open full-text local fallbacks are captured from PRISMA/PLOS/PMC where available.
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
4. At least one source card exists for each claimed source family; for claim-level reuse, prefer a passing `source_cards_v2/<source_id>.md` card for the specific source.
5. Retrieval or manual lookup can produce evidence packets with source ID, URL/path, section or locator, support type, and freshness.
6. Coverage gaps remain visible in the answer rather than hidden by synthesis prose.
7. Agents use the lazy-load indexes before opening canonical Markdown, fall back to source-card-v2 locators when split section indexes are absent, and do not bulk-load `canonical_sources/md/` as route context.

## Validation

- `../../validation/agent_qa_validation_2026-05-04.md`: two-agent Q/A validation passed for route-first behavior, SR authority boundaries, survey-writing routing, evidence locator rules, blocked-source handling, and GitHub/full-corpus boundaries.
- `../../validation/source_cards_v2_batch_2026-05-04.md`: source-card-v2 batch validation passed for 26 cards, covering first-wave PRISMA extensions, conduct/manual sources, appraisal/certainty/bias tools, survey/synthesis reporting methods, and taxonomy-method sources.
- `../../validation/source_cards_v2_full_coverage_2026-05-05.md`: source-card-v2 full coverage validation passed for 65 cards, one for every `source_manifest.jsonl` source ID.

## Recommended First Priority

For `sr_writing_prior`, source-card-v2 coverage now includes PRISMA 2020, PRISMA extensions, PRISMA-S, PRISMA-P, Cochrane Handbook, MECIR, JBI Manual, Campbell Standards, GRADE/CERQual, AMSTAR 2, ROBIS, RoB 2, ROBINS-I, PROSPERO, EQUATOR PRISMA, registry/API locators, and browser-live/no-local-content PRESS status. PRESS remains unavailable as local evidence until browser/manual or access-approved retrieval is stored.

For `survey_writing_prior`, source-card-v2 coverage now includes PRISMA-ScR, JBI Manual, Cochrane chapters 9 and 12, SWiM, ENTREQ, RAMESES, SANRA, state-of-the-art review methodology, York narrative synthesis guidance, narrative-review writing guidance, Nickerson taxonomy method, Kundisch taxonomy update, venue/exemplar cards, and scholarly-database/API cards. Use `state_of_art_review_2022` only for scoped SotA review methodology claims.
