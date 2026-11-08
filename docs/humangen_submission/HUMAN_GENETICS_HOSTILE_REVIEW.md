# Hostile review — Human Genetics submission

Three adversarial perspectives applied to the retargeted package before submission. Verdicts: BLOCKING / MAJOR / MINOR / NO ISSUE.

## Reviewer A — Human Genetics editor (scope, fit, desk-rejection screen)

**A1. "This is a methods/comparative-evolution paper wearing a human-genetics costume." Is the human application substantive enough for Hum Genet?**
Verdict: NO ISSUE.
The dataset is entirely human: 3,134 individuals, 66 populations, 2,145 population pairs, archaic-segment calls from 1000 Genomes + HGDP. The question — whether an unusually similar pair of human populations is evidence of shared history or a structural artifact — is squarely human population/evolutionary genetics (a listed scope area). The retargeted Introduction now motivates the problem with human inference (non-independence of human population pairs, biobank-scale structure per Lawson et al. 2020) rather than cross-species analogies. The workflow is presented as needed "wherever human populations are compared pair by pair for unusual similarity in archaic ancestry or any genome-wide profile." Cross-species language in Discussion compressed to one closing sentence.

**A2. "The result is null — why publish a null in Hum Genet?"**
Verdict: MINOR (rebuttal-ready, not fixable by text edits and does not need to be).
Response: the null is the point of the paper — pairwise anomalies in archaic-ancestry sharing that look exceptional (up to |z| = 2.53, nominal P as small as ~0.01 uncorrected) are fully predicted by population structure alone (partial Mantel r = −0.326 to −0.369, QAP P ≤ 0.0002). Publishing the calibrated null prevents future overcalling; this is the explicit argument of the Introduction and Discussion. Editors regularly publish rigorous null results that correct an inferential practice.

**A3. ABO is a blood-group marker — is it human-genetics enough / not too clinical?**
Verdict: NO ISSUE.
ABO is presented strictly as a worked example of the dyadic method (one locus, previously reported archaic-ancestry enrichment, tested against the structural background), ~1 paragraph in Discussion. No clinical claims.

**A4. Compliance with submission format.**
Verdict: NO ISSUE — abstract 150–250 words, 6 keywords, ≤3 heading levels, Springer author-date references alphabetised with DOIs, title page carries acknowledgements, declarations present, .docx editable, figures separate.

## Reviewer B — human population geneticist (data, populations, interpretation)

**B1. "66 populations from 1000G+HGDP with 62 non-admixed is a standard panel — is anything new learned about these populations?"**
Verdict: MINOR.
Response: the contribution is not new population characterization but a new test on pairwise archaic-ancestry similarity and the demonstration that the structural null explains all candidate outliers. The manuscript is explicit about this boundary (Discussion novelty paragraph).

**B2. "Denisovan calls are sparse outside Oceania — is the Denisovan contrast meaningful?"**
Verdict: MINOR.
Already acknowledged as a limitation in Discussion ("Denisovan calls are sparse outside Oceania; precision is limited"). Estimates retained with this caveat; no overclaim of detection power.

**B3. "hmmix calls and a 500-kb grid — could segment-call error masquerade as structure?"**
Verdict: NO ISSUE.
Robustness analyses (window-size, minimum-call-threshold, profile-encoding variants) show the structural association is stable (Methods "Robustness analyses"; Results "robust to analytical choices"). The null model is fit to the same called data any outlier claim would use, so the calibration is internally consistent.

**B4. "Admixed populations were excluded — reasonable?"**
Verdict: NO ISSUE.
Exclusion is motivated and stated (data sources section); admixed genomes violate the fixed-population dyadic interpretation. Standard practice.

## Reviewer C — statistical geneticist (dyadic methods, testing)

**C1. "Partial Mantel/QAP is known to have inflated Type-I error in some regimes (Legendre & Fortin critiques). Why is it adequate here?"**
Verdict: NO ISSUE.
We do not claim novel validity; we use QAP exactly as the conservative standard for dyadic data, cite Legendre & Fortin (2010) and Legendre (2000), and crucially do not rely on the test to assert an effect — the test detects structure (the nuisance), and the substantive question is answered by the residual outlier scan: every nominally outlying pair's residual is within the null envelope after BH-FDR at 0.10 (min q = 0.78/0.82). Even if QAP calibration were imperfect, the conclusion (no exceptional pairs) is supported by the direction of the evidence.

**C2. "The distance covariate set may be misspecified — a better geographic/demographic model could change residuals."**
Verdict: MINOR.
Robustness analyses vary the covariates (distance-only, distance + differentiation proxies, alternative encodings) with consistent conclusions. Residual dependence on specification is an inherent limitation and is stated. Not fixable without new analysis; adequately bounded.

**C3. "Multiple testing across two windows/archaic sources and the ABO focal test — is the family properly defined?"**
Verdict: NO ISSUE.
BH-FDR is applied per pairwise outcome family (Neanderthal-or-Both, Denisovan-or-Both) over all tested pairs; the ABO focal test is a single prespecified locus-level test reported with its empirical null (z = 1.78, 64th percentile, P = 0.36; z = 0.63, 8th percentile, P = 0.92). Family definitions are stated in Methods.

**C4. "ABO sign convention ambiguity."**
Verdict: NO ISSUE.
Methods state the convention explicitly: excess similarity = predicted − observed absolute frequency difference, standardised; positive values indicate greater-than-expected similarity.

## Summary

- BLOCKING issues: none.
- MAJOR issues: none.
- MINOR issues: 3 (novelty-of-null framing, Denisovan sparsity, covariate specification) — all already handled by existing limitation/robustness text; no new analysis required or performed.
- Package may proceed to submission.
