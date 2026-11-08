# HOSTILE_REVIEW_STATISTICAL_GENETICS — skeptical statistical geneticist

1. **Estimand.** Pairwise profile-similarity residual from a descriptive dyadic regression; pair-level excess above the population-wide expectation. Clearly defined (Methods "Analytical logic", "Residual outliers"). NO ISSUE.
2. **Unit of analysis.** Population pair (dyad); populations are the repeated units. Correct. NO ISSUE.
3. **Non-independence structure.** Same populations recur across row/column — stated repeatedly with the row/column propagation explanation. NO ISSUE.
4. **Why ordinary pairwise inference is invalid.** Independence-based reference ignores shared-unit recurrence; bootstrap/resampling breaks structure (Intro ¶2). Correct. NO ISSUE.
5. **Why QAP is appropriate.** Joint row+column label permutation preserves dyadic dependence while breaking pair identity — standard for MRQAP (Krackhardt 1988; Dekker et al. 2007), cited. NO ISSUE.
6. **What QAP does/doesn't guarantee.** Text does not overclaim: "well described" limitations (Legendre & Fortin 2010; Guillot & Rousset 2013) and "sensitivity intervals rather than independent-sample confidence intervals". NO ISSUE.
7. **Permutation scheme correct?** Same random label order applied to rows and columns of the response matrix, refit each iteration, +1 correction, two-sided coefficient P. Correct MRQAP form. NO ISSUE.
8. **Same permutation supporting both coefficient and residual inference?** Joint label permutation generates both nulls coherently — the standard joint-null argument; stated. MINOR — strictly, pair-residual empirical P under matrix permutation is less standard than coefficient QAP; flagged below (#9).
9. **Pair-level residual P values well-defined?** Each pair's residual referred to its own permutation-residual null across 9,999 relabellings. Defensible as an empirical null; pair-level QAP-residual testing is less standardised than coefficient-level — MINOR; disclosed as descriptive ("This comparison is descriptive of the observed matrix" applies to ABO; for pair residuals the framing is a support criterion z>2+q<0.10, not a formal per-pair test claim). Acceptable but a reviewer may press it; TEXT-defensible as written.
10. **BH FDR defensible under dependence?** BH valid under positive regression dependence (PRDS) but pair-level permutation P values under dyadic dependence are not guaranteed PRDS — however the text's operative claim is directional: no pair qualified, so any stricter procedure gives the same empty set. Correctly argued. NO ISSUE.
11. **Overstates dependence-aware FDR validity?** No — see #10; the claim relies on observed emptiness, not on asymptotic validity. NO ISSUE.
12. **"Stricter procedures would only strengthen the absence"** (Methods, Residual outliers). Logically sound for monotone stricter rejection rules applied to identical P values. MINOR — true given the observed configuration; keep as written.
13. **Population-deletion intervals correctly described?** Yes — "sensitivity intervals rather than independent-sample confidence intervals". NO ISSUE.
14. **Partial correlations vs regression coefficients distinguished?** Results report "partial distance correlations" and coefficient values separately with consistent labels. NO ISSUE.
15. **R-squared overinterpreted?** "Descriptive R-squared values quantify fit... not interpreted as independent observations or causal variance explained". NO ISSUE.
16. **Same-continent/dataset/admixture indicators too crude?** Labelled "coarse sensitivity covariates, not causal controls". Honest. MINOR — crude by design, disclosed.
17. **Distance model misspecified?** Possible (nonlinear IBD patterns), but residuals are the point and alternatives were sensitivity-checked; concede structural-null caveat ("only as good as the structure it encodes", Discussion ¶6). MINOR.
18. **Linearity assumed inappropriately?** Distance-decay is visibly monotone in Figure 2; a linear working model is descriptive, not mechanistic. MINOR.
19. **Pearson across non-zero union windows induces bias?** Union-window conditioning could inflate correlation (shared zeros excluded); addressed by full-window Pearson + Jaccard sensitivities (Methods Robustness; Results §3). NO ISSUE — handled.
20. **Alternative metrics adequate?** Spearman, cosine, full-window Pearson, Jaccard all reproduce the association. NO ISSUE.
21. **Unequal sample sizes distort frequencies?** Minimum population size 7 (sensitivities at 10/15/20 reproduce results). MINOR residual — small-n frequency noise exists, sensitivity-tested.
22. **Finite sampling uncertainty ignored?** Frequencies are ratios; per-population sampling error is not propagated into residuals. MINOR — sensitivity tiers (min N) partially cover it; propagation would be ANALYSIS-REQUIRING and is nonessential because the conclusion is a null.
23. **Residual z incorporates uncertainty?** Standardised by residual SD + permutation null — reasonable empirical standardisation; does not incorporate profile-frequency sampling error (see #22). MINOR.
24. **ABO focal-window genome-wide comparison coherent?** Per-window max standardised excess across windows with calls in ≥10 populations; ABO window's percentile/P reported. Coherent descriptive comparison; labelled "not a substitute for the pair-level permutation test". NO ISSUE.
25. **ABO residual sign correct?** Excess = predicted − observed absolute difference; positive = more similar. Stated exactly in Methods. NO ISSUE.
26. **Empirical P correctly defined?** Position of ABO-window max within genome-wide background distribution; one-sided proportion. Correct. NO ISSUE.
27. **Multiple-testing family level?** BH applied jointly within each ancestry over all non-admixed pairs — appropriate primary family; ABO focal test reported singly (defensible for a prespecified single-window comparison). MINOR — a strict reviewer could ask for a wider family; descriptive framing covers it.
28. **"Structural null" valid term?** Defined operationally and hedged ("only as good as the structure it encodes"). Acceptable coinage, clearly bounded. NO ISSUE.
29. **Merely MRQAP application?** Substantively yes — and the paper says so ("we do not propose a new permutation method"). Contribution is the inferential framing + pair-level residual machinery + application; honest. MINOR — the residual-inference layer is the thin part of the novelty.
30. **Any statistical claim exceeding the procedure?** None found after full-text scan; every strong statement is hedged at its source.

## Severity summary

- BLOCKING: none. MAJOR: none.
- MINOR (7): pair-residual P less standardised than coefficient QAP (defensible as written); #12 monotone-stricter argument (sound); crude covariates; model misspecification/linearity; sampling-error propagation (→ ANALYSIS-REQUIRING if demanded, nonessential); threshold/family conventions.
- ANALYSIS-REQUIRING (nonessential): propagating per-population frequency sampling error into residuals; dependence-explicit FDR alternatives — both would only bear on a positive-finding claim, not this null result.
