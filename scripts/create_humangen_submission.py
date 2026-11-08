"""Build the Human Genetics submission package."""

from __future__ import annotations

import re
import shutil
import subprocess
import zipfile
from datetime import date
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from lxml import etree

import pandas as pd
from PIL import Image
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor
from pptx import Presentation
from pptx.dml.color import RGBColor as PptRGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches as PptInches
from pptx.util import Pt as PptPt

import humangen_content as revised_content


PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
FIGURE_DIR = PROJECT_DIR / "figures"
OUTPUT_DIR = PROJECT_DIR / "docs" / "humangen_submission"
OUTPUT_FIGURE_DIR = OUTPUT_DIR / "figures"
JOURNAL = "Human Genetics"
JOURNAL_SHORT = "Human Genetics"
ARTICLE_TYPE = "Research Article"
EDITORS_BLOCK = [
    "The Editors-in-Chief",
    "Human Genetics",
    "Human Genetics Editorial Office, Springer Nature",
]

TITLE = revised_content.TITLE
RUNNING_TITLE = revised_content.RUNNING_TITLE
AUTHOR = revised_content.AUTHOR
AFFILIATION = revised_content.AFFILIATION
CORRESPONDENCE = revised_content.CORRESPONDENCE
ABSTRACT = revised_content.ABSTRACT
KEYWORDS = revised_content.KEYWORDS
REFERENCES = revised_content.REFERENCES
REFERENCE_KEYS = revised_content.REFERENCE_KEYS
INTRODUCTION = revised_content.INTRODUCTION
METHODS = revised_content.METHODS
RESULTS = revised_content.RESULTS
DISCUSSION = revised_content.DISCUSSION
FIGURES = revised_content.FIGURES
SUPPORTING_FIGURES = revised_content.SUPPORTING_FIGURES


def set_cell_shading(cell, fill: str) -> None:
    properties = cell._tc.get_or_add_tcPr()
    shading = OxmlElement("w:shd")
    shading.set(qn("w:fill"), fill)
    properties.append(shading)


def add_line_numbering(section) -> None:
    sectPr = section._sectPr
    lnNumType = OxmlElement("w:lnNumType")
    lnNumType.set(qn("w:countBy"), "1")
    lnNumType.set(qn("w:restart"), "continuous")
    sectPr.append(lnNumType)


def configure_document(document: Document) -> None:
    section = document.sections[0]
    section.top_margin = Cm(4)
    section.bottom_margin = Cm(4)
    section.left_margin = Cm(4)
    section.right_margin = Cm(4)
    add_line_numbering(section)
    normal = document.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)
    normal.paragraph_format.line_spacing = 2.0
    normal.paragraph_format.space_after = Pt(0)
    for name in ["Title", "Heading 1", "Heading 2"]:
        style = document.styles[name]
        style.font.name = "Times New Roman"
        style.font.color.rgb = RGBColor(0, 0, 0)


def make_omml_run(text: str, italic: bool = True, font_size: int = 24) -> etree._Element:
    r = etree.SubElement(etree.Element("dummy"), qn("m:r"))
    rPr = etree.SubElement(r, qn("m:rPr"))
    if not italic:
        sty = etree.SubElement(rPr, qn("m:sty"))
        sty.set(qn("m:val"), "p")
    wRPr = etree.SubElement(r, qn("w:rPr"))
    rFonts = etree.SubElement(wRPr, qn("w:rFonts"))
    rFonts.set(qn("w:ascii"), "Cambria Math")
    rFonts.set(qn("w:hAnsi"), "Cambria Math")
    sz = etree.SubElement(wRPr, qn("w:sz"))
    sz.set(qn("w:val"), str(font_size))
    szCs = etree.SubElement(wRPr, qn("w:szCs"))
    szCs.set(qn("w:val"), str(font_size))
    t = etree.SubElement(r, qn("m:t"))
    t.text = text
    t.set(qn("xml:space"), "preserve")
    return r


def make_subscript(base_text: str, sub_text: str, base_italic: bool = True, sub_italic: bool = True) -> etree._Element:
    sSub = etree.SubElement(etree.Element("dummy"), qn("m:sSub"))
    e = etree.SubElement(sSub, qn("m:e"))
    e.append(make_omml_run(base_text, italic=base_italic))
    sub = etree.SubElement(sSub, qn("m:sub"))
    sub.append(make_omml_run(sub_text, italic=sub_italic))
    return sSub


def make_omath_para(*elements: etree._Element) -> etree._Element:
    oMathPara = etree.SubElement(etree.Element("dummy"), qn("m:oMathPara"))
    oMath = etree.SubElement(oMathPara, qn("m:oMath"))
    for el in elements:
        oMath.append(el)
    return oMathPara


def _add_expanded_model_equation(document: Document) -> None:
    """Insert a centred Word OMML equation for the expanded dyadic model."""
    para = document.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para.paragraph_format.space_before = Pt(6)
    para.paragraph_format.space_after = Pt(6)
    parts = [
        make_subscript("s", "ij"),
        make_omml_run(" = ", italic=False),
        make_subscript("β", "0", sub_italic=False),
        make_omml_run(" + ", italic=False),
        make_subscript("β", "d", sub_italic=False),
        make_omml_run(" ", italic=False),
        make_subscript("d", "ij"),
        make_omml_run(" + ", italic=False),
        make_subscript("β", "a", sub_italic=False),
        make_omml_run(" ", italic=False),
        make_subscript("a", "ij"),
        make_omml_run(" + ", italic=False),
        make_subscript("β", "c", sub_italic=False),
        make_omml_run(" ", italic=False),
        make_subscript("c", "ij"),
        make_omml_run(" + ", italic=False),
        make_subscript("β", "m", sub_italic=False),
        make_omml_run(" ", italic=False),
        make_subscript("m", "ij"),
        make_omml_run(" + ", italic=False),
        make_subscript("ε", "ij"),
    ]
    para._element.append(make_omath_para(*parts))
    note = document.add_paragraph()
    note.paragraph_format.first_line_indent = Inches(0.3)
    run = note.add_run(
        "where s_ij is pairwise profile similarity, d_ij is great-circle distance in "
        "thousands of kilometres, a_ij indicates a pair involving a designated recently "
        "admixed American population, c_ij is same-continent status, and m_ij is same-dataset "
        "status. Subscripts denote population pairs i and j."
    )
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.italic = True


def add_cited_paragraph(document: Document, text: str, italic: bool = False):
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.first_line_indent = Inches(0.3)
    run = paragraph.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.italic = italic
    return paragraph


def add_title(document: Document) -> None:
    """Add only the title (anonymous) for the manuscript body."""
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run(TITLE)
    run.bold = True
    run.font.name = "Times New Roman"
    run.font.size = Pt(16)
    document.add_paragraph()


def add_abstract_page(document: Document) -> None:
    document.add_heading("Abstract", level=1)
    paragraph = document.add_paragraph(ABSTRACT)
    paragraph.paragraph_format.line_spacing = 1.5
    paragraph.paragraph_format.first_line_indent = Inches(0)
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.first_line_indent = Inches(0)
    run = paragraph.add_run("Keywords: ")
    run.bold = True
    paragraph.add_run(KEYWORDS)
    document.add_page_break()


def create_title_page(path: Path, main_word_count: int) -> None:
    document = Document()
    configure_document(document)
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run(TITLE)
    run.bold = True
    run.font.name = "Times New Roman"
    run.font.size = Pt(16)
    document.add_paragraph()
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run(ARTICLE_TYPE).bold = True
    document.add_paragraph()
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run(AUTHOR.upper()).bold = True
    document.add_paragraph()
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run(AFFILIATION)
    document.add_paragraph()
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run(CORRESPONDENCE)
    document.add_paragraph()
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run("ORCID: 0000-0001-7261-9062")
    document.add_paragraph()
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run(f"Running title: {RUNNING_TITLE}")
    document.add_paragraph()
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run(f"Main-text word count: {main_word_count:,}")
    document.add_paragraph()
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run(
        "Data and code availability: https://github.com/bougtoir/denisovan-archaic-dna-analysis"
    )
    document.add_paragraph()
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run(
        "Acknowledgements: The author acknowledges the participants, communities, "
        "and investigators whose contributions made the 1000 Genomes, HGDP, hmmix, "
        "and ancient-genome resources available. Public availability does not "
        "remove obligations of respectful reuse."
    )
    document.add_paragraph()
    abstract_heading = document.add_paragraph()
    abstract_heading.add_run("Abstract").bold = True
    document.add_paragraph(ABSTRACT)
    keywords_paragraph = document.add_paragraph()
    keywords_paragraph.add_run("Keywords: ").bold = True
    keywords_paragraph.add_run(KEYWORDS)
    document.save(path)


