"""Human Genetics manuscript content populated from current analysis outputs."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parents[1]
STATISTICS = json.loads(
    (PROJECT_DIR / "data" / "correction_stats.json").read_text(encoding="utf-8")
)
NEANDERTHAL = STATISTICS["nean"]
DENISOVAN = STATISTICS["deni"]
PROVENANCE = json.loads(
    (PROJECT_DIR / "data" / "analysis_provenance.json").read_text(encoding="utf-8")
)


def value(statistics: dict[str, object], key: str, digits: int = 3) -> str:
    return f"{float(statistics[key]):.{digits}f}"


def _abo_counts() -> dict[str, int]:
    segments = pd.read_csv(PROJECT_DIR / "data" / "abo_neanderthal_segments.csv")
    populations = pd.read_csv(PROJECT_DIR / "data" / "abo_population_summary.csv")
    indigenous = populations["analysis_group"] == "Indigenous Americas"
    return {
        "interval_segments": int(len(segments)),
        "strict_overlap": int(segments["strict_overlap"].sum()),
        "ties": int((segments["closest_reference"] == "Tie").sum()),
        "indigenous_individuals": int(populations.loc[indigenous, "n_total"].sum()),
    }


def _residual_summary() -> dict[str, object]:
    """Summarise the pair-level residual evidence from the committed outputs."""
    pairs = pd.read_csv(PROJECT_DIR / "data" / "pairwise_sharing_corrected.csv")
    pairs = pairs[pairs["any_admixed"] == 0]
    populations = pd.unique(pairs[["pop1", "pop2"]].values.ravel())
    summary: dict[str, object] = {
        "pairs": int(len(pairs)),
        "populations": int(len(populations)),
    }
    for prefix in ("nean", "deni"):
        residual = pairs[f"{prefix}_resid_z"].dropna()
        qvalues = pairs[f"{prefix}_fdr_pval"].dropna()
        summary[f"{prefix}_max_z"] = float(residual.max())
        summary[f"{prefix}_min_q"] = float(qvalues.min())
        summary[f"{prefix}_supported"] = int(
            ((pairs[f"{prefix}_resid_z"] > 2.0) & (pairs[f"{prefix}_fdr_pval"] < 0.10))
            .fillna(False)
            .sum()
        )
    return summary


ABO_FOCAL = json.loads(
    (PROJECT_DIR / "data" / "abo_focal_test.json").read_text(encoding="utf-8")
)
ABO = _abo_counts()
RESIDUALS = _residual_summary()
INDIVIDUALS = int(PROVENANCE["individuals"])
POPULATIONS = int(PROVENANCE["included_populations"])
PAIRS = int(PROVENANCE["population_pairs"])
PRIMARY_PERMUTATIONS = int(STATISTICS["permutations"])
SENSITIVITY_PERMUTATIONS = int(STATISTICS["sensitivity_permutations"])


TITLE = (
    "Population structure defines the null expectation for pairwise genomic "
    f"similarity: archaic-segment sharing across {POPULATIONS} human populations"
)
RUNNING_TITLE = "A structural null for pairwise similarity"
AUTHOR = "Onishi Tatsuki"
AFFILIATION = (
    "Data Science and AI Innovation Research Promotion Center, "
    "Shiga University, Hikone, Shiga, Japan"
)
CORRESPONDENCE = (
    "Onishi Tatsuki, Data Science and AI Innovation Research Promotion Center, "
    "Shiga University, Hikone, Shiga, Japan; Email: bougtoir@gmail.com"
)

ABSTRACT = (
    "Pairwise comparisons between populations are a standard currency of "
    "population genetics, but the same populations recur across many pairs, so "
    "pairwise measurements are not independent observations. A pair that looks "
    "unusually similar may simply sit where broad population structure places "
    "it, yet such pairs are often read as evidence of a specific historical or "
    "biological connection. We ask what similarity a pair should show given the "
    "relational structure of the whole population set, and use archaic-segment "
    "sharing as an empirical demonstration. High-confidence Neanderthal and "
    f"Denisovan introgression calls from {INDIVIDUALS:,} individuals in "
    f"{POPULATIONS} populations were summarised in 500-kilobase windows, and "
    f"profile similarity was computed for all {PAIRS:,} population pairs. "
    "Population-wide structure, pair-level residuals, and multiplicity were "
    "assessed with population-label permutation (the quadratic assignment "
    "procedure, QAP) and false-discovery-rate (FDR) control. Profile similarity "
    "declined with geographic distance for Neanderthal "
    f"(r={value(NEANDERTHAL, 'raw_r')}) and Denisovan "
    f"(r={value(DENISOVAN, 'raw_r')}) profiles, with partial distance "
    f"correlations of {value(NEANDERTHAL, 'partial_r')} and "
    f"{value(DENISOVAN, 'partial_r')} and permutation P values of "
    f"{value(NEANDERTHAL, 'distance_qap_p', 4)} and "
    f"{value(DENISOVAN, 'distance_qap_p', 4)}. No pair among the non-admixed "
    "populations reached both a positive residual above two standard deviations "
    "and an FDR-adjusted q below 0.10. A prespecified analysis of the ABO "
    "blood-group region, a focal locus frequently invoked in such arguments, "
    "did not exceed the genome-wide structural expectation either. Exceptional "
    "pairwise genomic similarity should be judged against a null that preserves "
    "population-wide relational structure before it is attributed to "
    "pair-specific human history or gene flow."
)

KEYWORDS = (
    "population structure; archaic introgression; dyadic data; "
    "permutation tests; Neanderthals; Denisovans"
)


# Helper for author formatting

def _format_authors(*authors: str, et_al: bool = False) -> str:
    """Format author names as 'Surname1 Initial1, Surname2 Initial2 et al.'"""
    parts = []
    for author in authors:
        bits = author.split()
        if len(bits) == 1:
            parts.append(bits[0])
        else:
            surname = bits[-1]
            initials = "".join(n[0].upper() for n in bits[:-1] if n)
            parts.append(f"{surname} {initials}")
    if et_al:
        return ", ".join(parts) + " et al."
    return ", ".join(parts)


REFERENCE_RECORDS = [
    (
        "1000 Genomes Project Consortium 2015",
        "1000 Genomes Project Consortium (2015) A global reference for human genetic variation. Nature 526:68-74. https://doi.org/10.1038/nature15393",
    ),
    (
        "Benjamini and Hochberg 1995",
        "Benjamini Y, Hochberg Y (1995) Controlling the false discovery rate: a practical and powerful approach to multiple testing. J R Stat Soc B 57:289-300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x",
    ),
    (
        "Bergström et al. 2020",
        "Bergström A, McCarthy SA, Hui R, Almarri MA, Ayub Q, Danecek P, et al (2020) Insights into human genetic variation and population history from 929 diverse genomes. Science 367:eaay5012. https://doi.org/10.1126/science.aay5012",
    ),
    (
        "Calafell et al. 2008",
        "Calafell F, Roubinet F, Ramírez-Soriano A, Saitou N, Bertranpetit J, Blancher A (2008) Evolutionary dynamics of the human ABO gene. Hum Genet 124:123-135. https://doi.org/10.1007/s00439-008-0530-8",
    ),
    (
        "Carroll et al. 2020",
        "Carroll SR, Garba I, Figueroa-Rodríguez OL, Holbrook J, Lovett R, Materechera S, et al (2020) The CARE principles for indigenous data governance. Data Sci J 19:43. https://doi.org/10.5334/dsj-2020-043",
    ),
    (
        "Claw et al. 2018",
        "Claw KG, Anderson MZ, Begay RL, Tsosie KS, Fox K, Garrison NA, et al (2018) A framework for enhancing ethical genomic research with Indigenous communities. Nat Commun 9:2957. https://doi.org/10.1038/s41467-018-05188-3",
    ),
    (
        "Condemi et al. 2021",
        "Condemi S, Mazières S, Faux P, Costedoat C, Ruiz-Linares A, Bailly P, et al (2021) Blood groups of Neandertals and Denisova decrypted. PLoS ONE 16:e0254175. https://doi.org/10.1371/journal.pone.0254175",
    ),
    (
        "Dekker, Krackhardt, and Snijders 2007",
        "Dekker D, Krackhardt D, Snijders TAB (2007) Sensitivity of MRQAP tests to collinearity and autocorrelation conditions. Psychometrika 72:563-581. https://doi.org/10.1007/s11336-007-9016-1",
    ),
    (
        "Green et al. 2010",
        "Green RE, Krause J, Briggs AW, Maricic T, Stenzel U, Kircher M, et al (2010) A draft sequence of the Neandertal genome. Science 328:710-722. https://doi.org/10.1126/science.1188021",
    ),
    (
        "Guillot and Rousset 2013",
        "Guillot G, Rousset F (2013) Dismantling the Mantel tests. Methods Ecol Evol 4:336-344. https://doi.org/10.1111/2041-210x.12018",
    ),
    (
        "Halverson and Bolnick 2008",
        "Halverson MS, Bolnick DA (2008) An ancient DNA test of a founder effect in Native American ABO blood group frequencies. Am J Phys Anthropol 137:342-347. https://doi.org/10.1002/ajpa.20887",
    ),
    (
        "Iasi et al. 2024",
        "Iasi LNM, Chintalapati M, Skov L, Bossoms Mesa A, Hajdinjak M, Peter BM, et al (2024) Neanderthal ancestry through time: insights from genomes of ancient and present-day humans. Science 386:eadq3010. https://doi.org/10.1126/science.adq3010",
    ),
    (
        "Jacobs et al. 2019",
        "Jacobs GS, Hudjashov G, Saag L, Kusuma P, Darusallam CC, Lawson DJ, et al (2019) Multiple deeply divergent Denisovan ancestries in Papuans. Cell 177:1010-1021.e32. https://doi.org/10.1016/j.cell.2019.02.035",
    ),
    (
        "Krackhardt 1988",
        "Krackhardt D (1988) Predicting with networks: nonparametric multiple regression analysis of dyadic data. Soc Networks 10:359-381. https://doi.org/10.1016/0378-8733(88)90004-4",
    ),
    (
        "Lawson et al. 2020",
        "Lawson DJ, Davies NM, Haworth S, Ashraf B, Howe L, Crawford A, Hemani G, Davey Smith G, Timpson NJ (2020) Is population structure in the genetic biobank era irrelevant, a challenge, or an opportunity? Hum Genet 139:23-41. https://doi.org/10.1007/s00439-019-02014-8",
    ),
    (
        "Legendre and Fortin 2010",
        "Legendre P, Fortin MJ (2010) Comparison of the Mantel test and alternative approaches for detecting complex multivariate relationships in the spatial analysis of genetic data. Mol Ecol Resour 10:831-844. https://doi.org/10.1111/j.1755-0998.2010.02866.x",
    ),
    (
        "Mantel 1967",
        "Mantel N (1967) The detection of disease clustering and a generalized regression approach. Cancer Res 27:209-220",
    ),
    (
        "Mazet et al. 2016",
        "Mazet O, Rodríguez W, Grusea S, Boitard S, Chikhi L (2016) On the importance of being structured: instantaneous coalescence rates and human evolution-lessons for ancestral population size inference? Heredity 116:362-371. https://doi.org/10.1038/hdy.2015.104",
    ),
    (
        "Ohashi et al. 2006",
        "Ohashi J, Naka I, Kimura R, Tokunaga K, Yamauchi T, Natsuhara K, et al (2006) Polymorphisms in the ABO blood group gene in three populations in the New Georgia Group of the Solomon Islands. J Hum Genet 51:407-411. https://doi.org/10.1007/s10038-006-0375-8",
    ),
    (
        "Ortega-Del Vecchyo and Slatkin 2019",
        "Ortega-Del Vecchyo D, Slatkin M (2019) FST between archaic and present-day samples. Heredity 122:711-718. https://doi.org/10.1038/s41437-018-0169-8",
    ),
    (
        "Petr et al. 2019",
        "Petr M, Pääbo S, Kelso J, Vernot B (2019) Limits of long-term selection against Neandertal introgression. Proc Natl Acad Sci USA 116:1639-1644. https://doi.org/10.1073/pnas.1814338116",
    ),
    (
        "Prüfer et al. 2017",
        "Prüfer K, de Filippo C, Grote S, Mafessoni F, Korlević P, Hajdinjak M, et al (2017) A high-coverage Neandertal genome from Vindija Cave in Croatia. Science 358:655-658. https://doi.org/10.1126/science.aao1887",
    ),
    (
        "Quilodran et al. 2023",
        "Quilodran CS, Rio J, Tsoupas A, Currat M (2023) Past human expansions shaped the spatial pattern of Neanderthal ancestry. Sci Adv 9:eadg9817. https://doi.org/10.1126/sciadv.adg9817",
    ),
    (
        "Reich et al. 2010",
        "Reich D, Green RE, Kircher M, Krause J, Patterson N, Durand EY, et al (2010) Genetic history of an archaic hominin group from Denisova Cave in Siberia. Nature 468:1053-1060. https://doi.org/10.1038/nature09710",
    ),
    (
        "Rousset 1997",
        "Rousset F (1997) Genetic differentiation and estimation of gene flow from F-statistics under isolation by distance. Genetics 145:1219-1228. https://doi.org/10.1093/genetics/145.4.1219",
    ),
    (
        "Sankararaman et al. 2014",
        "Sankararaman S, Mallick S, Dannemann M, Prüfer K, Kelso J, Pääbo S, et al (2014) The genomic landscape of Neanderthal ancestry in present-day humans. Nature 507:354-357. https://doi.org/10.1038/nature12961",
    ),
    (
        "Sankararaman et al. 2016",
        "Sankararaman S, Mallick S, Patterson N, Reich D (2016) The combined landscape of Denisovan and Neanderthal ancestry in present-day humans. Curr Biol 26:1241-1247. https://doi.org/10.1016/j.cub.2016.03.037",
    ),
    (
        "Segurel et al. 2012",
        "Segurel L, Thompson EE, Flutre T, Lovstad J, Venkat A, Margulis SW, et al (2012) The ABO blood group is a trans-species polymorphism in primates. Proc Natl Acad Sci USA 109:18493-18498. https://doi.org/10.1073/pnas.1210603109",
    ),
    (
        "Skov et al. 2018",
        "Skov L, Hui R, Shchur V, Hobolth A, Scally A, Schierup MH, et al (2018) Detecting archaic introgression using an unadmixed outgroup. PLoS Genet 14:e1007641. https://doi.org/10.1371/journal.pgen.1007641",
    ),
    (
        "Tournebize and Chikhi 2025",
        "Tournebize R, Chikhi L (2025) Ignoring population structure in hominin evolutionary models can lead to the inference of spurious admixture events. Nat Ecol Evol 9:225-236. https://doi.org/10.1038/s41559-024-02591-6",
    ),
    (
        "Wright 1943",
        "Wright S (1943) Isolation by distance. Genetics 28:114-138. https://doi.org/10.1093/genetics/28.2.114",
    ),
]

REFERENCE_KEYS = [record[0] for record in REFERENCE_RECORDS]
REFERENCES = [record[1] for record in REFERENCE_RECORDS]


INTRODUCTION = [
    (
        "Much of what we infer about population history is read off comparisons "
        "between pairs of populations. Genetic distance, allele-frequency "
        "similarity, haplotype sharing, and shared introgressed ancestry are all "
        "computed pair by pair, and the resulting matrix is then scanned for "
        "pairs that stand out. A pair that is more similar than its neighbours is "
        "a natural candidate for a specific explanation: recent migration between "
        "the two, a corridor of gene flow, a shared introgression event, or a "
        "common source population. This reasoning is applied across the whole "
        "discipline, from isolation-by-distance analyses of natural populations "
        "(Wright 1943; Rousset 1997) to comparisons of archaic ancestry among "
        "human groups (Sankararaman et al. 2014; Sankararaman et al. 2016)."
    ),
    (
        "The difficulty is that pairs built from a common set of units are not "
        "independent of one another. If populations A, B, and C are compared, the "
        "A-B and A-C measurements both contain A, so anything that makes A "
        "distinctive, such as its sample size, its demographic history, its "
        "position in a geographic gradient, or its share of recent admixture, "
        "moves both measurements together. In the data analysed here, "
        f"{POPULATIONS} populations generate {PAIRS:,} pairs, but those "
        f"{PAIRS:,} numbers are far from {PAIRS:,} independent observations. "
        "Population-wide forces, including geographic structure, serial founder "
        "effects, shared ancestry, and dataset provenance, act on whole rows and "
        "columns of the matrix at once. Procedures that shuffle rows, resample "
        "pairs, or bootstrap observations break this structure and can make an "
        "ordinary pair look exceptional."
    ),
    (
        "A more useful question is therefore not whether a pair is similar, but "
        "what similarity that pair should show given the relational structure of "
        "the full set of populations. We refer to the answer as the structural "
        "null, or the population-wide structural expectation. It can be "
        "approximated directly: hold the matrix of measurements intact and "
        "reassign the population labels, applying the same reassignment to rows "
        "and columns, so that each simulated dataset keeps the real pattern of "
        "repeated units while destroying the specific correspondence between a "
        "pair and its identity. Statistics recomputed across many such "
        "relabellings describe what the data would look like if nothing were "
        "special about any particular pair. This is the logic of matrix "
        "permutation introduced by the Mantel test (Mantel 1967) and extended to "
        "regression with several predictors by the quadratic assignment procedure "
        "(QAP; Krackhardt 1988; Dekker, Krackhardt, and Snijders 2007). The "
        "behaviour and limitations of these tests in spatial genetic settings are "
        "well described (Legendre and Fortin 2010; Guillot and Rousset 2013). We "
        "do not propose a new permutation method; we formulate and operationalise "
        "a structure-aware workflow that turns these tools into an explicit test "
        "of exceptional pairwise genomic similarity, with pair-level residuals "
        "and multiplicity control."
    ),
    (
        "The cost of ignoring structure is already documented on the model-based "
        "side of this literature. Inference of ancestral population size and of "
        "admixture from genomic data is sensitive to unmodelled population "
        "structure, so that structured histories without admixture can produce "
        "apparent size changes and apparent admixture events (Mazet et al. 2016; "
        "Tournebize and Chikhi 2025), and subtle population structure likewise "
        "biases association, prediction, and polygenic analyses at biobank scale "
        "(Lawson et al. 2020). The behaviour of divergence statistics "
        "computed between archaic and present-day samples depends on the "
        "demographic context in which they are read (Ortega-Del Vecchyo and "
        "Slatkin 2019). The problem addressed here is related but distinct. It "
        "arises in descriptive pairwise comparisons rather than in fitted "
        "demographic models, and its source is not only model misspecification "
        "but non-independence: the same populations reappear throughout the "
        "pairwise matrix, so a single population-wide property is expressed in "
        "many entries at once."
    ),
    (
        "Archaic ancestry in present-day humans is a convenient system in which to "
        "demonstrate the problem. Gene flow from Neanderthals "
        "and Denisovans left segments of archaic sequence in the ancestors of "
        "present-day populations outside Africa (Green et al. 2010; Reich et al. "
        "2010), and the amount and genomic placement of that sequence differ "
        "strongly among populations because of demographic history, drift, "
        "selection, and more than one introgression history (Sankararaman et al. "
        "2014; Sankararaman et al. 2016; Jacobs et al. 2019). Two properties make "
        "the system informative here: archaic ancestry is strongly geographically "
        "differentiated, so population-wide structure is large and easy to detect, "
        "and its demographic history is complex enough that pair-specific stories "
        "are readily available whenever a pair looks unusual. Focal loci sharpen "
        "the temptation further. The ABO blood-group gene is the clearest example: "
        "its polymorphism is ancient and medically visible, long shared haplotypes "
        "around it have been read as archaic contribution (Calafell et al. 2008), "
        "inferred archaic blood-group states have encouraged narratives of "
        "ABO-marked migration (Condemi et al. 2021), and other work has argued "
        "that founder effects (Halverson and Bolnick 2008) or trans-species "
        "balancing selection (Segurel et al. 2012) explain the same observations. "
        "We treat ABO as one worked example of a focal locus, not as the subject "
        "of the paper."
    ),
    (
        "We therefore ask three questions. First, how much of the variation in "
        "pairwise archaic-segment similarity is accounted for by broad, "
        "population-wide structure such as geographic separation? Second, does any "
        "individual pair show an excess of similarity that survives a "
        "dependence-preserving permutation null and correction for multiple "
        "testing? Third, does the prespecified ABO region exceed the same "
        "genome-wide structural expectation? Each answer is examined for "
        "robustness across window sizes, similarity measures, sample-size "
        "thresholds, source datasets, exclusion of recently admixed populations, "
        "and omission of whole regions. The inferential problem is generic, but "
        "its most immediate application is human population genetics: wherever "
        "human populations are compared pair by pair for unusual similarity in "
        "archaic ancestry or any genome-wide profile, the same non-independence "
        "applies and the same structural null is needed before a pair is called "
        "exceptional."
    ),
]


METHODS = [
    (
        "Analytical logic",
        [
            (
                "Before the technical detail, it is worth stating the shape of the "
                "analysis in plain terms (Figure 1). We first describe each "
                "population on its own, building a genomic profile without "
                "reference to any pair of interest, so that no focal comparison "
                "influences how the units are represented. We then compute the "
                "complete matrix of pairwise similarities rather than a selected "
                "subset, because the full matrix is what defines the expectation "
                "for any one pair. Next we characterise the broad structure in "
                "that matrix, here principally its association with geographic "
                "separation, and calibrate it against a null in which population "
                "labels are reassigned jointly to rows and columns. Each pair is "
                "then compared with the value its own structural background "
                "predicts, and the resulting pair-level evidence is corrected for "
                "the number of pairs examined. Finally, the ABO region is "
                "evaluated against the same genome-wide expectation rather than "
                "against a locus-specific standard."
            ),
        ],
    ),
    (
        "Data sources and population inclusion",
        [
            (
                "We analysed publicly archived segment calls generated with hmmix, "
                "a hidden Markov model-based method that detects candidate archaic "
                "sequence without requiring an unadmixed modern outgroup (Skov et al. "
                "2018). Segment files for the 1000 Genomes Project and HGDP samples were "
                "obtained from Zenodo record 14136628. Source population definitions "
                "followed those resources (1000 Genomes Project Consortium 2015; "
                "Bergström et al. 2020). Secure Hash Algorithm 256 (SHA-256) checksums "
                "of both raw files are written to the analysis provenance record."
            ),
            (
                "Segments with mean posterior probability below 0.8 were excluded. "
                "Populations with fewer than seven represented individuals were "
                f"excluded, leaving {INDIVIDUALS:,} individuals in {POPULATIONS} "
                "populations. Source calls annotated as Neanderthal or Both entered the "
                "Neanderthal profile; calls annotated as Denisova or Both entered the "
                "Denisovan profile."
            ),
        ],
    ),
    (
        "Population profiles and pairwise similarity",
        [
            (
                "Autosomes were partitioned into 500-kilobase (kb) windows. Within "
                "each ancestry category, overlapping or fragmented source segments were "
                "collapsed so that each individual-haplotype-window contributed at most "
                "one presence. For each population and window, unique haplotype "
                "presences were divided by twice the number of represented individuals. "
                "A runtime validity check required every frequency to lie between 0 and 1."
            ),
            (
                "For each population pair, Pearson correlation was calculated across the "
                "union of windows with a non-zero frequency in either population. Pairs "
                "required more than 100 union windows for Neanderthal and more than 50 "
                "for Denisovan profiles. The "
                f"{POPULATIONS}-population matrices contained {PAIRS:,} unique "
                "off-diagonal pairs. Correlations describe profile similarity and do not "
                "establish identity by descent. Spearman correlation and cosine similarity "
                "were calculated as metric sensitivities."
            ),
            (
                "Population coordinates were consolidated in a versioned metadata table "
                "from source sampling locations or population centroids. Great-circle "
                "distance was calculated with the Haversine formula. Coordinate "
                "uncertainty and co-located population labels were assessed by excluding "
                "zero-distance pairs."
            ),
        ],
    ),
    (
        "Dyadic regression and permutation inference",
        [
            (
                "The primary expanded descriptive model regressed pairwise similarity "
                "on great-circle distance per 1,000 km, an indicator for involvement of one "
                "of four designated recently admixed American populations (Puerto Ricans "
                "from Puerto Rico, PUR; Colombians from Medellín, Colombia, CLM; people "
                "with Mexican ancestry from Los Angeles, United States, MXL; and "
                "Peruvians from Lima, Peru, PEL), same-continent status, and same-dataset "
                "status. These indicators are coarse sensitivity covariates, not individual "
                "ancestry estimates or causal controls. Distance-only models were also fit."
            ),
            (
                f"Coefficient P values used {PRIMARY_PERMUTATIONS:,} QAP permutations. "
                "At each iteration, the response matrix was permuted by the same random "
                "population-label order on rows and columns, after which the model was "
                "refit. Two-sided P values were the proportion of permuted coefficient "
                "magnitudes at least as large as the observed magnitude, including a "
                "plus-one correction. Descriptive R-squared values quantify fit to the "
                "observed pair matrix and are not interpreted as independent "
                "observations or causal variance explained."
            ),
            (
                "Mantel tests and QAP both use matrix permutation to respect dyadic "
                "dependence, but they answer different questions. A Mantel test "
                "evaluates one correlation between two distance matrices (Mantel 1967); "
                "it does not estimate regression coefficients for several predictors, "
                "does not generate a residual for each pair, and does not support FDR "
                "control across pairs; these differences, and the sensitivity of "
                "matrix permutation tests to spatial autocorrelation, are well "
                "documented (Legendre and Fortin 2010; Guillot and Rousset 2013). "
                "Our QAP implementation permutes the response "
                "matrix, refits the multiple regression, and records the coefficient and "
                "each pair's residual at every iteration. The same population-label "
                "permutation therefore provides a dependence-aware null for the distance "
                "coefficient, a pair-level residual null distribution, and a joint basis "
                "for Benjamini-Hochberg FDR control."
            ),
            (
                "Population-deletion stability intervals were calculated by refitting "
                "the expanded model after removing every pair containing one population "
                "in turn and reporting the 2.5th and 97.5th percentiles of the resulting "
                "coefficients. These are sensitivity intervals rather than "
                "independent-sample confidence intervals."
            ),
        ],
    ),
    (
        "Residual outliers and multiple testing",
        [
            (
                "Outlier analysis was restricted to the complete matrix after removing "
                "PUR, CLM, MXL, and PEL. Similarity was modelled using distance, "
                "same-continent status, and same-dataset status. Positive residuals were "
                "standardised by the residual standard deviation. For every pair, a "
                "one-sided nominal P value was calculated from its own residual null "
                f"distribution across {PRIMARY_PERMUTATIONS:,} population-label "
                "permutations. Because pair residuals are dyadically dependent, this null "
                "was generated by the same joint row-and-column population-label "
                "permutation used for the coefficient tests rather than by row-wise "
                "resampling, following the rationale for multiple-regression QAP with "
                "dependent dyads (Dekker, Krackhardt, and Snijders 2007). The "
                "Benjamini-Hochberg procedure was applied jointly to all non-admixed "
                "pairs within each ancestry analysis to control the FDR (Benjamini and "
                "Hochberg 1995). A supported positive outlier required z>2 and q<0.10. "
                "Because no pair met this threshold, the qualitative absence of FDR-supported "
                "outliers is robust to the exact dependence structure among pair-level "
                "P values; stricter dependence-aware procedures would only strengthen the "
                "absence of findings."
            ),
        ],
    ),
    (
        "Robustness analyses",
        [
            (
                "We repeated distance-only population-label tests for 250-kb, 500-kb, "
                "and 1-megabase (Mb) windows. At 500 kb, robustness summaries compared "
                "Pearson, Spearman, and cosine similarity; minimum population sizes of "
                "7, 10, 15, and 20; the complete dataset, non-admixed populations, 1000 "
                "Genomes-only and HGDP-only subsets; exclusion of zero-distance pairs; "
                "and leave-one-continent-out subsets. Full-window Pearson correlation "
                "and presence-absence Jaccard similarity assessed sensitivity to the "
                "non-zero-window union. Sensitivity tests used "
                f"{SENSITIVITY_PERMUTATIONS:,} population-label permutations. No "
                "genome-wide callable mask was available in the source release, so "
                "mask-adjusted profiles could not be evaluated."
            ),
        ],
    ),
    (
        "Secondary ABO-centered analysis",
        [
            (
                "The ABO gene was defined on Genome Reference Consortium Human Build 38 "
                "(GRCh38) as chromosome 9 (chr9):133,233,278-133,276,024. We "
                "distinguished strict gene overlap from any overlap with a 500-kb "
                "interval spanning chr9:133.0-133.5 Mb. Population carrier frequencies "
                "used unique individuals in the numerator and all represented source "
                "individuals in the denominator."
            ),
            (
                "For Neanderthal or Both segments in the interval, similarity counts to "
                "Altai, Vindija, and Chagyrskaya were compared; tied maxima remained "
                "ties. The Vindija reference is a high-coverage Neanderthal genome "
                "(Prüfer et al. 2017). The O2 blood-group subtype-defining rs41302905 T "
                "allele was summarised from Ensembl/1000 Genomes frequencies and "
                "published Solomon Islands frequencies (Ohashi et al. 2006). Ancient-window "
                "observations were extracted by a documented, reproducible script from the "
                "public Neanderthal-segment catalogue of Iasi et al. (2024), using the "
                "GRCh37 ABO interval that corresponds to the GRCh38 window analysed here; "
                "ancient and modern calls used different pipelines and were not directly "
                "compared statistically."
            ),
            (
                "To ask whether the ABO region behaves differently from the rest of "
                "the genome, the window was evaluated against the genome-wide "
                "structural background rather than against a locus-specific "
                "standard. Within every 500-kb window, the absolute difference in "
                "population frequency between the two members of each non-admixed "
                "pair was regressed on geographic distance. Excess similarity was "
                "defined as the predicted difference minus the observed "
                "difference, so that positive values indicate population pairs "
                "that are more similar than expected from geographic distance, "
                "and these values were standardised by their within-window "
                "standard deviation. The largest standardised excess in a window "
                "summarises the strongest excess-similarity "
                "signal that window can offer. Collecting these per-window maxima "
                "across all windows with archaic calls in at least ten populations "
                "gives the genome-wide background distribution, and the position of "
                "the ABO window within it is reported as a percentile and an "
                "empirical P value. This comparison is descriptive of the observed "
                "matrix and is not a substitute for the pair-level permutation test."
            ),
        ],
    ),
    (
        "Ethical review, community engagement, and interpretation",
        [
            (
                "This computational secondary analysis used de-identified public data "
                "and involved no recruitment, contact, biospecimen collection, or new "
                "individual-level phenotype inference. The author did not obtain a "
                "separate institutional review determination for this secondary "
                "analysis; approvals, consent, and data-access procedures were those "
                "reported by the source studies. This limitation is disclosed rather "
                "than treating public availability as equivalent to unrestricted "
                "ethical reuse."
            ),
            (
                "No source community or stakeholder representatives participated in the "
                "design, analysis, interpretation, or dissemination of the present "
                "secondary study, and no direct community return-of-results process was "
                "conducted. Because the dataset includes Indigenous participants and the "
                "topic can affect narratives of ancestry and migration, analyses were "
                "interpreted in light of Indigenous data-governance guidance and the "
                "Collective Benefit, Authority to Control, Responsibility, and Ethics "
                "(CARE) Principles (Claw et al. 2018; Carroll et al. 2020). Population "
                "labels were retained only when needed for transparent source-data "
                "description; locus-level observations were not generalised to "
                "communities, and migration routes were not assigned from these data. "
                "The public article, code, and derived aggregate results are the current "
                "means of results availability. These disclosures are made in the "
                "interest of transparent ethical reporting for secondary genomic analyses."
            ),
        ],
    ),
]


RESULTS = [
    (
        "Archaic-segment similarity shows broad population structure",
        (
            f"After quality filtering, the analysis retained {POPULATIONS} "
            f"populations, {INDIVIDUALS:,} individuals, and all {PAIRS:,} unique "
            "population pairs. Collapsing fragmented segments at the "
            "individual-haplotype-window level ensured that no population-window "
            "frequency exceeded 1 in either ancestry category. Profile similarity "
            "declined steadily with geographic separation for both ancestries "
            f"(raw r={value(NEANDERTHAL, 'raw_r')} for Neanderthal and "
            f"{value(DENISOVAN, 'raw_r')} for Denisovan profiles; Figure 2), and the "
            "decline persisted after the coarse continent, dataset, and "
            "recent-admixture indicators were added, with partial distance "
            f"correlations of {value(NEANDERTHAL, 'partial_r')} and "
            f"{value(DENISOVAN, 'partial_r')}. Distance alone accounted for "
            f"R-squared values of {value(NEANDERTHAL, 'distance_only_r_squared')} "
            f"and {value(DENISOVAN, 'distance_only_r_squared')} in the observed "
            f"matrix, rising to {value(NEANDERTHAL, 'expanded_r_squared')} and "
            f"{value(DENISOVAN, 'expanded_r_squared')} in the expanded descriptive "
            f"models. Under {PRIMARY_PERMUTATIONS:,} joint population-label "
            "permutations, which preserve the recurrence of each population across "
            "pairs, the distance coefficients per 1,000 km were "
            f"{value(NEANDERTHAL, 'distance_qap_beta', 5)} "
            f"(P={value(NEANDERTHAL, 'distance_qap_p', 4)}) and "
            f"{value(DENISOVAN, 'distance_qap_beta', 5)} "
            f"(P={value(DENISOVAN, 'distance_qap_p', 4)}). The similarity matrices "
            "themselves are organised into broad regional blocks, with a stronger "
            "Oceanian contrast in the Denisovan profile (Figure 3); the complete "
            f"{POPULATIONS}-population matrices are given as Figure S1. "
            "Population-wide structure is thus a large and highly reproducible "
            "feature of these data, and it is this structure that sets the "
            "expectation for any individual pair."
        ),
        ["Figure 2", "Figure 3"],
    ),
    (
        "No population pair exceeds the structural expectation after multiplicity "
        "control",
        (
            "Each pair was next compared with the similarity predicted for it by "
            "the population-wide model, and its standardised positive residual was "
            "referred to a null distribution generated by the same joint "
            f"population-label permutation. Among the {RESIDUALS['pairs']:,} pairs "
            f"formed by the {RESIDUALS['populations']} populations remaining after "
            "the four designated recently admixed American populations were set "
            "aside, the largest positive residuals reached "
            f"z={RESIDUALS['nean_max_z']:.2f} for Neanderthal and "
            f"z={RESIDUALS['deni_max_z']:.2f} for Denisovan profiles, but the "
            "smallest Benjamini-Hochberg q values were "
            f"{RESIDUALS['nean_min_q']:.2f} and {RESIDUALS['deni_min_q']:.2f} "
            "respectively. No pair met the prespecified joint criterion of a "
            "positive residual above two standard deviations and q<0.10 for either "
            "ancestry (Figure 4; Table 1). Nominal residual ranks are retained in "
            "the full pairwise data table for auditability. This is a statement "
            "about excess similarity relative to the structural expectation, not "
            "about the existence of shared history: the pairs simply fall where "
            "population-wide structure places them."
        ),
        ["Figure 4", "Table 1"],
    ),
    (
        "Population-wide structure is robust to analytical choices",
        (
            "The distance association was reproduced under every variation we "
            "examined (Figure 5). It held at 250-kb, 500-kb, and 1-Mb window sizes; "
            "under Spearman, cosine, full-window Pearson, and presence-absence "
            "Jaccard similarity in place of Pearson correlation of the non-zero "
            "union; at minimum population sizes of 7, 10, 15, and 20; within the "
            "1000 Genomes and HGDP subsets analysed separately; after excluding "
            "co-located population pairs; after excluding the designated recently "
            "admixed populations; and after omitting each geographic region in turn. "
            "Excluding recently admixed populations or omitting the Americas "
            "strengthened rather than weakened the association, as expected if "
            "recent mixture blurs an underlying geographic gradient. Detailed "
            "per-subset grids, including the coefficients and permutation P values "
            f"from {SENSITIVITY_PERMUTATIONS:,} permutations, are tabulated in "
            "Supplementary Data, and the effect of excluding recently admixed "
            "populations is shown separately as Figure S2 and the effect of "
            "changing window size as Figure S3. These analyses are robustness "
            "checks on one structural "
            "pattern rather than independent confirmatory tests."
        ),
        ["Figure 5"],
    ),
    (
        "ABO does not exceed the genome-wide structural background",
        (
            "As a worked example of a focal locus, the prespecified 500-kb interval "
            f"centred on ABO contained {ABO['interval_segments']:,} Neanderthal or "
            f"Both source segments, of which {ABO['strict_overlap']} overlapped the "
            f"ABO gene itself and {ABO['ties']} were tied for maximum reference "
            "similarity. In the Indigenous American HGDP subset, only two segments "
            f"among {ABO['indigenous_individuals']} represented individuals fell in "
            "the interval. Judged against the genome-wide background, the ABO "
            "window is unremarkable: its strongest excess-similarity signal across "
            f"the {ABO_FOCAL['pairs']:,} non-admixed pairs reached "
            f"z={ABO_FOCAL['nean_abo_max_excess_z']:.2f} for Neanderthal profiles, "
            f"the {ABO_FOCAL['nean_abo_percentile']:.0f}th percentile of the "
            f"{ABO_FOCAL['nean_usable_windows']:,} comparable windows (empirical "
            f"P={ABO_FOCAL['nean_abo_empirical_p']:.2f}), and "
            f"z={ABO_FOCAL['deni_abo_max_excess_z']:.2f} for Denisovan profiles, "
            f"the {ABO_FOCAL['deni_abo_percentile']:.0f}th percentile of "
            f"{ABO_FOCAL['deni_usable_windows']:,} windows (empirical "
            f"P={ABO_FOCAL['deni_abo_empirical_p']:.2f}). The ABO region therefore "
            "provides no evidence of an exceptional connection between any pair of "
            "populations. "
            "Segment-level compositions (Figure S4; Table S1), carrier and "
            "O2-allele summaries drawn from different sources (Figure S5), and "
            "ancient and modern window observations produced by different pipelines "
            "(Figure S6) are presented as Supplementary material and are not "
            "interpreted as regional proportions, association tests, formal temporal "
            "comparisons, or migration routes. A bivariate global map of mean "
            "Neanderthal and Denisovan segment coverage per population is provided "
            "for geographic context only (Figure S7)."
        ),
        [],
    ),
]


DISCUSSION = [
    (
        "Across a complete matrix of population comparisons, archaic-segment "
        "similarity is dominated by broad population structure, and once that "
        "structure is used to define the expectation for each pair, no pair stands "
        "out. The largest positive residuals are unremarkable once the number of "
        "pairs examined is taken into account, and the prespecified ABO region "
        "behaves like the rest of the genome. The finding that matters is not the "
        "absence of outliers in these particular data but the demonstration that "
        "the expectation against which outliers are judged can be constructed, and "
        "that it is substantially different from the implicit expectation used "
        "when pairs are inspected one at a time."
    ),
    (
        "That population structure can distort evolutionary inference is not a "
        "new observation. Unmodelled structure can generate spurious signals of "
        "population-size change and of admixture in model-based analyses of "
        "hominin history (Mazet et al. 2016; Tournebize and Chikhi 2025), and "
        "subtle structure also biases association and prediction analyses of "
        "present-day human genomes (Lawson et al. 2020). Statistics computed "
        "between archaic and present-day samples are "
        "interpretable only within an assumed demographic context "
        "(Ortega-Del Vecchyo and Slatkin 2019). The contribution here lies "
        "elsewhere: it provides a way to evaluate pair-specific claims about "
        "genomic similarity against the relational structure of the full set of "
        "populations, under the dependence created by populations that recur "
        "across the pairwise matrix. Joint label permutation and matrix "
        "regression are long-established tools, and the structural insight about "
        "population structure is not ours; what is supplied is an explicit "
        "workflow in which pair-level residuals and multiplicity control make "
        "pairwise similarity claims testable."
    ),
    (
        "The reason is the relational structure of the measurement itself. A "
        f"matrix of {PAIRS:,} pairwise values built from {POPULATIONS} populations "
        f"does not contain {PAIRS:,} independent comparisons, because every "
        "population contributes to many entries and any property of that "
        "population propagates through an entire row and column. Permuting "
        "population labels jointly on rows and columns holds this dependence fixed "
        "while breaking the link between a pair and its identity, which is why the "
        "resulting null is the appropriate reference for both the population-wide "
        "coefficients and the pair-level residuals (Krackhardt 1988; Dekker, "
        "Krackhardt, and Snijders 2007). The descriptive R-squared values and the "
        "coarse continent, dataset, and recent-admixture indicators should be read "
        "as a description of the observed matrix rather than as causal adjustment, "
        "and the same caution that applies to matrix correlation tests in spatial "
        "genetics applies here (Legendre and Fortin 2010; Guillot and Rousset "
        "2013)."
    ),
    (
        "Biologically, the distance decay is consistent with serial demographic "
        "structure and with the spatial patterning of introgressed sequence "
        "reported previously (Sankararaman et al. 2014; Sankararaman et al. 2016; "
        "Quilodran et al. 2023), and it does not identify the timing, direction, or "
        "number of introgression events. The negative pair-level result requires "
        "an equally careful reading. Finding no pair with excess similarity is "
        "evidence that these data do not support pair-specific explanations beyond "
        "population-wide structure; it is not evidence that the populations in any "
        "pair lack a shared history. Two populations connected by real historical "
        "contact will often be exactly as similar as broad structure predicts, "
        "because that contact is part of what produced the structure. For the "
        "interpretation of human population history, this means that a visibly "
        "similar pair, in archaic-segment profiles or in any other genome-wide "
        "measure, is weak evidence for a special connection until it has been "
        "compared with the expectation set by the population set as a whole. "
        "Population coordinates are approximate, and profile similarity can also "
        "reflect callability, allele-frequency differences, linkage, selection, "
        "and reference-panel composition."
    ),
    (
        "ABO illustrates how a focal locus behaves under this framework. Its "
        "polymorphism is ancient and has been interpreted as a trans-species "
        "polymorphism maintained by balancing selection (Segurel et al. 2012), "
        "selection can alter the persistence of introgressed sequence near it "
        "(Petr et al. 2019), and compatible long haplotypes and inferred archaic "
        "blood-group states have been read as evidence of a specific connection "
        "(Calafell et al. 2008; Condemi et al. 2021), while other work attributes "
        "the same frequency patterns to founder effects (Halverson and Bolnick "
        "2008). Evaluated against the genome-wide structural expectation, the ABO "
        "window is not exceptional. This removes one class of explanation rather "
        "than settling the question: an inferred segment in a 500-kb interval is "
        "not an ABO allele, closest-reference similarity is not a transmission "
        "path, and proximity does not make the O2-defining variant "
        "Neanderthal-derived. What remains are alternatives that the present design "
        "cannot adjudicate, including balancing selection on an ancient "
        "polymorphism (Segurel et al. 2012), recurrent low-level gene flow from "
        "more than one archaic source (Jacobs et al. 2019), drift through "
        "bottlenecks (Halverson and Bolnick 2008), and technical effects of "
        "reference-panel composition and callable-mask variation (Sankararaman et "
        "al. 2014). Distinguishing them will require phased local genealogies, "
        "method-matched ancient genomes such as those catalogued by Iasi et al. "
        "(2024), and decomposition of identity by state from identity by descent; "
        "we state these as directions, not as results."
    ),
    (
        "Nothing in the workflow is specific to archaic ancestry, and the "
        "inferential logic may extend to any setting where a fixed set of "
        "populations, strains, or other repeated units is compared pair by pair: "
        "the same three ingredients, a complete comparison matrix, a "
        "label-permutation null that preserves unit recurrence, and explicit "
        "multiplicity control across pairs, answer the same question of what "
        "similarity a pair should show given the relational structure of the "
        "whole set. Several limitations of the present application qualify the "
        "interpretation for human population genetics. Several "
        "populations analysed here are modest in size, Denisovan calls are sparse "
        "outside Oceania, distances are centroid-based, no common callable mask was "
        "available, and correlation does not separate identity by descent from "
        "identity by state; the dataset combines two projects, and a same-dataset "
        "indicator captures technical heterogeneity only partially. The pair-level "
        "test is also deliberately conservative: a threshold of two standard "
        "deviations combined with false-discovery-rate control across close to two "
        "thousand pairs will detect only a substantial excess, so a real but modest "
        "pair-specific effect would not be recovered here, and the largest observed "
        "residuals are better read as an upper bound on such effects than as their "
        "refutation. More generally, "
        "a structural null is only as good as the structure it encodes, so in "
        "systems where the dominant structure is not geographic it must be modelled "
        "accordingly, and the absence of supported outliers in one system should "
        "not be generalised to others."
    ),
    (
        "In conclusion, pairwise archaic-segment similarity across "
        f"{POPULATIONS} human populations is structured at the level of the whole "
        "population set rather than at the level of individual pairs. Neither any "
        "focal pair nor the prespecified ABO comparison exceeded the structural "
        "expectation defined by that set. Claims that a particular pair or a "
        "particular locus is exceptional should therefore be evaluated against a "
        "null that preserves the relational structure of the data before they are "
        "explained by pair-specific history."
    ),
]

FIGURES = {
    1: (
        "figH1_structural_null_concept.png",
        "Why pairwise comparisons need a structural null. (a) Four sampling units. "
        "(b) Every unit recurs across many pairs, so pairwise measurements are not "
        "independent. (c) Reading one pair on its own invites a pair-specific "
        "explanation. (d) The same pair read against the expectation generated by "
        "the whole set of units. (e) The inferential workflow used here: population "
        "profiles, complete pairwise similarity matrix, population-wide structural "
        "model, population-label permutation (QAP), residual pair test, and "
        "multiplicity control. Panels a-d are schematic illustrations and do not "
        "display analysis results.",
    ),
    2: (
        "fig1_sharing_vs_distance.png",
        "Archaic-segment profile similarity against geographic distance. Each point "
        "is one population pair; pairs sharing a population are not independent. "
        "Lines are descriptive distance-only fits, and reported P values come from "
        "population-label QAP permutations.",
    ),
    3: (
        "fig2_sharing_heatmap.png",
        "Population-wide similarity structure. Pairwise archaic-segment profile "
        "similarity for 31 populations selected for visual legibility and ordered by "
        "geographic region; all 66 populations were analysed (Figure S1).",
    ),
    4: (
        "figH4_residual_evidence.png",
        "Pair-specific evidence against the structural expectation. For each "
        "non-admixed population pair, the standardised positive residual from the "
        "population-wide model is plotted against its Benjamini-Hochberg q value. "
        "The shaded region marks the prespecified support criterion (z>2 and "
        "q<0.10), which contains no pair for either ancestry.",
    ),
    5: (
        "figH5_robustness_summary.png",
        "Robustness of the population-wide distance association. (a) Population "
        "subsets, including dataset restrictions, minimum sample sizes, exclusion of "
        "recently admixed populations and co-located pairs, and omission of each "
        "region in turn. (b) Alternative similarity measures. (c) 250-kb, 500-kb, "
        "and 1-Mb window sizes. All panels summarise analyses reported in "
        "Supplementary Data; no additional hypothesis test is introduced.",
    ),
}


SUPPORTING_FIGURES = {
    1: (
        "figS1_full_heatmap.png",
        "Complete 66-population Neanderthal and Denisovan profile-similarity matrices.",
    ),
    2: (
        "fig4_sensitivity_admixed.png",
        "Sensitivity of the descriptive Neanderthal distance correlation to exclusion "
        "of designated recently admixed populations.",
    ),
    3: (
        "fig5_window_sensitivity.png",
        "Descriptive geographic distance correlations at 250-kb, 500-kb, and 1-Mb "
        "window sizes. QAP results are tabulated in Supplementary Data.",
    ),
    4: (
        "fig5_abo_sublineage.png",
        "Exploratory ABO-centered analysis preserving the historical grouped-bar and "
        "segment-map layout. Equal maximum-similarity ties are excluded from the "
        "displayed three-reference proportions and retained in Supplementary Data. The "
        "Pima segment overlaps ABO; the Maya segment is within the wider interval but "
        "does not overlap the gene. Counts are segments, not regional frequencies, and "
        "are not interpreted as a migration route.",
    ),
    5: (
        "fig6_o2_introgression.png",
        "O2 blood-group subtype-defining allele frequencies and ABO-window "
        "segment-carrier frequencies. The panels use different sources and are not an "
        "association analysis; proximity does not establish that the O2 allele is "
        "Neanderthal-derived.",
    ),
    6: (
        "fig8_temporal_dynamics.png",
        "Descriptive ancient and modern ABO-window summaries generated by different "
        "pipelines; no formal temporal comparison is made.",
    ),
    7: (
        "fig9_bivariate_world_map.png",
        "Bivariate global context computed in this study. Circle area encodes the mean "
        "per-bin Neanderthal-segment coverage and colour encodes the mean per-bin "
        "Denisovan-segment coverage for each population, both from "
        "data/population_profiles_500kb.npz; coordinates are approximate sampling "
        "locations from data/population_metadata.csv. These descriptive summaries were "
        "not used in the pairwise statistical models.",
    ),
}
