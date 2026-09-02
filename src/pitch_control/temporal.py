"""Rolling-origin splits for predicting unseen seasons."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class TemporalFold:
    validation_year: int
    train_index: np.ndarray
    validation_index: np.ndarray
    train_years: tuple[int, ...]


def rolling_origin_splits(
    seasons: Iterable[int],
    validation_years: Iterable[int],
    *,
    minimum_train_years: int = 2,
) -> list[TemporalFold]:
    season_values = np.asarray(list(seasons))
    if season_values.ndim != 1 or len(season_values) == 0:
        raise ValueError("seasons must be a non-empty one-dimensional sequence")
    if not np.isfinite(season_values.astype(float)).all():
        raise ValueError("seasons must be finite")

    available = tuple(sorted(int(value) for value in np.unique(season_values)))
    folds: list[TemporalFold] = []
    for year_value in validation_years:
        validation_year = int(year_value)
        if validation_year not in available:
            raise ValueError(f"validation year {validation_year} is unavailable")
        train_years = tuple(year for year in available if year < validation_year)
        if len(train_years) < minimum_train_years:
            raise ValueError(
                f"validation year {validation_year} has only "
                f"{len(train_years)} prior seasons"
            )
        train_index = np.flatnonzero(season_values < validation_year)
        validation_index = np.flatnonzero(season_values == validation_year)
        if np.intersect1d(train_index, validation_index).size:
            raise AssertionError("temporal split overlap detected")
        folds.append(
            TemporalFold(
                validation_year=validation_year,
                train_index=train_index,
                validation_index=validation_index,
                train_years=train_years,
            )
        )
    return folds
