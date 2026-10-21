# Text–figure–table consistency audit — Molecular Ecology package (2026-10-19)

- Figure 1 (schematic/workflow): panels a-d marked schematic; panel e matches Methods pipeline order (profiles → matrix → model → QAP → residuals → FDR). Consistent.
- Figure 2: plotted similarity vs geographic distance for 2,145 pairs; descriptive fits + QAP P values match correction_stats (-0.497/-0.462; P=0.0001/0.0002). Consistent.
- Figure 3: 31-population subset labelled as legibility selection; caption states all 66 analysed; Figure S1 shows full matrices. Consistent.
- Figure 4: plotted residual z vs BH q from pairwise_sharing_corrected.csv; shaded criterion z>2 & q<0.10; verified zero pairs in support region for both ancestries (max z 2.21/2.53, min q 0.78/0.82). Consistent.
- Figure 5: sensitivity panels regenerate from sensitivity_analysis.csv and window_size_sensitivity.csv (subsets, metrics, 250 kb/500 kb/1 Mb windows); captions describe them as robustness summaries, matching data. Consistent.
- Figure S1: complete 66×66 matrices — consistent with caption.
- Figure S2: Neanderthal distance-correlation sensitivity to admixed-population exclusion — values from sensitivity_analysis.csv.
- Figure S3: window-size QAP grid — values from window_size_sensitivity.csv.
- Figure S4: ABO-centered exploratory figure; ties excluded from displayed proportions, per caption and Table S1 note; segment counts (Pima strict overlap, Maya interval-only) verified in abo_neanderthal_segments.csv.
- Figure S5: O2/carrier frequencies from distinct sources; caption carries the non-association caveat.
- Figure S6: descriptive ancient vs modern summaries; no formal comparison claimed.
- Figure S7: bivariate map from population_profiles_500kb.npz + population_metadata.csv as captioned.
- Table 1: empty result table ("No qualifying pair") matches canonical: 0 pairs with z>2 & q<0.10 for either ancestry.
- Table S1 recomputation: percentages = n_<reference>/(group_total - ties) per region; recomputed exactly: East Asia 57 → 54.4/1.8/43.9; Europe 275 → 7.3/46.5/46.2; Indigenous Americas 2 → 0.0/100.0/0.0; Admixed Americas 98 → 3.1/61.2/35.7; Central/South Asia 98 → 9.2/44.9/45.9; Middle East 44 → 11.4/52.3/36.4; Oceania 13 → 0.0/0.0/100.0. Denominator (three-reference, tie-excluded) matches the caption. PASS.
- Figure/table first-appearance orders verified programmatically (submission_validation.txt: all PASS).

Verdict: **PASS**.
