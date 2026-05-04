# PubMed E-utilities Source Card v2

```yaml
source_id: pubmed_eutilities
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/pubmed_eutilities/canonical_nbk25497.md
  - references/canonical_sources/md/pubmed_eutilities/linked_1_bookshelf_nbk25497.pdf.md
canonical_urls:
  - https://www.ncbi.nlm.nih.gov/sites/books/NBK25497/
authority_level: canonical_database_api_doc
version_or_access_date: "Last Update: November 17, 2022; checked 2026-05-04"
applies_to:
  - PubMed and NCBI Entrez metadata retrieval
  - E-utilities API routing
  - biomedical source audit
not_for:
  - closed full-text access
  - cross-disciplinary coverage guarantees
  - systematic review methodology authority
  - appraisal or certainty grading
route_relevance:
  - general_domain_prior
  - source_audit
  - evidence_grounding
freshness_risk: high for rate limits, API keys, supported databases, and policy details; verify live NCBI docs before implementation.
reuse_or_license_risk: PubMed abstracts may include copyrighted material; NCBI disclaimer and copyright notice requirements apply.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: E-utilities are server-side programs providing a stable interface into the Entrez query and database system.
  supporting_canonical_paths:
    - references/canonical_sources/md/pubmed_eutilities/canonical_nbk25497.md
  support_type: direct
  verification_note: Use for API/data-access claims only.
  quote_or_locator: canonical_nbk25497.md:90-97
- claim: NCBI recommends no more than three E-utility URL requests per second without enhanced access, and API keys allow up to ten requests per second by default.
  supporting_canonical_paths:
    - references/canonical_sources/md/pubmed_eutilities/canonical_nbk25497.md
  support_type: direct
  verification_note: Recheck live NCBI docs before running production automation.
  quote_or_locator: canonical_nbk25497.md:108-122
- claim: For large jobs, the documentation recommends batching through Entrez History rather than separate requests for each record.
  supporting_canonical_paths:
    - references/canonical_sources/md/pubmed_eutilities/canonical_nbk25497.md
  support_type: direct
  verification_note: Use for implementation planning, not methodology claims.
  quote_or_locator: canonical_nbk25497.md:124-127
- claim: E-utilities retrieve data already in Entrez and should not be assumed to cover datasets outside Entrez.
  supporting_canonical_paths:
    - references/canonical_sources/md/pubmed_eutilities/canonical_nbk25497.md
  support_type: direct
  verification_note: Use as a coverage boundary when routing biomedical metadata searches.
  quote_or_locator: canonical_nbk25497.md:203-208
```

## Operational rules

- Use E-utilities for structured NCBI/PubMed metadata workflows.
- Include registered `tool` and `email` values and respect current rate limits for automation.
- Use Entrez History for large retrieval jobs.
- Do not cite E-utilities documentation as systematic-review methodology guidance.

## Common misuses

- Assuming PubMed metadata retrieval implies full-text access.
- Treating API rate limits captured locally as permanently current.
- Using PubMed coverage as a proxy for all scholarly literature.

## Evidence limits

This card covers NCBI E-utilities API behavior and boundaries only. It does not provide PRISMA, Cochrane, GRADE, or appraisal-method authority.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=pubmed_eutilities`.
- Canonical HTML conversion: `references/canonical_sources/md/pubmed_eutilities/canonical_nbk25497.md`.
- PDF conversion: `references/canonical_sources/md/pubmed_eutilities/linked_1_bookshelf_nbk25497.pdf.md`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=pubmed_eutilities`.
- Optional local section locators: `references/corpus_index/sections/by_source/pubmed_eutilities.jsonl`.

## Unresolved gaps

- Need live verification before operational use because API policy and database inventory can change.
- Need separate PMC/OA full-text documentation for full-text retrieval claims.
