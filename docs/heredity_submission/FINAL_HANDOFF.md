# Final handoff: Heredity new submission

Package: `HEREDITY_resubmission_FINAL_v3.zip` in `docs/heredity_submission/`.
Submitted as a new submission following editorial consideration of HDY-26-A0368.

## Verdict

READY FOR HEREDITY NEW SUBMISSION.

## Finishing pass: ABO focal-window residual sign

- The sign was already correct; no scientific change was required and no ABO number, figure or table changed.
- Residual formula, as implemented in `scripts/abo_window_focal_test.py`: within each 500-kb window the absolute between-population difference in archaic-segment frequency is regressed on geographic distance, and excess similarity is `predicted absolute difference - observed absolute difference`, standardised by its within-window standard deviation. Positive values therefore mark pairs that are more similar than geographic distance predicts, which is what the Methods claim. The per-window statistic is the maximum standardised excess across pairs, and the empirical P value is the upper-tail fraction of usable windows at or above the ABO value.
- The code previously expressed the same quantity as the negated ordinary residual; it now computes `predicted - observed` directly so the convention is explicit. Rerunning with warnings promoted to errors reproduces `data/abo_focal_test.json` byte-identically (Neanderthal z=1.78, 64th percentile, P=0.36; Denisovan z=0.63, 8th percentile, P=0.92).
- The Methods now state the sign convention explicitly rather than leaving it implicit in the word "residual".
- Canonical script path: `scripts/abo_window_focal_test.py` (public repository, invoked by `scripts/run_ajba_pipeline.py`). There is no second implementation.

## Finishing pass: editorial and formatting items

- Cover letter addressee: Dr Louise J. Johnson, Editor-in-Chief, Heredity, University of Reading, UK. Manuscript code HDY-26-A0368 is retained.
- Article type: "Article", the current Heredity category name, replacing "Original Article" on the title page, cover letter and checklist.
- Reference limit: 100 for Articles, confirmed against the current Guide to Authors; the 120-reference limit applies to Review Articles. The submission cites 27.
- Affiliation: Data Science and AI Innovation Research Promotion Center, Shiga University, Hikone, Shiga, Japan, applied to the title page, the correspondence line and the cover-letter signature block.
- Data Archiving and the reproducibility checklist now name `abo_window_focal_test.py` and no longer promise document-generation code, which is intentionally private.

## Regenerated files

`manuscript_heredity.docx` (clean anonymous main manuscript), `manuscript_heredity_inline_review.docx` (inline copy), `cover_letter_heredity.docx`, `title_page_heredity.docx`, `supporting_information_heredity.docx`, `Table_1_residual_outliers.docx`, `Table_S1_abo_summary.docx`, the Excel tables, `figures_tables_heredity.pptx`, `submission_checklist.md`, `reproducibility_checklist.md`, `HEREDITY_REQUIREMENTS_AUDIT.md`, `submission_validation.txt`, `numeric_consistency_check.txt`, `reference_validation.csv`, and `HEREDITY_resubmission_FINAL_v3.zip`. Figures were unchanged because no numerical result changed.

The file names above are the canonical package names; they correspond to the requested main-manuscript-clean, main-manuscript-inline, cover-letter, title-page and supporting-information documents respectively.

Every automated check passes, the raw inputs are archived locally with checksums that match the record written when the committed results were produced, and the remaining items are author-side form fields that only the corresponding author can complete (listed at the end).

## What the paper now argues

A general population-genetic inference paper: repeated pairwise comparisons between populations are not independent observations, so a claim that one pair is exceptionally similar has to be judged against a null that preserves the relational structure of the whole set. Archaic-segment sharing across 3,134 individuals in 66 populations (2,145 pairs) is the empirical demonstration, and ABO is a prespecified focal locus worked through the same machinery. The negative ABO result narrows the hypothesis space rather than denying shared history.

## Files to upload

| Submission slot | File |
| --- | --- |
| Manuscript | `manuscript_heredity.docx` (anonymous, no author information, no embedded figures) |
| Title page | `title_page_heredity.docx` |
| Cover letter | `cover_letter_heredity.docx` |
| Figures 1-5 | `figures/Figure_1..5.png` and `.tiff` |
| Table 1 | `Table_1_residual_outliers.docx` or `tables_heredity/Table_1.xlsx` |
| Supporting Information | `supporting_information_heredity.docx`, Figures S1-S7, `Table_S1`, `supplementary_data/` |

