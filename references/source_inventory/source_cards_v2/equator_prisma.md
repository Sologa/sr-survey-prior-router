# EQUATOR PRISMA Source Card v2

```yaml
source_id: equator_prisma
source_family: scholarly_databases_and_apis
canonical_paths:
  - references/canonical_sources/md/equator_prisma/canonical_prisma.md
  - references/canonical_sources/md/equator_prisma/linked_1_prisma_2020_checklist.docx.md
  - references/canonical_sources/md/equator_prisma/linked_2_prisma_2020_checklist.pdf.md
  - references/canonical_sources/md/equator_prisma/linked_3_prisma_2020_expanded_checklist.pdf.md
  - references/canonical_sources/md/equator_prisma/linked_4_prisma_2020_italian.pdf.md
canonical_urls:
  - https://www.equator-network.org/reporting-guidelines/prisma/
authority_level: locator_only
version_or_access_date: "record last updated 2025-02-06; checked 2026-05-04"
applies_to:
  - locating the EQUATOR registry record for PRISMA 2020
  - monitoring PRISMA links, bibliographic references, history, and translations
not_for:
  - replacing primary PRISMA source rows for reporting evidence
  - review conduct methodology
  - appraisal or certainty grading
  - database API behavior
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: medium; registry links and update dates can change, so verify the live EQUATOR record when link freshness matters.
reuse_or_license_risk: EQUATOR registry text and linked PRISMA files may have different reuse terms; verify the primary linked source before redistribution.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The EQUATOR record identifies PRISMA 2020 as a reporting guideline for systematic reviews and meta-analyses.
  supporting_canonical_paths:
    - references/canonical_sources/md/equator_prisma/canonical_prisma.md
  support_type: locator_only
  verification_note: Use this as a registry locator; cite `prisma_2020` canonical paths for PRISMA reporting claims.
  quote_or_locator: canonical_prisma.md:53-58
- claim: The EQUATOR record links to PRISMA 2020 checklist, expanded checklist, Shiny App, statement, flow diagram, translations, and related extensions.
  supporting_canonical_paths:
    - references/canonical_sources/md/equator_prisma/canonical_prisma.md
  support_type: locator_only
  verification_note: Treat linked files as pointers unless independently routed through the primary PRISMA source row.
  quote_or_locator: canonical_prisma.md:59-85,92-100,119-167
- claim: The local EQUATOR record states that the record was last updated on February 6, 2025.
  supporting_canonical_paths:
    - references/canonical_sources/md/equator_prisma/canonical_prisma.md
  support_type: direct
  verification_note: Use only for the local registry-record date; verify live EQUATOR before relying on currency.
  quote_or_locator: canonical_prisma.md:191
```

## Operational rules

- Use `equator_prisma` to find or audit the EQUATOR registry record for PRISMA.
- Use `prisma_2020` for PRISMA statement/checklist evidence, not this registry card.
- Use extension-specific source IDs for PRISMA-P, PRISMA-S, PRISMA-ScR, or other extension claims.

## Common misuses

- Treating EQUATOR as the primary PRISMA methodology authority.
- Merging EQUATOR-linked checklist captures into `prisma_2020` without checking provenance.
- Inferring review conduct requirements from a registry listing.

## Evidence limits

This card is mostly locator-only. The EQUATOR record can support statements about the registry entry and its links, but not primary reporting-item interpretations.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=equator_prisma`.
- Registry capture: `references/canonical_sources/md/equator_prisma/canonical_prisma.md`.
- Linked local captures under `references/canonical_sources/md/equator_prisma/`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=equator_prisma`.
- Optional local section locators: `references/corpus_index/sections/by_source/equator_prisma.jsonl`.

## Unresolved gaps

- Need live-link verification for registry currency when using EQUATOR as an update monitor.
- Primary PRISMA evidence should remain routed through `prisma_2020` and extension-specific cards.
