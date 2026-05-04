# Manual Browser Capture Validation

Date: 2026-05-05
Status: passed
Artifact type: validation note
Canonical evidence status: not canonical evidence

## Scope

The user manually downloaded browser/PDF captures for the two sources that remained locally script-blocked after the live recapture pass:

- `press`
- `cacm_author_guidelines`

The captures were inspected with `file`, `pdfinfo`, and `pdftotext`. They are readable PDFs with extractable source text, not error pages or empty downloads.

## Captures Added

### PRESS

- `manual_browser_pdf_hub_page`: official PRESS hub page, 7 pages.
- `manual_browser_pdf_press_ee_2015`: official PRESS E&E PDF, 79 pages; primary local PRESS evidence.
- `manual_browser_pdf_ee_detail_page`: official PRESS E&E detail page, 3 pages.

### CACM / ACM

- `manual_browser_pdf_author_guidelines`: CACM-specific author guidelines, 8 pages; primary local CACM evidence.
- `manual_browser_pdf_cacm_overview`: ACM Authors Gateway CACM overview, 2 pages.
- `manual_browser_pdf_acm_submissions`: ACM submissions workflow page, 9 pages.
- `manual_browser_pdf_acm_information_for_authors`: ACM information-for-authors page, 2 pages.

## Quality Notes

- The PRESS E&E PDF is the cleanest substantive capture and should be used first for PRESS method claims.
- PRESS hub/detail and CACM/ACM captures are browser print PDFs, so they include navigation, date, footer, and sometimes cookie text.
- Scripted HTTP fetches remain blocked for these sites; future refreshes may still require browser/manual capture.
- CACM/ACM materials are venue/publisher guidance, not survey methodology, and no open license was observed for the guidance pages.

## Validation Commands

```sh
file ~/Downloads/*.pdf
pdfinfo <downloaded-pdf>
pdftotext -f 1 -l 2 <downloaded-pdf> -
pdftotext <downloaded-pdf> - | rg -i 'PRESS|CACM|Author Guidelines|Submissions|Information for Authors'
python3 validation/validate_source_cards_v2.py
python3 validation/validate_graphify_navigation.py
git diff --check -- . ':!validation/chatgpt_deep_review_2026-05-04'
```

## Boundary

This note records capture and QA state. Use canonical Markdown under `references/canonical_sources/md/press/` and `references/canonical_sources/md/cacm_author_guidelines/` for source-grounded claims.
