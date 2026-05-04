# ACL Rolling Review Authors Source Card v2

```yaml
source_id: acl_arr_authors
source_family: nlp_speech_cs_exemplar_sources
canonical_paths:
  - references/canonical_sources/md/acl_arr_authors/canonical_authors.md
canonical_urls:
  - https://aclrollingreview.org/authors
authority_level: canonical_venue_policy
version_or_access_date: "checked 2026-05-04"
applies_to:
  - ACL Rolling Review author workflow
  - ARR review, response, resubmission, and commitment norms
  - NLP venue-process grounding for ACL-family submissions
not_for:
  - universal survey methodology standards
  - corpus registry or metadata access
  - non-ACL venue policy unless explicitly cross-referenced
  - judging scientific truth from review outcomes
route_relevance:
  - source_audit
  - evidence_grounding
  - survey_writing_prior
  - synthesis_writing
freshness_risk: high because ARR cycles, venue commitments, reviewer obligations, and author-response rules can change.
reuse_or_license_risk: web guidance only; do not redistribute large page excerpts without checking site terms.
qa_status: seed_verified_by_subagent_with_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: ARR provides reviews only; the reviews are not venue-specific decisions, though reviewer standards are those expected for main ACL-family long or short papers.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_arr_authors/canonical_authors.md
  support_type: direct
  verification_note: Use this claim only for ARR process routing, not for acceptance prediction.
  quote_or_locator: canonical_authors.md:66-69
- claim: ARR submissions must follow the submission templates and formatting page linked from the author guidance.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_arr_authors/canonical_authors.md
  support_type: direct
  verification_note: Route exact formatting details to aclpub_formatting.
  quote_or_locator: canonical_authors.md:78-83
- claim: A paper is considered under review at ARR after submission until the meta-review, and the page states it may not be submitted elsewhere during that period.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_arr_authors/canonical_authors.md
  support_type: direct
  verification_note: Verify cycle-specific CFP rules before advising on a live submission.
  quote_or_locator: canonical_authors.md:86-90
- claim: ARR author response is framed mainly around clarifying misunderstandings and factual inaccuracies rather than arguing for acceptance.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_arr_authors/canonical_authors.md
  support_type: direct
  verification_note: Use this for NLP rebuttal or response-process guidance, not for general peer-review methodology.
  quote_or_locator: canonical_authors.md:100-120
- claim: After final reviews and meta-review, authors may revise, commit ARR reviews to an accepting venue, submit to a direct-review venue, or resubmit to ARR, subject to venue rules.
  supporting_canonical_paths:
    - references/canonical_sources/md/acl_arr_authors/canonical_authors.md
  support_type: direct
  verification_note: Check the target venue policy before using this as operational submission advice.
  quote_or_locator: canonical_authors.md:146-163
```

## Operational rules

- Use this card for ACL/ARR process questions involving author obligations, review response, resubmission, and commitment.
- Route formatting details to `aclpub_formatting`; route TACL-specific waiting periods and survey-policy claims to `tacl_submission`.
- For final answers, cite `canonical_authors.md` or the live ARR page.
- Treat ARR as an ACL-family venue process source, not as survey methodology authority.

## Common misuses

- Treating ARR reviews as acceptance decisions.
- Applying ARR dual-submission or commitment rules to unrelated venues without checking the venue CFP.
- Using ARR author guidance as a general rule for all survey or systematic review writing.
- Ignoring cycle-specific updates and venue-specific commitment rules.

## Evidence limits

The local page is broad author guidance. It does not include every current CFP, every target venue's commitment policy, or a complete formatting specification.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=acl_arr_authors`.
- Canonical Markdown: `references/canonical_sources/md/acl_arr_authors/canonical_authors.md`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=acl_arr_authors`.
- Optional local section locators: `references/corpus_index/sections/by_source/acl_arr_authors.jsonl`.

## Unresolved gaps

- Live ARR cycle dates, venue list, and target-venue commitment rules need current verification.
- The local capture does not include linked reviewer guidelines, CFP pages, or OpenReview forms.
