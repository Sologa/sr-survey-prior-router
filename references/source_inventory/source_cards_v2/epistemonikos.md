# Epistemonikos Source Card v2

```yaml
source_id: epistemonikos
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/epistemonikos/canonical_en.md
canonical_urls:
  - https://www.epistemonikos.org/en/
authority_level: canonical_database_api_doc
version_or_access_date: "no page date visible; checked 2026-05-04"
applies_to:
  - evidence-database discovery
  - systematic-review and included-study linkage context
  - source audit for health evidence databases
not_for:
  - normative systematic review writing guidance
  - risk-of-bias assessment
  - certainty grading
  - full-text license determination
route_relevance:
  - general_domain_prior
  - source_audit
  - evidence_grounding
freshness_risk: medium; database size, API availability, language support, and terms can change.
reuse_or_license_risk: page states Creative Commons Attribution 3.0 Unported licensing for Epistemonikos, but data/API terms should still be checked for reuse.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: Epistemonikos presents itself as a health evidence database with systematic reviews curated and annotated by collaborators.
  supporting_canonical_paths:
    - references/canonical_sources/md/epistemonikos/canonical_en.md
  support_type: direct
  verification_note: Use for database-discovery scope only, not methodology authority.
  quote_or_locator: canonical_en.md:61-70
- claim: The page describes interconnected evidence that links articles and evidence answering the same question.
  supporting_canonical_paths:
    - references/canonical_sources/md/epistemonikos/canonical_en.md
  support_type: direct
  verification_note: Use as a route to review-study linkage checks.
  quote_or_locator: canonical_en.md:71-77,85-87
- claim: The page links to an Epistemonikos API and states a Creative Commons Attribution 3.0 Unported license.
  supporting_canonical_paths:
    - references/canonical_sources/md/epistemonikos/canonical_en.md
  support_type: direct
  verification_note: Verify current API and terms before implementation or reuse.
  quote_or_locator: canonical_en.md:114,124-132
```

## Operational rules

- Use Epistemonikos for evidence-database discovery and review-to-included-study linkage context.
- Do not present Epistemonikos as a reporting guideline, conduct manual, appraisal tool, or certainty framework.
- Verify live API and terms before using it in an automated workflow.

## Common misuses

- Treating database coverage claims as proof of exhaustive retrieval.
- Treating review-study links as screening decisions.
- Assuming Creative Commons page text resolves all record-level or linked-content reuse rights.

## Evidence limits

This card supports source routing and high-level database capability claims only. It does not establish methodological correctness, full-text rights, or current API behavior.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=epistemonikos`.
- Canonical capture: `references/canonical_sources/md/epistemonikos/canonical_en.md`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=epistemonikos`.
- Optional local section locator: `references/corpus_index/sections/by_source/epistemonikos.jsonl`.

## Unresolved gaps

- Need current API documentation capture if API automation is planned.
- Need a terms-of-use review for bulk record reuse and linked-content reuse.
