# JHG single-author voice audit

Author: **Onishi Tatsuki** (sole author, sole corresponding author).
Scope: presentation-only pass converting authorial first-person plural to single-author language. No scientific content, value, citation, figure, table, data file, or URL was changed (see `JHG_SINGLE_AUTHOR_FREEZE_CHECK.md`).

Method: every submission surface was searched (case-insensitive, whole word) for `we, our, ours, us, ourselves, co-author(s), coauthor(s), authors, all authors, the authors` and each hit was read in context. Edits are implemented as `VOICE_EDITS` in `scripts/jhg_content.py`; the module raises an error unless every edit applies exactly once, and the build (`scripts/create_jhg_submission.py`) now fails if any generated DOCX contains a first-person plural or plural-author term.

Style choice: result/process-centred prose first ("This study", "The answer is referred to here", passive for procedures); "I" only where author agency helps (the three questions, the analytical-logic sequence, the data source). "The author" is reserved for formal declarations.

## Surfaces audited
| Surface | File | Authorial plurals before | After |
|---|---|---|---|
| Abstract | JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx | 1 | 0 |
| Introduction, Methods, Results, Discussion | same | 14 | 0 |
| Figure legends (Figures 1-5), Table 1 caption | same; tables/Table_1.docx | 0 | 0 |
| Data availability, code availability, ethics, funding, COI, acknowledgements, AI declaration | same (declarations) | 0 (already "The author"/neutral) | 0 |
| Author contributions | same | 0 plural ("The author was ...") | named sole-author statement |
| Title page (one author, one corresponding author, COI, funding) | JHG_TITLE_PAGE_SINGLE_AUTHOR_FINAL.docx | 0 | 0 |
| Cover letter | JHG_COVER_LETTER_SINGLE_AUTHOR_FINAL.docx | 0 (already "I") | 0 |
| Supporting Information (Figures S1-S7, Table S1 legends, Data 1-10 descriptions) | JHG_SUPPORTING_INFORMATION_SINGLE_AUTHOR_FINAL.docx | 0 | 0 |
| Supplementary README | JHG_SUPPLEMENTARY_README_SINGLE_AUTHOR_FINAL.txt | 0 | 0 |
| Supplementary data (CSV/JSON headers and values) | JHG_Supplementary_Data.zip | not prose; unchanged | unchanged |
| Checklist, handoff, audits | *.md | 1 project-specific (hostile review row describing the old "we"), updated | 0 incorrect |

Title page check: exactly one author listed (Onishi Tatsuki), one corresponding author, ORCID 0000-0001-7261-9062, e-mail and affiliation unchanged. No "both authors", "co-author", "all authors", "contributed equally", or multiple corresponding authors anywhere.

