# Consistency repair report

## A. Input files (authoritative sources)

1. `data_detail.docx` (delivered as `data_detail(1).docx`)
2. `data.zip`
3. `manuscript_heredity_inline.docx`
4. `supporting_information_heredity.docx`

No other manuscript version, supplement, handoff note or cached summary was used as an authoritative source.

## B. Archive inventory

`data.zip` contains 25 ZIP entries: one directory entry (`data/`), one documentation file (`README_DATA.md`) and 23 data files under `data/`.

Formal Supplementary Data 1-10 (cited as such in the Supporting Information):

| Supplementary Data | File |
| --- | --- |
| 1 | data/population_metadata.csv |
| 2 | data/pairwise_sharing_corrected.csv |
| 3 | data/model_summary.csv |
| 4 | data/sensitivity_analysis.csv |
| 5 | data/window_size_sensitivity.csv |
| 6 | data/profile_quality_checks.csv |
| 7 | data/abo_focal_test.json |
| 8 | data/ancient_abo_summary.csv |
| 9 | data/ancient_abo_provenance.json |
| 10 | data/analysis_provenance.json |

Additional derived intermediate and auxiliary files (13), retained for reproducibility and auditability:

data/population_profiles_500kb.npz, data/pairwise_sharing.csv, data/correction_stats.json, data/correction_stats.txt, data/enhanced_statistics.csv, data/neanderthal_outliers.csv, data/denisovan_outliers.csv, data/outlier_summary.csv, data/abo_neanderthal_segments.csv, data/abo_denisovan_segments.csv, data/abo_population_summary.csv, data/abo_sublineage_summary.csv, data/o2_frequency_summary.csv.

Documentation: README_DATA.md.

## C. Corrections made

### C1. Supporting Information, Supplementary File Inventory

**Supplementary Data 5 (`window_size_sensitivity.csv`)**
- Original: "Window-size robustness summary for the focal-locus scan, reporting the ABO statistic and its genome-wide percentile across alternative window widths."
- Corrected: "Robustness of the population-wide geographic-distance association at 250-kb, 500-kb, and 1-Mb genomic window sizes, reporting for each ancestry the raw distance correlation, the quadratic assignment procedure distance coefficient, the two-sided permutation P value, the descriptive R-squared value, and the number of permutations."
- Reason: the file contains no ABO focal-window result.
- Verified against: `data/window_size_sensitivity.csv` (fields `window_size_bp`, `ancestry`, `populations`, `pairs`, `raw_distance_r`, `distance_qap_beta`, `distance_qap_p_two_sided`, `distance_only_r_squared`, `qap_permutations`; six rows at 250 kb, 500 kb and 1 Mb).

**Supplementary Data 6 (`profile_quality_checks.csv`)**
- Original: "Per-population quality summaries of the archaic-segment profiles: segment counts, callable coverage, profile totals, and the checks used to exclude unusable populations."
- Corrected: "Ancestry-level profile quality checks reporting the maximum observed population-window frequency, the number of bins exceeding one, and the number of non-zero population-window entries."
- Reason: the file is ancestry-level (two rows), not per-population, and contains none of the named fields.
- Verified against: `data/profile_quality_checks.csv` (fields `ancestry`, `maximum_frequency`, `bins_over_one`, `nonzero_population_bins`).

**Supplementary Data 8 (`ancient_abo_summary.csv`)**
- Original: "Published archaic and ancient ABO blood-group state calls used only as narrative context in the Discussion; no analysis result depends on this file."
- Corrected: an ancient-individual archaic-segment summary for the ABO interval (59 ancient individuals; age, population, region, closest archaic reference, reference proportions, segment-detection status, strict ABO gene overlap), descriptive only, different pipeline from the present-day profiles, no analysis result depends on it.
- Reason: the file contains no ABO blood-group state calls; it contains segment-detection records derived from the published Neanderthal-segment catalogue.
- Verified against: `data/ancient_abo_summary.csv` (59 rows; fields `individual`, `age_kya`, `population`, `region`, `closest_reference`, `altai_proportion`, `vindija_proportion`, `chagyrskaya_proportion`, `denisova_proportion`, `all_reads`, `segment_detected`, `strict_abo_overlap`, `source_doi`, `provenance_note`).

