# JHG requirements source inventory

Search date: 2026-11-08 (UTC). Searched: the whole `denisovan-archaic-dna-analysis/` working tree (scripts, `docs/`, `data/raw/journal/`), all git history touching it (`git log --all -S`), the three user instruction files of this session, and the text of every generated DOCX. Terms: `5000`, `5,000`, `1000`, `1,000`, `150`, `250`, `50 references`, `20 references`, `6 figures`, `3 figures`, `Article`, `Journal of Human Genetics`, `Human Genome Variation`, `JHG`, `HGV`, `GTA`, `Guide to Authors`, `submission guidelines`.

## Official source snapshots (data/raw/journal/, SHA-256 in ACQUISITION_LEDGER.json)

| File | Type | Journal shown | URL | Retrieved (UTC) | Article type | Abstract | Main text | Displays | Refs | Official | Current | Used by generator/audit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| JHG_GTA_v10.pdf | PDF | Journal of Human Genetics | https://www.nature.com/documents/JHG_GTA_v10.pdf | 2026-11-08 03:40:51 (file mtime); re-downloaded 04:40:56, byte-identical (SHA-256 6b920a00…) | Article | 250 | 5,000 | 6 | 50 | Yes | Yes (only guide linked by the live author page; v11/v12 → 404) | Yes: JHG_REQUIREMENTS_AUDIT.md (gate 0); since this pass, parsed by `scripts/journal_requirements.py` |
| JHG_GTA_v10.pdf (same file) | PDF | Journal of Human Genetics | https://www.nature.com/documents/JHG_GTA_v10.pdf | as above | Brief Communication | 150 | 1,000 | 3 | 20 | Yes | Yes | Only listed as an article type in the audit; never used as limits |
| jhg_authors_page_snapshot.txt | text | Journal of Human Genetics | https://www.nature.com/jhg/authors-and-referees/authors | first JHG pass | — (links the GTA) | — | — | — | — | Yes | Superseded by the 04:40 snapshot (same guide link) | Audit (self-archiving, guide link) |
| jhg_authors_page_20261108T0440Z.html | HTML | Journal of Human Genetics (`<title>For Authors \| Journal of Human Genetics`) | https://www.nature.com/jhg/authors-and-referees/authors | 2026-11-08 04:40:30 | — (links only JHG_GTA_v10.pdf) | — | — | — | — | Yes | Yes | Guard: second independent source (identity + current-guide link) |
| jhg_mts_auth_instructions_snapshot.txt | text | Journal of Human Genetics | http://mts-jhg.nature.com/cgi-bin/main.plex?form_type=display_auth_instructions | first JHG pass | — | no numeric limits | — | — | — | Yes | Yes | Audit (file formats, upload) |
| jhg_open_access_fees.html | HTML | Journal of Human Genetics | https://www.nature.com/jhg/about/open-access | first JHG pass | — | — | — | — | — | Yes | Yes | Audit (fees) |
| jhg_journal_information.html | HTML | Journal of Human Genetics | https://www.nature.com/jhg/about | first JHG pass | — | — | — | — | — | Yes | Yes | Audit (publisher/society) |
| springer_nature_ai_policy_snapshot.txt | text | Springer Nature (publisher) | https://www.nature.com/nature-portfolio/editorial-policies/ai | first JHG pass | — | — | — | — | — | Yes | Yes | Audit (AI disclosure) |
| hgv_gta_20261108.pdf | PDF | **Human Genome Variation** (Guide for Authors, revised 4 September 2018) | https://www.nature.com/documents/hgv_gta.pdf | 2026-11-08 06:24 | Article | 150–200 | 5,000 incl. abstract | 6 | 50 | Yes (for HGV) | HGV's only reachable guide; HGV author pages 404 | **No** — fetched only for this conflation check and as the foreign fixture in the regression test |
| hgv_about_20261108.html | HTML | Human Genome Variation | https://www.nature.com/hgv/about | 2026-11-08 06:20 | — | — | — | — | — | Yes (for HGV) | Yes | No — regression-test fixture only |

## Project files that state limits

| File | Path | Type | Journal | Values stated | Derived from | Official |
|---|---|---|---|---|---|---|
| JHG_REQUIREMENTS_AUDIT.md | docs/jhg_submission/ | audit | JHG | Article 250 / 5,000 / 6 / 50 | JHG_GTA_v10.pdf | Secondary (cites GTA) |
| create_jhg_submission.py | scripts/ | generator/validator | JHG | until this pass: literals 150 (title), 250, 5000, 6, 50; now read from the manifest | the audit | No |
| JHG_BUILD_CHECKS.md | docs/jhg_submission/ | generated | JHG | the builder's limits | builder | No |
| JHG_SUBMISSION_FORMAT_AUDIT.md, SUBMISSION_CHECKLIST_JHG*.md, FINAL_HANDOFF_JHG*.md | docs/jhg_submission/ | QC | JHG | 250 / 5,000 / 6 / 50 | the audit and build checks | No |
| jhg_requirements.json | data/journal_requirements/ | manifest (new) | JHG | Article 250 / 5,000 / 6 / 50 + identity fields | verified against GTA v10 and live page at build time | No (machine-checked copy) |
| DEVIN_JHG_RETARGET_PROMPT.txt | docs/jhg_submission/ | user instruction 1 | JHG | no numeric limits (asks Devin to determine them) | — | No |
| DEVIN_JHG_COMPACT_WITH_ROOT_CAUSE_PROMPT.txt | docs/jhg_submission/ | user instruction 3 (this pass) | JHG | asserts 5,000 / 6 / 50 are wrong; its compact target is 150 / 1,000 / 3 / 20 | not stated | No |
| create_molecol_submission.py | scripts/ | earlier generator | Molecular Ecology | 8,000 words; 150–250-word summary | Molecular Ecology guidance | No; not used by the JHG builder for limits |

No file in the repository or its history states 150 / 1,000 / 3 / 20 as JHG Article limits. The only place where these numbers appear as the "JHG" target is user instruction 3. `git log -S "Brief Communication"` finds only the first JHG commit (5eddb19ad), where the term appears in the list of article types.
