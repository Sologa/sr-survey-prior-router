# WHO ICTRP Source Card v2

```yaml
source_id: who_ictrp
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/who_ictrp/canonical_the-ictrp-search-portal.md
  - references/canonical_sources/md/who_ictrp/linked_1_ictrp_revisions_document.pdf.md
canonical_urls:
  - https://www.who.int/tools/clinical-trials-registry-platform/the-ictrp-search-portal
authority_level: canonical_database_api_doc
version_or_access_date: "WHO page copyright 2026; checked 2026-05-04"
applies_to:
  - global clinical trial registry search routing
  - ICTRP portal and record-bridging context
  - trial-registration source audit
not_for:
  - literature metadata discovery
  - full-text access
  - citation graph construction
  - systematic review methodology authority
route_relevance:
  - general_domain_prior
  - source_audit
  - evidence_grounding
freshness_risk: high; service availability, registry network status, crawling/web-service access, and data restrictions can change.
reuse_or_license_risk: WHO and ICTRP data-use restrictions apply; verify current terms before downloading, crawling, or reusing records.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The ICTRP Search Portal aims to provide a single point of access to information about ongoing and completed clinical trials.
  supporting_canonical_paths:
    - references/canonical_sources/md/who_ictrp/canonical_the-ictrp-search-portal.md
  support_type: direct
  verification_note: Use for trial-registry routing only.
  quote_or_locator: canonical_the-ictrp-search-portal.md:452-455
- claim: ICTRP contains trial registration data sets made available by data providers around the world meeting content and quality-control criteria.
  supporting_canonical_paths:
    - references/canonical_sources/md/who_ictrp/canonical_the-ictrp-search-portal.md
  support_type: direct
  verification_note: This does not imply literature full text or methodology authority.
  quote_or_locator: canonical_the-ictrp-search-portal.md:452-455
- claim: The portal bridges multiple records about the same trial to facilitate unambiguous identification.
  supporting_canonical_paths:
    - references/canonical_sources/md/who_ictrp/canonical_the-ictrp-search-portal.md
    - references/canonical_sources/md/who_ictrp/linked_1_ictrp_revisions_document.pdf.md
  support_type: direct
  verification_note: Use for record-linking context; verify current behavior before automation.
  quote_or_locator: canonical_the-ictrp-search-portal.md:476-478; linked_1_ictrp_revisions_document.pdf.md:155-162
- claim: The revision document records export/search changes but is old relative to the current WHO page.
  supporting_canonical_paths:
    - references/canonical_sources/md/who_ictrp/linked_1_ictrp_revisions_document.pdf.md
  support_type: direct
  verification_note: Treat the revision PDF as historical locator evidence unless live service docs are checked.
  quote_or_locator: linked_1_ictrp_revisions_document.pdf.md:32-39,111-141
```

## Operational rules

- Use WHO ICTRP for global clinical-trial registry discovery and duplicate/bridged-record context.
- Recheck current ICTRP service, crawling, web-service, and download rules before automation.
- Do not use ICTRP as a literature database, full-text source, or review-method authority.

## Common misuses

- Treating trial registration data as peer-reviewed literature metadata.
- Assuming multilingual registry records are searchable through the ICTRP English portal.
- Using the 2018 revision PDF as current API/service documentation.

## Evidence limits

This card supports trial-registry routing and local portal/revision-document claims. It does not establish current service availability, full data-use rights, or systematic-review methods.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=who_ictrp`.
- WHO portal capture: `references/canonical_sources/md/who_ictrp/canonical_the-ictrp-search-portal.md`.
- Revision document: `references/canonical_sources/md/who_ictrp/linked_1_ictrp_revisions_document.pdf.md`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=who_ictrp`.
- Optional local section locators: `references/corpus_index/sections/by_source/who_ictrp.jsonl`.

## Unresolved gaps

- Need current verification of ICTRP web-service/crawling/download status.
- Need explicit current data-use restrictions before bulk use.
