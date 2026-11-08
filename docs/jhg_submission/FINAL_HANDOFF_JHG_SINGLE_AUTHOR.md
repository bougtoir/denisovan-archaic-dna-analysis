# Final handoff — Journal of Human Genetics (single-author voice pass)

1. Single author: **Onishi Tatsuki**
2. Main manuscript authorial plural: **ZERO inappropriate occurrences**
3. Cover letter authorial plural: **ZERO inappropriate occurrences**
4. Supplement authorial plural: **ZERO inappropriate occurrences**
5. Formal declarations: **single-author wording confirmed** (COI "The author declares no conflict of interest."; contributions "Onishi Tatsuki was responsible for ..."; AI declaration "the author used ..."; funding and ethics neutral)
6. Scientific values changed: **NO**
7. Citations/references changed: **NO**
8. Figures/tables changed: **NO**
9. Data/code changed: **NO**
10. Exact upload-ready filenames (`JHG_SUBMISSION_SINGLE_AUTHOR_FINAL.zip/upload/`):
   - JHG_COVER_LETTER_SINGLE_AUTHOR_FINAL.docx
   - JHG_TITLE_PAGE_SINGLE_AUTHOR_FINAL.docx
   - JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx
   - figures/Figure_1.tiff, Figure_2.tiff, Figure_3.tiff, Figure_4.tiff, Figure_5.tiff
   - tables/Table_1.docx
   - supplementary_information/JHG_SUPPORTING_INFORMATION_SINGLE_AUTHOR_FINAL.docx
   - supplementary_information/JHG_Supplementary_Data.zip
   - supplementary_information/JHG_SUPPLEMENTARY_README_SINGLE_AUTHOR_FINAL.txt
11. Final verdict: **READY FOR JHG SUBMISSION**

## Package
- Target: *Journal of Human Genetics*, Article, traditional subscription route (no APC, page, or colour charges).
- `upload/` holds only the current single-author files; the obsolete plural-author versions were removed. `author_reference/` holds non-upload aids, `audits/` holds the audit set.
- Rebuild: `python3 scripts/create_jhg_submission.py` (fails if any JHG constraint or single-author check is violated; see `JHG_BUILD_CHECKS.md`).

## Status by gate
| Gate | Result | File |
|---|---|---|
| Requirements audit | PASS | JHG_REQUIREMENTS_AUDIT.md |
| Title (unchanged, 114 chars) | PASS | JHG_TITLE_DECISION.md |
| Hostile review | PASS | JHG_HOSTILE_REVIEW.md |
| References (31, Vancouver) | PASS | JHG_REFERENCE_AUDIT.md |
| Format (abstract 239, main text 4 045 words; 5 figures + Table 1) | PASS | JHG_SUBMISSION_FORMAT_AUDIT.md |
| Numeric consistency | PASS | JHG_FINAL_CONSISTENCY_AUDIT.md |
| Single-author voice | PASS | JHG_SINGLE_AUTHOR_VOICE_AUDIT.md |
| Single-author freeze | PASS | JHG_SINGLE_AUTHOR_FREEZE_CHECK.md |
| Upload checklist | — | SUBMISSION_CHECKLIST_JHG_SINGLE_AUTHOR_FINAL.md |

## Author actions at submission
1. Choose the traditional (non-OA) route unless OA is wanted (live page: £3590 / $5490 / €4190 plus VAT, charged only at acceptance).
2. Check name, affiliation, ORCID, and e-mail on the title page and cover letter.
3. Paste the 50-word SI summaries from the checklist into the upload form.

## Notes
- Journal source snapshots and ledger: `data/raw/journal/`; Crossref metadata: `data/raw/reference_metadata/` (private).
- Public analysis repository: https://github.com/bougtoir/denisovan-archaic-dna-analysis

## Requirements recheck and guard (after the compact instruction)
- JHG Guide to Authors v10 (revised 22 April 2026, the only guide the live author page links to) sets Article = abstract 250 / main text 5,000 / 6 displays / 50 references. The compact values 150 / 1,000 / 3 / 20 are the **Brief Communication** row. On the author's decision the package stays an Article; no text, number, figure, table or reference changed.
- Root cause and trace: JHG_REQUIREMENTS_ROOT_CAUSE.md, JHG_REQUIREMENTS_PROPAGATION_TRACE.md, JHG_QC_FAILURE_ANALYSIS.md, JHG_JOURNAL_CONFLATION_CHECK.md (HGV Article is also 5,000/6/50, but HGV played no part in the project history).
- Guard: the builder now takes its limits only from `data/journal_requirements/jhg_requirements.json`, verified on every build against the archived GTA and live page (journal identity, URL family, SHA-256, parsed article-type row, current-guide link, stale cache). 18 regression tests pass, including a foreign-journal manifest → FAIL (JHG_CROSS_JOURNAL_GUARD_TEST.md).
- Final verdict unchanged: **READY FOR JHG SUBMISSION**.
