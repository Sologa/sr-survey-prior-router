# State-of-Art Review 2022 Source Card v2

```yaml
source_id: state_of_art_review_2022
source_family: survey_writing_methods
canonical_paths:
  - references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md
canonical_urls:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC9582072/
authority_level: bad_capture_do_not_use
version_or_access_date: "2022 article target; local corpus fetched 2026-05-04 but captured only a PMC browser-check page"
applies_to:
  - documenting that the local capture is unusable as article evidence
  - routing source-audit tasks to recapture or independently verify the article body
  - preventing unsupported state-of-art review method claims from this local file
not_for:
  - article-body claims about a six-step approach
  - state-of-art review methodology claims
  - quoting or paraphrasing the target article
  - final evidence support until the article body is recaptured and validated
route_relevance:
  - survey_writing_prior
  - evidence_grounding
  - source_audit
  - synthesis_writing
freshness_risk: high because the local file is not the article body; live PMC or another access-approved source must be checked before any method claim.
reuse_or_license_risk: unknown for article body in local corpus because the available local file is a browser-check capture, not usable article content.
qa_status: bad_capture_browser_check_only_do_not_use_for_method_claims
last_reviewed: "2026-05-05"
```

## Key points

```yaml
- claim: The local canonical Markdown for `state_of_art_review_2022` is a PMC browser-check capture, not article body text.
  supporting_canonical_paths:
    - references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md
  support_type: direct
  verification_note: The file contains only a browser-check notice after the title and source URL.
  quote_or_locator: references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md:1-10; section_id=state_of_art_review_2022__canonical_pmc9582072__s0001_state_of_the_art_literature_review_methodology_a_six_step_approach_for_knowledge
- claim: The source should not be used locally for article-body claims about state-of-art review methodology.
  supporting_canonical_paths:
    - references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md
  support_type: unsupported
  verification_note: The title exists in the local capture, but the article text needed to support method claims is absent.
  quote_or_locator: references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md:6-10; section_id=state_of_art_review_2022__canonical_pmc9582072__s0001_state_of_the_art_literature_review_methodology_a_six_step_approach_for_knowledge
- claim: Any claim that the article provides a specific six-step state-of-art review method is unsupported by the current local Markdown capture.
  supporting_canonical_paths:
    - references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md
  support_type: unsupported
  verification_note: The title mentions a six-step approach, but the captured body is missing; do not infer the steps.
  quote_or_locator: references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md:1-10; section_id=state_of_art_review_2022__canonical_pmc9582072__s0001_state_of_the_art_literature_review_methodology_a_six_step_approach_for_knowledge
- claim: The only safe operational use of this local source is source-audit routing: recapture or verify the article body through an approved route before use.
  supporting_canonical_paths:
    - references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md
  support_type: indirect
  verification_note: This is inferred from the absence of article body text and the browser-check notice in the capture.
  quote_or_locator: references/canonical_sources/md/state_of_art_review_2022/canonical_pmc9582072.md:6-10; section_id=state_of_art_review_2022__canonical_pmc9582072__s0001_state_of_the_art_literature_review_methodology_a_six_step_approach_for_knowledge
```

## Operational rules

- Do not cite this local Markdown for state-of-art review methodology.
- Use this card to block unsupported use and to route the source to recapture/validation work.
- If a task needs this source, first obtain an article-body capture from PMC or another access-approved source, then create a revised card from the validated text.
- Do not make claims about the article's six steps from the title alone.

## Common misuses

- Treating the source title as evidence for the method content.
- Quoting the browser-check page as if it were the article.
- Using manifest metadata or the bad capture to populate methodology rules.
- Collapsing this source into generic narrative-review guidance without article-body verification.

## Evidence limits

The local canonical file supports only the fact that the capture is unusable browser-check content. It does not support article-body, method, framework, step, recommendation, or conclusion claims.

## Verification paths

- Source row: `references/source_inventory/source_manifest.jsonl` with `source_id=state_of_art_review_2022`.
- Download row: `references/canonical_sources/download_manifest.jsonl` with `source_id=state_of_art_review_2022`.
- Document locator: `references/corpus_index/document_index.jsonl` with `source_id=state_of_art_review_2022`, status `bad_capture`.
- Section locator: `references/corpus_index/sections/by_source/state_of_art_review_2022.jsonl`.

## Unresolved gaps

- Article body has not been captured locally.
- License/reuse terms for the article body need verification after recapture.
- No methodology claims should be added until the recaptured text is validated.
