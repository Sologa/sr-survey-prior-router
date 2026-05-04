# Source Cards v2 Batch Validation

Date: 2026-05-04
Status: passed
Artifact type: validation note
Canonical evidence status: not canonical evidence

## Scope

This batch expanded `references/source_inventory/source_cards_v2/` from the initial 6 cards to 26 checked source cards.

New cards added in this batch:

- PRISMA extensions: `prisma_s`, `prisma_scr`, `prisma_p`
- Conduct/manual sources: `cochrane_handbook`, `cochrane_mecir`, `jbi_manual_2024`, `campbell_standards`
- Appraisal/certainty/bias sources: `amstar2`, `robis`, `grade_working_group`, `grade_handbook`, `grade_cerqual`, `rob2`, `robins_i`
- Survey/synthesis reporting sources: `swim`, `entreq`, `rameses_meta_narrative`, `rameses_realist`
- Taxonomy-method sources: `nickerson_taxonomy_2013`, `kundisch_taxonomy_update_2021`

## Subagent Split

- Worker A: PRISMA extension cards.
- Worker B: conduct/manual cards.
- Worker C: appraisal/certainty cards.
- Worker D: survey/synthesis reporting cards.
- Worker E: taxonomy-method cards.
- Worker F: risk-of-bias tool cards.

Each worker wrote a disjoint set of card files and did not commit or push.

## Validation Commands

Run from the skill root:

```sh
python3 -m pip install -r requirements.txt
python3 validation/validate_source_cards_v2.py
python3 validation/validate_graphify_navigation.py
```

Observed result:

```text
source_cards_v2 validation: PASS
checked_cards: 26

graphify navigation validation: PASS
```

## Validator Hardening

This batch also tightened `validation/validate_source_cards_v2.py` to reject:

- duplicate card `source_id` values
- unsupported `support_type` values

The source-card and graphify validators also allow isolated local OMX state sidecars such as `._.omx` while still rejecting pack-content macOS metadata sidecars.

The validator already checks source IDs, filenames, metadata fields, route IDs, canonical path existence, key-point support paths, derivative-path misuse for direct/indirect evidence, and macOS metadata sidecars outside ignored local-state directories.

## Known Gaps Preserved in Cards

- PRISMA-S, PRISMA-ScR, and PRISMA-P have linked official materials that are not all fully converted locally.
- Cochrane linked supplements, MECIR detailed standard text, JBI PDF locators, and Campbell linked checklist coverage may need live/raw verification for fine-grained wording.
- ENTREQ and RAMESES cards are based on local registry-page captures; they should not be used for item-level checklist/standards claims until linked fulltext is captured.
- `grade_handbook` is a partial local bundle and should be paired with newer GRADE Working Group materials for current claims.
- `grade_cerqual` is landing-page-only locally and needs linked published guidance for component-level rules.
- AMSTAR 2 and ROBIS exact form layout should be checked in raw PDFs when layout matters.
- RoB 2 and ROBINS-I local captures are thin entrypoint captures; detailed domains, signaling questions, and judgment algorithms need tool/guidance files before fine-grained use.
- Nickerson has page-only locators and no local license text; Kundisch's card does not enumerate all taxonomy design recommendations item by item.

## Boundary

These cards are derivative routing artifacts. They help agents choose the right canonical Markdown files and locators. They are not canonical evidence for methodology, reporting, tool behavior, or licensing claims.
