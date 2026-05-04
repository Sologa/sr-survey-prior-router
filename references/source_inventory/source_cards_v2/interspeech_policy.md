# INTERSPEECH Policy Source Card v2

```yaml
source_id: interspeech_policy
source_family: nlp_speech_cs_exemplar_sources
canonical_paths:
  - references/canonical_sources/md/interspeech_policy/canonical_interspeech-policy.md
  - references/canonical_sources/md/interspeech_policy/linked_1_iscaprivacypolicy.pdf.md
canonical_urls:
  - https://www.isca-speech.org/Interspeech-Policy
authority_level: canonical_venue_policy
version_or_access_date: "checked 2026-05-04"
applies_to:
  - INTERSPEECH originality, copyright, preprint, citation, and no-show policy
  - speech venue policy grounding
  - ISCA event submission boundary checks
not_for:
  - universal survey methodology standards
  - ACL, TACL, or Computational Linguistics policy
  - ISCA Archive search behavior
  - unrestricted paper reuse or bulk corpus rights
route_relevance:
  - source_audit
  - evidence_grounding
  - survey_writing_prior
  - synthesis_writing
freshness_risk: high because conference policy, copyright terms, and no-show rules may change by year or event.
reuse_or_license_risk: policy text is copyright-centered and assigns accepted paper rights to ISCA; do not infer open bulk reuse rights.
qa_status: seed_verified_by_subagent_with_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: INTERSPEECH submissions must be original and not currently submitted to another conference, workshop, or journal during the review process.
  supporting_canonical_paths:
    - references/canonical_sources/md/interspeech_policy/canonical_interspeech-policy.md
  support_type: direct
  verification_note: Check the current year CFP and policy before advising on a live submission.
  quote_or_locator: canonical_interspeech-policy.md:508-510
- claim: Accepted ISCA Event papers should be presented by an author in person, and non-presented papers may be withdrawn from proceedings.
  supporting_canonical_paths:
    - references/canonical_sources/md/interspeech_policy/canonical_interspeech-policy.md
  support_type: direct
  verification_note: Use this for INTERSPEECH/ISCA no-show policy boundaries.
  quote_or_locator: canonical_interspeech-policy.md:512,524-530
- claim: The captured policy states that by submission authors assign rights, title, and interest including copyrights in the manuscript to ISCA, with definitive assignment if accepted.
  supporting_canonical_paths:
    - references/canonical_sources/md/interspeech_policy/canonical_interspeech-policy.md
  support_type: direct
  verification_note: Treat this as a rights-sensitive source and verify the current policy before reuse claims.
  quote_or_locator: canonical_interspeech-policy.md:514-516
- claim: The captured policy permits manuscripts posted in repositories such as arXiv only if authors can transfer rights to ISCA, and requires public repository references to be updated after rejection or acceptance.
  supporting_canonical_paths:
    - references/canonical_sources/md/interspeech_policy/canonical_interspeech-policy.md
  support_type: direct
  verification_note: Use for INTERSPEECH preprint-policy routing only.
  quote_or_locator: canonical_interspeech-policy.md:516-518
- claim: ISCA-endorsed event submissions should refer to peer-reviewed publications; non-peer-reviewed sources should be minimized and footnoted when no peer-reviewed publication is available.
  supporting_canonical_paths:
    - references/canonical_sources/md/interspeech_policy/canonical_interspeech-policy.md
  support_type: direct
  verification_note: This is an ISCA/INTERSPEECH citation policy, not a universal literature-review rule.
  quote_or_locator: canonical_interspeech-policy.md:522
- claim: The linked privacy policy concerns personal-data processing for ISCA members, reviewers, workshop organizers, and grant applicants, not scientific or survey methodology.
  supporting_canonical_paths:
    - references/canonical_sources/md/interspeech_policy/linked_1_iscaprivacypolicy.pdf.md
  support_type: direct
  verification_note: Keep privacy-policy evidence separate from manuscript-policy evidence.
  quote_or_locator: linked_1_iscaprivacypolicy.pdf.md:16-22
```

## Operational rules

- Use this card for INTERSPEECH originality, copyright, preprint, peer-reviewed citation, and no-show policy questions.
- Use `isca_archive` for archive/session/paper discovery, not policy claims.
- Scope survey-writing relevance to speech venue expectations only.
- Cite the canonical policy page or current live policy in final answers.

## Common misuses

- Applying INTERSPEECH policy to ACL, TACL, Computational Linguistics, or non-ISCA venues.
- Treating the citation policy as a universal standard for all surveys.
- Assuming ISCA Archive accessibility grants open reuse rights.
- Ignoring year-specific policy updates.

## Evidence limits

The local capture is a policy page plus a linked privacy policy PDF. It does not include the current year CFP, submission system instructions, or paper-level rights notices.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=interspeech_policy`.
- Canonical Markdown directory: `references/canonical_sources/md/interspeech_policy/`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=interspeech_policy`.
- Optional local section locators: `references/corpus_index/sections/by_source/interspeech_policy.jsonl`.

## Unresolved gaps

- Live current-year INTERSPEECH CFP and submission-system terms should be checked before operational advice.
- The local capture does not define bulk reuse terms for the archive or individual proceedings papers.