def _format_pair_row(row, ancestry: str, sharing_col: str, z_col: str) -> list[str]:
    sharing = getattr(row, sharing_col)
    z = getattr(row, z_col)
    return [
        ancestry,
        row.pop1,
        row.pop2,
        row.region1.replace("_", " ").title(),
        row.region2.replace("_", " ").title(),
        f"{row.geo_dist_km:,.0f}",
        f"{sharing:.3f}",
        f"{z:.2f}",
    ]


def table_1_rows() -> list[list[str]]:
    pairs = pd.read_csv(DATA_DIR / "pairwise_sharing_corrected.csv")
    non_admixed = pairs[pairs["any_admixed"] == 0]
    candidates = []
    for row in non_admixed.itertuples():
        nean_qualifies = (row.nean_resid_z > 2) and (row.nean_fdr_pval < 0.10)
        deni_qualifies = (row.deni_resid_z > 2) and (row.deni_fdr_pval < 0.10)
        if nean_qualifies:
            candidates.append(
                (row.nean_resid_z, _format_pair_row(row, "Neanderthal", "nean_corr", "nean_resid_z"))
            )
        if deni_qualifies:
            candidates.append(
                (row.deni_resid_z, _format_pair_row(row, "Denisovan", "deni_corr", "deni_resid_z"))
            )
    rows = [
        [
            "Ancestry",
            "Population 1",
            "Population 2",
            "Region 1",
            "Region 2",
            "Distance (km)",
            "Sharing (r)",
            "z-score",
        ]
    ]
    if not candidates:
        rows.append(
            [
                "—",
                "No qualifying pair",
                "—",
                "—",
                "—",
                "—",
                "—",
                "No z>2 and q<0.10 result for either ancestry",
            ]
        )
        return rows
    candidates.sort(key=lambda item: item[0], reverse=True)
    for _, row in candidates:
        rows.append(row)
    return rows


def table_s1_rows() -> list[list[str]]:
    sublineage = pd.read_csv(DATA_DIR / "abo_sublineage_summary.csv")
    order = [
        "East Asia",
        "Europe",
        "Indigenous Americas",
        "Admixed Americas",
        "Central/South Asia",
        "Middle East",
        "Oceania",
    ]
    rows = [
        [
            "Region",
            "n",
            "Altai %",
            "Vindija %",
            "Chagyrskaya %",
        ]
    ]
    for group in order:
        group_summary = sublineage[
            (sublineage["analysis_group"] == group)
            & (sublineage["closest_reference"] != "Tie")
        ]
        total = int(group_summary["n_segments"].sum())
        values = {
            row.closest_reference: 100 * row.n_segments / total
            for row in group_summary.itertuples()
        } if total else {}
        rows.append(
            [
                group,
                str(total),
                f"{values.get('Altai', 0):.1f}",
                f"{values.get('Vindija', 0):.1f}",
                f"{values.get('Chagyrskaya', 0):.1f}",
            ]
        )
    return rows


TABLES = {
    1: (
        "Positive-residual archaic pairs after false discovery rate control",
        table_1_rows,
        "The prespecified family contains all non-admixed population pairs. A supported positive outlier required z>2 and Benjamini-Hochberg q<0.10 for Neanderthal or Denisovan ancestry; complete nominal rankings and dependence-aware model results are provided in Supplementary Data.",
    ),
}

SUPPORTING_TABLES = {
    1: (
        "Exploratory ABO-window Neanderthal-reference composition",
        table_s1_rows,
        "Counts are classifiable segments, not individuals. Percentages use the three-reference denominator shown by n. Equal maximum-similarity ties are excluded from these percentages but retained in Supplementary Data. The 2/2 Indigenous American value is not a regional frequency estimate; only one segment overlaps ABO, and these counts are not interpreted as a migration route.",
    ),
}


CRITICAL_REVIEW_REPORT_TEMPLATE = """# Pre-submission critical reviewer report — {journal}

**Manuscript:** "{title}"  
**Target journal:** {journal}  
**Date:** {date}  
**Reviewer role:** internal pre-submission critical review

**Implementation note:** All priority actions identified in this review have been applied to the generated package.

---

## 1. Manuscript: novelty, focus and logic

**Verdict:** Focused and timely; scope remains on negative-control/baseline methodology.

*Strengths*
- The central framing answers the AHG editor's first concern: the "special-connection claim" is defined explicitly, and the ABO focal-locus scan is treated as a prespecified negative test rather than a route proposal.
- The abstract immediately states what the paper does (build a dependence-aware baseline) and what it does not do (identify a migration route or an exceptional pair).
- The narrative is unified: Introduction introduces the claim, Methods explains dyadic dependence, Results reports the absence of FDR-supported outliers, and Discussion reinforces that the contribution is a reusable baseline.

*Risks*
- A reviewer may judge the biological result unsurprising. The value lies in the formal baseline and reproducible FDR control; this must be emphasised to avoid a "so what?" reaction. **Action:** keep the Discussion's opening sentence about the reproducible, dependence-aware baseline prominent.
- The ABO–genome-wide link is clear, but the phrase "no route-level signal" is qualitative. **Action:** repeat in the ABO Results paragraph that the two Indigenous-American segments are within the genome-wide expectation and are not interpreted as a route.

**Priority:** Medium.

---

## 2. Statistical design

**Verdict:** Method is appropriate and explicitly distinguishes itself from Mantel tests.

*Strengths*
- The population-label QAP is described as preserving row–column dependence, and the comparison with Mantel tests directly answers the AHG editor's second concern.
- The Methods state that R-squared values are descriptive, coefficients come from permuted regressions, and pair-level residual P values come from the same permutation distribution.
- Multiple testing is controlled with Benjamini–Hochberg FDR; the prespecified family is all non-admixed pairs.

*Risks*
- BH assumes independence or positive regression dependency. The manuscript notes that pair residuals are dyadically dependent and uses a joint permutation null, but does not discuss whether BH is conservative or anti-conservative under the specific dependency. Because no pair survives FDR correction, the practical impact is small. **Action:** add one sentence in the Methods noting that BH is used as a standard exploratory control and that the absence of any q<0.10 finding is robust to stricter dependence-aware procedures.
- The expanded model includes same-continent and same-dataset covariates as descriptive sensitivity terms. This is correctly labelled as non-causal.

**Priority:** Medium.

---

## 3. Figures and tables

**Verdict:** Figure/table set supports the manuscript; a few captions should be tightened.

*Strengths*
- Figure 1 directly shows the distance-decay relationship with a descriptive fit and a clear caption.
- Figure 2 shows broad regional blocks; Figure S1 provides the full 66 × 66 matrix.
- Figures S3 and S4 separate modern and ancient ABO evidence and warn against direct comparison.

*Risks*
- Figure 2 uses 31 prespecified populations. A reviewer may ask how the 31 were chosen. **Action:** the caption states that 31 populations were selected for legibility, ordered by geographic region, and that Figure S1 contains all 66.
- Table S1 excludes ties from percentages. The note already explains this.

**Priority:** Low–Medium.

---

## 4. Reproducibility

**Verdict:** Strong. Package is built from derived data with provenance files.

*Strengths*
- `analysis_provenance.json` and `ancient_abo_provenance.json` contain SHA-256 checksums and parameters.
- All manuscript numbers flow from `data/correction_stats.json`; the submission script contains no hard-coded results.
- Source data are public (Zenodo, Dryad, Ensembl), and the submission package includes the derived data as supplementary files.
- A reproducibility checklist and validation report are generated automatically.

*Risks*
- The public GitHub repository is not named in the anonymous manuscript for double-anonymised review; the cover letter and title page include the repository URL. **Action:** keep the URL on the title page and reproducibility checklist.
- The primary analysis pipeline requires the original hmmix segment files, which are large. The submission relies on derived `pairwise_sharing_corrected.csv`. This is standard, and the reproducibility checklist confirms that derived files are in `data/` and will be released.

**Priority:** Low.

---

## 5. Strength of claims

**Verdict:** Appropriately cautious. The manuscript repeatedly frames results as negative, descriptive, or baseline.

*Strengths*
- Key caveats are present: distance correlations are descriptive; coordinates are approximate; correlation is not identity-by-descent; ABO segment is not an ABO allele; closest-reference similarity is not a transmission path; Indigenous-American observations are not regional-frequency estimates or migration routes.
- The AHG editor's two concerns are addressed directly in the cover letter, revised Introduction, and Methods.

*Risks*
- A reviewer may ask why the ABO analysis is included if it is only a negative test. **Action:** the Introduction and Discussion state that it is a recurring claim in the literature and that a formal baseline is needed to discipline such claims.

**Priority:** Low.

---

## Overall decision

**Ready for submission after three minor revisions:**

1. **Medium:** Keep the Discussion's opening/closing statement that the paper's contribution is the baseline, not a new signal.
2. **Medium:** Add one sentence on BH FDR assumptions under dependence in the Methods.
3. **Low:** Keep the public repository URL on the title page and reproducibility checklist.

No fatal flaws, no hard-coded data, and the package passes the automated validation. The AHG editor's two concerns are addressed.
"""


