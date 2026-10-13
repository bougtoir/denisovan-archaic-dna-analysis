"""Create the conceptual, residual-evidence, and robustness figures.

All panels are drawn from the committed analysis outputs; no new hypothesis
test is performed here.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ANCESTRIES = [
    ("Neanderthal", "nean_resid_z", "nean_fdr_pval", "#2c5f8a"),
    ("Denisovan", "deni_resid_z", "deni_fdr_pval", "#a0522d"),
]
Z_THRESHOLD = 2.0
Q_THRESHOLD = 0.10


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--figure-dir", type=Path, default=Path("figures"))
    return parser.parse_args()


def save_figure(figure: plt.Figure, directory: Path, stem: str) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    figure.savefig(directory / f"{stem}.png", dpi=300, bbox_inches="tight")
    figure.savefig(
        directory / f"{stem}.tiff",
        dpi=300,
        bbox_inches="tight",
        pil_kwargs={"compression": "tiff_lzw"},
    )
    plt.close(figure)


def _blank(axis: plt.Axes) -> None:
    axis.set_xlim(0, 1)
    axis.set_ylim(0, 1)
    axis.axis("off")


def _footnote(axis: plt.Axes, text: str, offset: float = -0.16) -> None:
    axis.text(
        0.5,
        offset,
        text,
        transform=axis.transAxes,
        ha="center",
        va="top",
        fontsize=9.5,
        style="italic",
    )


def _unit(axis: plt.Axes, x: float, y: float, name: str, colour: str) -> None:
    axis.add_patch(
        mpatches.Circle((x, y), 0.075, facecolor=colour, edgecolor="#333333", lw=1.2)
    )
    axis.text(x, y, name, ha="center", va="center", fontsize=11, fontweight="bold")


def concept_figure(figure_directory: Path) -> None:
    figure = plt.figure(figsize=(13.5, 9.8))
    grid = figure.add_gridspec(
        3, 2, height_ratios=[1.0, 1.0, 0.55], hspace=0.62, wspace=0.2
    )
    colours = {
        "A": "#c7dbef",
        "B": "#f6d6c2",
        "C": "#d8ead3",
        "D": "#e6ddf2",
    }

    axis = figure.add_subplot(grid[0, 0])
    _blank(axis)
    axis.set_aspect("equal")
    axis.set_title("a  Sampling units", fontsize=12.5, loc="left", fontweight="bold")
    positions = {"A": (0.22, 0.68), "B": (0.62, 0.78), "C": (0.34, 0.26), "D": (0.78, 0.32)}
    for name, (x, y) in positions.items():
        _unit(axis, x, y, name, colours[name])
    _footnote(axis, "populations, demes, breeds, strains or sampling locations")

    axis = figure.add_subplot(grid[0, 1])
    _blank(axis)
    axis.set_aspect("equal")
    axis.set_title(
        "b  Every unit recurs across many pairs",
        fontsize=12.5,
        loc="left",
        fontweight="bold",
    )
    for name, (x, y) in positions.items():
        _unit(axis, x, y, name, colours[name])
    for first, second, style in [
        ("A", "B", "-"),
        ("A", "C", "-"),
        ("A", "D", "-"),
        ("B", "C", (0, (4, 3))),
        ("B", "D", (0, (4, 3))),
        ("C", "D", (0, (4, 3))),
    ]:
        x1, y1 = positions[first]
        x2, y2 = positions[second]
        axis.plot(
            [x1, x2],
            [y1, y2],
            linestyle=style,
            color="#8a8a8a" if style != "-" else "#2c5f8a",
            lw=1.6 if style == "-" else 1.1,
            zorder=0,
        )
    _footnote(
        axis,
        "the three blue comparisons all contain unit A, so pairs are not "
        "independent observations",
    )

    axis = figure.add_subplot(grid[1, 0])
    axis.set_title(
        "c  Reading one pair on its own",
        fontsize=12.5,
        loc="left",
        fontweight="bold",
    )
    rng = np.random.default_rng(42)
    background = rng.normal(0.42, 0.075, 60)
    axis.hist(background, bins=16, color="#d9d9d9", edgecolor="#9e9e9e")
    axis.axvline(0.62, color="#b2182b", lw=2)
    axis.annotate(
        "pair A-B",
        xy=(0.62, 3.0),
        xytext=(0.66, 5.6),
        fontsize=10,
        color="#b2182b",
        arrowprops={"arrowstyle": "->", "color": "#b2182b"},
    )
    axis.set_xlabel("pairwise genomic similarity", fontsize=10)
    axis.set_ylabel("number of pairs", fontsize=10)
    axis.set_xlim(0.18, 0.8)
    _footnote(
        axis,
        "an extreme pair invites a pair-specific historical explanation",
        offset=-0.30,
    )

    axis = figure.add_subplot(grid[1, 1])
    axis.set_title(
        "d  Reading the same pair against structure",
        fontsize=12.5,
        loc="left",
        fontweight="bold",
    )
    distance = rng.uniform(0.3, 9.7, 70)
    similarity = 0.66 - 0.032 * distance + rng.normal(0, 0.035, 70)
    axis.scatter(distance, similarity, s=22, color="#bdbdbd", edgecolor="none")
    fit = np.polyfit(distance, similarity, 1)
    grid_x = np.linspace(0.2, 9.8, 50)
    axis.plot(grid_x, np.polyval(fit, grid_x), color="#2c5f8a", lw=2)
    axis.scatter([1.9], [0.62], s=90, color="#b2182b", zorder=5)
    axis.annotate(
        "pair A-B",
        xy=(1.9, 0.62),
        xytext=(3.1, 0.665),
        fontsize=10,
        color="#b2182b",
        arrowprops={"arrowstyle": "->", "color": "#b2182b"},
    )
    axis.set_xlabel("structural predictor (e.g. geographic distance)", fontsize=10)
    axis.set_ylabel("pairwise genomic similarity", fontsize=10)
    _footnote(
        axis,
        "once population-wide structure is modelled, the pair is close to its "
        "expected value",
        offset=-0.30,
    )

    axis = figure.add_subplot(grid[2, :])
    _blank(axis)
    axis.set_title(
        "e  Inferential workflow", fontsize=12.5, loc="left", fontweight="bold"
    )
    steps = [
        "unit profiles",
        "pairwise\nsimilarity matrix",
        "population-wide\nstructural model",
        "label permutation\n(QAP)",
        "pair residual\ntest",
        "multiplicity\ncontrol (FDR)",
    ]
    width = 0.145
    gap = (1 - len(steps) * width) / (len(steps) - 1)
    for index, step in enumerate(steps):
        left = index * (width + gap)
        axis.add_patch(
            mpatches.FancyBboxPatch(
                (left, 0.26),
                width,
                0.42,
                boxstyle="round,pad=0.012",
                facecolor="#eef3f8" if index < 3 else "#f3eef8",
                edgecolor="#4b6c8c",
                lw=1.2,
            )
        )
        axis.text(
            left + width / 2,
            0.47,
            step,
            ha="center",
            va="center",
            fontsize=9.6,
        )
        if index < len(steps) - 1:
            axis.annotate(
                "",
                xy=(left + width + gap * 0.92, 0.47),
                xytext=(left + width + gap * 0.08, 0.47),
                arrowprops={"arrowstyle": "-|>", "color": "#4b6c8c", "lw": 1.4},
            )
    save_figure(figure, figure_directory, "figH1_structural_null_concept")


def residual_figure(data_directory: Path, figure_directory: Path) -> None:
    pairs = pd.read_csv(data_directory / "pairwise_sharing_corrected.csv")
    pairs = pairs[pairs["any_admixed"] == 0]
    figure, axes = plt.subplots(1, 2, figsize=(13.4, 5.8))
    for axis, (label, z_column, q_column, colour) in zip(axes, ANCESTRIES):
        frame = pairs.dropna(subset=[z_column, q_column])
        axis.add_patch(
            mpatches.Rectangle(
                (Z_THRESHOLD, 0),
                10,
                Q_THRESHOLD,
                facecolor="#f7d5d5",
                edgecolor="#b2182b",
                lw=1.2,
                zorder=0,
            )
        )
        axis.scatter(
            frame[z_column],
            frame[q_column],
            s=14,
            color=colour,
            alpha=0.45,
            edgecolor="none",
            zorder=2,
        )
        axis.axvline(Z_THRESHOLD, color="#b2182b", lw=1.2, ls="--")
        axis.axhline(Q_THRESHOLD, color="#b2182b", lw=1.2, ls="--")
        axis.set_xlim(frame[z_column].min() - 0.3, max(frame[z_column].max() + 0.6, 3.2))
        axis.set_ylim(-0.03, 1.05)
        axis.set_xlabel("standardised positive residual (z)", fontsize=11)
        axis.set_ylabel("Benjamini-Hochberg q", fontsize=11)
        axis.set_title(
            f"{label} profiles ({len(frame):,} pairs)", fontsize=12, loc="left"
        )
        axis.text(
            0.985,
            0.06,
            "prespecified support region\n(z > 2 and q < 0.10): empty",
            transform=axis.transAxes,
            ha="right",
            va="bottom",
            fontsize=9.5,
            color="#b2182b",
        )
        highest = frame.loc[frame[z_column].idxmax()]
        axis.annotate(
            f"largest residual: z = {highest[z_column]:.2f}, q = {highest[q_column]:.2f}",
            xy=(highest[z_column], highest[q_column]),
            xytext=(0.38, 0.86),
            textcoords="axes fraction",
            fontsize=9.5,
            arrowprops={"arrowstyle": "->", "color": "#555555"},
        )
    figure.tight_layout()
    save_figure(figure, figure_directory, "figH4_residual_evidence")


ROBUSTNESS_LABELS = {
    "all": "All populations",
    "nonadmixed": "Recently admixed excluded",
    "zero_distance_excluded": "Co-located pairs excluded",
    "1000_genomes_only": "1000 Genomes only",
    "hgdp_only": "HGDP only",
    "minimum_n_10": "Minimum n = 10",
    "minimum_n_15": "Minimum n = 15",
    "minimum_n_20": "Minimum n = 20",
    "leave_out_AMR": "Americas omitted",
    "leave_out_EAS": "East Asia omitted",
    "leave_out_EUR": "Europe omitted",
    "leave_out_OCE": "Oceania omitted",
    "leave_out_SAS": "South Asia omitted",
    "leave_out_WAS": "West Asia omitted",
}


def robustness_figure(data_directory: Path, figure_directory: Path) -> None:
    sensitivity = pd.read_csv(data_directory / "sensitivity_analysis.csv")
    windows = pd.read_csv(data_directory / "window_size_sensitivity.csv")
    figure, axes = plt.subplots(
        1, 3, figsize=(15.2, 6.4), gridspec_kw={"width_ratios": [1.25, 1.0, 0.85]}
    )

    subset_frame = sensitivity[sensitivity["metric"] == "Pearson"]
    order = [key for key in ROBUSTNESS_LABELS if key in set(subset_frame["subset"])]
    axis = axes[0]
    for offset, (label, colour, marker) in enumerate(
        [("Neanderthal", "#2c5f8a", "o"), ("Denisovan", "#a0522d", "s")]
    ):
        values = [
            subset_frame[
                (subset_frame["subset"] == key) & (subset_frame["ancestry"] == label)
            ]["raw_distance_r"].iloc[0]
            for key in order
        ]
        axis.scatter(
            values,
            [index + (offset - 0.5) * 0.24 for index in range(len(order))],
            color=colour,
            marker=marker,
            s=46,
            label=label,
        )
    axis.set_yticks(range(len(order)))
    axis.set_yticklabels([ROBUSTNESS_LABELS[key] for key in order], fontsize=10)
    axis.invert_yaxis()
    axis.axvline(0, color="#999999", lw=1)
    axis.set_xlabel("distance correlation (Pearson r)", fontsize=11)
    axis.set_title("a  Population subsets", fontsize=12, loc="left")
    axis.legend(fontsize=9.5, loc="lower left", frameon=False)

    metric_frame = sensitivity[sensitivity["subset"] == "all"]
    metrics = metric_frame["metric"].unique().tolist()
    axis = axes[1]
    for offset, (label, colour, marker) in enumerate(
        [("Neanderthal", "#2c5f8a", "o"), ("Denisovan", "#a0522d", "s")]
    ):
        values = [
            metric_frame[
                (metric_frame["metric"] == metric)
                & (metric_frame["ancestry"] == label)
            ]["raw_distance_r"].iloc[0]
            for metric in metrics
        ]
        axis.scatter(
            values,
            [index + (offset - 0.5) * 0.24 for index in range(len(metrics))],
            color=colour,
            marker=marker,
            s=46,
        )
    axis.set_yticks(range(len(metrics)))
    axis.set_yticklabels(metrics, fontsize=10)
    axis.invert_yaxis()
    axis.axvline(0, color="#999999", lw=1)
    axis.set_xlabel("distance correlation (r)", fontsize=11)
    axis.set_title("b  Similarity measures", fontsize=12, loc="left")

    axis = axes[2]
    sizes = sorted(windows["window_size_bp"].unique())
    positions = np.arange(len(sizes))
    for offset, (label, colour) in enumerate(
        [("Neanderthal", "#2c5f8a"), ("Denisovan", "#a0522d")]
    ):
        values = [
            windows[
                (windows["window_size_bp"] == size) & (windows["ancestry"] == label)
            ]["raw_distance_r"].iloc[0]
            for size in sizes
        ]
        axis.bar(positions + (offset - 0.5) * 0.34, values, width=0.32, color=colour)
    axis.set_xticks(positions)
    axis.set_xticklabels([f"{size // 1000} kb" for size in sizes], fontsize=10)
    axis.axhline(0, color="#999999", lw=1)
    axis.set_ylabel("distance correlation (r)", fontsize=11)
    axis.set_title("c  Window size", fontsize=12, loc="left")

    figure.tight_layout()
    save_figure(figure, figure_directory, "figH5_robustness_summary")


def main() -> None:
    args = parse_args()
    concept_figure(args.figure_dir)
    residual_figure(args.data_dir, args.figure_dir)
    robustness_figure(args.data_dir, args.figure_dir)
    print("Created Heredity conceptual, residual, and robustness figures")


if __name__ == "__main__":
    main()
