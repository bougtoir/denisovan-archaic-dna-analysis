# Numeric reproducibility audit — Molecular Ecology package (2026-10-19)

Canonical sources: `data/analysis_provenance.json`, `data/correction_stats.json`, `data/abo_focal_test.json`, `data/pairwise_sharing_corrected.csv`, `data/model_summary.csv`, `data/abo_neanderthal_segments.csv`, `data/abo_population_summary.csv`, `data/ancient_abo_provenance.json`, `data/profile_quality_checks.csv`, `data/sensitivity_analysis.csv`, `data/window_size_sensitivity.csv`.

| Claim | Manuscript | Canonical source | Canonical value | Match? | Action |
|---|---|---|---|---|---|
| Individuals | 3,134 | analysis_provenance.individuals | 3134 | YES | none |
| Populations | 66 | analysis_provenance.included_populations | 66 | YES | none |
| Total pairs | 2,145 | analysis_provenance.population_pairs; pairwise CSV rows | 2145 | YES | none |
| Non-admixed populations | 62 | abo_focal_test.populations | 62 | YES | none |
| Non-admixed pairs | 1,891 | abo_focal_test.pairs; correction_stats.nonadmixed_pairs_tested | 1891 | YES | none |
| Neanderthal raw r | -0.497 | correction_stats.nean.raw_r | -0.49714 | YES | none |
| Denisovan raw r | -0.462 | correction_stats.deni.raw_r | -0.46166 | YES | none |
| Partial r | -0.369 / -0.326 | correction_stats partial_r | -0.36875 / -0.32591 | YES | none |
| Distance-only R² | 0.247 / 0.213 | correction_stats distance_only_r_squared | 0.24715 / 0.21313 | YES | none |
| Expanded R² | 0.546 / 0.511 | correction_stats expanded_r_squared | 0.54608 / 0.51129 | YES | none |
| QAP distance coefficients | -0.01892 / -0.01918 per 1,000 km | correction_stats distance_qap_beta; model_summary | -0.0189207 / -0.0191829 | YES | none |
| QAP P | 0.0001 / 0.0002 | correction_stats distance_qap_p | 0.0001 / 0.0002 | YES | none |
| Primary permutations | 9,999 | correction_stats.permutations | 9999 | YES | none |
| Sensitivity permutations | 999 | correction_stats.sensitivity_permutations; sensitivity CSV | 999 | YES | none |
| Largest residual z | 2.21 / 2.53 | max(nean_resid_z/deni_resid_z) in pairwise_sharing_corrected.csv | 2.21 / 2.53 | YES | none |
| Smallest BH q | 0.78 / 0.82 | min(*_fdr_pval) | 0.78 / 0.82 | YES | none |
| Supported pairs | 0 | correction_stats fdr_q_lt_0.10_positive_z_gt_2 | 0 / 0 | YES | none |
| Support criterion | z>2 and q<0.10 | manuscript/design | z>2 & q<0.10 | YES | none |
| ABO excess z | 1.78 / 0.63 | abo_focal_test max_excess_z | 1.7801 / 0.6346 | YES | none |
| ABO percentiles | 64th / 8th | abo_focal_test percentile | 64.30 / 8.01 | YES | none |
| ABO empirical P | 0.36 / 0.92 | abo_focal_test empirical_p | 0.35727 / 0.92058 | YES | none |
| Usable windows | 3,843 / 1,385 | abo_focal_test usable_windows | 3843 / 1385 | YES | none |
| ABO interval segments | 834 | abo_neanderthal_segments.csv rows | 834 | YES | none |
| Strict ABO overlap | 129 | strict_overlap==True count | 129 | YES | none |
| Tied max-reference similarity | 247 | closest_reference=='Tie' count | 247 | YES | none |
| Indigenous American carriers | 2 segments / 41 individuals (Pima 1/13, Maya 1/21, Colombian 0/7) | abo_population_summary.csv (HGDP Indigenous American pops) | 2 segments, 41 individuals | YES | none |
| Ancient individuals | 59 assessed / 16 with segment / 8 strict overlap | ancient_abo_provenance.json | 59 / 16 / 8 | YES | none |
| Window sizes | 500 kb primary; 250 kb / 1 Mb sensitivity | analysis_provenance.bin_size; window_size_sensitivity.csv | 500000; 250000/1000000 | YES | none |
| Min population size | 7 | analysis_provenance.minimum_population_size | 7 | YES | none |
| Min posterior probability | 0.8 | analysis_provenance.minimum_probability | 0.8 | YES | none |
| Union-window thresholds | >100 Nea / >50 Den | archaic_sharing_analysis.py defaults | 100 / 50 | YES | none |
| ABO gene coords | chr9:133,233,278-133,276,024 (GRCh38); interval 133.0-133.5 Mb | analyze_abo_window.py constants | 133233278-133276024; 133000000-133500000 | YES | none |
| Minimum nonzero populations (window usability) | ≥10 | abo_focal_test.py MINIMUM_NONZERO_POPULATIONS | 10 | YES | none |
| No population-window frequency > 1 | stated | profile_quality_checks.csv bins_over_one | 0 / 0 | YES | none |
| Cover-letter numbers | 3,134 / 66 / 2,145 | same canonical sources | identical | YES | none |
| Title-page word count | 4,523 | submission_validation.txt | 4523 | YES | none |

Verdict: **PASS** — every reported number matches the canonical machine-readable outputs; no transcription errors found.
