# OpenAlex Snapshot Source Card v2

```yaml
source_id: openalex_snapshot
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/openalex_snapshot/canonical_snapshot_format_manifest_url_snapshot-format_9050c8de.md
  - references/canonical_sources/md/openalex_snapshot/official_snapshot_data_format_snapshot-format.md
  - references/canonical_sources/md/openalex_snapshot/official_api_overview_introduction.md
canonical_urls:
  - https://developers.openalex.org/download/snapshot-format
  - https://developers.openalex.org/api-reference/introduction
authority_level: canonical_database_api_doc
version_or_access_date: "official docs; local corpus fetched 2026-05-04"
applies_to:
  - OpenAlex bulk snapshot routing
  - snapshot storage-format and update-mechanics checks
  - metadata corpus infrastructure planning
not_for:
  - systematic review reporting guidance
  - review conduct methodology
  - appraisal or certainty grading
  - guaranteed full-text or PDF access
route_relevance:
  - general_domain_prior
  - evidence_grounding
  - source_audit
freshness_risk: high for snapshot size, cadence, S3 layout, API examples, and operational download mechanics; verify live docs before implementation.
reuse_or_license_risk: OpenAlex snapshot reuse and linked-content reuse are separate; verify current OpenAlex terms and downstream source licenses.
qa_status: partial_seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: OpenAlex snapshot data is stored in Amazon S3 and uses gzip-compressed JSON Lines files with one entity per line.
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex_snapshot/official_snapshot_data_format_snapshot-format.md
  support_type: direct
  verification_note: Treat this as operational documentation that can change.
  quote_or_locator: official_snapshot_data_format_snapshot-format.md:86; section_id=openalex_snapshot__official_snapshot_data_format_snapshot_format__s0004_documentation_index
- claim: The snapshot bucket uses entity-type prefixes such as works, authors, sources, institutions, topics, publishers, and funders.
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex_snapshot/official_snapshot_data_format_snapshot-format.md
  support_type: direct
  verification_note: Verify current entity list before building a downloader.
  quote_or_locator: official_snapshot_data_format_snapshot-format.md:91-164; section_id=openalex_snapshot__official_snapshot_data_format_snapshot_format__s0004_documentation_index
- claim: Snapshot records are partitioned by updated_date, enabling incremental update logic.
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex_snapshot/official_snapshot_data_format_snapshot-format.md
  support_type: direct
  verification_note: Use the official snapshot docs for current update mechanics.
  quote_or_locator: official_snapshot_data_format_snapshot-format.md:166-170,201-224; section_ids=openalex_snapshot__official_snapshot_data_format_snapshot_format__s0004_documentation_index, __s0010_publishers
- claim: The captured API overview includes entity endpoint examples that can help route metadata lookup work.
  supporting_canonical_paths:
    - references/canonical_sources/md/openalex_snapshot/official_api_overview_introduction.md
  support_type: direct
  verification_note: API examples are freshness-sensitive and should be checked live before implementation.
  quote_or_locator: official_api_overview_introduction.md:155-464; section_ids=openalex_snapshot__official_api_overview_introduction__s0006_documentation_index, __s0007_by_doi_get_works_https_doi_org_10_7717_peerj_4375_get_works_doi_10_7717_peerj_43
```

## Operational rules

- Use this card for bulk snapshot/storage questions, not general OpenAlex API homepage claims.
- Verify current S3 paths, snapshot size, update cadence, and authentication/access expectations before implementation.
- Keep OpenAlex metadata separate from full-text/PDF availability.
- Keep OpenAlex discovery infrastructure separate from SR methodology authorities.

## Common misuses

- Treating the snapshot as a full-text corpus.
- Treating snapshot format as stable without live verification.
- Combining this source ID with `openalex` in one source card.

## Evidence limits

The local source row is partial: the manifest includes skipped broad/license-constrained attempts plus later downloaded docs. Use this card for routing and preliminary operational planning only until current docs are checked for implementation work.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=openalex_snapshot`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=openalex_snapshot`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=openalex_snapshot`.
- Optional local section locators: `references/corpus_index/sections/by_source/openalex_snapshot.jsonl`.

## Unresolved gaps

- Confirm current snapshot availability, size, terms, and paid/free access details before any downloader or storage-cost decision.
- Decide whether API-overview captures should remain under `openalex_snapshot` or be split in a future inventory cleanup.
