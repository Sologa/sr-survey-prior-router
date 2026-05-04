# Source Card: Scholarly Databases And APIs

source_ids: `crossref_api`, `openalex`, `openalex_snapshot`, `pubmed_eutilities`, `europe_pmc`, `clinicaltrials_api`, `who_ictrp`, `prospero`, `equator_prisma`, `cochrane_library`, `epistemonikos`, `opencitations`, `semantic_scholar`, `core_api`, `lens_api`, `dimensions_api`, `scite_api`, `ieee_xplore_api`

related_source_ids: `dblp`, `acl_anthology`, `acl_arr_authors`, `aclpub_formatting`, `arxiv`, `acm_dl`

## Summary

The best open/public metadata baseline is layered: Crossref and OpenAlex for broad scholarly metadata, PubMed/Europe PMC for biomedical literature, DBLP/ACL/arXiv for CS/NLP/preprints, ClinicalTrials.gov and WHO ICTRP for trial registries, EQUATOR/PROSPERO for guideline or protocol registry lookups, and OpenCitations/OpenAlex/Semantic Scholar for citation graph enrichment.

## Decision Boundary

Databases and APIs are discovery/state infrastructure. They do not define writing methodology. Commercial or restricted sources such as Dimensions, Lens, Scite, ACM DL, IEEE Xplore, and Semantic Scholar require explicit licensing/access checks before retrieval-corpus use.

## Supported Uses

- Build `source_manifest` rows and metadata lookup pipelines.
- Normalize identifiers and discover candidate exemplars.
- Add citation graph or trial registry context when needed.

## Gaps

- Local API documentation snapshots now exist for the retrieved database/API rows under `../../canonical_sources/`; use `source_manifest.jsonl` `local_documents` entries to locate them.
- DBLP, ACL Anthology, ACL ARR/ACLPUB, arXiv, and ACM DL are cross-family related sources mentioned for CS/NLP discovery; use their own source rows/cards before treating them as evidence.
- EQUATOR PRISMA is included here only as a registry/update locator. Use primary PRISMA rows for method or reporting evidence.
- Some local API Markdown files are short entry-point captures, especially selected CORE and Scite API docs. ClinicalTrials.gov now has a local OpenAPI v2 snapshot and live version endpoint capture, but human docs remain partially SPA-rendered and should be live-checked before automation.
- Bulk snapshots, data dumps, and commercial data products are not mirrored locally.
- Rate-limit and license checks are not encoded as executable validators.
- Full text is source-specific and usually not guaranteed by metadata APIs.

last_reviewed: 2026-05-05