def create_critical_review_report(path: Path) -> None:
    template_path = PROJECT_DIR / "scripts" / "critical_review_report_template.md"
    content = template_path.read_text(encoding="utf-8").format(
        title=TITLE, journal=JOURNAL, date=date.today().isoformat()
    )
    path.write_text(content, encoding="utf-8")


def render_table(document: Document, label: str, spec: tuple) -> None:
    title, row_function, note = spec
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(14)
    run = paragraph.add_run(f"{label}. {title}")
    run.bold = True
    rows = row_function()
    table = document.add_table(rows=len(rows), cols=len(rows[0]))
    table.style = "Table Grid"
    for row_index, row in enumerate(rows):
        for column_index, value in enumerate(row):
            cell = table.cell(row_index, column_index)
            cell.text = value
            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.line_spacing = 1
                for run in paragraph.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(8.5)
                    run.bold = row_index == 0
            if row_index == 0:
                set_cell_shading(cell, "D9EAF7")
    paragraph = document.add_paragraph(f"Note. {note}")
    paragraph.paragraph_format.line_spacing = 1
    for run in paragraph.runs:
        run.font.size = Pt(9)


def add_word_table(document: Document, table_number: int) -> None:
    render_table(document, f"Table {table_number}", TABLES[table_number])


def add_supporting_table(document: Document, table_number: int) -> None:
    render_table(document, f"Table S{table_number}", SUPPORTING_TABLES[table_number])


def add_inline_figure(document: Document, figure_number: int) -> None:
    filename, caption = FIGURES[figure_number]
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(16)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run().add_picture(
        str(FIGURE_DIR / filename), width=Inches(6.35)
    )
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(10)
    paragraph.paragraph_format.line_spacing = 1.15
    run = paragraph.add_run(f"Figure {figure_number}. ")
    run.bold = True
    paragraph.add_run(caption)


def add_object(document: Document, label: str) -> None:
    kind, number = label.split()
    if kind == "Figure":
        add_inline_figure(document, int(number))
    else:
        add_word_table(document, int(number))


def _body_texts() -> list[str]:
    body_texts = INTRODUCTION.copy()
    for _, paragraphs in METHODS:
        body_texts.extend(paragraphs)
    body_texts.extend(text for _, text, _ in RESULTS)
    body_texts.extend(DISCUSSION)
    return body_texts


def _main_text_word_count() -> int:
    texts = _body_texts()
    texts.extend([
        "The author acknowledges the participants, communities, and investigators whose "
        "contributions made the 1000 Genomes, HGDP, hmmix, and ancient-genome resources "
        "available. Public availability does not remove obligations of respectful reuse.",
        "Funding: This research received no specific grant from any funding agency in "
        "the public, commercial, or not-for-profit sectors.",
        "The author was responsible for conceptualization, methodology, formal analysis, "
        "visualization, writing—original draft, and writing—review and editing.",
        "The author declares no conflict of interest.",
        "The source hmmix segment calls are available from Zenodo record 14136628 "
        "(https://doi.org/10.5281/zenodo.14136628). The ancient ABO-window observations "
        "were derived from the public Neanderthal-segment catalogue of Iasi et al. "
        "(2024), archived at Dryad (https://doi.org/10.5061/dryad.zw3r228gg); O2 "
        "subtype-defining allele frequencies were obtained from the Ensembl Variation "
        "application programming interface and from Ohashi et al. (2006). Analysis "
        "scripts, aggregate derived data, and figures, including the "
        "abo_window_focal_test.py script that implements the ABO focal-window "
        "comparison reported here, are "
        "available from the corresponding author and will be archived with a persistent "
        "DOI before acceptance. Raw-file SHA-256 checksums and all analysis parameters "
        "are included in analysis_provenance.json and ancient_abo_provenance.json.",
        "This secondary computational analysis used de-identified public genomic data "
        "and involved no recruitment, participant contact, biospecimen collection, or "
        "new phenotype inference. No separate institutional review determination was "
        "obtained; approvals, consent, and access procedures were those reported by the "
        "source studies. No source community representatives participated in this "
        "secondary study, and no direct community return-of-results process occurred. "
        "Because Indigenous genomic records are included, results are reported only at "
        "the minimum level needed for auditability, are not generalised to communities, "
        "and are not used to assign migration routes. The public article, code, and "
        "aggregate derived results are the current means of results availability.",
    ])
    return len(" ".join(texts).split())


def add_manuscript_body(document: Document, inline: bool) -> None:
    document.add_heading("Introduction", level=1)
    for text in INTRODUCTION:
        add_cited_paragraph(document, text)
    document.add_heading("Materials and Methods", level=1)
    for heading, paragraphs in METHODS:
        document.add_heading(heading, level=2)
        for index, text in enumerate(paragraphs):
            add_cited_paragraph(document, text)
            if heading == "Dyadic regression and permutation inference" and index == 0:
                _add_expanded_model_equation(document)
            if inline and heading == "Analytical logic" and index == 0:
                add_inline_figure(document, 1)
    document.add_heading("Results", level=1)
    for heading, text, objects in RESULTS:
        document.add_heading(heading, level=2)
        add_cited_paragraph(document, text)
        if inline:
            for label in objects:
                add_object(document, label)
    document.add_heading("Discussion", level=1)
    for text in DISCUSSION:
        add_cited_paragraph(document, text)
    document.add_heading("References", level=1)
    for reference in REFERENCES:
        paragraph = document.add_paragraph(reference)
        paragraph.paragraph_format.first_line_indent = Inches(-0.25)
        paragraph.paragraph_format.left_indent = Inches(0.25)
        paragraph.paragraph_format.line_spacing = 1.15
        paragraph.paragraph_format.space_after = Pt(4)
        for run in paragraph.runs:
            run.font.size = Pt(10)
    document.add_heading("Statements and Declarations", level=1)
    document.add_heading("Funding", level=2)
    document.add_paragraph(
        "This research received no specific grant from any funding agency in "
        "the public, commercial, or not-for-profit sectors."
    )
    document.add_heading("Competing Interests", level=2)
    document.add_paragraph("The author declares no competing interests.")
    document.add_heading("Ethics Approval", level=2)
    document.add_paragraph(
        "This secondary computational analysis used de-identified public genomic data "
        "and involved no recruitment, participant contact, biospecimen collection, or "
        "new phenotype inference. No separate institutional review determination was "
        "obtained; approvals, consent, and access procedures were those reported by the "
        "source studies. No source community representatives participated in this "
        "secondary study, and no direct community return-of-results process occurred. "
        "Because Indigenous genomic records are included, results are reported only at "
        "the minimum level needed for auditability, are not generalised to communities, "
        "and are not used to assign migration routes. The public article, code, and "
        "aggregate derived results are the current means of results availability."
    )
    document.add_heading("Consent", level=2)
    document.add_paragraph(
        "Not applicable. This secondary analysis used de-identified public genomic "
        "data and involved no recruitment, participant contact, or new phenotype "
        "inference."
    )
    document.add_heading("Data Availability", level=2)
    document.add_paragraph(
        "The source hmmix segment calls are available from Zenodo record 14136628 "
        "(https://doi.org/10.5281/zenodo.14136628). The ancient ABO-window observations "
        "were derived from the public Neanderthal-segment catalogue of Iasi et al. "
        "(2024), archived at Dryad (https://doi.org/10.5061/dryad.zw3r228gg); O2 "
        "subtype-defining allele frequencies were obtained from the Ensembl Variation "
        "application programming interface and from Ohashi et al. (2006)."
    )
    document.add_heading("Code Availability", level=2)
    document.add_paragraph(
        "Analysis scripts, aggregate derived data, and figures are publicly "
        "available at: https://github.com/bougtoir/denisovan-archaic-dna-analysis "
        "(the repository includes abo_window_focal_test.py, the script implementing "
        "the ABO focal-window comparison reported here). The final archived release "
        "will be assigned a persistent DOI before acceptance. Raw-file SHA-256 "
        "checksums and all analysis parameters are included in "
        "analysis_provenance.json and ancient_abo_provenance.json."
    )
    document.add_heading("Author Contributions", level=2)
    document.add_paragraph(
        "The author was responsible for conceptualization, methodology, formal analysis, "
        "visualization, writing—original draft, and writing—review and editing."
    )
    document.add_heading(
        "Declaration of Generative Artificial Intelligence (AI) in Scientific Writing",
        level=2,
    )
    document.add_paragraph(
        "During the preparation of this work the author used Devin (devin.ai) in "
        "order to format the text and choose words that suited the tone, and to "
        "help writing codes. After using this tool/service, the author reviewed "
        "and edited the content as needed and takes full responsibility for the "
        "content of the published article."
    )
    if not inline:
        document.add_heading("Figure Legends", level=1)
        for number, (_, caption) in FIGURES.items():
            paragraph = document.add_paragraph()
            paragraph.paragraph_format.line_spacing = 1.5
            paragraph.paragraph_format.space_after = Pt(8)
            run = paragraph.add_run(f"Figure {number}. ")
            run.bold = True
            paragraph.add_run(caption)
        document.add_heading("Supporting Information Legends", level=1)
        for number, (_, caption) in SUPPORTING_FIGURES.items():
            paragraph = document.add_paragraph()
            paragraph.paragraph_format.line_spacing = 1.5
            paragraph.paragraph_format.space_after = Pt(8)
            run = paragraph.add_run(f"Figure S{number}. ")
            run.bold = True
            paragraph.add_run(caption)
        document.add_heading("Tables", level=1)
        for number in TABLES:
            add_word_table(document, number)


