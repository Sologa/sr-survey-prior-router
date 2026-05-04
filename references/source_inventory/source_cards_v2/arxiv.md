# arXiv API and Bulk Access Source Card v2

```yaml
source_id: arxiv
source_family: nlp_speech_cs_exemplar_sources
canonical_paths:
  - references/canonical_sources/md/arxiv/canonical_index.html.md
canonical_urls:
  - https://info.arxiv.org/help/api/index.html
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04; local corpus fetched 2026-05-04"
applies_to:
  - preprint metadata lookup
  - arXiv API and OAI-PMH routing
  - approved bulk metadata and full-text access planning
not_for:
  - systematic review reporting guidance
  - survey writing methodology
  - peer-review status verification
  - published-version source-of-record metadata
  - universal citation graph
route_relevance:
  - general_domain_prior
  - evidence_grounding
  - source_audit
freshness_risk: high for API terms, bulk data pipelines, branding guidance, OAI/S3/Kaggle/AWS routes, and access limits; verify live arXiv docs before implementation.
reuse_or_license_risk: arXiv papers have per-paper licenses and API/bulk/branding terms; open access does not imply uniform reuse rights.
qa_status: seed_verified_from_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: arXiv offers public API access to maximize openness and interoperability.
  supporting_canonical_paths:
    - references/canonical_sources/md/arxiv/canonical_index.html.md
  support_type: direct
  verification_note: Use for arXiv preprint metadata/access routing, not peer-review status.
  quote_or_locator: canonical_index.html.md:296-299
- claim: Commercial projects using arXiv APIs should review public API, bulk-data, brand-use, and affiliate documentation.
  supporting_canonical_paths:
    - references/canonical_sources/md/arxiv/canonical_index.html.md
  support_type: direct
  verification_note: Commercial or productized use needs current policy review.
  quote_or_locator: canonical_index.html.md:300-312
- claim: All API users are instructed to review API Terms of Use, API Basics, API User Manual, and interoperability resources including identifier scheme, bulk data access, and OAI.
  supporting_canonical_paths:
    - references/canonical_sources/md/arxiv/canonical_index.html.md
  support_type: direct
  verification_note: Treat terms and bulk/OAI routes as live-doc checks before implementation.
  quote_or_locator: canonical_index.html.md:314-326
- claim: The captured arXiv page advertises bulk access to metadata and full text through dedicated routes.
  supporting_canonical_paths:
    - references/canonical_sources/md/arxiv/canonical_index.html.md
  support_type: direct
  verification_note: Bulk access does not remove per-paper license checks.
  quote_or_locator: canonical_index.html.md:199-206,326
```

## Operational rules

- Use arXiv for preprint metadata and approved arXiv source/PDF/full-text access routes.
- Treat API terms, branding rules, OAI-PMH, and bulk-access channels as current implementation prerequisites.
- Separate arXiv preprints from peer-reviewed/published versions when building evidence packets.
- Do not use arXiv access docs as SR reporting, conduct, appraisal, certainty, or survey-writing authority.

## Common misuses

- Treating arXiv presence as peer-review or published-version evidence.
- Assuming all arXiv full text has the same reuse license.
- Using general API routes for bulk work without checking bulk-access instructions.
- Branding a downstream product in a way that implies arXiv endorsement.

## Evidence limits

This card supports routing to arXiv API and bulk-access documentation. It does not establish article-level license rights, publication status, or current operational limits.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=arxiv`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=arxiv`.
- Canonical Markdown: `references/canonical_sources/md/arxiv/canonical_index.html.md`.
- Optional section locators: `references/corpus_index/sections/by_source/arxiv.jsonl`.

## Unresolved gaps

- Capture more specific arXiv API manual, OAI-PMH, bulk, and license pages if executable retrieval work is needed.
- Confirm per-paper license handling before any redistribution or derived full-text corpus.
