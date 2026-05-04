# PRISMA 2020 Source Card v2

```yaml
source_id: prisma_2020
source_family: sr_reporting_and_conduct
canonical_paths:
  - references/canonical_sources/md/prisma_2020/canonical_prisma-2020.md
  - references/canonical_sources/md/prisma_2020/pmc_bmj_statement_printable_html_pmc8005924.md
  - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
  - references/canonical_sources/md/prisma_2020/subpage_checklist_prisma-2020-checklist.md
canonical_urls:
  - https://www.prisma-statement.org/prisma-2020
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC8005924/?report=printable
authority_level: canonical_reporting_guideline
version_or_access_date: "PRISMA 2020; local corpus fetched 2026-05-04"
applies_to:
  - systematic review reporting
  - PRISMA 2020 checklist and flow-diagram routing
not_for:
  - selecting review conduct methods
  - risk-of-bias assessment
  - certainty or quality appraisal
  - database search API behavior
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: low for PRISMA 2020 core reporting guidance; verify newer extensions or updated templates for specialized review types.
reuse_or_license_risk: PRISMA and publisher/open-access terms apply; verify source-specific license text before redistributing large excerpts or raw files.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: PRISMA 2020 is a reporting guideline bundle with statement, checklist, expanded checklist, abstracts checklist, and flow diagrams.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/canonical_prisma-2020.md
  support_type: direct
  verification_note: Open the official PRISMA 2020 page after selecting source_id=prisma_2020.
  quote_or_locator: canonical_prisma-2020.md:46-50; section_id=prisma_2020__canonical_prisma_2020__s0002_prisma_2020
- claim: PRISMA 2020 supports reporting claims; it is not a conduct-method or methodological-quality appraisal manual.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/pmc_bmj_statement_printable_html_pmc8005924.md
  support_type: direct
  verification_note: Use the statement article for scope boundaries before making method/conduct claims.
  quote_or_locator: pmc_bmj_statement_printable_html_pmc8005924.md:470-472,498,526
- claim: PRISMA checklist items cover title, methods, results, and other-information reporting fields.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
  support_type: direct
  verification_note: Use checklist page sections for exact item wording.
  quote_or_locator: title lines 17-22, methods lines 39-117, results item 16a lines 130-135, other information lines 195-222; section_ids=prisma_2020__linked_prisma_2020_checklist_ab3g_pdf_prisma_2020_checklist_pdf__s0002_page_1 and __s0003_page_2
- claim: The checklist conversion records CC BY 4.0 license text for the checklist material.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
    - references/canonical_sources/md/prisma_2020/subpage_checklist_prisma-2020-checklist.md
  support_type: direct
  verification_note: Verify license/reuse text in the specific checklist file used.
  quote_or_locator: checklist PDF lines 225-226; checklist subpage line 58
```

## Operational rules

- Use PRISMA 2020 for SR reporting structure, checklist-item wording, and flow-diagram routing.
- Do not use PRISMA 2020 alone to justify search strategy conduct, risk-of-bias judgments, certainty grading, or review eligibility decisions.
- For citation-search reporting, route separately to `prisma_s`; do not cite this PRISMA 2020 card as PRISMA-S/TARCiS evidence.
- For specialized review types, check PRISMA extensions before treating PRISMA 2020 as sufficient.

## Common misuses

- Treating PRISMA as a complete manual for how to conduct a review.
- Treating PRISMA checklist item presence as evidence that a review's methods were correct.
- Citing the source card, route registry, or section index instead of the canonical checklist/statement text.

## Evidence limits

This card is a router aid. Final answers must cite canonical PRISMA paths or the official source URL. Split section indexes are locator-only and may not be present in the GitHub review surface.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=prisma_2020`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=prisma_2020`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=prisma_2020`.
- Optional local section locators: `references/corpus_index/sections/by_source/prisma_2020.jsonl`.

## Unresolved gaps

- Exact template/flow-diagram formatting should be checked in the original downloaded template when layout matters.
- Extension-specific reporting claims need the relevant PRISMA extension source card, not only this card.
