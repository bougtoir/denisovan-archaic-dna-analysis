# Journal-conflation check (JHG vs HGV)

| Journal | Article type | Abstract | Main text | Displays | References | Source URL |
|---|---|---|---|---|---|---|
| Journal of Human Genetics | Article | 250 | 5,000 (excl. abstract) | 6 | 50 | https://www.nature.com/documents/JHG_GTA_v10.pdf |
| Journal of Human Genetics | Brief Communication | 150 | 1,000 | 3 | 20 | https://www.nature.com/documents/JHG_GTA_v10.pdf |
| Human Genome Variation | Article | 150–200 | 5,000 (incl. abstract) | 6 | 50 | https://www.nature.com/documents/hgv_gta.pdf (revised 4 Sep 2018) |
| Human Genome Variation | Review Article | — | 5,000 | 8 | 100 | https://www.nature.com/documents/hgv_gta.pdf |
| Human Genome Variation | Data Report | ≤70 | 1,500 | 2 | 20 | https://www.nature.com/documents/hgv_gta.pdf |
| Human Genome Variation | Software Report | — | 1,200 | 3 | 20 | https://www.nature.com/documents/hgv_gta.pdf |

Findings:
1. The earlier 5,000 / 6 / 50 values match the JHG Article row of JHG's own current guide exactly. They also happen to match the HGV Article row, but the project history shows they were taken from JHG_GTA_v10.pdf (JHG_REQUIREMENTS_AUDIT.md, commit 5eddb19ad). No HGV source was fetched, cached or cited before this check. **HGV was not the source of the earlier values.**
2. The compact target 150 / 1,000 / 3 / 20 matches the **JHG Brief Communication** row exactly. The closest HGV row (Software Report, 1,200 / 3 / 20) does not match exactly. So the compact premise most likely mixes up two article types within JHG, not two journals. Its origin lies outside the repository (see JHG_REQUIREMENTS_ROOT_CAUSE.md).
3. Other journals in the project history (Molecular Ecology: 8,000 words; BioEssays) give neither set of values.
