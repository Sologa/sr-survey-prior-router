# PRISMA Extensions Source Card v2

```yaml
source_id: prisma_extensions
source_family: sr_reporting_and_conduct
canonical_paths:
  - references/canonical_sources/md/prisma_extensions/canonical_extensions.md
  - references/canonical_sources/md/prisma_extensions/linked_1_prisma_register_extension_form.docx.md
canonical_urls:
  - https://www.prisma-statement.org/extensions
authority_level: canonical_reporting_guideline
version_or_access_date: "no page date visible; checked 2026-05-04"
applies_to:
  - routing to official PRISMA reporting extensions
  - identifying extension-specific reporting guidance for specialized systematic reviews
not_for:
  - generic systematic review conduct rules by itself
  - risk-of-bias assessment
  - certainty grading
  - database or registry API behavior
route_relevance:
  - sr_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: medium; extension inventory and under-development list can change, so verify the live PRISMA extensions page before claiming completeness.
reuse_or_license_risk: mixed extension pages and linked papers may have different hosts and licenses; verify the specific extension material before redistributing excerpts.
qa_status: seed_verified_by_subagent_with_local_locators
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The PRISMA extensions page says official PRISMA extensions cover reporting aspects not captured in the main PRISMA statement.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_extensions/canonical_extensions.md
  support_type: direct
  verification_note: Use the official extensions page before selecting an extension-specific reporting source.
  quote_or_locator: canonical_extensions.md:46-49
- claim: The local page lists extensions including abstracts, diagnostic test accuracy, harms, individual participant data, living systematic reviews, network meta-analyses, protocols, scoping reviews, and search.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_extensions/canonical_extensions.md
  support_type: direct
  verification_note: Treat the list as a routing aid; open the extension-specific source before making item-level claims.
  quote_or_locator: canonical_extensions.md:50-99
- claim: New PRISMA extension proposals are reviewed by the PRISMA Executive against approval criteria.
  supporting_canonical_paths:
    - references/canonical_sources/md/prisma_extensions/canonical_extensions.md
    - references/canonical_sources/md/prisma_extensions/linked_1_prisma_register_extension_form.docx.md
  support_type: direct
  verification_note: Use only for extension-development context, not for review conduct rules.
  quote_or_locator: canonical_extensions.md:146-148; linked_1_prisma_register_extension_form.docx.md:8-10
```

## Operational rules

- Use this card to decide whether a specialized PRISMA extension should be opened before applying generic PRISMA 2020 reporting guidance.
- Route item-level claims to the specific extension document or to the existing extension-specific card when one exists, such as `prisma_p`, `prisma_s`, or `prisma_scr`.
- Do not use this extension index as a substitute for Cochrane, JBI, GRADE, AMSTAR, ROB, or database documentation.

## Common misuses

- Treating the extensions index as a conduct manual.
- Claiming that every extension in the current live ecosystem is captured locally without checking the live page.
- Citing this card or the extension index for details that only appear in a linked extension paper or checklist.

## Evidence limits

This card establishes extension routing only. It does not provide full reporting-item text for each extension and does not validate whether a particular review type requires a given extension.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=prisma_extensions`.
- Canonical page: `references/canonical_sources/md/prisma_extensions/canonical_extensions.md`.
- Extension registration form: `references/canonical_sources/md/prisma_extensions/linked_1_prisma_register_extension_form.docx.md`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=prisma_extensions`.
- Optional local section locators: `references/corpus_index/sections/by_source/prisma_extensions.jsonl`.

## Unresolved gaps

- Extension-specific details still need separate canonical documents or source cards.
- The local extension list may lag behind the live PRISMA site.
