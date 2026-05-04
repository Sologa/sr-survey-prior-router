# IEEE COMST Guidelines Source Card v2

```yaml
source_id: ieee_comst_guidelines
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/ieee_comst_guidelines/canonical_policies-guidelines.md
  - references/canonical_sources/md/ieee_comst_guidelines/linked_2_opsmanual.pdf.md
  - references/canonical_sources/md/ieee_comst_guidelines/official_comsoc_author_kit_author-kit.md
canonical_urls:
  - https://www.comsoc.org/publications/journals/ieee-comst/policies-guidelines
  - https://pspb.ieee.org/images/files/PSPB/opsmanual.pdf
  - https://www.comsoc.org/publications/ieee-comsoc-technical-committees-newsletter/author-kit
authority_level: canonical_venue_policy
version_or_access_date: "official venue guidance; local corpus fetched 2026-05-04"
applies_to:
  - IEEE Communications Surveys and Tutorials venue expectations
  - communications-field survey and tutorial article fit
  - reviewer-facing checks for scope, citations, readability, and audience
not_for:
  - general systematic review methodology
  - qualitative synthesis, appraisal, or certainty frameworks
  - non-communications survey venues without their own instructions
  - current IEEE policy advice without live verification
route_relevance:
  - survey_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: high for venue policy, submission portal, fees, AI-disclosure rules, and IEEE publication-policy changes; verify live pages before submission advice.
reuse_or_license_risk: IEEE and ComSoc policy documents are publisher materials; reuse, templates, figures, and text require current IEEE permission checks.
qa_status: seed_verified_with_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: IEEE Communications Surveys and Tutorials targets generalist readers across communications and communications networking.
  supporting_canonical_paths:
    - references/canonical_sources/md/ieee_comst_guidelines/canonical_policies-guidelines.md
  support_type: direct
  verification_note: Use this for COMST audience-fit and readability expectations only.
  quote_or_locator: canonical_policies-guidelines.md:554-556
- claim: COMST distinguishes tutorial articles from survey articles by purpose and citation strategy.
  supporting_canonical_paths:
    - references/canonical_sources/md/ieee_comst_guidelines/canonical_policies-guidelines.md
  support_type: direct
  verification_note: This is venue-specific but useful for communications survey-vs-tutorial routing.
  quote_or_locator: canonical_policies-guidelines.md:562-564
- claim: COMST asks authors to state the article category and scope in the abstract and introductory section.
  supporting_canonical_paths:
    - references/canonical_sources/md/ieee_comst_guidelines/canonical_policies-guidelines.md
  support_type: direct
  verification_note: This supports article-fit and manuscript-audit checks for COMST submissions.
  quote_or_locator: canonical_policies-guidelines.md:568
- claim: COMST reviewer guidance emphasizes value to readers, tutorial content, comprehensive survey references, scope control, and readability.
  supporting_canonical_paths:
    - references/canonical_sources/md/ieee_comst_guidelines/canonical_policies-guidelines.md
  support_type: direct
  verification_note: Use these as venue-review criteria, not as a universal survey-quality rubric.
  quote_or_locator: canonical_policies-guidelines.md:692-730
- claim: The local bundle includes broader IEEE policy material and a ComSoc author-kit page, but the COMST policy page is the primary source for COMST-specific survey/tutorial claims.
  supporting_canonical_paths:
    - references/canonical_sources/md/ieee_comst_guidelines/canonical_policies-guidelines.md
    - references/canonical_sources/md/ieee_comst_guidelines/linked_2_opsmanual.pdf.md
    - references/canonical_sources/md/ieee_comst_guidelines/official_comsoc_author_kit_author-kit.md
  support_type: indirect
  verification_note: Route COMST-specific article-type claims to the canonical policy page; use broader IEEE/ComSoc files only for their own policy or author-kit claims.
  quote_or_locator: canonical_policies-guidelines.md:542-574,660; official_comsoc_author_kit_author-kit.md:515
```

## Operational rules

- Use this source for communications survey/tutorial venue-fit checks and reviewer-style manuscript audits.
- Keep the tutorial-vs-survey distinction tied to COMST unless another venue explicitly adopts it.
- Recheck current COMST and IEEE pages before advising on submissions, fees, AI disclosure, or policy compliance.
- Prefer `canonical_policies-guidelines.md` for COMST article-type and scope claims.

## Common misuses

- Treating COMST as a cross-domain survey-method standard.
- Applying communications-specific citation and scope expectations to biomedical, social-science, or humanities reviews without caveat.
- Using broader IEEE operations-manual material as if it were COMST-specific author guidance.
- Treating the local failed EIC-guide download as available evidence.

## Evidence limits

The local evidence is official venue and publisher guidance, not a research-method handbook. It supports COMST source routing and venue checks, but not systematic-review conduct, reporting, appraisal, or certainty claims.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=ieee_comst_guidelines`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=ieee_comst_guidelines`.
- Canonical Markdown: `references/canonical_sources/md/ieee_comst_guidelines/`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=ieee_comst_guidelines`.

## Unresolved gaps

- The EIC guide linked from the COMST page failed local capture; reattempt only if that document becomes necessary.
- Confirm current COMST submission portal, fees, length rules, and AI policy before submission-facing use.
