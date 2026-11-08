# Single-source-of-truth / stale-result audit — Molecular Ecology package (2026-10-19)

- supplementary_data/ (10 designated files) compared byte-for-byte with canonical data/: all 10 identical (cmp).
- data_archive_molecol.zip lists 25 files = data/ contents + README_DATA.md; timestamps from the committed build.
- Manuscript, title page, cover letter, and SI numbers all trace to the committed canonical outputs (see NUMERIC_REPRODUCIBILITY_AUDIT).
- No obsolete CSVs, older exports, duplicate outputs with differing values, or numbers copied from earlier journal versions found inside the package. pairwise_sharing.csv (uncorrected) is retained inside the data archive as a documented intermediate, clearly distinguished from the corrected matrix used for inference.
- mecol builders read the same canonical files used by the previous journal packages; no parallel value set exists.

Verdict: **PASS**.
