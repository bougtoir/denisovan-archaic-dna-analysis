# Heredity requirements audit

Journal: *Heredity* (Springer Nature, for The Genetics Society).
Guidelines consulted: https://www.nature.com/hdy/authors-and-referees/gta (re-checked 2026-10-13).
Article type: Article. The journal's current Article Type Specifications name the category "Article"; "Original Article" is not current Heredity terminology, and the title page, cover letter and checklist use "Article".
New submission following editorial consideration of `HDY-26-A0368`.

## Hard limits

| Requirement | Limit | This submission | Status |
| --- | --- | --- | --- |
| Abstract length | 250 words | 227 words | PASS |
| Main-text length (excluding abstract, references, legends, tables) | 7,000 words | 4,439 words | PASS |
| Combined main figures and tables | 8 | 5 figures + 1 table = 6 | PASS |
| References | 100 | 30 | PASS |
| Keywords | 3-6 | within range (validator check) | PASS |
| Running title | short form for page headers | `A structural null for pairwise similarity` (40 characters) | PASS |

The 100-reference ceiling is the current Article limit verified against the Guide to Authors; the 120-reference limit that applies to Review Articles does not apply here. Supplementary material is uploaded as a single Supporting Information file plus separate supplementary data files, which the guide permits.

## Reference style

Checked against the current Guide to Authors: author-date citations in the text, reference list alphabetised by first-author surname, all authors listed for works with six or fewer authors, and the first six authors followed by `et al.` for works with seven or more. Author lists, initials, year placement, abbreviated journal titles, volume, pages or article numbers, and DOIs were verified record by record against Crossref; see `FINAL_HANDOFF.md` for the audit result and `reference_validation.csv` for the per-reference checks.

## Supplementary files

Inventoried in `SUPPLEMENTARY_FILE_INVENTORY.md` and in the Supporting Information: 5 main figures, 7 supplementary figures, 1 main table, 1 supplementary table, and 10 machine-readable supplementary data files.

## Formatting

| Requirement | Implementation | Status |
| --- | --- | --- |
| Double spacing | `Normal` style line spacing 2.0 in every generated DOCX | PASS |
| Continuous line numbers | `w:lnNumType` with `countBy=1`, `restart=continuous` in the section properties | PASS |
| Margins of at least 4 cm | top/bottom/left/right set to 4 cm | PASS |
| Continuous page numbering | page-number field in the footer | PASS |
| Editable word-processor file (not PDF) | DOCX for manuscript, title page, tables, Supporting Information, cover letter | PASS |
| Equations as native Word objects | OMML (`m:oMathPara`) runs; no LaTeX source strings in the text | PASS |
| Figures supplied as separate files | `Figure_1`-`Figure_5` and `Figure_S1`-`Figure_S7` as PNG and TIFF at 300 dpi; figure legends in the manuscript, figures not embedded in `manuscript_heredity.docx` | PASS |
| Editable tables | `tables_heredity/Table_1.xlsx` and `tables_heredity/Table_S1.xlsx`, plus DOCX versions | PASS |
| No CJK / full-width characters in the English files | checked across all generated DOCX | PASS |

## Double-anonymised review

| Requirement | Implementation | Status |
| --- | --- | --- |
| Title page uploaded separately | `title_page_heredity.docx` carries title, article type, author, affiliation, correspondence, running title, word count, previous manuscript number, and data/code availability | PASS |
| Manuscript file anonymous | `manuscript_heredity.docx` contains the title and text only; no author, affiliation, funding or acknowledgement identifiers in the body | PASS |
| Self-identifying repository links kept off the anonymous file | data/code URL appears on the title page and in the cover letter, not in the anonymous manuscript | PASS |
| No tracked changes or comments | generated fresh from code; no revision marks or annotations present | PASS |

## Required sections

Present in `manuscript_heredity.docx`, in this order: Abstract, Keywords, Introduction, Materials and Methods, Results, Discussion, Data Availability, Research Ethics, Acknowledgements, Author Contributions, Conflict of Interest, References, Figure Legends, Table Legends.

## Submission-system items

| Item | Notes |
| --- | --- |
| Cover letter | `cover_letter_heredity.docx`, addressed to Dr Louise J. Johnson, Editor-in-Chief, University of Reading; states the new submission follows consideration of `HDY-26-A0368`, explains the restructuring, and includes originality, exclusivity and competing-interest statements |
| Previous manuscript number | `HDY-26-A0368`, stated in the cover letter and on the title page |
| Recommended editor | Lounès Chikhi (CRBE-CNRS, University of Toulouse) |
| Cover art | optional; not supplied |
| Student paper eligibility | author to complete locally |
| Plagiarism declaration | author to confirm in the submission system |

## Items that must be completed by the author locally

- Confirm the plagiarism declaration and student-eligibility fields in the submission system.
- Confirm ORCID and institutional details on the title page.
- Upload files in the order listed in `submission_checklist.md`.
