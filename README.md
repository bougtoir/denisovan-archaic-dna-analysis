# Denisovan & Archaic DNA Analysis

Archaic human (Neanderthal/Denisovan) DNA introgression patterns across modern human populations: visualization, sharing analysis, and implications for ancient human migration.

## Contents

```
scripts/          Analysis and visualization scripts (Python)
figures/          Generated figures (PNG/TIFF)
data/             Pairwise sharing data and provenance (CSV/JSON)
docs/             Submission packages and discussion notes
```

## Figures

| File | Description |
|------|-------------|
| `denisovan_world_map.png` | Denisovan DNA proportion by population (bubble map) |
| `archaic_dna_world_map.png` | Bivariate map: Neanderthal (size) + Denisovan (color) |
| `minard_human_migration.png` | Minard-style flow chart of Out-of-Africa migration with archaic admixture events |
| `archaic_sharing_vs_distance.png` | Archaic segment sharing correlation vs geographic distance |
| `archaic_sharing_heatmap.png` | Pairwise sharing heatmap for 30 key populations |

## Data Sources

- **hmmix introgression segments**: Zenodo record 14136628 (1000 Genomes + HGDP)
- **Sankararaman et al. 2016** (Current Biology): Denisovan + Neanderthal ancestry proportions
- **Terao et al. 2024** (Science Advances): JEWEL Japanese genome study
- **Jacobs et al. 2019** (Cell): Multiple Denisovan ancestries in Papuans

## Requirements

```
pip install matplotlib cartopy numpy pandas scipy statsmodels seaborn \
  python-docx python-pptx Pillow requests
sudo apt install fonts-noto-cjk  # for Japanese labels
```

LibreOffice and Poppler are required for the optional DOCX/PPTX rendering
checks.

## Usage

```bash
# Generate world maps
python scripts/denisovan_map.py
python scripts/denisovan_neanderthal_map.py
python scripts/minard_migration.py
```

The final Heredity submission documents (`manuscript_heredity.docx`,
`manuscript_heredity_inline_review.docx`, `Heredity_submission_package.zip`,
etc.) are provided in `docs/heredity_submission/`. The scripts that assemble
these submission files are kept in the private repository; the public repository
contains the analysis code, derived data, and pre-built outputs.

To reproduce the full analysis from the original hmmix segment files, run the
source pipeline:

```bash
python scripts/run_ajba_pipeline.py \
  --segments-1kg /path/to/hg38_1000g_segments.txt \
  --segments-hgdp /path/to/hg38_HGDP_segments.txt \
  --permutations 9999 \
  --sensitivity-permutations 999
```

This deduplicates individual-haplotype-window presence, validates that every
population-window frequency is at most one, runs population-label QAP inference
and sensitivity analyses, and records raw source paths and SHA-256 checksums in
`data/analysis_provenance.json`.
