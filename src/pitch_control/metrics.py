"""Probability metrics used by the case study."""

from __future__ import annotations

import numpy as np


def _validated_arrays(
    y_true: np.ndarray, probability: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    y = np.asarray(y_true, dtype=np.float64).reshape(-1)
    p = np.asarray(probability, dtype=np.float64).reshape(-1)
    if y.shape != p.shape:
        raise ValueError(f"shape mismatch: y={y.shape}, p={p.shape}")
    if len(y) == 0:
        raise ValueError("at least one observation is required")
    if not np.isfinite(y).all() or not np.isfinite(p).all():
        raise ValueError("targets and predictions must be finite")
    if ((p < 0.0) | (p > 1.0)).any():
        raise ValueError("predictions must be in [0, 1]")
    return y, p


def brier_score(y_true: np.ndarray, probability: np.ndarray) -> float:
    y, p = _validated_arrays(y_true, probability)
    return float(np.mean((p - y) ** 2))


def raw_brier_skill_score(y_true: np.ndarray, probability: np.ndarray) -> float:
    """Return the competition-style score before flooring it at zero."""
    y, p = _validated_arrays(y_true, probability)
    rate = float(y.mean())
    reference = rate * (1.0 - rate)
    if reference <= 0.0:
        raise ValueError("skill score is undefined for a constant target")
    return float(100_000.0 * (1.0 - brier_score(y, p) / reference))


def brier_skill_score(y_true: np.ndarray, probability: np.ndarray) -> float:
    return float(max(0.0, raw_brier_skill_score(y_true, probability)))
