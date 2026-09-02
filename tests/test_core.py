import numpy as np
import pytest

from pitch_control.blending import (
    analytic_blend_weight,
    blend_two,
    optimize_brier_blend,
)
from pitch_control.metrics import brier_score, brier_skill_score
from pitch_control.temporal import rolling_origin_splits


def test_brier_metric_exact_cases():
    target = np.array([0.0, 1.0])
    assert brier_score(target, np.array([0.0, 1.0])) == 0.0
    assert brier_skill_score(target, np.array([0.0, 1.0])) == 100_000.0
    assert brier_score(target, np.array([0.5, 0.5])) == 0.25


def test_temporal_splits_never_use_validation_or_future_years():
    seasons = np.repeat(np.arange(2019, 2025), 3)
    folds = rolling_origin_splits(seasons, [2022, 2023, 2024])
    for fold in folds:
        assert seasons[fold.train_index].max() < fold.validation_year
        assert np.unique(seasons[fold.validation_index]).tolist() == [fold.validation_year]
        assert np.intersect1d(fold.train_index, fold.validation_index).size == 0


def test_convex_blend_prefers_the_better_prediction():
    target = np.array([0.0, 0.0, 1.0, 1.0])
    strong = np.array([0.1, 0.2, 0.8, 0.9])
    weak = np.array([0.45, 0.55, 0.45, 0.55])
    weights = optimize_brier_blend(np.column_stack([strong, weak]), target)
    assert weights.sum() == pytest.approx(1.0)
    assert np.all(weights >= 0.0)
    assert weights[0] > weights[1]


def test_analytic_weight_is_fit_then_reusable():
    target = np.array([0.0, 1.0, 0.0, 1.0])
    anchor = np.array([0.4, 0.6, 0.4, 0.6])
    candidate = np.array([0.1, 0.9, 0.2, 0.8])
    weight = analytic_blend_weight(target, candidate, anchor)
    blended = blend_two(candidate, anchor, weight)
    assert 0.0 <= weight <= 1.0
    assert brier_score(target, blended) <= brier_score(target, anchor)
