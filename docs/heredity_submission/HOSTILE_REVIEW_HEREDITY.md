# Hostile review of the restructured Heredity submission

Review carried out against the generated `manuscript_heredity.docx`, the figure set, and the committed data files, adopting the position of a sceptical population-genetics referee who is willing to recommend rejection.

Severity scale: **H** blocking, **M** should be fixed, **L** optional.

## H1. "ABO does not exceed the genome-wide structural background" was asserted, not tested

The earlier draft reported ABO-window segment counts and then concluded that they do not exceed the genome-wide structural expectation. No statistic compared the window with the rest of the genome, so the section heading promised a test that the text did not perform. A referee would treat this as an unsupported claim in the paper's most contested section.

**Resolved.** A prespecified focal-window test was added (`scripts/abo_window_focal_test.py`). For every 500-kb window, the absolute between-population difference in archaic-segment frequency across the 1,891 non-admixed pairs is regressed on geographic distance, residuals are standardised so that a large positive value marks the pair that is more similar than geography predicts, and the per-window maximum is taken. The genome-wide distribution of these maxima is the background. The ABO window sits at the 64th percentile of 3,843 comparable windows for Neanderthal profiles (z=1.78, empirical P=0.36) and at the 8th percentile of 1,385 windows for Denisovan profiles (z=0.63, empirical P=0.92). The Methods now describe the test, the Results report it, and the numbers are read from `data/abo_focal_test.json` rather than written into the text.

## H2. A null result could be read as evidence that the populations are unrelated

Interpreting "no pair exceeds the structural expectation" as "no historical connection" would be a serious inferential error, and the earlier Discussion did not close that door explicitly.

**Resolved.** The Discussion now states that finding no pair with excess similarity is evidence against pair-specific explanations beyond population-wide structure, not evidence that a pair lacks shared history, and notes that populations connected by real contact will often be exactly as similar as broad structure predicts because that contact helped produce the structure.

## H3. The conceptual figure could be mistaken for data

Figure 1 contains an illustrative distribution. If read as an empirical result it would misrepresent the analysis.

**Resolved.** The legend states that panels a-d are schematic illustrations and do not display analysis results, and the panel notes in the figure repeat this.

## M1. Novelty could be read as a claim to have invented QAP

**Resolved.** The Introduction states explicitly that no new permutation method is proposed and that the contribution is the inferential framing and the workflow, with Mantel (1967), Krackhardt (1988) and Dekker et al. (2007) credited and the known limitations of matrix permutation tests cited (Legendre and Fortin 2010; Guillot and Rousset 2013).

## M2. Power of the pair-level test was not discussed

With a two-standard-deviation threshold plus false-discovery-rate control across 1,891 pairs, only a substantial excess is detectable. A referee would object that the negative result may reflect low power.

**Resolved.** The Discussion now states that the test is deliberately conservative, that a real but modest pair-specific effect would not be recovered, and that the largest observed residuals are best read as an upper bound rather than a refutation.

## M3. Covariates could be read as causal adjustment

**Resolved.** The Discussion states that the descriptive R-squared values and the coarse continent, dataset and recent-admixture indicators describe the observed matrix and are not causal adjustment.

## M4. Robustness section risked being read as independent confirmation

Repeating the same association under many analytical variants is not independent evidence.

**Resolved.** The Results state that these are robustness checks on one structural pattern rather than independent confirmatory tests, and the detailed grids are in Supporting Information.

## M5. Generality was asserted for a human-only analysis

**Resolved.** The Discussion names the systems in which the same non-independence arises (conservation genetics, hybrid zones, crop landraces and livestock breeds, microbial strains, simulated demes), states the three transferable ingredients, and then states that a structural null is only as good as the structure it encodes and that a null result in one system does not generalise to others.

## L1. Geographic distance is the only structural axis modelled

Acknowledged in the Discussion. Modelling additional structure (drift-based or admixture-graph distances) is identified as a direction rather than attempted here, which keeps the analysis frozen as intended.

## L2. Centroid coordinates, no common callable mask, identity by state versus identity by descent

Retained in the limitations paragraph.

## Checks that did not raise objections

- Every figure and table is cited in the text, and first appearances run 1-5 for main figures, S1-S7 for supporting figures, and 1 for the single table.
- All 27 references are cited, alphabetised, and resolve against Crossref or PubMed.
- Every numeric value in the manuscript traces to `correction_stats.json`, `analysis_provenance.json`, `abo_focal_test.json`, or `pairwise_sharing_corrected.csv`; none is written into the text by hand.
- No "previous version" or "earlier analysis" framing appears anywhere in the manuscript.
- No CJK or full-width characters; equations are native Word objects.
