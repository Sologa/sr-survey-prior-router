# ISCA Archive Source Card v2

```yaml
source_id: isca_archive
source_family: nlp_speech_cs_exemplar_sources
canonical_paths:
  - references/canonical_sources/md/isca_archive/canonical.md
  - references/canonical_sources/md/isca_archive/linked_1_interspeech_2025_booklet_pdf_booklet.pdf.md
canonical_urls:
  - https://www.isca-archive.org/
authority_level: canonical_database_api_doc
version_or_access_date: "checked 2026-05-04; Interspeech 2025 booklet in local capture"
applies_to:
  - speech conference proceedings discovery
  - ISCA Archive paper/session lookup
  - speech-domain corpus and venue exemplar routing
not_for:
  - universal survey methodology standards
  - open bulk full-text reuse assumptions
  - Interspeech copyright or author policy without interspeech_policy
  - paper quality judgments from archive presence alone
route_relevance:
  - survey_writing_prior
  - source_audit
  - evidence_grounding
  - synthesis_writing
freshness_risk: high because proceedings listings, search interface behavior, and annual booklet contents change.
reuse_or_license_risk: local capture does not establish broad bulk-download or full-text redistribution rights; verify individual paper and ISCA policy pages.
qa_status: seed_verified_by_subagent_with_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The ISCA Archive local capture includes an Interspeech 2025 proceedings/session listing with searchable sessions and paper records.
  supporting_canonical_paths:
    - references/canonical_sources/md/isca_archive/canonical.md
  support_type: direct
  verification_note: Use the archive page as a speech proceedings locator.
  quote_or_locator: canonical.md:6-36
- claim: The ISCA Archive search help supports term conjunction, exact phrase matching with double quotes, case-insensitive search, and optional diacritics matching.
  supporting_canonical_paths:
    - references/canonical_sources/md/isca_archive/canonical.md
  support_type: direct
  verification_note: Use only for local archive search behavior reflected in the capture.
  quote_or_locator: canonical.md:14-27
- claim: The captured Interspeech 2025 booklet is a book of abstracts and includes survey talks, special sessions, review committee, schedule, and author index sections.
  supporting_canonical_paths:
    - references/canonical_sources/md/isca_archive/linked_1_interspeech_2025_booklet_pdf_booklet.pdf.md
  support_type: direct
  verification_note: Treat the booklet as event/proceedings context, not as a methodology standard.
  quote_or_locator: linked_1_interspeech_2025_booklet_pdf_booklet.pdf.md:6-36
- claim: The booklet welcome letter reports Interspeech 2025 as the 26th Interspeech conference and describes record submissions, reviews, and accepted papers.
  supporting_canonical_paths:
    - references/canonical_sources/md/isca_archive/linked_1_interspeech_2025_booklet_pdf_booklet.pdf.md
  support_type: direct
  verification_note: Use this only for event-context claims about the captured booklet.
  quote_or_locator: linked_1_interspeech_2025_booklet_pdf_booklet.pdf.md:40-68
- claim: ISCA Archive is useful as a speech-domain corpus locator, but it does not itself provide survey-writing methodology rules.
  supporting_canonical_paths:
    - references/canonical_sources/md/isca_archive/canonical.md
  support_type: indirect
  verification_note: The canonical archive page lists proceedings/search content, not review-method guidance.
  quote_or_locator: canonical.md:6-36
```

## Operational rules

- Use this source for speech-domain paper, session, proceedings, and event-context discovery.
- Route copyright, originality, preprint, and no-show policy questions to `interspeech_policy`.
- For evidence in final answers, cite the archive page, booklet, or specific paper page/PDF.
- Do not infer bulk reuse rights from archive accessibility.

## Common misuses

- Treating the archive as a methodology authority.
- Treating all accessible archive PDFs as freely reusable for redistribution.
- Assuming archive search behavior is a stable public API.
- Inferring paper quality or survey relevance from proceedings presence alone.

## Evidence limits

The local capture is centered on the archive landing/session listing and an Interspeech 2025 booklet. It does not include a public API specification or comprehensive rights terms.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=isca_archive`.
- Canonical Markdown directory: `references/canonical_sources/md/isca_archive/`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=isca_archive`.
- Optional local section locators: `references/corpus_index/sections/by_source/isca_archive.jsonl`.

## Unresolved gaps

- No official public API was verified in the local source card context.
- Paper-level licenses and download/reuse terms need specific verification.