`manuscript_heredity_inline_review.docx` is the author-side copy with figures placed inline. Do not upload it.

## Compliance

- Abstract 227 words (limit 250); main text 4,439 words (limit 7,000)
- 5 main figures plus 1 main table (limit 8 combined); 30 references (limit 100)
- Running title 40 characters
- Double spacing, continuous line numbers, continuous page numbers, 4 cm margins
- Double-anonymised: no author, affiliation, funding, or repository identifier in the manuscript file
- Acknowledgements, Author Contributions, Conflict of Interest, Data Archiving and Research Ethics sections present
- Equations are native Word objects, not LaTeX strings or images
- No CJK or full-width characters, no tracked changes, no comments, no placeholder strings in any docx

## Verification performed

- `submission_validation.txt`: all checks PASS, including citation order (figures 1-5, supporting figures S1-S7, table 1), every reference cited, references alphabetised, and Heredity figure/reference limits
- `numeric_consistency_check.txt`: every checked value in the manuscript, including the residual maxima, minimum q values, and the ABO focal-test statistics, matches `correction_stats.json`, `analysis_provenance.json`, `abo_focal_test.json`, and `pairwise_sharing_corrected.csv`. No number is hand-written into the text
- `reference_validation.csv`: 29 of 30 references resolve automatically against Crossref or PubMed. The single flag is a year convention, not an error: Tournebize and Chikhi was released online on 13 December 2024 and published in the February 2025 print issue (Nat Ecol Evol 9:225-236), which is the year cited. Mantel 1967 predates DOI assignment and is checked manually
- `RAW_DATA_PROVENANCE.md`: all four Zenodo 14136628 source files downloaded in full to `/home/ubuntu/research_raw_data/zenodo_14136628/`, sizes verified against the record metadata, SHA-256 recorded. The two segment-file checksums match those stored in `data/analysis_provenance.json`, so the committed derived data descend from exactly this archived content
- `HOSTILE_REVIEW_HEREDITY.md`: adversarial referee pass; the blocking objections it raised (an untested ABO claim, a null result readable as absence of history, a schematic figure readable as data) were fixed before this package was built
- `scripts/abo_window_focal_test.py` reruns cleanly with warnings promoted to errors and reproduces `data/abo_focal_test.json` byte-identically

## Final editorial QC pass

### References added

| Reference | Cited in |
| --- | --- |
| Mazet O, Rodriguez W, Grusea S, Boitard S, Chikhi L. 2016. On the importance of being structured: instantaneous coalescence rates and human evolution-lessons for ancestral population size inference? Heredity 116:362-371. https://doi.org/10.1038/hdy.2015.104. | Introduction (closest-prior paragraph following the structural-null paragraph) and Discussion (novelty-boundary paragraph) |
| Ortega-Del Vecchyo D, Slatkin M. 2019. FST between archaic and present-day samples. Heredity 122:711-718. https://doi.org/10.1038/s41437-018-0169-8. | Introduction (closest-prior paragraph) and Discussion (novelty-boundary paragraph) |
| Tournebize R, Chikhi L. 2025. Ignoring population structure in hominin evolutionary models can lead to the inference of spurious admixture events. Nat Ecol Evol 9:225-236. https://doi.org/10.1038/s41559-024-02591-6. | Introduction (closest-prior paragraph) and Discussion (novelty-boundary paragraph) |

All three were verified against Crossref for author list, title, journal, volume, pages and DOI.

### Novelty boundary against each closest prior study

- Tournebize and Chikhi 2025: that unmodelled population structure can produce spurious admixture inferences in model-based hominin histories is established there, not here; this manuscript addresses descriptive pairwise similarity, where the problem is non-independence among entries built from recurring populations rather than misspecification of a fitted demographic model.
- Mazet et al. 2016: that structured histories without admixture can mimic population-size change in coalescence-based inference is their result; the present contribution is a permutation null and pair-level residual test that make claims about individual population pairs testable.
- Ortega-Del Vecchyo and Slatkin 2019: they characterise how divergence statistics between archaic and present-day samples depend on the assumed demographic context; here the comparison is not a single statistic but the whole pairwise matrix, judged against a null that preserves the dependence created by repeated population units.

