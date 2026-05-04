# Cochrane Library Source Card v2

```yaml
source_id: cochrane_library
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/cochrane_library/canonical_cochrane-library.md
canonical_urls:
  - https://www.cochrane.org/products-and-services/cochrane-library
authority_level: canonical_database_api_doc
version_or_access_date: "no page update stamp visible; checked 2026-05-04"
applies_to:
  - discovery of Cochrane reviews, protocols, CENTRAL, and related review content
  - source audit for health evidence databases
not_for:
  - replacing the Cochrane Handbook as methodology guidance
  - generic open full-text corpus access
  - risk-of-bias tool instructions
  - certainty grading rules
route_relevance:
  - general_domain_prior
  - source_audit
  - evidence_grounding
freshness_risk: medium; access options, pricing, subscriptions, and database counts can change.
reuse_or_license_risk: access is subscription constrained for much content; verify Cochrane Library terms before bulk use or redistribution.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: A Cochrane Library subscription is described as spanning reviews, protocols, data, and editorials.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_library/canonical_cochrane-library.md
  support_type: direct
  verification_note: Use for database/source-discovery scope only.
  quote_or_locator: canonical_cochrane-library.md:70-74
- claim: The Cochrane Database of Systematic Reviews includes Cochrane reviews, protocols, editorials, and occasional supplements.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_library/canonical_cochrane-library.md
  support_type: direct
  verification_note: Do not convert this database-scope claim into methodology guidance.
  quote_or_locator: canonical_cochrane-library.md:76-86
- claim: CENTRAL is described as a concentrated source of reports of randomized and quasi-randomized controlled trials, with bibliographic details and usually abstracts.
  supporting_canonical_paths:
    - references/canonical_sources/md/cochrane_library/canonical_cochrane-library.md
  support_type: direct
  verification_note: Use for trial-report discovery context, not full-text availability.
  quote_or_locator: canonical_cochrane-library.md:88-89
```

## Operational rules

- Use `cochrane_library` for discovery-source context and source-audit routing.
- Use `cochrane_handbook` or `cochrane_mecir` for conduct/methodology claims.
- Treat subscription, access, and pricing details as freshness-sensitive.

## Common misuses

- Citing Cochrane Library product-page text as Cochrane methodology guidance.
- Assuming subscription discovery implies open full-text access.
- Treating CENTRAL records as clinical-trial registry records.

## Evidence limits

This card covers the Cochrane Library product/source page only. It does not provide Cochrane Handbook methods, MECIR standards, risk-of-bias instructions, or article-level license rights.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=cochrane_library`.
- Canonical capture: `references/canonical_sources/md/cochrane_library/canonical_cochrane-library.md`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=cochrane_library`.
- Optional local section locator: `references/corpus_index/sections/by_source/cochrane_library.jsonl`.

## Unresolved gaps

- Need live access verification for subscription and pricing details.
- Need source-specific search/export documentation if the pack later automates Cochrane Library retrieval.
