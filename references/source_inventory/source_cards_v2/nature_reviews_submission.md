# Nature Reviews Submission Source Card v2

```yaml
source_id: nature_reviews_submission
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/nature_reviews_submission/canonical_preparing-your-submission.md
  - references/canonical_sources/md/nature_reviews_submission/linked_1_natrev-articleformatguide-review.pdf.md
  - references/canonical_sources/md/nature_reviews_submission/linked_2_natrev-articleformatguide-perspective.pdf.md
  - references/canonical_sources/md/nature_reviews_submission/linked_3_natrev-articleformatguide-recommendations.pdf.md
  - references/canonical_sources/md/nature_reviews_submission/linked_4_natrev-articleformatguide-news.pdf.md
canonical_urls:
  - https://www.nature.com/natrevphys/for-authors/preparing-your-submission
  - https://www.nature.com/documents/natrev-articleformatguide-review.pdf
  - https://www.nature.com/documents/natrev-articleformatguide-perspective.pdf
  - https://www.nature.com/documents/natrev-articleformatguide-recommendations.pdf
  - https://www.nature.com/documents/natrev-articleformatguide-news.pdf
authority_level: canonical_venue_policy
version_or_access_date: "official venue guidance; local corpus fetched 2026-05-04"
applies_to:
  - Nature Reviews venue-specific article-type routing
  - review, technical review, perspective, recommendations, and news-format checks
  - venue-norm prior for accessible review writing
not_for:
  - formal systematic review methodology
  - meta-analysis conduct or reporting advice
  - cross-publisher review standards
  - article rights or open-access conclusions without live verification
route_relevance:
  - survey_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: high for article-type availability, commissioning norms, publication route, licensing, and self-archiving rules; verify live venue pages.
reuse_or_license_risk: Nature Reviews content and article-format PDFs are publisher materials; publication route and reuse permissions must be checked against current Nature policies.
qa_status: seed_verified_with_local_canonical_markdown
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: Nature Reviews publishes multiple non-primary article types and provides separate article-format guides.
  supporting_canonical_paths:
    - references/canonical_sources/md/nature_reviews_submission/canonical_preparing-your-submission.md
  support_type: direct
  verification_note: Use this for Nature Reviews article routing and format-guide selection only.
  quote_or_locator: canonical_preparing-your-submission.md:57-85
- claim: The captured Nature Reviews page says proposals are limited to Review-type and Comment-type articles and that the journal does not publish original research, case studies, meta-analyses, or systematic reviews.
  supporting_canonical_paths:
    - references/canonical_sources/md/nature_reviews_submission/canonical_preparing-your-submission.md
  support_type: direct
  verification_note: This is a Nature Reviews venue boundary, not a general statement about review publishing.
  quote_or_locator: canonical_preparing-your-submission.md:119-125
- claim: Nature Reviews articles are written for advanced-undergraduate readers and specialists, with emphasis on accessibility across related disciplines.
  supporting_canonical_paths:
    - references/canonical_sources/md/nature_reviews_submission/canonical_preparing-your-submission.md
  support_type: direct
  verification_note: Supports style, readability, and audience-positioning prior.
  quote_or_locator: canonical_preparing-your-submission.md:99-109
- claim: The Review/Technical Review/Roadmap format guide includes constraints for abstract style, reference density, review criteria, key points, and display items.
  supporting_canonical_paths:
    - references/canonical_sources/md/nature_reviews_submission/linked_1_natrev-articleformatguide-review.pdf.md
  support_type: direct
  verification_note: Format-guide details are venue-specific and may differ across Nature Reviews journals.
  quote_or_locator: linked_1_natrev-articleformatguide-review.pdf.md:14-15,44-63,79-92,264-283
- claim: The captured page describes subscription publication and self-archiving conditions for Nature Reviews articles.
  supporting_canonical_paths:
    - references/canonical_sources/md/nature_reviews_submission/canonical_preparing-your-submission.md
  support_type: direct
  verification_note: Treat publication-route and license details as freshness-sensitive.
  quote_or_locator: canonical_preparing-your-submission.md:123-127
```

## Operational rules

- Use the canonical page to choose the relevant Nature Reviews article type, then open the matching format-guide PDF Markdown.
- Keep Nature Reviews venue expectations separate from cross-domain survey or systematic-review methods.
- Recheck the live journal page before advising on publication route, self-archiving, article types, or proposal process.
- Cite source files directly for format constraints; this card is only a routing aid.

## Common misuses

- Treating Nature Reviews format rules as a universal survey-writing standard.
- Using this source to support systematic-review, meta-analysis, PRISMA, or evidence-synthesis methodology claims.
- Collapsing Review, Perspective, Recommendation, and News guidance into one generic article template.
- Assuming all Nature Reviews journals publish all article types.

## Evidence limits

The local bundle is venue/publisher guidance, partly from a Nature Reviews Physics author page and linked Nature Reviews format PDFs. It does not define review methodology and does not establish current licensing or publication-route facts without live verification.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=nature_reviews_submission`.
- Download rows: `references/canonical_sources/download_manifest.jsonl` with `source_id=nature_reviews_submission`.
- Canonical Markdown: `references/canonical_sources/md/nature_reviews_submission/`.
- Document locators: `references/corpus_index/document_index.jsonl` with `source_id=nature_reviews_submission`.

## Unresolved gaps

- Confirm whether the target Nature Reviews journal follows the same article-type set and format PDFs.
- If used for submission planning, verify current editorial contact, proposal workflow, rights, and self-archiving terms live.
