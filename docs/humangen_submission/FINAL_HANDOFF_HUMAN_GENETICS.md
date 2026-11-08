# FINAL HANDOFF — Human Genetics submission

Manuscript: "Population structure defines the null expectation for pairwise genomic similarity: archaic-segment sharing across 66 human populations" — Tatsuki Onishi (Shiga University).
Target: Human Genetics (Springer Nature), Research Article, traditional (subscription) route — no mandatory charges.
Date: 2026-10-14.

## A. Task

Retarget the finalized Heredity-version manuscript (rejected as HDY-26-A0368) to Human Genetics. Targeting revision only: reframed toward human population/evolutionary/statistical genetics; analysis, numbers, figures frozen. New first-person cover letter; no Heredity history mentioned.

## B. Files produced (docs/humangen_submission/)

- `HUMAN_GENETICS_MAIN_MANUSCRIPT.docx` — full manuscript, TNR 12pt, double-spaced, line numbering, OMML equations, references Springer author-date.
- `HUMAN_GENETICS_MAIN_MANUSCRIPT_inline_review.docx` — same + figures inline (review copy).
- `HUMAN_GENETICS_TITLE_PAGE.docx` — title, author/affiliation/ORCID, corresponding email, abstract, 6 keywords, acknowledgements incl. funding, declarations.
- `HUMAN_GENETICS_COVER_LETTER.docx` — NEW, first person singular, Dear Editors-in-Chief; no HDY numbers.
- `HUMAN_GENETICS_SUPPORTING_INFORMATION.docx` — S1–S7 figure legends + Table S1 + supplementary data descriptions (corrected SD5/6/8/9/10).
- `Table_1_residual_outliers.docx`, `Table_S1_abo_summary.docx`, `tables_humangen/` (xlsx), `figures_tables_humangen.pptx`.
- `figures/` — Figure 1–5 + S1–S7 as PNG + TIFF (unchanged validated files).
- `supplementary_data/` — SD1–SD10 CSV/JSON.
- `data_archive_humangen.zip` + `data_detail_humangen.docx` — corrected consistent versions carried over from `docs/heredity_submission/consistency_pass/`.
- `SUPPLEMENTARY_FILE_INVENTORY.md`, `SUBMISSION_CHECKLIST_HUMAN_GENETICS.md`, `reproducibility_checklist.md`, `submission_validation.txt`, `numeric_consistency_check.txt`, `reference_validation.csv`.
- Audit docs: `HUMAN_GENETICS_REQUIREMENTS_AUDIT.md`, `HUMAN_GENETICS_CITATION_ECOLOGY.md`, `HUMAN_GENETICS_HOSTILE_REVIEW.md`, `REFERENCE_AUDIT.md`.
- `DEVIN_HUMAN_GENETICS_RETARGET_PROMPT.txt` — copy of the task prompt.
- `HUMAN_GENETICS_SUBMISSION_FINAL.zip` — all of the above in one archive.

## C. Journal compliance (verified 2026-10-14, link.springer.com/journal/439)

Research Article; abstract 150–250 words (pass); 4–6 keywords (6 given); ≤3 heading levels; Springer author-date references alphabetical with DOI links (31 entries); editable .docx; title page carries acknowledgements/funding; declarations in body; figures separate; AI declaration retained; ethics statement retained; hybrid journal — traditional route has no mandatory charge. EiCs: Gonzaga-Jauregui & Wang → "Dear Editors-in-Chief,".

## D. Retarget edits made

- References: all 31 converted to Springer format; added Lawson DJ et al. (2020) Hum Genet 139:23-41 (PubMed-verified); alphabetical order; keys unchanged.
- Abstract: tail redirected to human population genetics ("pair-specific human history or gene flow").
- Introduction: kept 7-part architecture; added biobank-scale structure bias sentence (Lawson et al. 2020); closing paragraph now ends on human population-genetic inference; demes/breeds list cut.
- Methods: scientifically unchanged (500-kb windows, partial Mantel/QAP, BH-FDR, ABO focal test incl. sign convention, ethics/CARE).
- Results: four-part structure and all numbers preserved verbatim.
- Discussion: novelty boundary explicit; human-evolution interpretation slightly strengthened; cross-species examples compressed to one sentence; all limitations retained; ABO remains ~1 paragraph.
- Conclusion: ends on the human population-genetic message.
- Title: kept (documents decision — fits Human Genetics conventions; states estimand + finding).
- Cover letter: fully rewritten, first person singular, 8 content blocks, no Heredity identifiers.

## E. Frozen numbers (verified unchanged, from canonical data files)

3,134 individuals / 66 populations / 2,145 pairs; 62 non-admixed populations / 1,891 pairs. Raw r = −0.497/−0.462; partial r = −0.369/−0.326; QAP P = 0.0001/0.0002; distance-only R² = 0.2471/0.2131; max |z| = 2.21/2.53; min BH q = 0.78/0.82; 0 supported pairs. ABO: Neanderthal z = 1.78 (64th pct, P = 0.36), Denisovan z = 0.63 (8th pct, P = 0.92); 3,843/1,385 usable windows; 834 ABO-interval segments (129 strict, 247 ties); ancient 59 assessed/16 detected/8 strict.

## F. QC results

- Numeric consistency vs canonical data archive: PASSED (validate_numeric_consistency_humangen.py).
- Reference validation: 30/31 verified (Tournebize & Chikhi: online 2024 vs print volume year 2025 — print convention kept, documented in REFERENCE_AUDIT.md).
- Hostile review: no BLOCKING, no MAJOR; 3 MINOR items already covered by existing limitations text.
- Figure/table citation order and formats: unchanged from validated Heredity pass.
- Public repo check: github.com/bougtoir/denisovan-archaic-dna-analysis contains scripts/abo_window_focal_test.py, run_ajba_pipeline.py, data/ — code-availability text accurate; doc-generation scripts are excluded from sync (EXCLUDE_MAP covers create_humangen/heredity machinery via the doc-gen exclusions; humangen scripts added to the private branch only — see open item G3 if a sync of THIS branch is desired).

## G. Open items / author actions at submission

1. Submission interface declarations (funding, competing interests, ethics, data availability, author contribution) must be entered in Editorial Manager fields; text exists in the manuscript body.
2. Declare the bioRxiv preprint at submission.
3. The public-repo sync is configured for branch `devin/1791854931-heredity-editorial-qc`, not this retarget branch; no public content changes are needed (analysis code/data unchanged), but if a future branch syncs, ensure doc-gen scripts stay excluded.
4. Optional: Open Choice APC is optional — submit via the traditional route for zero charges.

## H. Rebuild instructions

From repo root:
```
python3 scripts/create_humangen_submission.py
```
Regenerates all docx/pptx/xlsx/zip + validators in docs/humangen_submission/. Requires python-docx, python-pptx, openpyxl, statsmodels, requests. Consistency-pass inputs are copied from docs/heredity_submission/consistency_pass/.

## I. Journal chain

BioEssays (concept proposal) → AJBA → Heredity (HDY-26-A0368, rejected) → **Human Genetics** (this package).

## J. Repository state

Branch: `devin/1791946419-human-genetics-retarget` (branched off `devin/1791864833-heredity-consistency-repair`, PR #670 base). New files: `scripts/humangen_content.py`, `scripts/create_humangen_submission.py`, `scripts/validate_numeric_consistency_humangen.py`, `scripts/validate_references_humangen.py`, `docs/humangen_submission/`.

## K. Final verdict: READY

Submission-ready pending the author's Editorial Manager entries (G1–G2). No analysis, numeric, or figure changes were made.