**Supplementary Data 9 (`ancient_abo_provenance.json`)**
- Original: "Source publications, accessions, and retrieval records for the ancient ABO context table."
- Corrected: source publication and source data DOIs, GRCh37/hg19 genome build, ABO gene and window coordinates, diagnostic-site and genetic-map settings, source file names with SHA-256 checksums, and counts of ancient individuals assessed / with a detected segment / with strict ABO overlap.
- Reason: the file holds no accessions and no retrieval records.
- Verified against: `data/ancient_abo_provenance.json`.

**Supplementary Data 10 (`analysis_provenance.json`)**
- Original: "Input file names, SHA-256 checksums, software versions, random seeds, and counts of individuals, populations, and pairs for the committed analysis."
- Corrected: analysis release, analysis code commit, input file names with SHA-256 checksums, minimum segment probability and minimum population size, genomic bin size, frequency definition, and final counts of individuals, populations and population pairs.
- Reason: the file holds no software versions and no random seeds.
- Verified against: `data/analysis_provenance.json`.

**New clarification paragraph** added after Supplementary Data 10, stating that Supplementary Data 1-10 are the formal machine-readable supplementary files and that the archive additionally contains 13 derived intermediate and auxiliary files plus `README_DATA.md`.
- Verified against: the ZIP listing of `data.zip`.

Supplementary Data 1-4 and 7 were checked field by field and left unchanged; Figures S1-S7, Table S1, its note and all figure captions were left unchanged.

### C2. Data detail document (`data_detail_consistent.docx`)

1. Overstated reproducibility claim removed. Original: file names "match the names used in the manuscript ... so a reader can place this data/ directory at the root of a clone of that repository and rerun the document and figure builds without any further download." Corrected: the archive holds 23 files under `data/` plus this documentation file; ten are the formal Supplementary Data 1-10 and 13 are additional derived intermediate and auxiliary files. A separate paragraph now distinguishes recomputing the reported summary values from the included derived files versus rerunning the complete upstream analysis, which requires downloading the two large source segment files from Zenodo record 14136628.
2. `analysis_provenance.json` description extended to the fields actually present (analysis release, code commit, minimum segment probability, minimum population size, frequency definition).
3. `enhanced_statistics.csv` description corrected: it holds exploratory uncorrected statistics (for example `nean_dist_r` = -0.4847, `nean_partial_r` = -0.1890) that are not the values reported in the manuscript; the reported values come from `correction_stats.json`, `model_summary.csv` and `pairwise_sharing_corrected.csv`.
4. `profile_quality_checks.csv` described as ancestry-level checks with the three fields actually present ("per-ancestry frequency range checks confirming no frequency exceeds one" was incomplete).
5. `neanderthal_outliers.csv` / `denisovan_outliers.csv` described as descriptive distance-only residual rankings (99 and 118 rows, maximum z 2.142 and 2.194) and explicitly separated from the dependence-aware residuals used for the reported test.
6. `outlier_summary.csv` described as the record layout for Table 1 that contains the header row only, because no pair met z>2 together with q<0.10. Original wording ("the pairs reported in Table 1, with the full covariate and residual record") implied data rows.
7. `window_size_sensitivity.csv` described as the population-wide distance association across window sizes.
8. `ancient_abo_summary.csv` / `ancient_abo_provenance.json` description extended with the actual counts (59 assessed, 16 with a detected segment, 8 with strict ABO overlap) and the different-pipeline caution.
9. A list of the formal Supplementary Data 1-10 file names was added.

### C3. `README_DATA.md` inside the archive

The same corrections as C2 items 1, 2, 3, 4, 5, 6, 7 and 8 were applied to `README_DATA.md`, which is documentation only. No scientific data file in the archive was modified.

### C4. Manuscript

No manuscript correction was necessary. Every value and count checked below already agrees with the machine-readable files, and no data file name in the manuscript is misspelled or absent. `manuscript_heredity_inline_consistent.docx` is a validated copy with identical scientific text.

## D. Scientific freeze confirmation

