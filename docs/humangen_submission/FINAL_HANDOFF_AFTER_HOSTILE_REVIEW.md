# FINAL_HANDOFF_AFTER_HOSTILE_REVIEW — Human Genetics

Manuscript: "Population structure defines the null expectation for pairwise genomic similarity: archaic-segment sharing across 66 human populations" — Tatsuki Onishi (Shiga University).
Target: Human Genetics (Springer Nature), Research Article, traditional route (no mandatory charges).
Date: 2026-10-14.

## 1. Final verdict: READY FOR SUBMISSION

## 2. Desk-reject risk: LOW-MODERATE

Residual risk is editorial appetite for a null-result inferential-framing paper, not a compliance or framing defect.

## 3. Top 5 residual risks

1. "Workflow application of MRQAP" judged incremental — mitigated by explicit novelty boundary.
2. Null-result editorial fatigue — mitigated by nominal-outlier contrast.
3. Pair-level permutation-residual P less standardised than coefficient QAP — defended textually; may draw statistical-review comments.
4. Sparse Denisovan signal outside Oceania — disclosed limitation.
5. Distance+coarse-indicator model called misspecified — robustness battery + directional argument cover it.

## 4. BLOCKING issues found and resolution

- **Figure 1 missing from the inline review manuscript** (Figures 2–5 embedded; Figure 1 cited in Methods was never inserted). FIXED: `create_humangen_submission.py` now inserts Figure 1 after the Methods "Analytical logic" paragraph in inline mode; rebuilt inline docx contains all 5 figures. No other blocking issues.

## 5. MAJOR issues found and resolution

- **Internal documentation errors**: first-pass `REFERENCE_AUDIT.md` and `HUMAN_GENETICS_CITATION_ECOLOGY.md` described references that are not in the bibliography (fabricated rows). FIXED: both rewritten against the actual 31-entry reference list and validator output.
- No MAJOR scientific issues found in the manuscript itself.

## 6. ANALYSIS-REQUIRING issues

| Issue | Publication-blocking? |
|---|---|
| Propagating per-population frequency sampling error into pair residuals | NO — nonessential; conclusion is a null |
| Dependence-explicit FDR alternatives beyond BH | NO — only bears on positive findings; none exist |
| Formal upper bound on pair-specific effect size | NO — useful but nonessential; claim is calibration |
| Mask-adjusted profiles | Impossible — no callable mask in source release (disclosed) |

## Files produced this pass (docs/humangen_submission/)

Reviews: `HUMAN_GENETICS_CURRENT_REQUIREMENTS_RECHECK.md`, `EDITORIAL_DESK_REVIEW.md`, `HOSTILE_REVIEW_POPULATION_GENETICS.md`, `HOSTILE_REVIEW_STATISTICAL_GENETICS.md`, `HOSTILE_REVIEW_NOVELTY_AND_CITATION.md`, `CLAIM_CALIBRATION_AUDIT_HUMAN_GENETICS.md`, `NEGATIVE_RESULT_INTERPRETATION_AUDIT.md`, `FIGURE_TABLE_HOSTILE_REVIEW.md`, `HUMAN_GENETICS_SUBMISSION_FORMAT_AUDIT.md`, `HUMAN_GENETICS_HOSTILE_REVIEW_SYNTHESIS.md`.
Corrected: `REFERENCE_AUDIT.md`, `HUMAN_GENETICS_CITATION_ECOLOGY.md`.
Final package: `HUMAN_GENETICS_*_FINAL.docx` (manuscript, inline manuscript with all 5 figures, title page, cover letter, supporting information) + `HUMAN_GENETICS_SUBMISSION_HOSTILE_REVIEWED_FINAL.zip`.
Prompt saved: `DEVIN_HUMAN_GENETICS_HOSTILE_REVIEW_PROMPT.txt`.

## Numbers verified unchanged

Numeric consistency check PASSED on rebuild; all frozen statistics identical (3,134/66/2,145; 62/1,891; r=−0.497/−0.462; partial −0.369/−0.326; QAP P=0.0001/0.0002; R² 0.2471/0.2131; z≤2.21/2.53; q≥0.78/0.82; ABO 1.78/64th/0.36 and 0.63/8th/0.92; 3,843/1,385 windows; 834/129/247 segments; 59/16/8 ancient).

## Author actions at submission

1. Enter declarations (author contribution, competing interests) via the submission interface.
2. Declare the bioRxiv preprint.
3. Use traditional (subscription) route — no mandatory charge.
