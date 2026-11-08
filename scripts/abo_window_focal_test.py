#!/usr/bin/env python3
"""Evaluate the ABO window against the genome-wide structural background.

For every 500-kb window the absolute between-population difference in
archaic-segment frequency is regressed on geographic distance across the
non-admixed population pairs. Excess similarity is defined as

    excess = predicted absolute difference - observed absolute difference

so a positive value marks a pair that is more similar than geographic distance
predicts, and it is standardised by the within-window standard deviation. The
maximum standardised excess in a window is the strongest excess-similarity
signal that window offers; the distribution of those per-window maxima is the
genome-wide structural background against which the prespecified ABO window is
judged, using an upper-tail empirical P value.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
ABO_CHROM = "chr9"
ABO_WINDOW_START = 133_000_000
BIN_SIZE = 500_000
MINIMUM_NONZERO_POPULATIONS = 10


def haversine(lat1, lon1, lat2, lon2):
    radius = 6371.0088
    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    dphi = phi2 - phi1
    dlambda = np.radians(lon2) - np.radians(lon1)
    a = np.sin(dphi / 2.0) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(dlambda / 2.0) ** 2
    return 2 * radius * np.arcsin(np.sqrt(a))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=PROJECT_DIR / "data")
    parser.add_argument(
        "--output",
        type=Path,
        default=PROJECT_DIR / "data" / "abo_focal_test.json",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data_dir = args.data_dir
    profiles = np.load(data_dir / "population_profiles_500kb.npz", allow_pickle=True)
    populations = [str(name) for name in profiles["populations"]]
    chromosomes = np.array([str(value) for value in profiles["chromosomes"]])
    bin_numbers = np.asarray(profiles["bin_numbers"])

    pairs = pd.read_csv(data_dir / "pairwise_sharing_corrected.csv")
    admixed = set()
    for population in populations:
        involved = pairs[(pairs["pop1"] == population) | (pairs["pop2"] == population)]
        if len(involved) and involved["any_admixed"].eq(1).all():
            admixed.add(population)

    metadata = pd.read_csv(data_dir / "population_metadata.csv").set_index("population")
    kept = [
        population
        for population in populations
        if population not in admixed and population in metadata.index
    ]
    indices = [populations.index(population) for population in kept]
    latitudes = metadata.loc[kept, "latitude"].to_numpy(dtype=float)
    longitudes = metadata.loc[kept, "longitude"].to_numpy(dtype=float)

    pair_index = list(combinations(range(len(kept)), 2))
    first = np.array([i for i, _ in pair_index])
    second = np.array([j for _, j in pair_index])
    distance = haversine(
        latitudes[first], longitudes[first], latitudes[second], longitudes[second]
    )
    design = np.column_stack([np.ones_like(distance), distance])
    projector = design @ np.linalg.pinv(design)

    abo_bin = ABO_WINDOW_START // BIN_SIZE
    abo_position = np.where((chromosomes == ABO_CHROM) & (bin_numbers == abo_bin))[0]
    if abo_position.size != 1:
        raise RuntimeError("Could not locate a unique ABO window in the profiles")
    abo_index = int(abo_position[0])

    results: dict[str, object] = {
        "abo_chromosome": ABO_CHROM,
        "abo_window_start": ABO_WINDOW_START,
        "bin_size": BIN_SIZE,
        "populations": len(kept),
        "pairs": len(pair_index),
        "minimum_nonzero_populations": MINIMUM_NONZERO_POPULATIONS,
    }

    for key, label in (("neanderthal", "nean"), ("denisovan", "deni")):
        matrix = np.asarray(profiles[key], dtype=float)[indices, :]
        difference = np.abs(matrix[first, :] - matrix[second, :])
        nonzero_populations = (matrix > 0).sum(axis=0)
        usable = nonzero_populations >= MINIMUM_NONZERO_POPULATIONS
        predicted = projector @ difference
        excess = predicted - difference
        spread = excess.std(axis=0, ddof=1)
        scalable = spread > 0
        standardised = excess[:, scalable] / spread[scalable]
        window_maximum = np.full(excess.shape[1], np.nan)
        window_maximum[scalable] = standardised.max(axis=0)
        usable &= np.isfinite(window_maximum)
        abo_value = float(window_maximum[abo_index])
        background = window_maximum[usable]
        percentile = float((background <= abo_value).mean() * 100.0)
        empirical_p = float((background >= abo_value).mean())
        results[f"{label}_usable_windows"] = int(usable.sum())
        results[f"{label}_abo_max_excess_z"] = abo_value
        results[f"{label}_background_median"] = float(np.median(background))
        results[f"{label}_background_p95"] = float(np.percentile(background, 95))
        results[f"{label}_abo_percentile"] = percentile
        results[f"{label}_abo_empirical_p"] = empirical_p

    args.output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
