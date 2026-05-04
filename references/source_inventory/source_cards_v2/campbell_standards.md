# Campbell Standards Source Card v2

```yaml
source_id: campbell_standards
source_family: sr_reporting_and_conduct
canonical_paths:
  - references/canonical_sources/md/campbell_standards/canonical_standards.md
canonical_urls:
  - https://www.campbellcollaboration.org/methods/standards/
authority_level: canonical_conduct_manual
version_or_access_date: "living document; local corpus fetched 2026-05-04"
applies_to:
  - Campbell protocols, reviews, and updates
  - Campbell Systematic Reviews journal submission standards
  - social-policy evidence synthesis standards when Campbell scope is appropriate
not_for:
  - primary biomedical SR conduct guidance
  - treating Campbell journal requirements as universal SR rules
  - replacing PRISMA 2020 reporting guidance
  - assuming analyzed-data guidance applies to protocols, reviews without meta-analysis, or qualitative syntheses
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: high because Campbell says the Standards are a living document updated periodically.
reuse_or_license_risk: Campbell and linked checklist/document terms apply; verify before redistributing standards or checklist text.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-04"
```

## Key points

```yaml
- claim: Campbell Standards are based on MECCIR and PRISMA 2020 reporting standards and include seven main sections with 35 items.
  supporting_canonical_paths:
    - references/canonical_sources/md/campbell_standards/canonical_standards.md
  support_type: direct
  verification_note: Use the Campbell standards page for source role, then open linked checklist material for item wording.
  quote_or_locator: canonical_standards.md:20-22; section_id=campbell_standards__canonical_standards__s0002_standards_for_reviews
- claim: Campbell checklist items are mandatory for a protocol, review, or update to be published in the Campbell Systematic Reviews journal.
  supporting_canonical_paths:
    - references/canonical_sources/md/campbell_standards/canonical_standards.md
  support_type: direct
  verification_note: Keep this as a Campbell publication-standard claim, not a universal SR rule.
  quote_or_locator: canonical_standards.md:22-24; section_id=campbell_standards__canonical_standards__s0002_standards_for_reviews
- claim: Campbell notes that guidance related to analyzed data may not be relevant for protocols, reviews without meta-analysis, or reviews with qualitative syntheses.
  supporting_canonical_paths:
    - references/canonical_sources/md/campbell_standards/canonical_standards.md
  support_type: direct
  verification_note: Preserve this boundary before applying analyzed-data checklist items.
  quote_or_locator: canonical_standards.md:22; section_id=campbell_standards__canonical_standards__s0002_standards_for_reviews
- claim: Authors must submit the checklist affirming adherence to Campbell Standards when submitting a protocol or review for editorial processing.
  supporting_canonical_paths:
    - references/canonical_sources/md/campbell_standards/canonical_standards.md
  support_type: direct
  verification_note: Use this for Campbell editorial-process claims only.
  quote_or_locator: canonical_standards.md:24; section_id=campbell_standards__canonical_standards__s0002_standards_for_reviews
- claim: Campbell Standards are a living document that will be updated periodically considering new evidence.
  supporting_canonical_paths:
    - references/canonical_sources/md/campbell_standards/canonical_standards.md
  support_type: direct
  verification_note: Recheck the live Campbell page before relying on current item counts or checklist requirements.
  quote_or_locator: canonical_standards.md:26; section_id=campbell_standards__canonical_standards__s0002_standards_for_reviews
```

## Operational rules

- Use Campbell Standards for Campbell protocols, reviews, updates, and Campbell Systematic Reviews journal requirements.
- Treat MECCIR and PRISMA 2020 as upstream standards named by Campbell, but route exact MECIR or PRISMA claims to those source IDs.
- Do not apply analyzed-data guidance blindly to protocols, no-meta-analysis reviews, or qualitative syntheses.
- Verify the live Campbell page before current compliance checks because the standards are living.

## Common misuses

- Treating Campbell mandatory checklist items as universal requirements for all systematic reviews.
- Using Campbell as the primary biomedical SR conduct manual instead of Cochrane, JBI, or a domain-specific authority.
- Citing Campbell for exact PRISMA 2020 wording rather than the PRISMA source.

## Evidence limits

The local Campbell capture is a short standards landing page. It supports high-level source role, mandatory Campbell submission boundary, and freshness-risk claims, but detailed checklist-item wording requires the linked checklist or official standards document.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=campbell_standards`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=campbell_standards`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=campbell_standards`.
- Optional local section locators: `references/corpus_index/sections/by_source/campbell_standards.jsonl`.

## Unresolved gaps

- The local canonical Markdown does not include the full linked checklist contents.
- The source page does not expose a visible publication date beyond living-document language in the captured Markdown.
