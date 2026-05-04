# State-of-Art Review 2022 Source Card v2

```yaml
source_id: state_of_art_review_2022
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md
canonical_urls:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC9582072/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC9582072/?report=xml
authority_level: peer_reviewed_method_paper
version_or_access_date: "2022 article; article body recaptured from PMC on 2026-05-05"
applies_to:
  - state-of-the-art review methodology
  - survey-writing prior when the task explicitly asks for SotA review framing
  - source-audit examples of repaired bad captures
not_for:
  - systematic review conduct
  - scoping-review reporting
  - generic narrative-review rules
  - claims that every literature review should follow the SotA six-stage method
route_relevance:
  - survey_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: low for the 2022 article text; recapture route may need browser/OAI/BioC fallback if PMC landing HTML is challenge-gated.
reuse_or_license_risk: PMC page states CC BY 4.0; verify third-party material separately.
qa_status: article_body_recaptured_2026_05_05
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The local canonical Markdown now contains article body text rather than only a browser-check page.
  supporting_canonical_paths:
    - references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md
  support_type: direct
  verification_note: The recaptured file includes citation metadata, abstract, methods, results, SotA methodology, discussion, and references.
  quote_or_locator: canonical_pmc9582072.md:1-27 and 75-137
- claim: The article is a peer-reviewed method paper for state-of-the-art reviews, not a universal survey or SR method.
  supporting_canonical_paths:
    - references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md
  support_type: direct
  verification_note: The abstract and discussion frame the paper as a SotA review methodology and contrast it with systematic, scoping, and critical reviews.
  quote_or_locator: canonical_pmc9582072.md:20-27 and 133-137
- claim: The paper uses both title wording "six-step" and body wording "six-stage"; preserve that distinction.
  supporting_canonical_paths:
    - references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md
  support_type: direct
  verification_note: The title uses six-step language, while the methodology table and section use six-stage language.
  quote_or_locator: canonical_pmc9582072.md:1-12 and 75-116
- claim: The six-stage process covers initial question and field, timeframe, revised questions, search strategy, analyses, and reflexivity.
  supporting_canonical_paths:
    - references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md
  support_type: direct
  verification_note: The recaptured methodology table and following subsections list the six stages and descriptions.
  quote_or_locator: canonical_pmc9582072.md:82-132
```

## Operational rules

- Use this source only when a task explicitly concerns state-of-the-art reviews or when comparing review types.
- Preserve the article's subjectivist/relativist framing and do not convert it into an objectivist systematic-review checklist.
- For final claims, open the canonical Markdown and cite the relevant article span.
- If the PMC landing page is challenge-gated, use the recaptured local Markdown or an approved PMC OAI/BioC route.

## Common misuses

- Treating SotA review methodology as a default survey-writing method.
- Collapsing the six-stage SotA method into PRISMA, scoping-review, or narrative-review guidance.
- Saying the article has only a bad local capture; that was true before the 2026-05-05 recapture and is now superseded.
- Ignoring the six-step title versus six-stage body terminology.

## Evidence limits

The source supports claims about SotA review methodology and its article-specific scope. It does not define SR conduct, PRISMA reporting, database search interfaces, citation graph APIs, or venue submission rules.

## Verification paths

- Article Markdown: `references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md`.
- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=state_of_art_review_2022`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=state_of_art_review_2022`.
- Optional local section locator: `references/corpus_index/sections/by_source/state_of_art_review_2022.jsonl`.

## Unresolved gaps

- The raw PMC landing HTML may remain challenge-gated; future refreshes should prefer approved PMC OAI/BioC or browser-assisted capture.
- Supplementary DOCX was identified but not added as a tracked Markdown source in this pass.
