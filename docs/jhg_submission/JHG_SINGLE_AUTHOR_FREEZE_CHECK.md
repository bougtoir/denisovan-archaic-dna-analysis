# JHG single-author freeze check

Comparison of the pre-edit package (`JHG_SUBMISSION_FINAL.zip` build, commit 5eddb19ad) with the single-author build, made programmatically on extracted DOCX text (paragraphs and table cells), superscript citation runs, image pixels, and archive members.

| Check | Result |
|---|---|
| Scientific numbers in main manuscript (multiset of all numeric tokens, 131 paragraphs) | identical |
| Numbers in Supporting Information, cover letter | identical |
| Numbers on title page | identical except the word-count metadata line (abstract 238 -> 239, main text 4 040 -> 4 045), a consequence of the wording change, not a scientific value |
| Citations (42 superscript citation runs, in order) | identical: none added or removed, order unchanged |
| Reference list (31 entries) | identical |
| Title | identical |
| Figures 1-5 (TIFF and PNG previews) | pixel-identical |
| Table 1 (DOCX/XLSX) | content-identical; committed files byte-identical to the previous commit |
| Supplementary data archive (10 CSV/JSON members) | byte-identical |
| Supporting Information text | identical (no authorial plural was present) |
| Analysis code | unchanged (only document-generation scripts `jhg_content.py` and `create_jhg_submission.py` edited) |
| DOIs, URLs, accessions, data/code availability, ethics, AI disclosure substance | unchanged |
| Changed main-manuscript paragraphs | 13: 12 voice edits (15 phrases) + Author contributions sentence |

Raw comparison output:

```
## JHG_MAIN_MANUSCRIPT_SINGLE_AUTHOR_FINAL.docx
paragraphs 131->131; numeric tokens identical: True (diff {}); reference-like lines identical: True (30); changed paragraphs: 13
superscript citation runs identical: True 42
  - 'c historical connection. We ask ' -> 'c historical connection. This study asks'
  - 'orical connection. We ask what' -> 'onnection. This study asks what'
  - 'full set of populations. We refer to the answer as t' -> 'full set of populations. The answer is referred to here as t'
  - 'are well described10,11. We do not ' -> 'are well described10,11. This study does not '
  - ' new permutation method; we formulate and operationalise a st' -> ' new permutation method; it formulates and operationalises a st'
  - 'n the same observations. We treat ABO a' -> 'n the same observations. ABO i'
  - 'servations. We treat ABO as on' -> 'e same observations. ABO is treated here as on'
  - 'We ther' -> 'I ther'
  - ' plain terms (Figure 1). We firs' -> ' plain terms (Figure 1). I firs'
  - 'e units are represented. We then' -> 'e units are represented. I then'
  - 'n for any one pair. Next we char' -> 'n for any one pair. Next I char'
  - 'We anal' -> 'I anal'
  - 're well documented10,11. Our QAP ' -> 're well documented10,11. The QAP '
  - '. Our QAP implementation permu' -> '. The QAP implementation used here permu'
  - 'We repeated distan' -> 'Distan'
  - 'ly population-label tests for ' -> 'ly population-label tests were repeated for '
  - '133 233 278-133 276 024. We distinguish' -> '133 233 278-133 276 024. Strict gene '
  - '8-133 276 024. We distinguished strict gene ' -> '278-133 276 024. Strict gene overlap was distinguish'
  - 'We distinguished strict gene overlap from' -> ' gene overlap was distinguished from'
  - 'ced under every variation we exam' -> 'ced under every variation exam'
  - 'ulation structure is not ours; wha' -> 'ulation structure is not new here; wha'
  - 'rom identity by descent; we state these as d' -> 'rom identity by descent; these are stated as d'
  - 'The a' -> 'Onishi Tatsu'
  - 'The autho' -> 'Onishi Tatsuk'
  - 'The author' -> 'Onishi Tatsuki w'
  - 'The author was ' -> 'Onishi Tatsuki was '
## JHG_TITLE_PAGE_SINGLE_AUTHOR_FINAL.docx
paragraphs 10->10; numeric tokens identical: False (diff {'238': 1, '4\xa0040': 1, '239': 1, '4\xa0045': 1}); reference-like lines identical: True (0); changed paragraphs: 1
superscript citation runs identical: True 0
  - 'Abstract: 238 word' -> 'Abstract: 239 word'
  - 'uctured). Main text: 4 040 word' -> 'uctured). Main text: 4 045 word'
## JHG_COVER_LETTER_SINGLE_AUTHOR_FINAL.docx
paragraphs 17->17; numeric tokens identical: True (diff {}); reference-like lines identical: True (0); changed paragraphs: 0
superscript citation runs identical: True 0
## supplementary_information/JHG_SUPPORTING_INFORMATION_SINGLE_AUTHOR_FINAL.docx
paragraphs 79->79; numeric tokens identical: True (diff {}); reference-like lines identical: True (0); changed paragraphs: 0
superscript citation runs identical: True 0
figures/Figure_1.tiff pixel/data identical: True
figures/Figure_2.tiff pixel/data identical: True
figures/Figure_3.tiff pixel/data identical: True
figures/Figure_4.tiff pixel/data identical: True
figures/Figure_5.tiff pixel/data identical: True
figures/Figure_1_preview.png pixel/data identical: True
figures/Figure_2_preview.png pixel/data identical: True
figures/Figure_3_preview.png pixel/data identical: True
figures/Figure_4_preview.png pixel/data identical: True
figures/Figure_5_preview.png pixel/data identical: True
tables/Table_1.docx pixel/data identical: True
tables/Table_1.xlsx pixel/data identical: content-check
Supplementary data zip members identical: True 10
```

**Final status: PASS**
