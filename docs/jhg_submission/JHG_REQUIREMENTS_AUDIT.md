# JHG requirements audit (gate 0)

Audit date: 2026-11-08 (UTC). Sources were captured live in this session and archived privately under `data/raw/journal/` (SHA-256 values in `data/raw/journal/ACQUISITION_LEDGER.json`).

| Source | URL |
|---|---|
| JHG Guide to Authors v10 (revised 22 April 2026) | https://www.nature.com/documents/JHG_GTA_v10.pdf |
| JHG author page | https://www.nature.com/jhg/authors-and-referees/authors |
| JHG online submission instructions (MTS) | http://mts-jhg.nature.com/cgi-bin/main.plex?form_type=display_auth_instructions |
| JHG open-access fees page | https://www.nature.com/jhg/about/open-access |
| JHG journal information | https://www.nature.com/jhg/about |
| Springer Nature AI policy | https://www.nature.com/nature-portfolio/editorial-policies/ai |

| # | Requirement | Finding (source) | Implication for this manuscript |
|---|---|---|---|
| 1 | Article types | Article, Brief Communication, Review Article, Correspondence, Comment; Perspectives/special issues by invitation or consultation (GTA) | — |
| 2 | Appropriate type | **Article**: full primary research report (GTA) | Article |
| 3 | Abstract | Unstructured, ≤250 words (GTA) | Current abstract ≈245 words; keep ≤250 and unstructured |
| 4 | Main text | ≤5,000 words excluding abstract, references, figures and tables (GTA). One GTA table cell is ambiguous about the abstract, so the conservative check uses main text + abstract ≤5,000 | Source ≈4,523 + 245 words; **no destructive compression needed** |
| 5 | Figures/tables | ≤6 combined (GTA) | Source has 5 figures + 1 table = 6. Keep all six main items; S1–S7 and Table S1 stay in the SI |
| 6 | References | ≤50, Vancouver style, numbered in order of citation, ≤6 authors then et al., Index Medicus abbreviations, first and last pages (GTA) | 33 references (author-year in source) → convert to numbered Vancouver |
| 7 | Title page | Title (≤150 characters, must not state a conclusion), full author names, affiliations, corresponding author and e-mail, conflict-of-interest statement; running title filled in automatically (GTA/MTS) | Current title is a declarative statement → **must change** (see JHG_TITLE_DECISION.md) |
| 8 | Supplementary information | Peer reviewed, final form, the article must be self-contained without it; ≤50-word summary per file plus file format; the sentence "Supplementary information is available at Journal of Human Genetics's website" goes before the references; a **read-me file is required**; ≤8 files, ≤8 MB total, ≤1 MB per file (GTA) | Consolidate into a 3-file SI: SI document, data archive, read-me. Each file must be ≤1 MB |
| 9 | Data/code | Springer Nature research-data policy: deposit datasets in community repositories where mandated, otherwise make them available and disclose any access limits; new sequences need accession numbers (GTA/editorial policies) | No new sequence data. Cite Zenodo 14136628, Dryad 10.5061/dryad.zw3r228gg, the public GitHub repository and SI data. Claim no archive DOI that does not exist |
| 10 | AI/LLM | AI may support work but not replace human scholarly judgement. Assistive and evaluative use is permitted with disclosure; opaque use is not permitted; an AI tool cannot be an author (SN AI policy). JHG sets no exact wording | Keep the existing truthful disclosure unchanged in meaning |
| 11 | Peer review | Confidential and anonymous for reviewers; authors are not required to anonymise (GTA) | Title page carries author details; the manuscript body need not be anonymised |
| 12 | Cover letter | State that the work is original, unpublished and not under consideration elsewhere; name the corresponding author; reviewers may be suggested; include the COI statement; disclose any prior consideration or preprint if applicable (GTA/MTS) | New cover letter in first-person singular |
| 13 | Publication route | Subscription (traditional) or gold OA, chosen after acceptance (OA fees page) | Choose traditional |
| 14 | Traditional route available | Yes: "Authors can also choose to publish under the traditional publishing model (no APC charges apply)" (OA fees page) | — |
| 15 | Mandatory fees on traditional route | No APC (OA fees page). "There is no fee to reproduce colour figures in print or on the web" (GTA). No page charge or submission fee found in GTA/MTS/author page | **No financial blocker** |
| 16 | Optional OA APC | Current web page: £3590.00/$5490.00/€4190.00 plus VAT/local taxes, priced at the acceptance date. GTA PDF lists an older £3,060/$4,480/€3,580 | Optional only. Web page treated as authoritative; recheck at acceptance |
| 17 | Repository/self-archiving | Accepted manuscript may be self-archived 6 months after publication (author page) | — |
| — | House style | Double spacing, wide margins, page and continuous line numbers; spaces (not commas) as thousands separators; define abbreviations in both abstract and body; do not abbreviate terms used fewer than 4 times; ≤5 abbreviations advised; figure legends on a page titled "Titles and legends to figures" after the references; figures uploaded separately (TIFF/JPEG, CMYK/greyscale per MTS); each table in its own file; uploads ≤150 MB; 1–4 subject terms entered at submission | Apply in the builder |
| — | Ethics | Human-data studies need an ethics/consent statement (GTA) | Keep the secondary-use statement |

## Stop-rule assessment
The Article type allows 5,000 words of main text and 6 display items. The source manuscript fits without removing any scientific content, so **no JHG_FORMAT_BLOCKER_REPORT is needed** and the retarget proceeds.

## Financial assessment
No mandatory APC, page charge or colour charge applies on the traditional route. **No FINANCIAL BLOCKER.**
