# HUMAN_GENETICS_HOSTILE_REVIEW_SYNTHESIS

Four-reviewer adversarial panel on the Human Genetics package + claim calibration + negative-result audit + figure/table + format audits.

## Issue table

| Issue | Reviewer | Severity | Location | Fix | New analysis? | Status |
|---|---|---|---|---|---|---|
| Null main result lowers priority | A (editor) | MINOR (residual) | — | Framing already maximised | No | Mitigated |
| "Workflow not method" novelty thin | A/D | MINOR | Intro ¶3, Discussion ¶2 | Honest bounds already stated | No | Mitigated |
| Figure 1 missing from inline manuscript | Format | BLOCKING (format) | inline docx | Insert Figure 1 after Methods Analytical-logic para | No | FIXED |
| Figure 1 internal label "demes, breeds, strains" | Format | MINOR | Figure 1 PNG | Regenerate figure — frozen | No | Documented, deferred |
| Pair-residual P less standardised than coefficient QAP | C | MINOR | Methods outliers | Text defensible as written | No | Accepted |
| Frequency sampling error not propagated to residuals | C | ANALYSIS-REQUIRING | Methods | Would need new analysis; nonessential for a null result | Yes (nonessential) | Documented |
| Dependence-explicit FDR alternatives | C | ANALYSIS-REQUIRING | Methods outliers | Only bears on positive findings | Yes (nonessential) | Documented |
| Centroid distances, panel heterogeneity, sparse Denisovan | B | MINOR | Discussion ¶6 | Limitations already stated | No | Mitigated |
| "Prespecified" ABO asserted not registered | B | MINOR | Methods | Standard for genre | No | Accepted |
| Formal upper bound on pair effect size | Neg-result | ANALYSIS-REQUIRING | Results §2 | Nonessential; claim is calibration | Yes (nonessential) | Documented |
| "Statements and Declarations" wrapper heading absent | Format | MINOR | Declarations | Individual headings acceptable per Springer | No | Accepted |
| Mantel 1967 no DOI | Format | MINOR | References | None exists; PubMed-verified | No | Resolved |
| Table 1 empty | Format | MINOR | Table 1 | Defensible: documents prespecified criterion | No | Accepted |
| REFERENCE_AUDIT/CITATION_ECOLOGY internal errors (wrong table contents) | Internal | MAJOR (docs only) | docs/ | Rewritten to match actual 31-entry bibliography | No | FIXED |

## TOP 5 REJECTION RISKS

1. **"Interesting but incremental" (probability: highest)** — a reviewer may judge the contribution a workflow application of MRQAP. Mitigated by explicit novelty boundary; residual: editorial appetite for framing contributions. Cannot be reduced further without new analysis.
2. **Null-result fatigue** — desk or review decision that a negative result lacks priority. Mitigated by nominal-outlier contrast (z≤2.53 → q≥0.78); residual: journal taste.
3. **Statistical-review depth** — pair-level permutation-residual P values are less standardised than coefficient QAP; a statistical reviewer may demand justification or alternative procedures. Mitigated by honest framing + conservative-direction argument; residual moderate.
4. **Sparse Denisovan inference** — calls sparse outside Oceania; may be read as underpowered for the Denisovan arm. Mitigated by union-window thresholds + disclosed limitation; residual low-moderate.
5. **Model-specification scepticism** — distance+coarse indicators may be called misspecified; a finer demographic null could shift residuals. Mitigated by robustness battery + "null is only as good as the structure it encodes"; residual low (would strengthen the null finding anyway).

## WHAT THE PAPER ACTUALLY CONTRIBUTES

- An operational definition of a structural null for pairwise genomic similarity (label-permutation preserving dyadic dependence).
- A pair-level residual test with prespecified support criterion and FDR control over ~1,900 human population pairs.
- First application to archaic-segment sharing across 66 human populations: similarity is distance-structured and no pair exceeds the null.
- A prespecified focal-locus evaluation (ABO) showing a repeatedly-invoked "exceptional" locus is unremarkable.
- Honest calibration discipline: nominal outliers exist but dissolve under the correct expectation.

## WHAT THE PAPER DOES NOT CLAIM

- A new permutation or regression method.
- A newly discovered fact that population structure biases inference.
- That any population pair lacks shared history or gene flow.
- That ABO has no archaic relationship (it removes one class of explanation only).
- Independent confirmatory tests in the robustness battery.

## Cover letter hostile review (condensed)

First paragraph communicates importance immediately: YES. Novelty clear within ~150 words: YES (¶3). Journal fit specific: YES (¶5 quotes scope areas). Negative result justified: YES (¶4). Generality overclaim: NO. Method-novelty overclaim: NO — explicitly disclaimed. First person singular throughout: YES. Stale Heredity language: NONE. Prior rejection mentioned: NO. "Similar pair" vs "exceptional relative to structure" distinction: explicitly drawn (¶4). No rewrite needed.