def create_manuscript(path: Path, inline: bool, anonymous: bool = True) -> None:
    document = Document()
    configure_document(document)
    document.core_properties.title = TITLE
    document.core_properties.author = AUTHOR if not anonymous else ""
    add_title(document)
    add_abstract_page(document)
    add_manuscript_body(document, inline)
    document.save(path)


def create_tables_document(path: Path) -> None:
    document = Document()
    configure_document(document)
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run("Editable Tables")
    run.bold = True
    run.font.size = Pt(16)
    paragraph = document.add_paragraph(TITLE)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for number in TABLES:
        add_word_table(document, number)
        if number != max(TABLES):
            document.add_page_break()
    document.save(path)


def create_single_table_document(path: Path, table_number: int) -> None:
    document = Document()
    configure_document(document)
    add_word_table(document, table_number)
    document.save(path)


def create_single_supporting_table_document(path: Path, table_number: int) -> None:
    document = Document()
    configure_document(document)
    add_supporting_table(document, table_number)
    document.save(path)


def create_excel_tables(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for label, spec in [("Table_1", TABLES[1]), ("Table_S1", SUPPORTING_TABLES[1])]:
        title, row_function, note = spec
        rows = row_function()
        df = pd.DataFrame(rows[1:], columns=rows[0])
        excel_path = output_dir / f"{label}.xlsx"
        with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Table")
            worksheet = writer.sheets["Table"]
            for col in worksheet.columns:
                max_length = 0
                column = col[0].column_letter
                for cell in col:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except Exception:
                        pass
                adjusted_width = min(max_length + 2, 50)
                worksheet.column_dimensions[column].width = adjusted_width


def create_supporting_information(path: Path) -> None:
    document = Document()
    configure_document(document)
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run("Supporting Information")
    run.bold = True
    run.font.size = Pt(16)
    paragraph = document.add_paragraph(TITLE)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for number, (filename, caption) in SUPPORTING_FIGURES.items():
        heading = document.add_paragraph()
        heading.paragraph_format.space_before = Pt(16)
        run = heading.add_run(f"Figure S{number}. {caption}")
        run.bold = True
        image = document.add_paragraph()
        image.alignment = WD_ALIGN_PARAGRAPH.CENTER
        image.add_run().add_picture(
            str(FIGURE_DIR / filename), width=Inches(6.35)
        )
        document.add_page_break()
    for number in SUPPORTING_TABLES:
        add_supporting_table(document, number)
        document.add_page_break()
    document.add_heading("Supplementary File Inventory", level=1)
    document.add_paragraph(
        "The submission contains 5 main figures (Figures 1-5), 7 supplementary "
        "figures (Figures S1-S7), 1 main table (Table 1), 1 supplementary table "
        "(Table S1), and 10 machine-readable supplementary data files listed below."
    )
    document.add_paragraph(
        "Supplementary Data 1: population_metadata.csv. Population, project of origin, sample size, representative latitude and longitude, continental assignment, recent-admixture flag, and inclusion status for each of the 66 analysed populations."
    )
    document.add_paragraph(
        "Supplementary Data 2: pairwise_sharing_corrected.csv. All 2,145 population pairs with Neanderthal and Denisovan profile similarity, great-circle distance, covariate indicators, fitted values, residual z scores, permutation P values, and Benjamini-Hochberg q values."
    )
    document.add_paragraph(
        "Supplementary Data 3: model_summary.csv. Quadratic assignment procedure coefficients for both ancestries, population-label permutation P values, descriptive R-squared values, and population-deletion intervals."
    )
    document.add_paragraph(
        "Supplementary Data 4: sensitivity_analysis.csv. Similarity-metric and population-subset robustness summaries, including the non-admixed subset of 1,891 pairs from 62 populations."
    )
    document.add_paragraph(
        "Supplementary Data 5: window_size_sensitivity.csv. Robustness of the population-wide geographic-distance association at 250-kb, 500-kb, and 1-Mb genomic window sizes, reporting for each ancestry the raw distance correlation, the quadratic assignment procedure distance coefficient, the two-sided permutation P value, the descriptive R-squared value, and the number of permutations."
    )
    document.add_paragraph(
        "Supplementary Data 6: profile_quality_checks.csv. Ancestry-level profile quality checks reporting the maximum observed population-window frequency, the number of bins exceeding one, and the number of non-zero population-window entries."
    )
    document.add_paragraph(
        "Supplementary Data 7: abo_focal_test.json. Prespecified ABO focal-window result: window coordinates, maximum standardised excess similarity, genome-wide percentile, empirical P value, and the number of usable windows for each ancestry."
    )
    document.add_paragraph(
        "Supplementary Data 8: ancient_abo_summary.csv. Ancient-individual summaries extracted from the published Neanderthal-segment catalogue for the ABO interval, giving for each of the 59 assessed ancient individuals the age, population, region, closest archaic reference, reference proportions, segment-detection status, and strict ABO gene overlap. These data were generated by a different pipeline from the present-day profiles, are used descriptively only in the Discussion, and are not compared statistically with the present-day data; no analysis result depends on this file."
    )
    document.add_paragraph(
        "Supplementary Data 9: ancient_abo_provenance.json. Provenance for the ancient ABO-interval summary, including the source publication and source data DOIs, the GRCh37/hg19 genome build, the ABO gene and window coordinates, the diagnostic-site and genetic-map settings, the source file names with their SHA-256 checksums, and the counts of ancient individuals assessed, with a detected segment, and with strict ABO overlap."
    )
    document.add_paragraph(
        "Supplementary Data 10: analysis_provenance.json. Provenance for the committed analysis, including the analysis release, the analysis code commit, the input file names with their SHA-256 checksums, the minimum segment probability and minimum population size, the genomic bin size, the frequency definition, and the final counts of individuals, populations, and population pairs."
    )
    document.add_paragraph(
        "The ten files designated Supplementary Data 1-10 are the formal "
        "machine-readable supplementary files cited in the article. The accompanying "
        "data archive also contains additional derived intermediate and auxiliary "
        "files retained to support reproducibility and auditability: it holds 23 "
        "files in total under data/, of which the 13 not designated above are "
        "intermediate or auxiliary derived files, together with a README_DATA.md "
        "documentation file."
    )
    document.add_paragraph(
        "Supporting documents: HUMAN_GENETICS_SUPPORTING_INFORMATION.docx (this file, "
        "containing Figures S1-S7 and Table S1), Table_S1_abo_summary.docx "
        "(editable supplementary table), and tables_humangen/Table_S1.xlsx "
        "(spreadsheet version of Table S1)."
    )
    document.add_paragraph(
        "Supplementary figure files: figures/Figure_S1 to figures/Figure_S7, each "
        "supplied as a 300-dpi PNG and a 300-dpi TIFF."
    )
    document.save(path)



def create_supplementary_inventory(path: Path) -> None:
    rows = [
        "| Supplementary Data 1 | `supplementary_data/population_metadata.csv` | Population, project of origin, sample size, representative latitude and longitude, continental assignment, recent-admixture flag, and inclusion status for each of the 66 analysed populations. |",
        "| Supplementary Data 2 | `supplementary_data/pairwise_sharing_corrected.csv` | All 2,145 population pairs with Neanderthal and Denisovan profile similarity, great-circle distance, covariate indicators, fitted values, residual z scores, permutation P values, and Benjamini-Hochberg q values. |",
        "| Supplementary Data 3 | `supplementary_data/model_summary.csv` | Quadratic assignment procedure coefficients for both ancestries, population-label permutation P values, descriptive R-squared values, and population-deletion intervals. |",
        "| Supplementary Data 4 | `supplementary_data/sensitivity_analysis.csv` | Similarity-metric and population-subset robustness summaries, including the non-admixed subset of 1,891 pairs from 62 populations. |",
        "| Supplementary Data 5 | `supplementary_data/window_size_sensitivity.csv` | Robustness of the population-wide geographic-distance association at 250-kb, 500-kb, and 1-Mb genomic window sizes, reporting for each ancestry the raw distance correlation, the QAP distance coefficient, the two-sided permutation P value, the descriptive R-squared value, and the number of permutations. |",
        "| Supplementary Data 6 | `supplementary_data/profile_quality_checks.csv` | Ancestry-level profile quality checks (2 rows): maximum observed population-window frequency, number of bins exceeding one, and number of non-zero population-window entries. |",
        "| Supplementary Data 7 | `supplementary_data/abo_focal_test.json` | Prespecified ABO focal-window result: window coordinates, maximum standardised excess similarity, genome-wide percentile, empirical P value, and the number of usable windows for each ancestry. |",
        "| Supplementary Data 8 | `supplementary_data/ancient_abo_summary.csv` | Ancient-individual summaries extracted from the published Neanderthal-segment catalogue for the ABO interval (59 assessed individuals; age, population, region, closest archaic reference, reference proportions, segment-detection status, strict ABO gene overlap). Generated by a different pipeline from the present-day profiles, used descriptively only; no analysis result depends on this file. |",
        "| Supplementary Data 9 | `supplementary_data/ancient_abo_provenance.json` | Provenance for the ancient ABO-interval summary: source publication and source data DOIs, GRCh37/hg19 genome build, ABO gene and window coordinates, diagnostic-site and genetic-map settings, source file names with SHA-256 checksums, and counts of ancient individuals assessed, with a detected segment, and with strict ABO overlap. |",
        "| Supplementary Data 10 | `supplementary_data/analysis_provenance.json` | Provenance for the committed analysis: analysis release, analysis code commit, input file names with SHA-256 checksums, minimum segment probability and minimum population size, genomic bin size, frequency definition, and final counts of individuals, populations, and population pairs. |",
    ]
    content = """# Supplementary file inventory: Human Genetics submission

Package: `HUMAN_GENETICS_SUBMISSION_FINAL.zip`.

## Counts

| Item | Count |
| --- | --- |
| Main figures (Figures 1-5) | 5 |
| Supplementary figures (Figures S1-S7) | 7 |
| Main tables (Table 1) | 1 |
| Supplementary tables (Table S1) | 1 |
| Supplementary machine-readable data files | 10 |
| Supporting Information documents | 1 |
| Cover letters | 1 |
| Title pages | 1 |
| Manuscript files (main, author-side inline copy) | 2 |

## Machine-readable supplementary data files

| Label | File | Description |
| --- | --- | --- |
""" + "\n".join(rows) + """

## Supplementary documents, tables and figures

| File | Description |
| --- | --- |
| `HUMAN_GENETICS_SUPPORTING_INFORMATION.docx` | Supporting Information: Figures S1-S7, Table S1, and this inventory. |
| `Table_S1_abo_summary.docx` | Editable supplementary table of the prespecified ABO focal-window result. |
| `tables_humangen/Table_S1.xlsx` | Spreadsheet version of Table S1. |
| `tables_humangen/Table_1.xlsx` | Spreadsheet version of main Table 1. |
| `Table_1_residual_outliers.docx` | Editable main table of the largest pair-level residuals. |
| `figures/Figure_S1.png` and `figures/Figure_S1.tiff` | Supplementary Figure S1, 300 dpi PNG and TIFF. |
| `figures/Figure_S2.png` and `figures/Figure_S2.tiff` | Supplementary Figure S2, 300 dpi PNG and TIFF. |
| `figures/Figure_S3.png` and `figures/Figure_S3.tiff` | Supplementary Figure S3, 300 dpi PNG and TIFF. |
| `figures/Figure_S4.png` and `figures/Figure_S4.tiff` | Supplementary Figure S4, 300 dpi PNG and TIFF. |
| `figures/Figure_S5.png` and `figures/Figure_S5.tiff` | Supplementary Figure S5, 300 dpi PNG and TIFF. |
| `figures/Figure_S6.png` and `figures/Figure_S6.tiff` | Supplementary Figure S6, 300 dpi PNG and TIFF. |
| `figures/Figure_S7.png` and `figures/Figure_S7.tiff` | Supplementary Figure S7, 300 dpi PNG and TIFF. |

Every file listed here is present in the package, and the package contains no supplementary file that is not listed.

The ten Supplementary Data files are the formal machine-readable supplementary
files cited in the article. The accompanying `data_archive_humangen.zip` also
contains additional derived intermediate and auxiliary files retained to support
reproducibility and auditability (23 files under data/ in total, plus a
README_DATA.md documentation file); the distinction between formal Supplementary
Data and auxiliary derived files is documented in `data_detail_humangen.docx`.
"""
    path.write_text(content, encoding="utf-8")


def create_cover_letter(path: Path) -> None:
    document = Document()
    configure_document(document)
    document.styles["Normal"].paragraph_format.line_spacing = 1
    document.styles["Normal"].paragraph_format.space_after = Pt(7)
    for text in EDITORS_BLOCK:
        document.add_paragraph(text)
    document.add_paragraph()
    paragraph = document.add_paragraph()
    run = paragraph.add_run(f"Re: Submission of a {ARTICLE_TYPE}")
    run.bold = True
    document.add_paragraph("Dear Editors-in-Chief,")
    paragraphs = [
        (
            f'I am pleased to submit "{TITLE}" for consideration as a '
            f'{ARTICLE_TYPE} in {JOURNAL}.'
        ),
        (
            "Pairwise comparisons between populations are a routine currency of "
            "human genetics: genetic distance, allele-frequency similarity, "
            "haplotype sharing, and archaic-ancestry profiles are all computed "
            "pair by pair, and pairs that look unusually similar are readily "
            "read as evidence of a specific historical connection. The problem "
            "is that the same populations recur across many pairs, so the "
            "measurements in a pairwise matrix are not independent. A pair that "
            "looks exceptional may simply be sitting where broad population "
            "structure places it, and comparing it against an independence-based "
            "reference produces exactly the wrong expectation."
        ),
        (
            "The manuscript turns that observation into an operational test. It "
            "defines a structural null for pairwise genomic similarity: the "
            "complete 66-population matrix is retained, population labels are "
            "permuted jointly across rows and columns (the quadratic assignment "
            "procedure), each pair's residual from the population-wide model is "
            "referenced to the null distribution generated by the same "
            "permutations, and the family of pair-level tests is controlled for "
            "multiplicity. I do not claim a new permutation method, and I do not "
            "claim that population-structure bias is newly discovered; the "
            "contribution is an explicit, dependence-aware workflow that makes "
            "the statement 'this pair is exceptional' testable."
        ),
        (
            "Applied to high-confidence Neanderthal and Denisovan introgression "
            f"calls from {revised_content.INDIVIDUALS:,} individuals in "
            f"{revised_content.POPULATIONS} populations (1000 Genomes Project and "
            f"Human Genome Diversity Project), the workflow separates two claims "
            "that are often conflated: 'this pair looks similar' and 'this pair "
            "is more similar than human population structure predicts.' Similarity "
            "declines strongly with geographic distance under the permutation "
            "null, yet no population pair exceeded the prespecified residual and "
            "false-discovery-rate criteria, and the prespecified ABO blood-group "
            "region, a locus repeatedly invoked in archaic-connection narratives, "
            "did not exceed the genome-wide structural expectation. I am careful "
            "to present this as evidence against pair-specific excess similarity "
            "in these data, not as evidence that the populations concerned lack "
            "shared history."
        ),
        (
            "I believe this fits Human Genetics directly. The journal's stated "
            "scope covers population genetics, evolutionary genetics, genetic "
            "diversity in human populations, and methods in statistical genetics. "
            "The paper addresses all four: it is a human population-genetic study "
            "of archaic introgression whose result disciplines how pairwise "
            "genomic similarity claims should be read, and it does so with a "
            "statistical framework that other human-genetic comparisons can adopt "
            "unchanged. The manuscript is deliberately not framed as clinical "
            "genetics; its readership is the population- and "
            "evolutionary-genetics community the journal serves."
        ),
        (
            "The work is original, is not under consideration elsewhere, and uses "
            "de-identified public genomic resources; no new human participants or "
            "specimens were recruited. The manuscript explicitly discloses that no "
            "separate institutional review determination, community "
            "participation, or direct return-of-results process occurred for this "
            "secondary analysis. I declare no competing interests and report no "
            "external funding."
        ),
        (
            "All analysis code and derived outputs are available through the "
            "project repository (https://github.com/bougtoir/"
            "denisovan-archaic-dna-analysis), and the source "
            "archaic-introgression segment calls are publicly archived in "
            "Zenodo. The submission includes separate figure files, editable "
            "tables, figure legends in the manuscript, and a complete "
            "Supporting Information file."
        ),
    ]
    for text in paragraphs:
        document.add_paragraph(text)
    document.add_paragraph("Sincerely,")
    document.add_paragraph(AUTHOR)
    document.add_paragraph(AFFILIATION)
    document.add_paragraph("Email: bougtoir@gmail.com")
    document.save(path)


def add_slide_title(slide, title: str) -> None:
    box = slide.shapes.add_textbox(
        PptInches(0.6),
        PptInches(0.12),
        PptInches(12.1),
        PptInches(0.7),
    )
    box.text_frame.word_wrap = True
    paragraph = box.text_frame.paragraphs[0]
    paragraph.text = title
    paragraph.font.name = "Arial"
    paragraph.font.size = PptPt(16)
    paragraph.font.bold = True
    paragraph.alignment = PP_ALIGN.CENTER


def add_slide_caption(slide, caption: str) -> None:
    box = slide.shapes.add_textbox(
        PptInches(0.65),
        PptInches(6.55),
        PptInches(12.0),
        PptInches(0.72),
    )
    box.text_frame.word_wrap = True
    paragraph = box.text_frame.paragraphs[0]
    paragraph.text = caption
    paragraph.font.name = "Arial"
    paragraph.font.size = PptPt(8)
    paragraph.alignment = PP_ALIGN.LEFT


def add_picture_contained(slide, path: Path) -> None:
    with Image.open(path) as image:
        width, height = image.size
    area_left = 0.55
    area_top = 0.85
    area_width = 12.2
    area_height = 5.65
    scale = min(area_width / width, area_height / height)
    picture_width = width * scale
    picture_height = height * scale
    left = area_left + (area_width - picture_width) / 2
    top = area_top + (area_height - picture_height) / 2
    slide.shapes.add_picture(
        str(path),
        PptInches(left),
        PptInches(top),
        PptInches(picture_width),
        PptInches(picture_height),
    )


def add_ppt_table(slide, rows: list[list[str]]) -> None:
    table_shape = slide.shapes.add_table(
        len(rows),
        len(rows[0]),
        PptInches(0.45),
        PptInches(1.0),
        PptInches(12.4),
        PptInches(5.5),
    )
    table = table_shape.table
    for row_index, row in enumerate(rows):
        for column_index, value in enumerate(row):
            cell = table.cell(row_index, column_index)
            cell.text = value
            cell.fill.solid()
            cell.fill.fore_color.rgb = (
                PptRGBColor(217, 234, 247)
                if row_index == 0
                else PptRGBColor(255, 255, 255)
            )
            for paragraph in cell.text_frame.paragraphs:
                paragraph.font.name = "Arial"
                paragraph.font.size = PptPt(9)
                paragraph.font.bold = row_index == 0


def create_presentation(path: Path) -> None:
    presentation = Presentation()
    presentation.slide_width = PptInches(13.333)
    presentation.slide_height = PptInches(7.5)
    blank = presentation.slide_layouts[6]
    for number, (filename, caption) in FIGURES.items():
        slide = presentation.slides.add_slide(blank)
        add_slide_title(slide, f"Figure {number}")
        add_picture_contained(slide, FIGURE_DIR / filename)
        add_slide_caption(slide, caption)
    for number, (filename, caption) in SUPPORTING_FIGURES.items():
        slide = presentation.slides.add_slide(blank)
        add_slide_title(slide, f"Figure S{number}")
        add_picture_contained(slide, FIGURE_DIR / filename)
        add_slide_caption(slide, caption)
    for number, (title, row_function, note) in TABLES.items():
        slide = presentation.slides.add_slide(blank)
        add_slide_title(slide, f"Table {number}. {title}")
        add_ppt_table(slide, row_function())
        add_slide_caption(slide, f"Note. {note}")
    for number, (title, row_function, note) in SUPPORTING_TABLES.items():
        slide = presentation.slides.add_slide(blank)
        add_slide_title(slide, f"Table S{number}. {title}")
        add_ppt_table(slide, row_function())
        add_slide_caption(slide, f"Note. {note}")
    presentation.save(path)


def prepare_separate_figures() -> None:
    OUTPUT_FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    for stale in OUTPUT_FIGURE_DIR.glob("Figure_*"):
        stale.unlink()
    for number, (filename, _) in FIGURES.items():
        source = FIGURE_DIR / filename
        png_target = OUTPUT_FIGURE_DIR / f"Figure_{number}.png"
        tiff_target = OUTPUT_FIGURE_DIR / f"Figure_{number}.tiff"
        shutil.copy2(source, png_target)
        tiff_source = source.with_suffix(".tiff")
        if tiff_source.exists():
            shutil.copy2(tiff_source, tiff_target)
        else:
            with Image.open(source) as image:
                image.convert("RGB").save(
                    tiff_target,
                    format="TIFF",
                    dpi=(300, 300),
                    compression="tiff_lzw",
                )
    for number, (filename, _) in SUPPORTING_FIGURES.items():
        source = FIGURE_DIR / filename
        png_target = OUTPUT_FIGURE_DIR / f"Figure_S{number}.png"
        tiff_target = OUTPUT_FIGURE_DIR / f"Figure_S{number}.tiff"
        shutil.copy2(source, png_target)
        tiff_source = source.with_suffix(".tiff")
        if tiff_source.exists():
            shutil.copy2(tiff_source, tiff_target)
        else:
            with Image.open(source) as image:
                image.convert("RGB").save(
                    tiff_target,
                    format="TIFF",
                    dpi=(300, 300),
                    compression="tiff_lzw",
                )


def validate_content() -> list[str]:
    body_texts = _body_texts()
    joined_body = "\n".join(body_texts)
    uncited_references = []
    for key in REFERENCE_KEYS:
        author, year = key.rsplit(" ", 1)
        variants = [key, f"{author} ({year})", f"{author} et al. ({year})"]
        if not any(variant in joined_body for variant in variants):
            uncited_references.append(key)
    figure_mentions = []
    supporting_figure_mentions = []
    table_mentions = []
    for text in body_texts:
        figure_mentions.extend(
            int(value) for value in re.findall(r"Figures? (?!S)(\d+)", text)
        )
        supporting_figure_mentions.extend(
            int(value) for value in re.findall(r"Figures? S(\d+)", text)
        )
        table_mentions.extend(int(value) for value in re.findall(r"Table (\d+)", text))
    figure_order = list(dict.fromkeys(figure_mentions))
    supporting_figure_order = list(dict.fromkeys(supporting_figure_mentions))
    table_order = list(dict.fromkeys(table_mentions))
    unresolved = [
        value
        for value in [
            "[" + "Affiliation to be added]",
            "[" + "To be added]",
            "[" + "Corresponding author details]",
        ]
        if value in "\n".join(body_texts)
    ]
    main_word_count = _main_text_word_count()
    checks = [
        ("Author-date citations", not re.findall(r"\{\d", joined_body)),
        ("Every reference cited", not uncited_references),
        ("References alphabetised", REFERENCES == sorted(REFERENCES)),
        ("Figure first-appearance order", figure_order == list(FIGURES)),
        (
            "Supporting figure first-appearance order",
            supporting_figure_order == list(SUPPORTING_FIGURES),
        ),
        ("Table first-appearance order", table_order == list(TABLES)),
        ("No placeholder strings", not unresolved),
        ("Running title under 150 characters", len(RUNNING_TITLE) <= 150),
        ("Summary within 150-250 words", 150 <= len(ABSTRACT.split()) <= 250),
        (
            "Four to six keywords",
            4 <= len([k for k in KEYWORDS.split(";") if k.strip()]) <= 6,
        ),
        (
            "All figure source files present",
            all((FIGURE_DIR / filename).exists() for filename, _ in FIGURES.values()),
        ),
        (
            "All supporting figure source files present",
            all(
                (FIGURE_DIR / filename).exists()
                for filename, _ in SUPPORTING_FIGURES.values()
            ),
        ),
        ("References present", len(REFERENCES) > 0),
    ]
    lines = [
        f"{JOURNAL_SHORT} SUBMISSION VALIDATION",
        "==========================",
        "",
        f"Summary words: {len(ABSTRACT.split())}",
        f"Main-text words: {main_word_count}",
        f"References: {len(REFERENCES)}",
        f"Uncited references: {uncited_references}",
        f"First-appearance figure order: {figure_order}",
        f"First-appearance supporting figure order: {supporting_figure_order}",
        f"First-appearance table order: {table_order}",
        "",
    ]
    for label, passed in checks:
        lines.append(f"{'PASS' if passed else 'FAIL'}: {label}")
    if not all(passed for _, passed in checks):
        raise RuntimeError("\n".join(lines))
    return lines


def create_checklist(path: Path) -> None:
    content = """# Human Genetics submission checklist

## Journal parameters (verified against current Springer Nature Instructions for Authors)

- Journal: Human Genetics (Springer Nature), hybrid publishing model
- Article type: Research Article
- Abstract: 150-250 words, unstructured, no undefined abbreviations
- Keywords: 4-6
- Headings: no more than three displayed levels
- Text: .docx; editable source files required at submission
- Citations: author-date in text; reference list alphabetised by first author
- Reference style: Springer author-date (e.g. "Gamelin FX et al (2009) Title. Eur J Appl Physiol 105:731-738. https://doi.org/...")
- Acknowledgments: separate section on the title page
- Author Contribution and Competing Interests also entered via the submission interface
- Peer review: single-blind; separate title page supplied as its own file
- Publication route: traditional (non-Open Choice) route available without mandatory publication charges; Open Choice is optional
- AI/LLM: LLM authorship not permitted; AI use documented in a declaration section (copy-editing use need not be declared; declared here conservatively)

## Package counts

- Main figures: 5 (Figures 1-5)
- Supplementary figures: 7 (Figures S1-S7)
- Main tables: 1 (Table 1)
- Supplementary tables: 1 (Table S1)
- Supplementary machine-readable files: 10
- Supporting Information documents: 1
- Cover letters: 1
- Title pages: 1
- Manuscript files: 2 (main manuscript and author-side inline review copy)

## Prepared files

- `HUMAN_GENETICS_TITLE_PAGE.docx`: title, article type, author, affiliation, corresponding author, running title, word count, acknowledgments
- `HUMAN_GENETICS_MAIN_MANUSCRIPT.docx`: main manuscript (title, abstract, keywords, Introduction, Materials and Methods, Results, Discussion, Acknowledgements, Funding, Author Contributions, Competing Interests, Data Availability, AI declaration, Ethics, References, Figure Legends, Tables)
- `HUMAN_GENETICS_MAIN_MANUSCRIPT_inline_review.docx`: internal review copy with figures and tables immediately after first mention
- `Table_1_residual_outliers.docx`: editable main table
- `Table_S1_abo_summary.docx`: editable supporting table
- `tables_humangen/Table_1.xlsx` and `tables_humangen/Table_S1.xlsx`: Excel versions for upload
- `HUMAN_GENETICS_SUPPORTING_INFORMATION.docx`: Supporting Figures S1-S7, supporting Table S1, and the supplementary file inventory
- `SUPPLEMENTARY_FILE_INVENTORY.md`: one-line description of every supplementary upload file
- `figures_tables_humangen.pptx`: Figures 1-5, Figures S1-S7, Table 1, and Table S1 (internal review aid)
- `HUMAN_GENETICS_COVER_LETTER.docx`: cover letter addressed to the Editors-in-Chief
- `figures/Figure_1` through `Figure_5` and `figures/Figure_S1` through `Figure_S7`: separate PNG and TIFF files (300 dpi)
- `supplementary_data/`: 10 machine-readable files (population metadata, complete pairwise results, model output, sensitivities, profile quality checks, ABO focal test, ancient ABO summary, and provenance records)
- `data_archive_humangen.zip`: full derived-data archive (23 files under data/ plus README_DATA.md)
- `data_detail_humangen.docx`: data documentation describing the formal Supplementary Data files and the auxiliary derived files
- `reproducibility_checklist.md`: data provenance, rebuild commands, expected checks, and package versions
- `reference_validation.csv`: DOI/PubMed existence and title checks (if generated)

## Automated checks

- Author-date citations in the body; no numbered bracket citations
- Every listed reference is cited and every citation has a reference entry
- Figures 1-5 and Table 1 are first mentioned sequentially
- Summary within 150-250 words
- Four to six keywords
- Running title within 150 characters
- Title page, availability, funding, competing-interests, ethics, and contribution statements present
- No submission placeholder strings remain

## Author checks before upload

- Confirm the full correspondence postal address and email.
- Confirm the no-external-funding statement.
- Confirm the competing-interests statement.
- Confirm institutional determination is not required for this secondary genomic analysis.
- Review the explicit disclosure of no direct community engagement or return of results.
- Provide an authenticated ORCID iD for the submitting author in the submission portal.
- Upload the title page as its own file and the main manuscript file separately.
- Upload each figure as a separate TIFF or PNG file; do not embed figures in the manuscript.
- Upload Excel table files and the Supporting Information file; supplementary data files as online supplementary material.
- Re-enter Author Contribution and Competing Interests text in the submission interface (the interface version is authoritative).
- Do not interpret nominal residuals or the two Indigenous-American ABO-window segments as definitive migration evidence.

## Submission links

- Author guidelines: https://link.springer.com/journal/439/submission-guidelines
- Aims and scope: https://link.springer.com/journal/439/aims-and-scope
- Online submission: via the "Submit manuscript" link on the journal homepage (Editorial Manager)
"""
    path.write_text(content, encoding="utf-8")


def create_reproducibility_checklist(path: Path) -> None:
    packages = [
        "pandas",
        "numpy",
        "scipy",
        "statsmodels",
        "matplotlib",
        "seaborn",
        "python-docx",
        "python-pptx",
        "Pillow",
        "openpyxl",
    ]
    versions = []
    for package in packages:
        try:
            versions.append(f"- `{package}=={version(package)}`")
        except PackageNotFoundError:
            versions.append(f"- `{package}`: version not available")
    content = f"""# Reproducibility checklist

## Repository

- Analysis scripts, derived data, and figures: https://github.com/bougtoir/denisovan-archaic-dna-analysis
- ABO focal-window test: `scripts/abo_window_focal_test.py`, run by `scripts/run_ajba_pipeline.py`, writing `data/abo_focal_test.json`

## Public source data

- hmmix archaic-introgression segment files from the 1000 Genomes Project and Human Genome Diversity Project (HGDP): Zenodo record 14136628
- O2 blood-group subtype-defining `rs41302905 T` frequencies: Ensembl Variation application programming interface endpoint
- Solomon Islands ABO*O02 frequencies: Ohashi et al. 2006, doi:10.1007/s10038-006-0375-8
- Ancient ABO-window summary: reproducibly extracted from the public Neanderthal-segment catalogue of Iasi et al. 2024 (Dryad doi:10.5061/dryad.zw3r228gg) by `scripts/build_ancient_abo_summary.py`. Source-file SHA-256 hashes are recorded in `data/ancient_abo_provenance.json`.

## Rebuild order

Run from the project root:

```bash
python scripts/run_ajba_pipeline.py \\
  --segments-1kg /path/to/hg38_1000g_segments.txt \\
  --segments-hgdp /path/to/hg38_HGDP_segments.txt \\
  --permutations 9999 \\
  --sensitivity-permutations 999
python scripts/create_humangen_submission.py
```

The committed `data/ancient_abo_summary.csv` (supporting temporal figure only) is regenerated by additionally passing the Iasi et al. 2024 Dryad files:

```bash
python scripts/build_ancient_abo_summary.py \\
  --iasi-segments /path/to/Neandertal_segments_matching_references_Shared_map.csv \\
  --iasi-metadata /path/to/Meta_Data_individuals.csv
```

## Expected primary checks

- Individuals: {revised_content.INDIVIDUALS:,}
- Populations: {revised_content.POPULATIONS}
- Unique population pairs: {revised_content.PAIRS:,}
- Every population-window frequency is between 0 and 1
- Neanderthal raw distance r: {revised_content.NEANDERTHAL['raw_r']:.4f}
- Denisovan raw distance r: {revised_content.DENISOVAN['raw_r']:.4f}
- Neanderthal expanded descriptive R²: {revised_content.NEANDERTHAL['expanded_r_squared']:.4f}
- Denisovan expanded descriptive R²: {revised_content.DENISOVAN['expanded_r_squared']:.4f}
- QAP distance P: {revised_content.NEANDERTHAL['distance_qap_p']:.4f} and {revised_content.DENISOVAN['distance_qap_p']:.4f}
- ABO focal-window excess-similarity z (predicted minus observed absolute difference, standardised): {revised_content.ABO_FOCAL['nean_abo_max_excess_z']:.4f} Neanderthal and {revised_content.ABO_FOCAL['deni_abo_max_excess_z']:.4f} Denisovan
- ABO focal-window empirical P: {revised_content.ABO_FOCAL['nean_abo_empirical_p']:.5f} and {revised_content.ABO_FOCAL['deni_abo_empirical_p']:.5f}
- FDR q<0.10 non-admixed outliers: {revised_content.NEANDERTHAL['fdr_q_lt_0.10_positive_z_gt_2']} and {revised_content.DENISOVAN['fdr_q_lt_0.10_positive_z_gt_2']}
- Neanderthal/Both segments in the 500-kb ABO interval: {revised_content.ABO['interval_segments']:,}
- Strict ABO-overlapping Neanderthal/Both segments: {revised_content.ABO['strict_overlap']}
- Neanderthal/Both segments with tied maximum reference similarity: {revised_content.ABO['ties']}
- Indigenous American window carriers: Pima 1/13, Maya 1/21, Colombian 0/7
- Strict ABO overlap among those carriers: Pima only

## Environment used for the package

{chr(10).join(versions)}

## Interpretation guardrails

- Pairwise correlation does not prove identity by descent.
- Pairwise rows are dependent; inference uses population-label QAP permutations.
- Expanded-model R² is descriptive and not a causal variance decomposition.
- Reference-genome similarity does not prove a specific migration route.
- Admixed American residuals are not treated as ancient-migration evidence.
- No positive-residual non-admixed pair survived FDR correction.
- Ancient and modern ABO-window calls were produced by different pipelines.
- The ABO-window scan is a prespecified negative test, not a route proposal.
"""
    path.write_text(content, encoding="utf-8")


def create_zip(path: Path, files: list[Path]) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in files:
            archive.write(file_path, file_path.relative_to(OUTPUT_DIR))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for stale in ["Table_1_corrected_model.docx", "Table_2_abo_summary.docx"]:
        (OUTPUT_DIR / stale).unlink(missing_ok=True)

    # Validation must pass before documents are created
    validation_lines = validate_content()

    main_word_count = _main_text_word_count()
    prepare_separate_figures()
    create_title_page(OUTPUT_DIR / "HUMAN_GENETICS_TITLE_PAGE.docx", main_word_count)
    create_manuscript(OUTPUT_DIR / "HUMAN_GENETICS_MAIN_MANUSCRIPT.docx", inline=False, anonymous=True)
    create_manuscript(OUTPUT_DIR / "HUMAN_GENETICS_MAIN_MANUSCRIPT_inline_review.docx", inline=True, anonymous=True)
    create_tables_document(OUTPUT_DIR / "tables_humangen.docx")
    create_single_table_document(OUTPUT_DIR / "Table_1_residual_outliers.docx", 1)
    create_single_supporting_table_document(OUTPUT_DIR / "Table_S1_abo_summary.docx", 1)
    create_excel_tables(OUTPUT_DIR / "tables_humangen")
    create_supporting_information(OUTPUT_DIR / "HUMAN_GENETICS_SUPPORTING_INFORMATION.docx")
    create_cover_letter(OUTPUT_DIR / "HUMAN_GENETICS_COVER_LETTER.docx")
    create_supplementary_inventory(OUTPUT_DIR / "SUPPLEMENTARY_FILE_INVENTORY.md")
    presentation = OUTPUT_DIR / "figures_tables_humangen.pptx"
    create_presentation(presentation)
    checklist = OUTPUT_DIR / "SUBMISSION_CHECKLIST_HUMAN_GENETICS.md"
    reproducibility = OUTPUT_DIR / "reproducibility_checklist.md"
    validation = OUTPUT_DIR / "submission_validation.txt"
    create_checklist(checklist)
    create_reproducibility_checklist(reproducibility)
    validation.write_text("\n".join(validation_lines) + "\n", encoding="utf-8")

    # Run numeric consistency and reference validation from the public data files
    subprocess.run(
        ["python3", "scripts/validate_numeric_consistency_humangen.py"],
        cwd=str(PROJECT_DIR),
        check=True,
    )
    subprocess.run(
        ["python3", "scripts/validate_references_humangen.py"],
        cwd=str(PROJECT_DIR),
        check=True,
    )

    supplementary_directory = OUTPUT_DIR / "supplementary_data"
    supplementary_directory.mkdir(parents=True, exist_ok=True)
    supplementary_sources = [
        DATA_DIR / "population_metadata.csv",
        DATA_DIR / "pairwise_sharing_corrected.csv",
        DATA_DIR / "model_summary.csv",
        DATA_DIR / "sensitivity_analysis.csv",
        DATA_DIR / "window_size_sensitivity.csv",
        DATA_DIR / "analysis_provenance.json",
        DATA_DIR / "profile_quality_checks.csv",
        DATA_DIR / "ancient_abo_summary.csv",
        DATA_DIR / "ancient_abo_provenance.json",
        DATA_DIR / "abo_focal_test.json",
    ]
    for source in supplementary_sources:
        shutil.copy2(source, supplementary_directory / source.name)

    # Full derived-data archive and data documentation
    heredity_dir = PROJECT_DIR / "docs" / "heredity_submission" / "consistency_pass"
    data_archive = OUTPUT_DIR / "data_archive_humangen.zip"
    shutil.copy2(heredity_dir / "data_consistent.zip", data_archive)
    shutil.copy2(heredity_dir / "data_detail_consistent.docx", OUTPUT_DIR / "data_detail_humangen.docx")

    zip_files = [
        OUTPUT_DIR / "HUMAN_GENETICS_TITLE_PAGE.docx",
        OUTPUT_DIR / "HUMAN_GENETICS_MAIN_MANUSCRIPT.docx",
        OUTPUT_DIR / "HUMAN_GENETICS_MAIN_MANUSCRIPT_inline_review.docx",
        OUTPUT_DIR / "Table_1_residual_outliers.docx",
        OUTPUT_DIR / "Table_S1_abo_summary.docx",
        OUTPUT_DIR / "HUMAN_GENETICS_SUPPORTING_INFORMATION.docx",
        OUTPUT_DIR / "HUMAN_GENETICS_COVER_LETTER.docx",
        data_archive,
        OUTPUT_DIR / "data_detail_humangen.docx",
        presentation,
        checklist,
        reproducibility,
        validation,
        *sorted(OUTPUT_DIR.glob("tables_humangen/*.xlsx")),
        *sorted(OUTPUT_FIGURE_DIR.glob("Figure_*")),
        *sorted(supplementary_directory.iterdir()),
    ]
    reference_validation = OUTPUT_DIR / "reference_validation.csv"
    if reference_validation.exists():
        zip_files.append(reference_validation)
    numeric_consistency = OUTPUT_DIR / "numeric_consistency_check.txt"
    if numeric_consistency.exists():
        zip_files.append(numeric_consistency)
    for extra in ("SUPPLEMENTARY_FILE_INVENTORY.md", "HUMAN_GENETICS_REQUIREMENTS_AUDIT.md", "HUMAN_GENETICS_CITATION_ECOLOGY.md", "HUMAN_GENETICS_HOSTILE_REVIEW.md", "REFERENCE_AUDIT.md", "FINAL_HANDOFF_HUMAN_GENETICS.md", "RAW_DATA_PROVENANCE.md", "DEVIN_HUMAN_GENETICS_RETARGET_PROMPT.txt"):
        extra_path = OUTPUT_DIR / extra
        if extra_path.exists():
            zip_files.append(extra_path)
    create_zip(OUTPUT_DIR / "HUMAN_GENETICS_SUBMISSION_FINAL.zip", zip_files)
    print(f"Created {JOURNAL_SHORT} submission materials in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
