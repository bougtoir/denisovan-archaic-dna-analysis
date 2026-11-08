# HOSTILE_REVIEW_NOVELTY_AND_CITATION — hostile literature reviewer

## Closest prior studies (reassessed from scratch)

| Study | Question | Data | Method | Estimand | Result | Overlap | Residual novelty |
|---|---|---|---|---|---|---|---|
| Mazet et al. 2016 (Heredity 116:362) | Does unmodelled structure bias ancestral size inference? | Simulated + human genomic | IICR/coalescent | Size-change signal under structure | Spurious size changes | Conceptual motivation only | Our target is pairwise similarity, not model-based demography |
| Tournebize & Chikhi 2025 (Nat Ecol Evol 9:225) | Do structured histories fake admixture events? | Hominin genomic | PSMC-style models | Spurious admixture inference | Structure creates false admixture | Same "structure misleads" family | They test demographic-model outputs; we test pair-level similarity claims |
| Ortega-Del Vecchyo & Slatkin 2019 (Heredity 122:711) | How to read FST between archaic and modern? | Archaic + modern genomes | FST under demographic models | Divergence statistic | Context-dependent | Adjacent | Not a pairwise-similarity null |
| Krackhardt 1988 / Dekker et al. 2007 (MRQAP) | Regression on dyadic data | Network data | QAP permutation | Coefficient nulls | Machinery | Supplies our method | We add the pair-level residual layer + human-genomic application |
| Legendre & Fortin 2010 / Guillot & Rousset 2013 | Validity of Mantel-type tests in spatial genetics | Simulated | Permutation-test critique | Type-I error | Cautions | Constraint on us, not competition | — |
| Sankararaman et al. 2014/2016 | Landscape of archaic ancestry | 1000G etc. | Archaic segment inference | Ancestry maps | Global archaic landscape | Data-domain, no null for pairs | — |
| Jacobs et al. 2019 (Cell 177) | Denisovan ancestries in Papuans | Papuan genomes | Introgression modelling | Multiple Denisovan sources | Deep divergence | Pair-specific story example we test against | — |
| Skov et al. 2018 (hmmix) | Detect archaic segments w/o outgroup | Archaic calls | HMM | Segment calls | Call generation | Source data | — |
| Lawson et al. 2020 (Hum Genet 139:23) | Does subtle structure still matter? | UK Biobank | Review/analyses | Bias at scale | Structure biases GWAS/polygenic | Human-genetics anchor | We formalise the pairwise-similarity case they don't treat |
| Iasi et al. 2024 (Science 386) | Neanderthal ancestry over time | Ancient + present-day | Segment dating | Temporal archaic dynamics | Time-resolved ancestry | Source of ancient ABO data only | — |

## Answers

1. **"Structural null for pairwise genomic similarity" new as framing?** YES — no located study names or operationalises the pair-level expectation test this way; the components are old, the composite test is new.
2. **Same workflow already published?** NO — joint label-permutation + pair-level residual outlier testing + FDR on archaic-sharing profiles is not found in prior art.
3. **Novelty mainly?** Inferential framing + workflow + application (NOT method, NOT biological result). Correctly stated in text.
4. **Honest about novelty level?** YES — "we do not propose a new permutation method"; "the structural insight about population structure is not ours". Cannot be accused of overclaiming.
5. **Missing citations a reviewer would demand?** Checked: Mantel, Krackhardt/MRQAP, Dekker et al., Legendre & Fortin, Guillot & Rousset, Mazet, Tournebize & Chikhi, Ortega-Del Vecchyo & Slatkin, Sankararaman x2, Jacobs, Skov, hmmix lineage, Iasi, Calafell, Condemi, Halverson & Bolnick, Segurel, Petr, Prüfer, Ohashi, Claw, Carroll, Green, Reich, Bergström, 1000G, Benjamini & Hochberg, Wright, Rousset, Lawson et al., Quilodran — the demanded set is covered. No obvious missing demand.
6. **Human Genetics bibliographic neighborhood?** YES — Calafell 2008 and Lawson 2020 are Hum Genet; the journal routinely publishes population/evolutionary-genetics analyses; neighborhood is real, not gamed.
7. **Journal-gaming citations?** NO — Lawson 2020 supports a specific biobank-scale bias claim (Intro ¶4, Discussion ¶2); Calafell 2008 supports the ABO archaic-reading precedent. Both load-bearing.
8. **Hum Genet paper cited without supporting a claim?** NO.
9. **Cover letter overstates novelty?** NO — ¶3 explicitly disclaims new-method and new-insight claims ("I do not claim a new permutation method, and I do not claim that population-structure bias is newly discovered").

## Verdict

No substantially overlapping prior art. Novelty = inferential framing + operational workflow + first application to archaic pairwise similarity in humans. NOT BLOCKING. No missing demanded citations.
