# JHG cross-journal guard and regression tests

Command (from `denisovan-archaic-dna-analysis/`):

```
python3 -m pytest tests/test_journal_requirements.py -v
```

Result (2026-11-08): **18 passed**.

| Test | Input | Expected | Result |
|---|---|---|---|
| test_current_jhg_requirements_pass | current JHG manifest (GTA v10 + live page) | PASS, Article 250/5000/6/50 | PASS |
| test_foreign_journal_manifest_fails | full Human Genome Variation manifest (HGV guide + HGV page) passed to the JHG target | FAIL "Cross-journal" | FAIL as expected |
| test_jhg_labelled_manifest_with_foreign_guide_pdf_fails | JHG manifest whose guide file is the HGV PDF | FAIL identity | FAIL as expected |
| test_jhg_labelled_manifest_with_foreign_live_page_fails | JHG manifest whose live page is the HGV page | FAIL "Live page title" | FAIL as expected |
| test_foreign_guide_url_fails | guide_url = hgv_gta.pdf | FAIL | FAIL as expected |
| test_canonical_url_outside_jhg_fails | canonical_url = /hgv/ | FAIL | FAIL as expected |
| test_brief_communication_limits_labelled_article_fail | 150/1000/3/20 as Article limits | FAIL "differ from the guide" | FAIL as expected |
| test_brief_communication_row_parses_to_compact_values | parse the Brief Communication row | 150/1000/3/20 | as expected |
| test_missing_field_fails ×4 | journal_full / guide_url / access_utc / article_type removed | FAIL "incomplete" | FAIL as expected |
| test_missing_limit_fails | references limit removed | FAIL | FAIL as expected |
| test_ambiguous_row_anchor_fails | row boundary spanning two article types | FAIL "Ambiguous guide row" | FAIL as expected |
| test_tampered_source_fails | wrong SHA-256 | FAIL | FAIL as expected |
| test_single_source_fails | only one source | FAIL "two independent" | FAIL as expected |
| test_live_page_linking_other_guide_version_fails | live page links JHG_GTA_v11.pdf | FAIL "Sources conflict" | FAIL as expected |
| test_newer_conflicting_snapshot_fails | newer ledger entry with a different hash | FAIL "Newer snapshot" | FAIL as expected |

Full build with the guard: `cd scripts && python3 create_jhg_submission.py` → first check "[PASS] Requirements manifest verified against official sources Journal of Human Genetics v10 (Revised 22 April 2026), Article: 250/5000/6/50"; all 18 checks PASS.