- Any numerical analysis output changed: NO
- Any P value changed: NO
- Any q value changed: NO
- Any z score changed: NO
- Any sample, population or pair count changed: NO
- Any figure or table value changed: NO
- Any data file inside the archive changed: NO (all 23 data files are byte-identical; only `README_DATA.md` documentation text changed)

## E. Key numerical cross-check

| Quantity | Value | Machine-readable source |
| --- | --- | --- |
| Individuals | 3,134 | analysis_provenance.json; sum of population_metadata.csv `n_individuals` |
| Populations | 66 | analysis_provenance.json; population_metadata.csv (66 rows, all included) |
| Total pairs | 2,145 | analysis_provenance.json; pairwise_sharing.csv and pairwise_sharing_corrected.csv (2,145 rows) |
| Non-admixed populations / pairs | 62 / 1,891 | pairwise_sharing_corrected.csv (`any_admixed` = 0); correction_stats.json; abo_focal_test.json |
| Neanderthal raw distance r | -0.497 | correction_stats.json (-0.49713856388371713) |
| Denisovan raw distance r | -0.462 | correction_stats.json (-0.46166392962508196) |
| Partial distance correlations | -0.369 / -0.326 | correction_stats.json |
| Distance QAP P values | 0.0001 / 0.0002 | correction_stats.json; model_summary.csv |
| Distance-only R-squared | 0.2471 / 0.2131 | correction_stats.json; model_summary.csv |
| Largest positive residual z (non-admixed) | 2.21 / 2.53 | pairwise_sharing_corrected.csv (2.213868912624981 / 2.532988089971604) |
| Smallest BH q (non-admixed) | 0.78 / 0.82 | pairwise_sharing_corrected.csv (0.7830218994413408 / 0.818065592064476) |
| Pairs with z>2 and q<0.10 | 0 | pairwise_sharing_corrected.csv; correction_stats.json; outlier_summary.csv (header only) |
| ABO Neanderthal z / percentile / P | 1.78 / 64th / 0.36 | abo_focal_test.json (1.7800778543670575 / 64.29872495446266 / 0.3572729638303409) |
| ABO Denisovan z / percentile / P | 0.63 / 8th / 0.92 | abo_focal_test.json (0.6345965040702676 / 8.014440433212997 / 0.9205776173285198) |
| ABO usable windows | 3,843 / 1,385 | abo_focal_test.json |
| ABO-window Neanderthal or Both segments | 834 (129 strict overlap, 247 ties) | abo_neanderthal_segments.csv |
| Indigenous American ABO-window segments | 2 of 41 represented individuals | abo_population_summary.csv (Colombian 7, Maya 21, Pima 13; 1 + 1 segments) |
| Windows in the profile matrix | 5,760 (66 x 5,760) | population_profiles_500kb.npz |
| Ancient individuals | 59 assessed, 16 with segment, 8 strict overlap | ancient_abo_summary.csv; ancient_abo_provenance.json |

Table S1 was recomputed from `abo_sublineage_summary.csv` using the three-reference denominator with equal ties excluded: East Asia n=57 (54.4 / 1.8 / 43.9), Europe n=275 (7.3 / 46.5 / 46.2), Indigenous Americas n=2 (0.0 / 100.0 / 0.0), Admixed Americas n=98 (3.1 / 61.2 / 35.7), Central/South Asia n=98 (9.2 / 44.9 / 45.9), Middle East n=44 (11.4 / 52.3 / 36.4), Oceania n=13 (0.0 / 0.0 / 100.0). All values match Table S1 exactly.

Provenance cross-check: Zenodo record 14136628 and the two SHA-256 checksums in the data detail document match `analysis_provenance.json`; the Dryad DOI 10.5061/dryad.zw3r228gg, the source article DOI 10.1126/science.adq3010 and the GRCh37/hg19 build match `ancient_abo_provenance.json`.

## F. Supplementary inventory check

Supplementary Data 5, 6, 8, 9 and 10 now describe their actual files correctly, field by field, and no longer refer to an ABO statistic across window sizes, per-population quality checks, ABO blood-group state calls, accessions, retrieval records, software versions or random seeds.

## G. Final verdict

CONSISTENCY CHECK = PASS
