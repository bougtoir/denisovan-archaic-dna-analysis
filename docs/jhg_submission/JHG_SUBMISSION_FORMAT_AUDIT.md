# JHG submission format audit

| Requirement (GTA v10 / MTS instructions) | Status | Evidence |
|---|---|---|
| Article type: Article | PASS | Full primary research report |
| Title <=150 chars, not a conclusion | PASS | 114 chars |
| Unstructured abstract <=250 words | PASS | 239 words |
| Main text <=5 000 words (excl. abstract, refs, legends, tables) | PASS | 4 045 (4 284 including the abstract) |
| <=6 figures + tables | PASS | 5 figures + Table 1 |
| <=50 references, Vancouver | PASS | 31 |
| Title page: title, full author name, affiliation, corresponding author and email, COI, funding | PASS | `JHG_TITLE_PAGE_SINGLE_AUTHOR_FINAL.docx` |
| Sections: Introduction, Materials and Methods, Results, Discussion, Acknowledgements, Conflict of Interest, References, figure legends, tables | PASS | Headings checked in the DOCX |
| Double spacing, wide margins (4 cm), page numbers, continuous line numbers | PASS | `configure_document` reused from the audited builder; checked by PDF render |
| Thousands separated by spaces | PASS | Automated check |
| Figures separate (TIFF, CMYK, 300 dpi), not embedded | PASS | `figures/` |
| Legends on a separate page headed "Titles and legends to figures" | PASS | |
| Tables numbered/titled, separate editable files | PASS | `tables/` |
| SI: <=8 files, <=8 MB total, <=1 MB each, README, 50-word summaries, availability sentence | PASS | 3 files; see `JHG_BUILD_CHECKS.md` |
| Peer review not blinded; anonymisation not required | PASS | Named title page |
| Ethics (secondary public data) | PASS | Ethics Statement kept |
| Data availability | PASS | Zenodo 14136628, Dryad 10.5061/dryad.zw3r228gg, public GitHub |
| AI disclosure (Springer Nature policy) | PASS | Existing truthful disclosure kept unchanged in meaning |
| Total upload <=150 MB | PASS | See the ZIP size in `FINAL_HANDOFF_JHG_SINGLE_AUTHOR.md` |
| Cover letter (first person singular; no prior journals) | PASS | `JHG_COVER_LETTER_SINGLE_AUTHOR_FINAL.docx`: no authorial plural; no previous journal named |
| Single-author voice across the package | PASS | `JHG_SINGLE_AUTHOR_VOICE_AUDIT.md` (zero incorrect authorial plurals) |
