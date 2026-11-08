# JHG final consistency audit

All numbers are generated at build time from `data/analysis_provenance.json` and the analysis statistics JSON, through `mecol_content.py` and then `jhg_content.py`. Nothing was hard-coded during retargeting; the only transformation is formatting (comma to space thousands separators).

| Frozen value | Found in `JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx` |
|---|---|
| 3 134 individuals; 66 populations; 2 145 pairs | PASS |
| 62 non-admixed populations; 1 891 pairs | PASS |
| r = -0.497 / -0.462; partial -0.369 / -0.326 | PASS |
| P = 0.0001 / 0.0002 | PASS |
| max z 2.21 / 2.53; min q 0.78 / 0.82; zero supported pairs | PASS |
| ABO z 1.78 (P 0.36) / 0.63 (P 0.92) | PASS |
| Usable windows 3 843 / 1 385 | PASS |
| R2 0.247 / 0.213 and 0.546 / 0.511 | PASS |
| 9 999 and 999 permutations | PASS |
| ABO segments 834 / 129 / 247 | PASS |

- Figures: the audited PNG sources were converted to CMYK TIFF without changing values. Supplementary data: the audited files were copied byte-for-byte into the ZIP.
- No stale journal-target terms (Molecular Ecology, Human Genetics target, Heredity target, Wiley, Bioessays) appear in the manuscript, title page, cover letter, or SI. The automated check passed; the only "Heredity" is cited reference 15.
- Public reproducibility: the only script named in the manuscript (`abo_window_focal_test.py`) and the pipeline scripts it depends on (`archaic_sharing_*.py`, `create_core_figures.py`, `build_ancient_abo_summary.py`) exist in https://github.com/bougtoir/denisovan-archaic-dna-analysis (checked via GitHub API). The document generators stay private under the existing public/private split.

Verdict: PASS.
