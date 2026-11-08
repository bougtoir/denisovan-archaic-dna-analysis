# Reproducibility execution audit — Molecular Ecology package (2026-10-19)

Environment: Ubuntu VM, Python 3.10, numpy/scipy/pandas/statsmodels.

| Command | Result |
|---|---|
| `python3 scripts/abo_window_focal_test.py --output /tmp/abo_focal_rerun.json` | Numerically identical to committed data/abo_focal_test.json; differences only in final-ulp float bits (e.g. 1.7800778543670577 vs .575, platform BLAS nondeterminism). PASS |
| Raw-input SHA-256 verification | hg38_1000g_segments.txt = d3ea9fe7ac6b… and hg38_HGDP_segments.txt = c222d44a05fe…, both exactly matching analysis_provenance.json after re-download from Zenodo 14136628. PASS |
| `python3 scripts/run_ajba_pipeline.py --segments-1kg … --segments-hgdp … --permutations 9999 --sensitivity-permutations 999` | All canonical outputs regenerated: every CSV/JSON byte-identical to committed files (pairwise_sharing, pairwise_sharing_corrected, model_summary, sensitivity_analysis, window_size_sensitivity, abo_*_segments, abo_population_summary, profile_quality_checks, correction_stats) with two expected exceptions: abo_focal_test.json float-ulp bits, and analysis_provenance.json's analysis_code_commit field (by design — records the commit running the pipeline). The only failed step was fetch_o2_frequencies.py: the external Ensembl API returned HTTP 500; this is an external service failure, not an analysis defect, and the committed o2_frequency_summary.csv remains canonical. PASS (one external-step caveat) |
| Figure builders (create_core_figures, create_ajba_figures, create_minard_figure, create_bivariate_map, create_heredity_figures) | All run clean; regenerated PNGs are pixel-identical to committed figures (PNG metadata bytes may differ). PASS |
| `python3 scripts/create_molecol_submission.py` | Package regeneration completed; numeric consistency PASSED; reference validation 32/33 (Tournebize year documented). PASS |

Deterministic behaviour: permutation RNG seeded (default seed 42); identical inputs reproduce identical outputs up to float-formatting ulps, as documented in prior provenance notes.
