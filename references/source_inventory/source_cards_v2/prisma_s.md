# PRISMA-S Source Card v2

```yaml
source_id: prisma_s
source_family: sr_reporting_and_conduct
canonical_paths:
  - references/canonical_sources/md/prisma_s/canonical_prisma-s.md
  - references/canonical_sources/md/prisma_s/linked_1_protocol-prisma-s-delphi.pdf.md
  - references/canonical_sources/md/prisma_s/linked_2_tarcis_checklist_for_terminology_and_reporting_of_citation_searching.docx.md
  - references/canonical_sources/md/prisma_s/linked_3_tarcis_checklist_for_terminology_and_reporting_of_citation_searching.pdf.md
canonical_urls:
  - https://www.equator-network.org/reporting-guidelines/prisma-s/
  - https://www.equator-network.org/wp-content/uploads/2009/02/Protocol-PRISMA-S-Delphi.pdf
  - https://ub.unibas.ch/fileadmin/user_upload/universitaetsbibliothek/Universitaetsbibliothek/5_Standorte/UB_Medizin/TARCiS/TARCiS_Checklist_for_Terminology_and_Reporting_of_Citation_Searching.docx
  - https://ub.unibas.ch/fileadmin/user_upload/universitaetsbibliothek/Universitaetsbibliothek/5_Standorte/UB_Medizin/TARCiS/TARCiS_Checklist_for_Terminology_and_Reporting_of_Citation_Searching.pdf
authority_level: canonical_reporting_guideline
version_or_access_date: "PRISMA-S 2021; EQUATOR record last updated 2025-02-06; local corpus fetched 2026-05-04"
applies_to:
  - reporting literature searches in systematic reviews
  - search reporting provenance and reproducibility checks
  - citation-search terminology/reporting when routed to the bundled TARCiS material
not_for:
  - designing a search strategy from scratch
  - database-specific search syntax advice
  - risk-of-bias assessment
  - certainty or methodological quality appraisal
  - final PRISMA-S checklist item wording unless the linked checklist itself is opened
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: low-to-moderate; the EQUATOR record is dated 2025-02-06, but the locally captured linked PRISMA-S PDF is a development protocol rather than the final checklist.
reuse_or_license_risk: PRISMA-S full-text/checklist and TARCiS materials may have separate terms; verify the specific linked source before redistributing large excerpts or raw files.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: PRISMA-S is an extension to PRISMA for reporting literature searches in systematic reviews.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_s/canonical_prisma-s.md
  support_type: direct
  verification_note: Use the official EQUATOR record for source scope before making PRISMA-S claims.
  quote_or_locator: canonical_prisma-s.md:53-59,63-75; section_id=prisma_s__canonical_prisma_s__s0003_prisma_s_an_extension_to_the_prisma_statement_for_reporting_literature_searches_
- claim: The EQUATOR record classifies PRISMA-S as a reporting guideline acronym for systematic reviews, meta-analyses, reviews, HTA, and overviews, applying to procedure/method sections.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_s/canonical_prisma-s.md
  support_type: direct
  verification_note: Keep the claim at reporting-scope level; do not convert it into a search-conduct manual claim.
  quote_or_locator: canonical_prisma-s.md:140-146; section_id=prisma_s__canonical_prisma_s__s0003_prisma_s_an_extension_to_the_prisma_statement_for_reporting_literature_searches_
- claim: The captured PRISMA-S protocol supports the development rationale for a checklist, including reproducible reporting of search strategies, but it is not the final checklist text.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_s/linked_1_protocol-prisma-s-delphi.pdf.md
  support_type: direct
  verification_note: Use the protocol for development rationale only; open the final checklist or guideline article for checklist item wording.
  quote_or_locator: linked_1_protocol-prisma-s-delphi.pdf.md:10,27-38,57-63; section_ids=prisma_s__linked_1_protocol_prisma_s_delphi_pdf__s0002_page_1 and __s0003_page_2
- claim: The captured TARCiS material is an adjunct for terminology and reporting of citation searching, including recommended terms and reporting items such as seed references, search direction, search dates, tools, deduplication, screening method, and search results.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_s/canonical_prisma-s.md
    - references/canonical_sources/md/prisma_s/linked_3_tarcis_checklist_for_terminology_and_reporting_of_citation_searching.pdf.md
  support_type: direct
  verification_note: Treat TARCiS as citation-search reporting support, not as a replacement for PRISMA-S checklist verification.
  quote_or_locator: canonical_prisma-s.md:152-154; linked_3_tarcis_checklist_for_terminology_and_reporting_of_citation_searching.pdf.md:10-37,38-80; section_id=prisma_s__linked_3_tarcis_checklist_for_terminology_and_reporting_of_citation_searching_pdf__s0002_page_1
```

## Operational rules

- Use PRISMA-S when the task asks how to report systematic-review literature searches or audit search-reporting reproducibility.
- Use the protocol only for development rationale and scope; verify final checklist wording in the linked checklist or guideline article before citing specific PRISMA-S items.
- Use TARCiS only for citation-search terminology/reporting support after noting that it is an adjunct linked from the PRISMA-S record.
- Route conduct questions about designing comprehensive searches to Cochrane, JBI, PRESS, database documentation, or another conduct/search-method source as appropriate.

## Common misuses

- Treating PRISMA-S as a database-search construction manual.
- Treating the locally captured development protocol as the final PRISMA-S checklist.
- Treating TARCiS citation-search guidance as the full PRISMA-S extension.
- Citing the source card, manifest, or section index instead of the canonical Markdown span or official source.

## Evidence limits

This card is a router aid. Final answers must cite the canonical PRISMA-S/TARCiS Markdown path or official source URL. The local bundle has the EQUATOR record, development protocol, and TARCiS files; it does not locally capture the PRISMA-S OSF checklist files named on the EQUATOR page.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=prisma_s`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=prisma_s`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=prisma_s`.
- Optional local section locators: `references/corpus_index/sections/by_source/prisma_s.jsonl`.

## Unresolved gaps

- The final PRISMA-S checklist files are linked from the EQUATOR record but are not present in the local canonical Markdown bundle reviewed for this card.
- License/reuse terms should be checked in the specific PRISMA-S article/checklist or TARCiS source before reuse beyond short grounded excerpts.
