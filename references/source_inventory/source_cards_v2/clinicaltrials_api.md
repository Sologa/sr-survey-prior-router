# ClinicalTrials.gov API Source Card v2

```yaml
source_id: clinicaltrials_api
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/clinicaltrials_api/canonical_learn-about-api.md
canonical_urls:
  - https://clinicaltrials.gov/data-about-studies/learn-about-api
authority_level: bad_capture_do_not_use
version_or_access_date: "checked 2026-05-04"
applies_to:
  - inventory target for ClinicalTrials.gov API documentation
  - trial-registry source routing after recapture
not_for:
  - methodology authority
  - scholarly citation graph discovery
  - full-text access
  - API implementation from the current local capture
route_relevance:
  - general_domain_prior
  - source_audit
  - evidence_grounding
freshness_risk: high; API details and data refresh behavior are current facts and the local capture is incomplete.
reuse_or_license_risk: ClinicalTrials.gov registry data and API terms apply; verify current terms before bulk use.
qa_status: bad_capture_local_markdown_too_sparse
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The local canonical Markdown identifies the source URL as the ClinicalTrials.gov learn-about-API page, but it does not preserve substantive API documentation.
  supporting_canonical_paths:
    - references/canonical_sources/md/clinicaltrials_api/canonical_learn-about-api.md
  support_type: locator_only
  verification_note: The local capture has only 12 lines and should not be used for API implementation claims.
  quote_or_locator: canonical_learn-about-api.md:1-12
- claim: The local capture mentions ClinicalTrials.gov and points study record managers to Data Element Definitions.
  supporting_canonical_paths:
    - references/canonical_sources/md/clinicaltrials_api/canonical_learn-about-api.md
  support_type: direct
  verification_note: This is a minimal identity/locator claim only.
  quote_or_locator: canonical_learn-about-api.md:6-12
- claim: Detailed claims about ClinicalTrials.gov API endpoints, refresh cadence, output formats, or rate limits are unsupported by the current local Markdown.
  supporting_canonical_paths:
    - references/canonical_sources/md/clinicaltrials_api/canonical_learn-about-api.md
  support_type: unsupported
  verification_note: Recapture or live verification is required before operational API use.
  quote_or_locator: canonical_learn-about-api.md:1-12
```

## Operational rules

- Treat this card as a bad-capture warning and source locator.
- Do not implement ClinicalTrials.gov API workflows from this local capture.
- Recapture the canonical API documentation or verify the live site before making endpoint, schema, refresh, export, or rate-limit claims.

## Common misuses

- Treating the manifest row as API evidence.
- Treating ClinicalTrials.gov as a systematic-review methodology authority.
- Inferring endpoint details from the source title alone.

## Evidence limits

The current local canonical Markdown is too sparse for API documentation. It can only identify the intended page and flag the need for recapture.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=clinicaltrials_api`.
- Sparse capture: `references/canonical_sources/md/clinicaltrials_api/canonical_learn-about-api.md`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=clinicaltrials_api`.
- Optional local section locator: `references/corpus_index/sections/by_source/clinicaltrials_api.jsonl`.

## Unresolved gaps

- Need a complete recapture of ClinicalTrials.gov API docs.
- Need current terms, refresh cadence, endpoint/schema, and export-format verification before automation.
