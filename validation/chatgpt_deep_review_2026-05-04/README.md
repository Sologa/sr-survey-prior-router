# ChatGPT Deep Review Inbox

Use this directory as a staging area for ChatGPT's external deep review of this
draft skill. Keep generated analysis here first; do not apply proposed changes
directly into `references/` until they have been reviewed.

## Placement

- `review.md`: main ChatGPT review report.
- `proposed_files/`: exact file contents proposed by ChatGPT, mirrored by
  intended repo-relative path.
- `evidence/`: external evidence notes, source lists, screenshots, or exported
  supporting material used by the review.

## Proposed File Mirror Examples

- `proposed_files/references/distillation-plan.md`
- `proposed_files/references/source_inventory/source_cards_v2/README.md`
- `proposed_files/references/source_inventory/source_cards_v2/<source_id>.md`

## Rules

- Treat this directory as review input, not canonical evidence.
- Important claims still need verification against `references/canonical_sources/md/`
  or the source URLs recorded in `references/canonical_sources/download_manifest.jsonl`.
- Keep raw PDFs, HTML, DOCX, and other large canonical captures out of this
  directory unless they are small, necessary review evidence.
