# PRISMA-P Source Card v2

```yaml
source_id: prisma_p
source_family: sr_reporting_and_conduct
canonical_paths:
  - references/canonical_sources/md/prisma_p/canonical_protocols.md
  - references/canonical_sources/md/prisma_p/linked_1_prisma-p-checklist.pdf.md
  - references/canonical_sources/md/prisma_p/linked_2_prisma-p-checklist.docx.md
  - references/canonical_sources/md/prisma_p/linked_3_prisma-p-systrev-checklist.docx.md
canonical_urls:
  - https://www.prisma-statement.org/protocols
  - https://static1.squarespace.com/static/65b880e13b6ca75573dfe217/t/65b9e4128a67f31f64b09aeb/1706681363097/PRISMA-P-checklist.pdf
  - https://static1.squarespace.com/static/65b880e13b6ca75573dfe217/t/65b9e420e49d7a4b0a5fd936/1706681376976/PRISMA-P-checklist.docx
  - https://static1.squarespace.com/static/65b880e13b6ca75573dfe217/t/65b9e40262cf31766c6134bb/1706681346899/PRISMA-P-SystRev-checklist.docx
authority_level: canonical_reporting_guideline
version_or_access_date: "PRISMA-P 2015; local corpus fetched 2026-05-04"
applies_to:
  - reporting systematic review protocols
  - protocol checklist routing
  - protocol registration and amendment reporting fields
not_for:
  - registry platform behavior
  - full systematic-review conduct guidance
  - risk-of-bias tool selection
  - certainty grading methods
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: low for PRISMA-P 2015 checklist content; moderate for current PRISMA website templates or registry-related instructions.
reuse_or_license_risk: The captured checklist states PRISMA-P checklist material is distributed under Creative Commons Attribution Licence 4.0; verify source-specific terms for other linked materials.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: PRISMA-P was published in 2015 to facilitate the development and reporting of systematic review protocols.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_p/canonical_protocols.md
  support_type: direct
  verification_note: Use the official PRISMA protocols page for high-level scope and key document routing.
  quote_or_locator: canonical_protocols.md:46-56; section_ids=prisma_p__canonical_protocols__s0002_prisma_protocols and __s0003_key_documents
- claim: The PRISMA-P checklist contains recommended items to address in a systematic review protocol.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_p/linked_1_prisma-p-checklist.pdf.md
    - references/canonical_sources/md/prisma_p/linked_2_prisma-p-checklist.docx.md
  support_type: direct
  verification_note: Use checklist paths for exact item wording, not the route registry or source card.
  quote_or_locator: linked_1_prisma-p-checklist.pdf.md:10-15; linked_2_prisma-p-checklist.docx.md:6-15; section_ids=prisma_p__linked_1_prisma_p_checklist_pdf__s0002_page_1 and prisma_p__linked_2_prisma_p_checklist_docx__s0002_table_1
- claim: Administrative protocol reporting items include identifying the report as a protocol, update status, registry name/number if registered, author contact/contributions, amendments, support sources, sponsor, and funder role.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_p/linked_1_prisma-p-checklist.pdf.md
    - references/canonical_sources/md/prisma_p/linked_2_prisma-p-checklist.docx.md
  support_type: direct
  verification_note: Registration is a reporting field here; use registry documentation for registry behavior.
  quote_or_locator: linked_1_prisma-p-checklist.pdf.md:15-53; linked_2_prisma-p-checklist.docx.md:16-28; section_ids=prisma_p__linked_1_prisma_p_checklist_pdf__s0002_page_1 and prisma_p__linked_2_prisma_p_checklist_docx__s0002_table_1
- claim: Methods-related PRISMA-P items ask authors to report planned eligibility criteria, information sources, draft search strategy, data management, selection, data collection, data items, outcomes, risk-of-bias methods, synthesis, meta-bias, and confidence in cumulative evidence.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_p/linked_1_prisma-p-checklist.pdf.md
    - references/canonical_sources/md/prisma_p/linked_2_prisma-p-checklist.docx.md
  support_type: direct
  verification_note: Treat these as planned reporting fields, not as a substitute for conduct manuals or appraisal frameworks.
  quote_or_locator: linked_1_prisma-p-checklist.pdf.md:62-80,86-122; linked_2_prisma-p-checklist.docx.md:32-48; section_ids=prisma_p__linked_1_prisma_p_checklist_pdf__s0002_page_1, __s0003_page_2, and prisma_p__linked_2_prisma_p_checklist_docx__s0002_table_1
- claim: The PRISMA-P checklist should be read with the Explanation and Elaboration paper, amendments should be tracked and dated, and the checklist copyright notice states Creative Commons Attribution Licence 4.0.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_p/linked_1_prisma-p-checklist.pdf.md
    - references/canonical_sources/md/prisma_p/linked_2_prisma-p-checklist.docx.md
  support_type: direct
  verification_note: Use this span for license/reuse notes and for avoiding checklist-only overinterpretation.
  quote_or_locator: linked_1_prisma-p-checklist.pdf.md:123-128; linked_2_prisma-p-checklist.docx.md:8-10; section_ids=prisma_p__linked_1_prisma_p_checklist_pdf__s0003_page_2 and prisma_p__linked_2_prisma_p_checklist_docx__s0001_prisma_p_preferred_reporting_items_for_systematic_review_and_meta_analysis_proto
```

## Operational rules

- Use PRISMA-P for protocol-reporting structure and checklist item routing.
- Do not use PRISMA-P alone as a manual for how to conduct the review, select a risk-of-bias tool, or grade certainty.
- Treat PROSPERO and other registries as external systems; PRISMA-P only supports reporting registration name/number when applicable.
- When exact checklist wording matters, verify against the PDF/DOCX checklist or the explanation-and-elaboration paper.

## Common misuses

- Treating PRISMA-P as current registry guidance.
- Treating planned-methods reporting items as evidence that the methods are correct or sufficient.
- Using PRISMA-P to answer final-review reporting questions better handled by PRISMA 2020 or another extension.
- Citing the source card, manifest, or section index instead of the canonical checklist/page.

## Evidence limits

This card is a router aid. Final answers must cite the canonical PRISMA-P Markdown path or official source URL. The checklist records what should be addressed in protocols; it does not replace current conduct manuals, registry documentation, or appraisal/certainty frameworks.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=prisma_p`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=prisma_p`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=prisma_p`.
- Optional local section locators: `references/corpus_index/sections/by_source/prisma_p.jsonl`.

## Unresolved gaps

- The statement and explanation-and-elaboration papers are linked on the official PRISMA page but were not locally converted as full canonical Markdown in this bundle.
- Current behavior of PROSPERO or other protocol registries must be verified from those registry sources, not from PRISMA-P.
