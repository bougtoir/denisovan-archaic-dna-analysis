# Closest prior studies and novelty boundary (JHG)

| Prior work | What it established | How this manuscript differs |
|---|---|---|
| Mantel 1967; Krackhardt 1988; Dekker et al. 2007 | Permutation/QAP inference for dyadic matrices | Uses these methods; **no new algorithm is claimed** |
| Legendre & Fortin 2010; Guillot & Rousset 2013 | Limits of Mantel-type tests under spatial autocorrelation | Cited as caveats. Residual testing is framed as conditional on the fitted structure. |
| Wright 1943; Rousset 1997 | Isolation by distance | Supplies the structural expectation and is **not presented as a discovery** |
| Sankararaman et al. 2014, 2016; Skov et al. 2018; Iasi et al. 2024 | Maps of archaic ancestry; hmmix segment calls | Data source and empirical system. **No new introgression event is claimed.** |
| Quilodrán et al. 2023 | Expansions shaped the spatial pattern of Neanderthal ancestry | Closest work on population-level spatial structure. The present work asks whether any *pair* exceeds that structure. |
| Mazet et al. 2016; Tournebize & Chikhi 2025; Lawson et al. 2020 | Unmodelled structure creates spurious signals | Motivates the structural null. The present work applies that logic to pairwise similarity matrices. |
| Calafell et al. 2008; Ségurel et al. 2012; Condemi et al. 2021 | ABO deep polymorphism / archaic ABO | ABO is a prespecified example. **No new ABO evolutionary claim is made.** |

Contribution, stated honestly: an explicit workflow for pair-specific excess in archaic-segment profiles. It combines a structural null (distance plus covariates), label-permutation QAP that keeps the dependence among pairs, standardised pair residuals, and BH-FDR across all 2 145 pairs. It is applied to 3 134 individuals in 66 populations. The workflow is new in this application; the methods it uses are not.
