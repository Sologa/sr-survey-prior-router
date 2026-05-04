# ACLPUB Formatting Source Card v2

```yaml
source_id: aclpub_formatting
source_family: nlp_speech_cs_exemplar_sources
canonical_paths:
  - references/canonical_sources/md/aclpub_formatting/canonical_formatting.html.md
canonical_urls:
  - https://acl-org.github.io/ACLPUB/formatting.html
authority_level: canonical_venue_policy
version_or_access_date: "checked 2026-05-04"
applies_to:
  - ACL conference paper formatting
  - ACL review and final-version PDF preparation
  - NLP venue formatting checks for manuscripts targeting ACL-family proceedings
not_for:
  - universal survey methodology standards
  - deciding scientific contribution or inclusion criteria
  - non-ACL venues without target-CFP confirmation
  - paper corpus licensing
route_relevance:
  - source_audit
  - evidence_grounding
  - survey_writing_prior
  - synthesis_writing
freshness_risk: high because ACL style files, page limits, CFP exceptions, and publication-chair requirements can change by venue and year.
reuse_or_license_risk: formatting guidance only; style files and linked assets may have separate terms.
qa_status: seed_verified_by_subagent_with_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: ACLPUB formatting guidance applies to ACL conference review versions and accepted final versions, and authors are required to follow the specifications.
  supporting_canonical_paths:
    - references/canonical_sources/md/aclpub_formatting/canonical_formatting.html.md
  support_type: direct
  verification_note: Use this for ACL formatting compliance, not survey methodology.
  quote_or_locator: canonical_formatting.html.md:54-60
- claim: ACL provides LaTeX and Microsoft Word style files and strongly recommends using them for ACL proceedings.
  supporting_canonical_paths:
    - references/canonical_sources/md/aclpub_formatting/canonical_formatting.html.md
  support_type: direct
  verification_note: Verify current style files from the linked ACL style repository before live submission.
  quote_or_locator: canonical_formatting.html.md:78-83
- claim: The captured guidance states long and short paper content limits for review and final versions, while warning that workshops may set different rules and the CFP is authoritative.
  supporting_canonical_paths:
    - references/canonical_sources/md/aclpub_formatting/canonical_formatting.html.md
  support_type: direct
  verification_note: Always check the specific CFP before applying page limits.
  quote_or_locator: canonical_formatting.html.md:84-95
- claim: Review versions should be self-contained and should not refer reviewers to unavailable documents, code, or data resources for further detail.
  supporting_canonical_paths:
    - references/canonical_sources/md/aclpub_formatting/canonical_formatting.html.md
  support_type: direct
  verification_note: Use this only for ACL review-version preparation.
  quote_or_locator: canonical_formatting.html.md:88-92
- claim: ACLPUB includes concrete PDF, A4 page-size, font, margin, and metadata requirements.
  supporting_canonical_paths:
    - references/canonical_sources/md/aclpub_formatting/canonical_formatting.html.md
  support_type: direct
  verification_note: Use the canonical page for exact formatting checks.
  quote_or_locator: canonical_formatting.html.md:96-119,121-205
```

## Operational rules

- Use this source for ACL-family formatting and submission-prep questions.
- For ARR author process, route to `acl_arr_authors`; for TACL, route to `tacl_submission`.
- Check the target CFP first when the page mentions workshop or venue-specific exceptions.
- Do not use this formatting page as evidence for research methods, survey quality, or corpus rights.

## Common misuses

- Applying ACL conference page limits to TACL, Computational Linguistics, or non-ACL venues.
- Treating formatting compliance as evidence of scientific quality.
- Treating this page as a survey-writing method source.
- Ignoring year-specific CFP overrides.

## Evidence limits

The card covers a captured formatting page only. It does not include all linked style files, target-conference CFPs, or publication-chair instructions.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=aclpub_formatting`.
- Canonical Markdown: `references/canonical_sources/md/aclpub_formatting/canonical_formatting.html.md`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=aclpub_formatting`.
- Optional local section locators: `references/corpus_index/sections/by_source/aclpub_formatting.jsonl`.

## Unresolved gaps

- Current ACL style-file repository contents are not summarized here.
- Venue CFPs may override or refine limits and must be checked separately.