## Changes
| File | Original phrase | Revised phrase | Reason |
|---|---|---|---|
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Abstract) | We ask what similarity a pair should show | This study asks what similarity a pair should show | Authorial plural in a single-author paper. Neutral/process-centred phrasing reads better than repeated "I" |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Introduction) | We refer to the answer as the structural null | The answer is referred to here as the structural null | Authorial plural in a single-author paper. Neutral/process-centred phrasing reads better than repeated "I" |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Introduction) | We do not propose a new permutation method; we formulate and operationalise | This study does not propose a new permutation method; it formulates and operationalises | Authorial plural in a single-author paper. Neutral/process-centred phrasing reads better than repeated "I" |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Introduction) | We treat ABO as one worked example | ABO is treated here as one worked example | Authorial plural in a single-author paper. Neutral/process-centred phrasing reads better than repeated "I" |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Introduction) | We therefore ask three questions. | I therefore ask three questions. | Authorial plural in a single-author paper. Author agency is useful here; first person singular |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Methods: Analytical logic) | We first describe each population | I first describe each population | Authorial plural in a single-author paper. Author agency is useful here; first person singular |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Methods: Analytical logic) | We then compute the complete matrix | I then compute the complete matrix | Authorial plural in a single-author paper. Author agency is useful here; first person singular |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Methods: Analytical logic) | Next we characterise the broad structure | Next I characterise the broad structure | Authorial plural in a single-author paper. Author agency is useful here; first person singular |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Methods: Data sources) | We analysed publicly archived segment calls | I analysed publicly archived segment calls | Authorial plural in a single-author paper. Author agency is useful here; first person singular |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Methods: Dyadic regression) | Our QAP implementation permutes | The QAP implementation used here permutes | Authorial plural in a single-author paper. Neutral/process-centred phrasing reads better than repeated "I" |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Methods: Robustness analyses) | We repeated distance-only population-label tests | Distance-only population-label tests were repeated | Authorial plural in a single-author paper. Neutral/process-centred phrasing reads better than repeated "I" |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Methods: Secondary ABO analysis) | We distinguished strict gene overlap | Strict gene overlap was distinguished | Authorial plural in a single-author paper. Neutral/process-centred phrasing reads better than repeated "I" |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Results: robustness) | every variation we examined | every variation examined | Authorial plural in a single-author paper. Neutral/process-centred phrasing reads better than repeated "I" |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Discussion) | is not ours; | is not new here; | Authorial plural in a single-author paper. Neutral/process-centred phrasing reads better than repeated "I" |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Discussion) | ; we state these as directions, not as results. | ; these are stated as directions, not as results. | Authorial plural in a single-author paper. Neutral/process-centred phrasing reads better than repeated "I" |
| JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx (Author contributions) | The author was responsible for conceptualization, ... | Onishi Tatsuki was responsible for conceptualization, ... | Named CRediT-style sole-author statement (prompt preference); roles unchanged |
| JHG_HOSTILE_REVIEW.md | Kept. Authorial "we" is conventional and allowed. | Fixed in the single-author voice pass ... | Status updated to reflect this pass |
| JHG_SUBMISSION_FORMAT_AUDIT.md | Cover letter (I, not we; ...) | Cover letter (first person singular; ...) + single-author voice row | Project-specific audit text; word counts updated (239 / 4 045) |
| Output file names | JHG_MAIN_MANUSCRIPT.docx etc. | *_SINGLE_AUTHOR_FINAL.* | Obsolete plural-author versions removed from upload/ |

Word-count effect: abstract 238 -> 239 words; main text 4 040 -> 4 045 words (limits 250 / 5 000).

## REMAINING "WE/OUR/US" OCCURRENCES

Upload-ready files (`upload/` in `JHG_SUBMISSION_SINGLE_AUTHOR_FINAL.zip`: main manuscript, title page, cover letter, Table 1, Supporting Information, README, and the CSV/JSON members of the data archive, including DOCX headers/footers and table cells): **0 occurrences** of any search term. Author-reference copies (inline-review manuscript): 0.

Remaining occurrences are only in author-side audit files (`audits/`, not uploaded):

| File | Occurrence | Class | Why valid |
|---|---|---|---|
| JHG_REQUIREMENTS_AUDIT.md:7 | "JHG Guide to Authors v10" | B | Fixed journal document title |
| JHG_REQUIREMENTS_AUDIT.md:8 | `.../jhg/authors-and-referees/authors` (x2) | B | Journal URL |
| JHG_REQUIREMENTS_AUDIT.md:21 | "<=6 authors then et al." | B | Journal reference-style rule (refers to cited papers' authors) |
| JHG_REQUIREMENTS_AUDIT.md:26 | "authors are not required to anonymise (GTA)" | B | Paraphrased journal policy for authors in general |
| JHG_REQUIREMENTS_AUDIT.md:29 | "Authors can also choose to publish under the traditional ..." | B | Direct quotation from the journal |
| JHG_REFERENCE_AUDIT.md:3 | "Up to 6 authors then \"et al.\"" | B | Journal reference-style rule |
| JHG_TITLE_DECISION.md:3 | "Guide to Authors v10" | B | Fixed journal document title |
| JHG_HOSTILE_REVIEW.md:15 | 'Single author writes "we" in the manuscript' | B | Quotes the reviewer issue that this pass fixed |
| JHG_SINGLE_AUTHOR_VOICE_AUDIT.md (this file) | "Original phrase" column and search-term lists | B | Quotes the pre-edit text being documented |
| DEVIN_JHG_RETARGET_PROMPT.txt | 3 hits | B | Verbatim archived task prompt, not submission prose |
| DEVIN_JHG_SINGLE_AUTHOR_PROMPT.txt | 95 hits | B | Verbatim archived task prompt (this pass), not submission prose |

Category A (general/community use): 0. Category C (cited titles): 0 (no reference title contains a search term).
**Category D (incorrect authorial plural): 0.**