The manuscript does not claim population-structure bias as a new discovery, does not claim QAP as a new method, makes no "first ever" claim, does not return ABO to the identity of the paper, and adds no route-specific interpretation. The cover letter now bounds the novelty claim in the same terms.

### Reference-style audit (Heredity author-date style)

- Rule applied: all authors listed for six or fewer; first six followed by `et al.` for seven or more; author-date in-text citations; reference list alphabetised by first-author surname.
- Expanded to full author lists because the work has six or fewer authors: Calafell et al. 2008 (previously truncated at three names).
- Corrected to the first six authors in the published order, where the previous entry either truncated early or listed names out of order: Bergstrom et al. 2020, Carroll et al. 2020, Claw et al. 2018 (previous entry named co-authors who are not the second to sixth authors of record), Condemi et al. 2021 (initial of the second author corrected to Mazieres S), Green et al. 2010, Iasi et al. 2024, Jacobs et al. 2019, Ohashi et al. 2006, Prufer et al. 2017, Reich et al. 2010, Sankararaman et al. 2014, Segurel et al. 2012, Skov et al. 2018.
- Unchanged because already compliant: 1000 Genomes Project Consortium 2015 (corporate author), Benjamini and Hochberg 1995, Dekker, Krackhardt, and Snijders 2007, Guillot and Rousset 2013, Halverson and Bolnick 2008, Krackhardt 1988, Legendre and Fortin 2010, Mantel 1967, Petr et al. 2019, Quilodran et al. 2023, Rousset 1997, Sankararaman et al. 2016, Wright 1943.
- Volume, pages or article numbers, abbreviated journal titles, year placement and DOIs were checked record by record against Crossref. No citation was added or removed other than the three studies listed above, and `submission_validation.txt` confirms the list is alphabetised and that every reference is cited.

### Supplementary file inventory

`SUPPLEMENTARY_FILE_INVENTORY.md` and the Supporting Information now list every supplementary upload file with a short description. Every listed file exists in the package and the package contains no unlisted supplementary file.

### Actual counts in this package

| Item | Count |
| --- | --- |
| Main figures (Figures 1-5) | 5 |
| Supplementary figures (Figures S1-S7) | 7 |
| Main tables (Table 1) | 1 |
| Supplementary tables (Table S1) | 1 |
| Supplementary machine-readable data files | 10 |
| Supporting Information documents | 1 |
| Cover letters | 1 |
| Title pages | 1 |
| Manuscript files (anonymous main, author-side inline copy) | 2 |

`submission_checklist.md`, the Supporting Information, the requirements audit and this handoff were corrected from the stale counts (Figures 1-4, Figures S1-S5, a non-existent `tables_heredity.xlsx`) to these actual values.

### Analysis and results unchanged

- No analysis script was rerun and no analysis definition, seed, window, model or permutation setting was altered. 3,134 individuals, 66 populations, 2,145 pairs, raw geographic correlations -0.497 and -0.462, partial correlations -0.369 and -0.326, QAP P values 0.0001 and 0.0002, the non-admixed subset of 1,891 pairs from 62 populations, zero pairs at q<0.10, maximum residual z values 2.21 and 2.53, minimum q values 0.78 and 0.82, and the ABO focal-test statistics (Neanderthal z=1.78, 64th percentile, P=0.36; Denisovan z=0.63, 8th percentile, P=0.92) are unchanged, and `numeric_consistency_check.txt` passes against the committed data files.
- Figure images were not regenerated because no numerical result changed. The main-text word count rose from 4,172 to 4,439 because two short paragraphs were added.
- The structural-null framing is unchanged.

### No AI disclosure added

No ChatGPT, Devin, generative-AI or large-language-model disclosure, methods paragraph, acknowledgement or placeholder was added anywhere in the package, and no existing disclosure was expanded or rewritten.

## Known limitations stated in the paper

Centroid-based distances, sparse Denisovan calls outside Oceania, no common callable mask, no separation of identity by descent from identity by state, two combined projects with only a coarse dataset indicator, and a deliberately conservative pair-level test whose largest residuals bound rather than refute modest pair-specific effects.

## Author-side items before clicking submit

- Student eligibility question: answer No with `Not applicable`, or Yes with the student's name and status
- Plagiarism declaration: must be set to Yes
- ORCID, affiliations, corresponding-author contact, funding statement
- Suggested handling editor: Lounes Chikhi is the closest fit on the Heredity board
- Cover art is optional and separate from the title page
