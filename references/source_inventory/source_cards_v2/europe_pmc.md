# Europe PMC Source Card v2

```yaml
source_id: europe_pmc
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/europe_pmc/canonical_restfulwebservice.md
  - references/canonical_sources/md/europe_pmc/linked_1_europe_pmc_restful_release_notes.pdf.md
  - references/canonical_sources/md/europe_pmc/linked_2_ebi_europe_pmc_web_service_reference.pdf.md
canonical_urls:
  - https://europepmc.org/RestfulWebService
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04"
applies_to:
  - life-sciences metadata discovery
  - Europe PMC REST and bulk-service routing
  - open full-text subset and citation-network context
not_for:
  - universal all-discipline coverage
  - license-uniform full-text corpus claims
  - systematic review methodology authority
  - appraisal or certainty grading
route_relevance:
  - general_domain_prior
  - source_audit
  - evidence_grounding
freshness_risk: high for API versions, counts, endpoints, release behavior, and terms; verify live docs before implementation.
reuse_or_license_risk: article licenses vary; public API use implies privacy-notice acceptance and full-text reuse must be checked per article/license.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: Europe PMC RESTful Web Service provides access to publications from sources including PubMed, Agricola, EPO, and NICE, plus full text, open access articles, references, citation counts, and text-mined terms.
  supporting_canonical_paths:
    - references/canonical_sources/md/europe_pmc/canonical_restfulwebservice.md
  support_type: direct
  verification_note: Counts are freshness-sensitive; use for route scope, not current live totals.
  quote_or_locator: canonical_restfulwebservice.md:138-152
- claim: Europe PMC REST responses can be XML or JSON, with Dublin Core available for the search module.
  supporting_canonical_paths:
    - references/canonical_sources/md/europe_pmc/canonical_restfulwebservice.md
  support_type: direct
  verification_note: Verify live docs before implementing response parsing.
  quote_or_locator: canonical_restfulwebservice.md:154-157,191-210
- claim: Europe PMC maintains simultaneous production and test REST service versions to support release preparation.
  supporting_canonical_paths:
    - references/canonical_sources/md/europe_pmc/canonical_restfulwebservice.md
  support_type: direct
  verification_note: Check release notes for current version details.
  quote_or_locator: canonical_restfulwebservice.md:158-166
- claim: The core result type returns full metadata including abstract, full text links, and MeSH terms.
  supporting_canonical_paths:
    - references/canonical_sources/md/europe_pmc/canonical_restfulwebservice.md
  support_type: direct
  verification_note: Full text links are not the same as redistribution rights.
  quote_or_locator: canonical_restfulwebservice.md:181-190
```

## Operational rules

- Use Europe PMC for life-sciences metadata, open-full-text subset routing, citation/reference context, and API-backed discovery.
- Verify current API version, fields, and terms before automation.
- Do not treat Europe PMC as a methods source or a license-uniform full-text corpus.

## Common misuses

- Assuming a full-text link grants reuse rights.
- Treating coverage counts in a local capture as current.
- Treating Europe PMC citation metrics as review-quality or methodology evidence.

## Evidence limits

This card supports Europe PMC API/source-routing claims only. It does not prove article-level access rights, current service limits, or methodological authority.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=europe_pmc`.
- REST service page: `references/canonical_sources/md/europe_pmc/canonical_restfulwebservice.md`.
- Release notes: `references/canonical_sources/md/europe_pmc/linked_1_europe_pmc_restful_release_notes.pdf.md`.
- Web service reference: `references/canonical_sources/md/europe_pmc/linked_2_ebi_europe_pmc_web_service_reference.pdf.md`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=europe_pmc`.
- Optional local section locators: `references/corpus_index/sections/by_source/europe_pmc.jsonl`.

## Unresolved gaps

- Need live API documentation check for current endpoints, counts, and release status.
- Need per-article license handling before full-text reuse.
