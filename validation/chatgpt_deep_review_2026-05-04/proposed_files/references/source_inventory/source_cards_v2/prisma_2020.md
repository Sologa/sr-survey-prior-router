# Source card v2: PRISMA 2020

```yaml
source_id: prisma_2020
source_family: sr_reporting_and_conduct
canonical_paths:
  - references/canonical_sources/md/prisma_2020/canonical_prisma-2020.md
  - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
  - references/canonical_sources/md/prisma_2020/subpage_statement_prisma-2020-statement.md
  - references/canonical_sources/md/prisma_2020/subpage_checklist_prisma-2020-checklist.md
  - references/canonical_sources/md/prisma_2020/pmc_bmj_statement_printable_html_pmc8005924.md
canonical_urls:
  - https://www.prisma-statement.org/prisma-2020
  - https://static1.squarespace.com/static/65b880e13b6ca75573dfe217/t/67ad313f1c80aa5235fce0d0/1739403584136/PRISMA_2020_checklist.pdf
authority_level: canonical_reporting_guideline
version_or_access_date: PRISMA 2020; local capture reviewed 2026-05-04
applies_to:
  - reporting completed systematic reviews
  - reporting systematic reviews with or without meta-analysis
  - methods and results reporting completeness checks
not_for:
  - designing the entire conduct method without Cochrane/JBI/manual guidance
  - assessing methodological quality of systematic reviews
  - rating certainty of evidence
  - venue-specific survey-writing advice
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
freshness_risk: low to medium; reporting guideline is stable, but official site/download URLs can change.
reuse_or_license_risk: checklist states CC BY 4.0; still verify source-specific license before redistributing large derived text.
qa_status: draft_v2_example
last_reviewed: 2026-05-04
```

## Key points

```yaml
- claim: "PRISMA 2020 is a reporting guideline for completed systematic review reports, not a full conduct manual."
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/canonical_prisma-2020.md
  support_type: direct
  verification_note: "The PRISMA 2020 page describes the statement paper, checklist, expanded checklist, abstract checklist, and flow diagrams."
  quote_or_locator: "Open canonical_prisma-2020.md and verify the paragraph beginning 'PRISMA 2020 consists of a statement paper...'."

- claim: "A report should identify itself as a systematic review in the title."
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
  support_type: direct
  verification_note: "Checklist item 1 states this requirement."
  quote_or_locator: "Page 1, TITLE / Title / Item 1."

- claim: "The Methods section should report eligibility criteria, information sources, full search strategies, selection process, data collection process, risk-of-bias assessment, synthesis methods, reporting-bias assessment, and certainty assessment."
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
  support_type: direct
  verification_note: "Checklist items 5-15 cover these reporting elements."
  quote_or_locator: "Page 1, METHODS, items 5-15."

- claim: "The Results section should report the search/selection process, ideally using a flow diagram."
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
  support_type: direct
  verification_note: "Checklist item 16a asks for numbers from records identified to included studies, ideally with a flow diagram."
  quote_or_locator: "Page 2, RESULTS / Study selection / Item 16a."

- claim: "PRISMA 2020 asks reports to disclose registration/protocol information, support, competing interests, and availability of data/code/materials."
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md
  support_type: direct
  verification_note: "Checklist items 24a-27 cover these other-information elements."
  quote_or_locator: "Page 2, OTHER INFORMATION, items 24a-27."
```

## Operational rules

1. Use PRISMA 2020 first for reporting-completeness claims about completed systematic reviews.
2. Pair with Cochrane Handbook or JBI Manual for conduct/method-design claims.
3. Pair with GRADE/CERQual for certainty/confidence claims.
4. Pair with PRISMA-S/TARCiS for detailed search/citation-search reporting.
5. For item-level claims, open the checklist Markdown, not only the PRISMA landing page.

## Common misuses

1. Treating PRISMA as proof that a review was well conducted.
2. Treating PRISMA as a substitute for a protocol, conduct manual, or certainty framework.
3. Using an EQUATOR registry page as if it contained the full checklist item wording.
4. Applying PRISMA 2020 unchanged to scoping reviews when PRISMA-ScR is the better reporting source.

## Evidence limits

- PRISMA 2020 supports reporting claims, not full conduct prescriptions.
- The landing page is a locator and overview; the checklist and statement/E&E files are better for item-level evidence.
- Some PRISMA files are partial or linked downloads; verify the specific Markdown path before final answers.

## Verification paths

1. `references/canonical_sources/md/prisma_2020/canonical_prisma-2020.md`
2. `references/canonical_sources/md/prisma_2020/linked_prisma_2020_checklist-ab3g.pdf_prisma_2020_checklist.pdf.md`
3. `references/canonical_sources/download_manifest.jsonl`
4. `references/source_inventory/local_corpus_index.md`

## Unresolved gaps

- Confirm whether all PRISMA linked PDFs/DOCX files convert cleanly after any future retrieval update.
- Add quote-level line or page locators for statement and explanation/elaboration papers after public section indexes are available or rebuilt.
