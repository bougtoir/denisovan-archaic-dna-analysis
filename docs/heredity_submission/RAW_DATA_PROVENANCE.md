# Raw-data provenance ledger

Primary inputs for every number, figure, and table in the Heredity submission. The two segment files are the only inputs required by `scripts/run_ajba_pipeline.py`; the two SNP files are archived alongside them for completeness of the source record.

## Source

- Repository: Zenodo
- Record: 14136628 (https://zenodo.org/records/14136628)
- Content: hmmix archaic-segment calls and SNP tables on GRCh38 for the 1000 Genomes and HGDP panels
- Access conditions: open access, no authentication, no request throttling encountered
- Acquisition: anonymous HTTPS GET of `https://zenodo.org/api/records/14136628/files/<name>/content`
- Acquisition time (UTC): 2026-09-29, 11:17 to 11:34
- Persistent local path: `/home/ubuntu/research_raw_data/zenodo_14136628/`
- Checksum manifest: `/home/ubuntu/research_raw_data/zenodo_14136628/SHA256SUMS.txt`

The files are not committed to Git: the two segment files alone are about 1.4 GB. They are kept as unmodified originals; all derived products are written to `data/` in the repository by the pipeline and never overwrite the originals.

## Files acquired

| File | Bytes | SHA-256 | Used by pipeline |
| --- | --- | --- | --- |
| `hg38_1000g_segments.txt` | 1,059,395,992 | `d3ea9fe7ac6b5abacb176acecf4747bacdead89c0a35e1750a4f8ee71b2bb1d4` | yes |
| `hg38_HGDP_segments.txt` | 399,257,886 | `c222d44a05fed3f059b2907ca6e9deb8899c41ff8fd59bc629bd57c910a593ac` | yes |
| `hg38_1000g_SNPS.txt` | 30,177,906 | `dc882708898ffb001d33ae033628fc4fd5c3484dd36ae38de6c724bb06fe6911` | no (archived) |
| `hg38_HGDP_SNPS.txt` | 34,982,935 | `e3c5867425158a44e013ffce4314d70ac3dddb448737228355cbf4ca2669daf9` | no (archived) |

Sizes were verified against the Zenodo record metadata after download; all four downloads completed and none is truncated.

## Verification against the analysis record

`data/analysis_provenance.json`, written by `scripts/archaic_sharing_analysis.py` at the time the committed results were produced, records:

- `segments_1kg.sha256` = `d3ea9fe7ac6b5abacb176acecf4747bacdead89c0a35e1750a4f8ee71b2bb1d4`
- `segments_hgdp.sha256` = `c222d44a05fed3f059b2907ca6e9deb8899c41ff8fd59bc629bd57c910a593ac`

Both match the freshly downloaded files byte-for-byte by checksum. The committed derived data in `data/` therefore descend from exactly the archived record 14136628 content, not from a later or different version of it.

## Reproduction path

```
python scripts/run_ajba_pipeline.py \
  --segments-1kg /home/ubuntu/research_raw_data/zenodo_14136628/hg38_1000g_segments.txt \
  --segments-hgdp /home/ubuntu/research_raw_data/zenodo_14136628/hg38_HGDP_segments.txt
```

The pipeline regenerates `data/analysis_provenance.json`, `data/correction_stats.json`, `data/pairwise_sharing_corrected.csv`, `data/population_profiles_500kb.npz`, the sensitivity tables, `data/abo_focal_test.json`, and the figure set. Random seeds are fixed at 42 in `archaic_sharing_analysis.py` and `archaic_sharing_corrected.py`, so the QAP permutation results are deterministic given these inputs.

Document generation (`scripts/create_heredity_submission.py`) is kept in the private repository and reads only the derived files listed above.
