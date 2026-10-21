# HOSTILE_REVIEW_POPULATION_GENETICS — skeptical human population geneticist

All manuscript locations refer to HUMAN_GENETICS_MAIN_MANUSCRIPT.docx section/paragraph.

1. **Interpretation of Neanderthal/Denisovan segment sharing.** Results §1 reports profile-correlation decay with distance and explicitly declines to infer event number/timing ("does not identify the timing, direction, or number of introgression events", Discussion ¶4). NO ISSUE.
2. **Is correlation of segment-frequency profiles biologically meaningful?** Methods "Population profiles": haplotype-presence frequencies per 500-kb window per population. Correlation across shared non-zero windows is a standard profile-similarity summary; limitations concede it conflates IBD/IBS (Discussion ¶6). NO ISSUE — meaning is statistical, not genealogical, and the text says so.
3. **Similarity conflated with shared descent?** Explicitly guarded: Methods "Correlations describe profile similarity and do not establish identity by descent"; Discussion ¶4 "not evidence that the populations in any pair lack a shared history." NO ISSUE.
4. **Geography overinterpreted?** The model is deliberately coarse ("coarse sensitivity covariates, not individual ancestry estimates or causal controls", Methods). Distance is the dominant structure but R² is called "descriptive". NO ISSUE.
5. **Population labels/centroids appropriate?** Disclosed limitation: "distances are centroid-based" (Discussion ¶6); zero-distance pairs excluded in sensitivity. MINOR — inherent to source metadata, handled.
6. **Source-panel heterogeneity (1000G vs HGDP)?** Same-dataset indicator included; per-dataset subsets reproduce the association (Results §3). MINOR residual — "captures technical heterogeneity only partially", already conceded.
7. **Recently admixed populations?** PUR/CLM/MXL/PEL designated, used as covariate in expanded model and excluded for outlier analysis; exclusion "strengthened" association, interpreted as mixture blurring the gradient. Correct handling. NO ISSUE.
8. **Are archaic calls comparable across panels?** Same hmmix call source (Zenodo 14136628) for both panels — harmonised by construction. NO ISSUE.
9. **Sparse Denisovan signal outside Oceania.** Conceded limitation; pair threshold (≥50 union windows) guards degenerate pairs; Denisovan results reported with same machinery. MINOR — coverage bias is inherent to the calls, disclosed.
10. **Is the structural expectation too coarse?** Distance+continent+dataset+admixture covariates only. A richer demographic model could shift residuals — but the paper's argument is that even this coarse null already absorbs every nominal outlier; a finer null only strengthens the conclusion direction. MINOR.
11. **Absence of outliers = low power?** Addressed directly: threshold z>2 + FDR over ~1,900 pairs detects only "a substantial excess"; "the largest observed residuals are better read as an upper bound" (Discussion ¶6). Honestly framed. NO ISSUE.
12. **z>2 + q<0.10 arbitrary?** Prespecified and conventional; results reported with all nominal ranks available for auditability. MINOR — any threshold is conventional; disclosure adequate.
13. **IBS/IBD/shared introgression/demographic similarity distinguished?** Methods (correlation ≠ IBD), Discussion ¶5 (alternatives incl. phased genealogies + IBS/IBD decomposition stated as needed). NO ISSUE.
14. **ABO justified as worked example?** Yes — prespecified focal locus repeatedly invoked in archaic-connection narratives (Calafell 2008, Condemi 2021); subordinate status stated twice. NO ISSUE.
15. **ABO post hoc risk?** Framed as prespecified in Abstract/Methods; rationale predates the analysis textually. MINOR residual — "prespecified" is asserted, not externally registered; common for this genre.
16. **Ancient vs present-day ABO separated?** "ancient and modern calls used different pipelines and were not directly compared statistically" (Methods); Figure S6 legend repeats it. NO ISSUE.
17. **Indigenous interpretation cautious?** CARE-framed ethics section; no community generalisation; no migration routes; minimal-level reporting. NO ISSUE.
18. **Route-specific claims absent?** Verified — "migration routes were not assigned from these data"; Figure S4 legend "not interpreted as a migration route". NO ISSUE.
19. **Negative result biologically informative?** Yes — reframes what "exceptional" means for human pairs; Discussion ¶1 states the expectation itself is the finding. NO ISSUE.
20. **Changes human population-genetic interpretation meaningfully?** Modestly — calibrates how similar-looking human pairs should be read; a discipline/contribution of method application, not new biology. Honest claim level. NO ISSUE.

## Severity summary

- BLOCKING: none. MAJOR: none.
- MINOR (4, all already mitigated in text): centroid distances; panel heterogeneity partial; sparse Denisovan signal; threshold conventionality + unregistered "prespecified" claim.
- Recommended fixes: NONE required — all mitigations already in the manuscript.
