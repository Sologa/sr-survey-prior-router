# PDF, Markdown, and Locator Completeness Audit

Date: 2026-05-05

Scope: `docs/agent_capability_packs/sr-survey-prior-router`.

This audit closes the file-completeness and PDF-to-Markdown checks requested after the
ChatGPT deep review. The review requires route-first source selection, source cards,
document/section indexes, and targeted canonical Markdown loading instead of opening
`references/canonical_sources/md/` by default.

## Repairs Made

- `grade_working_group` linked newsletter: the local
  `linked_2_grade-working-group-newsletter-202409.pdf.pdf` file was a Dropbox HTML
  preview capture. It was recaptured from the Dropbox `dl=1` route as a real 6-page
  PDF, converted to page-level Markdown, and given explicit provenance in the download
  manifest, source manifest, document index, section manifest, and source card.
- `press`: all three manual browser PDF captures were converted from single-block
  Markdown into page-addressable Markdown with `## Page N` headings, and
  `sections/by_source/press.jsonl` was regenerated.
- `cacm_author_guidelines`: all four manual browser PDF captures were converted from
  single-block Markdown into page-addressable Markdown with `## Page N` headings, and
  `sections/by_source/cacm_author_guidelines.jsonl` was regenerated.
- `document_index.jsonl` byte, line, heading, and page-heading statistics were
  synchronized to current Markdown files.
- macOS AppleDouble `._*` sidecars created on the external volume were deleted.

## Final Counts

```json
{
  "download_rows": 254,
  "source_rows": 65,
  "local_corpus_sources": 65,
  "document_rows": 212,
  "section_manifest_rows": 65,
  "section_rows": 4647,
  "actual_pdf_signature_files": 65,
  "issues_count": 0
}
```

The only document-index rows without section rows are the two Papers with Code
`bad_capture` / `do_not_load` redirect-provenance records. They are intentionally
excluded from section locators because agents must not load them as content.

## Validation Results

- All `download_manifest.jsonl` raw and Markdown paths exist.
- All `source_manifest.jsonl` local raw and Markdown paths exist.
- All raw SHA-256 values checked from download/source manifests match the current
  local files.
- All Markdown SHA-256 values present in manifests match the current local files.
- All `local_corpus_index.json` Markdown paths exist.
- All `document_index.jsonl` Markdown paths exist, with synchronized byte, line, and
  heading counts.
- All `section_index_manifest.jsonl` files exist, with synchronized section counts and
  byte counts.
- All section rows point to existing Markdown files with valid line ranges.
- All 65 actual `%PDF-` raw files have Markdown extractions.
- All 65 actual PDFs have at least as many `## Page N` Markdown headings as PDF pages.
- No non-PDF `.pdf` / `.pdf.pdf` raw files remain after excluding deleted AppleDouble
  sidecars.
- `validation/validate_source_cards_v2.py` passes after AppleDouble cleanup.

## Remaining Caveats

- PRESS and CACM remain accepted manual browser captures. The Markdown is now
  page-addressable, but the browser-print captures still include navigation/footer
  artifacts and should keep their manual provenance.
- Cheap `file(1)` MIME sniffing can classify some YAML/JSON/Markdown raw files as
  `text/plain`, `text/xml`, or `text/x-script.python`; this was not treated as a
  missing-file or corruption issue because manifest paths and SHA checks pass.
- Graphify refresh was deferred at the time of this audit, then completed and validated in `validation/graphify_refresh_validation_2026-05-05.md`. Use `validation/source_integrity_tracker.md` for live status.
