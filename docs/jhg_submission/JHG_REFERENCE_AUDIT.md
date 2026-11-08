# JHG reference audit

- Style: Vancouver, numbered in order of first citation, superscript (font-based superscript runs, not Unicode). Up to 6 authors then "et al.", NLM journal abbreviations, first and last pages.
- Count: 31 (limit 50). No orphan references. The highest citation number equals the reference count. The automated builder check confirms citation order.
- Existence verification: 30 of 31 references were checked against Crossref metadata, archived in `data/raw/reference_metadata/` with SHA-256 values in `crossref_summary.json`. For each, the year, volume, first page, and DOI in the formatted string match the Crossref record. The remaining reference, Mantel 1967 (*Cancer Res* 27:209-220), has no DOI; its metadata is unchanged from the audited source reference audit.
- Changes from the audited source list: removed Manel et al. 2003 and Wang & Bradburd 2014 (their supporting sentence was removed). No new references were added.
- "Heredity (Edinb)" in reference 15 is a cited journal (Ortega-Del Vecchyo & Slatkin 2019), not leftover journal-target text.

Verdict: PASS.
