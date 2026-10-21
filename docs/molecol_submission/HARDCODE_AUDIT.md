# Hard-coded scientific numbers audit — Molecular Ecology package (2026-10-19)

Method: regex scan of scripts/mecol_content.py and scripts/create_molecol_submission.py for result literals (correlations, P/q/z, counts, ABO values, segment counts).

Findings:
- All scientific values in the manuscript text are read from canonical outputs at build time: STATISTICS = correction_stats.json, PROVENANCE = analysis_provenance.json, ABO_FOCAL = abo_focal_test.json, RESIDUALS computed from pairwise_sharing_corrected.csv, ABO counts computed from abo_neanderthal_segments.csv / abo_population_summary.csv. No embedded result literals in the prose modules.
- create_molecol_submission.py contains repeated counts inside Supporting-Data caption strings and checklist/inventory text ("2,145", "1,891", "62", "13" auxiliary files, "Pima 1/13, Maya 1/21, Colombian 0/7"). These are presentation/documentation strings; each was verified equal to the canonical value in this audit. Classified: presentation literals, verified — no change required.
- Allowed literals present and correct: method thresholds (0.8 posterior, min population size 7, >100/>50 union bins, ≥10 nonzero populations, 9,999/999 permutations), genomic coordinates, the four admixed-population labels, journal formatting constants.

Status: **PASS**.
