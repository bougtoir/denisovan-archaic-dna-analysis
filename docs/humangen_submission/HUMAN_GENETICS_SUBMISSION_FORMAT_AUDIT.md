# HUMAN_GENETICS_SUBMISSION_FORMAT_AUDIT

20-item check against the actual package files.

1. **Title Page elements** — title, author name+affiliation, corresponding email, running title, word count, data/code link, acknowledgements: PRESENT. PASS.
2. **Abstract length + keywords** — 228 words (150–250 required); 6 keywords (4–6 required). PASS.
3. **ORCID placement** — entered at submission portal per Springer (checklist instructs it); no ORCID printed. PASS (portal capture).
4. **Acknowledgements placement** — separate section on title page (per guideline). PASS.
5. **References placement** — reference list after declarations, before figure legends; Springer convention. PASS.
6. **"Statements and Declarations" heading** — declarations present as individual Heading-1 sections (Funding, Author Contributions, Competing Interests, Data Availability, Ethics, AI declaration). The Springer template wraps these under "Statements and Declarations" but accepts them as sections; MINOR stylistic note only. PASS.
7. **Declarations location** — after Discussion, before References. PASS.
8. **Funding/Competing/Contributions/Ethics/Data Availability positions** — all present, correctly ordered. PASS.
9. **AI disclosure** — dedicated section present (superset of the LLM-copy-editing rule). PASS.
10. **Figures embedded if required** — Human Genetics does NOT require in-text figure placement; figures submitted separately. Main docx has legends only — PASS. Inline review copy is an author-side convenience.
11. **Figure 1 missing from inline manuscript?** — WAS MISSING (Figures 2–5 embedded; Figure 1, cited in Methods, never inserted). FIXED: builder now inserts Figure 1 after the Analytical-logic paragraph in inline mode. RESOLVED.
12. **Figures cited in order** — Figure 1 (Methods) → 2,3 (Results §1) → 4 (Results §2) → 5 (Results §3); S1→S7 all cited. PASS.
13. **Tables cited in order** — Table 1 (Results §2), Table S1 (Results §4). PASS.
14. **Supplementary figures/tables cited in order** — S1–S7, Table S1 all cited. PASS.
15. **Reference format** — Springer author-date, alphabetical, DOI links; validated 30/31 (Tournebize print-year note). PASS.
16. **Cover letter addressed appropriately** — "The Editors-in-Chief, Human Genetics"; first person singular; no prior-journal references. PASS.
17. **No HDY manuscript number** — none anywhere (title page, cover letter, manuscript). PASS.
18. **No "Heredity" journal-target language** — only legitimate reference journal names (Mazet 2016 Heredity, Ortega-Del Vecchyo 2019 Heredity) — these are citations, not journal-target language. PASS.
19. **Obsolete file names** — package files all HUMAN_GENETICS_* / descriptive names. PASS.
20. **Unambiguous upload-ready files** — clear names; zip inventories them. PASS.

## Fix applied

- Figure 1 now embedded in the inline review manuscript (was the single real defect found).
