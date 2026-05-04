# ClinicalTrials.gov API Source Card v2

```yaml
source_id: clinicaltrials_api
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/clinicaltrials_api/official_openapi_v2.md
  - references/canonical_sources/md/clinicaltrials_api/official_version_v2.md
  - references/canonical_sources/md/clinicaltrials_api/canonical_learn-about-api.md
canonical_urls:
  - https://clinicaltrials.gov/data-api/api
  - https://clinicaltrials.gov/api/oas/v2
  - https://clinicaltrials.gov/api/v2/version
authority_level: canonical_database_api_doc
version_or_access_date: "OpenAPI document version 2.0.5; checked 2026-05-05"
applies_to:
  - ClinicalTrials.gov API routing
  - trial registry metadata and currentness checks
  - API schema and endpoint locator questions
not_for:
  - methodology authority
  - scholarly citation graph discovery
  - full-text article access
  - bulk mirror permission without terms review
route_relevance:
  - general_domain_prior
  - source_audit
  - evidence_grounding
freshness_risk: high; API behavior, data timestamps, and human docs can change and should be live-checked before automation.
reuse_or_license_risk: ClinicalTrials.gov data and API terms apply; avoid static study-result copies when currency matters.
qa_status: partial_human_docs_plus_official_openapi_and_live_version
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The local pack now contains an official OpenAPI document for ClinicalTrials.gov API v2.
  supporting_canonical_paths:
    - references/canonical_sources/md/clinicaltrials_api/official_openapi_v2.md
  support_type: direct
  verification_note: The OpenAPI wrapper records source URL, API title, document version, and base server URL.
  quote_or_locator: official_openapi_v2.md:1-13
- claim: The OpenAPI document locates study retrieval, metadata, search-area, stats, and version endpoints.
  supporting_canonical_paths:
    - references/canonical_sources/md/clinicaltrials_api/official_openapi_v2.md
  support_type: direct
  verification_note: The endpoint summary and full YAML list the high-value endpoint families.
  quote_or_locator: official_openapi_v2.md:15-27 and 47-860
- claim: The live version endpoint capture reports API version 2.0.5 and data timestamp 2026-05-04T09:00:05.
  supporting_canonical_paths:
    - references/canonical_sources/md/clinicaltrials_api/official_version_v2.md
  support_type: direct
  verification_note: The local JSON wrapper contains the current version endpoint response captured on 2026-05-05.
  quote_or_locator: official_version_v2.md:1-13
- claim: The older learn-about-API HTML capture is only a sparse entry-point locator and should not drive API implementation.
  supporting_canonical_paths:
    - references/canonical_sources/md/clinicaltrials_api/canonical_learn-about-api.md
  support_type: locator_only
  verification_note: The old capture remains short and only identifies the page context.
  quote_or_locator: canonical_learn-about-api.md:1-12
```

## Operational rules

- Use `official_openapi_v2.md` for endpoint and schema lookup.
- Use `official_version_v2.md` only for currentness/version facts tied to the 2026-05-05 capture.
- Live-check before building automation, especially for pagination, formats, rate/terms, or endpoint migration claims.
- Treat ClinicalTrials.gov as a registry/API source, not as SR or survey methodology guidance.

## Common misuses

- Treating trial-registry API docs as evidence-synthesis method guidance.
- Implementing against the sparse `canonical_learn-about-api.md` page instead of the OpenAPI capture.
- Assuming endpoint behavior or data timestamps are stable without a fresh live check.
- Using static copies of study records when current trial status matters.

## Evidence limits

The OpenAPI and version captures support API routing, schema, endpoint, and currentness-locator claims. They do not support review-writing method claims, broad citation graph coverage, full-text access, or permission for bulk redistribution of registry records.

## Verification paths

- OpenAPI capture: `references/canonical_sources/md/clinicaltrials_api/official_openapi_v2.md`.
- Version endpoint capture: `references/canonical_sources/md/clinicaltrials_api/official_version_v2.md`.
- Sparse old landing capture: `references/canonical_sources/md/clinicaltrials_api/canonical_learn-about-api.md`.
- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=clinicaltrials_api`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=clinicaltrials_api`.
- Optional local section locator: `references/corpus_index/sections/by_source/clinicaltrials_api.jsonl`.

## Unresolved gaps

- Human docs are SPA-rendered and not fully represented by simple HTML capture.
- Browser subagent reported an advertised `ctg-oas-v2.yaml` path returned 404 on 2026-05-05; `/api/oas/v2` succeeded locally and is the tracked OpenAPI capture.
- Terms, rate behavior, and study-data currentness still need live verification before production automation.
