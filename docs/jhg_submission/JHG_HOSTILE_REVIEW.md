# Hostile review before final QC (JHG)

Classes: BLOCKING / MAJOR / MINOR / NO ISSUE. All BLOCKING and MAJOR items were fixed without new analysis.

## 1. JHG editor
| Issue | Class | Action |
|---|---|---|
| Molecular Ecology version used author-year citations; JHG requires Vancouver | BLOCKING | Fixed: numbered superscripts in order of first appearance, 31 refs |
| The source title read as an ecology methods paper for many species | MAJOR | Fixed: new neutral human-genetics title (114 chars) |
| Figures embedded in the manuscript | MAJOR | Fixed: separate TIFF files; legends on their own page |
| 10+ supplementary files, above the 8-file cap | MAJOR | Fixed: consolidated to 3 files (DOCX 0.50 MB, ZIP 0.39 MB, README), each below 1 MB |
| Comma thousands separators | MAJOR | Fixed: spaces (house style), checked automatically |
| Required sentence "Supplementary information is available at Journal of Human Genetics's website" missing | MAJOR | Fixed |
| Section order (Data Availability before Acknowledgements; JHG lists Acknowledgements, Conflict of Interest, References) | MINOR | Acknowledgements, Funding, Conflict of Interest, Ethics, Author Contributions, and AI declaration all precede the References |
| Single author writes "we" in the manuscript (the cover letter uses "I") | MINOR | Fixed in the single-author voice pass: authorial plurals converted to neutral, passive, or "I" (`JHG_SINGLE_AUTHOR_VOICE_AUDIT.md`). |
| Abbreviations (ABO, QAP, HGDP, FDR) | NO ISSUE | 4 abbreviations, each defined at first use, within the advised ~5 |
## 2. Human population geneticist
| Issue | Class | Action |
|---|---|---|
| Is "structure explains pairwise similarity" just isolation by distance restated? | MAJOR | Fixed in framing: the Introduction says IBD is established, and the contribution is the pair-level residual test |
| Admixed American populations | NO ISSUE | Non-admixed sensitivity (62 populations, 1 891 pairs) already reported |
| Indigenous data governance | NO ISSUE | CARE/Claw statements kept; no route assignment |
## 3. Statistical geneticist
| Issue | Class | Action |
|---|---|---|
| Residuals are conditional on the fitted structural model | MAJOR | Stated explicitly in Methods and Discussion (as in the audited source) |
| Power for modest pair effects | MAJOR (interpretation) | Handled as a stated limitation. No power analysis added (scientific freeze). |
| Mantel/QAP caveats (Guillot & Rousset) | NO ISSUE | Cited; the claims are about permutation-calibrated dependence only |
| BH across dependent pairs | MINOR | Already discussed as a conservative screening rule; unchanged |
## 4. Human evolution reader
| Issue | Class | Action |
|---|---|---|
| Does a negative test deny archaic gene flow history? | MAJOR | Fixed in wording: "no supported excess does not mean no shared history" is in the Abstract and Discussion |
| ABO overemphasised? | MINOR | ABO stays a prespecified focal example in one Results subsection; title and abstract lead with the general problem |

Residual BLOCKING/MAJOR: none.
