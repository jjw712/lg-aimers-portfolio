"""Convex probability blending for Brier Score."""

from __future__ import annotations

import numpy as np


def project_simplex(vector: np.ndarray) -> np.ndarray:
    values = np.asarray(vector, dtype=np.float64).reshape(-1)
    if len(values) == 0 or not np.isfinite(values).all():
        raise ValueError("simplex projection requires finite values")
    ordered = np.sort(values)[::-1]
    cumulative = np.cumsum(ordered) - 1.0
    indices = np.arange(1, len(values) + 1)
    valid = ordered - cumulative / indices > 0.0
    rho = int(indices[valid][-1])
    theta = cumulative[rho - 1] / rho
    return np.maximum(values - theta, 0.0)


def _validated_blend_inputs(
    prediction_matrix: np.ndarray, target: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    matrix = np.asarray(prediction_matrix, dtype=np.float64)
    y = np.asarray(target, dtype=np.float64).reshape(-1)
    if matrix.ndim != 2 or matrix.shape[0] != len(y):
        raise ValueError("prediction_matrix must have shape (rows, models)")
    if len(y) == 0 or matrix.shape[1] == 0:
        raise ValueError("blend optimization requires rows and models")
    if not np.isfinite(matrix).all() or not np.isfinite(y).all():
        raise ValueError("blend inputs must be finite")
    if ((matrix < 0.0) | (matrix > 1.0)).any():
        raise ValueError("probabilities must be in [0, 1]")
    return matrix, y


def optimize_brier_blend(
    prediction_matrix: np.ndarray,
    target: np.ndarray,
    *,
    iterations: int = 2_000,
    tolerance: float = 1e-12,
) -> np.ndarray:
    """Fit non-negative weights constrained to sum to one."""
    matrix, y = _validated_blend_inputs(prediction_matrix, target)
    weights = np.full(matrix.shape[1], 1.0 / matrix.shape[1], dtype=np.float64)
    gram = matrix.T @ matrix / len(y)
    cross = matrix.T @ y / len(y)
    largest_eigenvalue = float(np.linalg.eigvalsh(gram)[-1])
    step = 1.0 / max(2.0 * largest_eigenvalue, 1e-12)
    for _ in range(iterations):
        gradient = 2.0 * (gram @ weights - cross)
        updated = project_simplex(weights - step * gradient)
        if np.max(np.abs(updated - weights)) < tolerance:
            return updated
        weights = updated
    return weights


def analytic_blend_weight(
    target: np.ndarray,
    candidate_probability: np.ndarray,
    anchor_probability: np.ndarray,
) -> float:
    """Return the candidate weight in anchor + w * (candidate - anchor)."""
    y = np.asarray(target, dtype=np.float64).reshape(-1)
    candidate = np.asarray(candidate_probability, dtype=np.float64).reshape(-1)
    anchor = np.asarray(anchor_probability, dtype=np.float64).reshape(-1)
    if y.shape != candidate.shape or y.shape != anchor.shape or len(y) == 0:
        raise ValueError("target, candidate and anchor must have the same non-empty shape")
    if not np.isfinite(y).all() or not np.isfinite(candidate).all() or not np.isfinite(anchor).all():
        raise ValueError("blend inputs must be finite")
    delta = candidate - anchor
    denominator = float(delta @ delta)
    if denominator <= 0.0:
        return 0.0
    return float(np.clip((delta @ (y - anchor)) / denominator, 0.0, 1.0))


def blend_two(
    candidate_probability: np.ndarray,
    anchor_probability: np.ndarray,
    candidate_weight: float,
) -> np.ndarray:
    if not np.isfinite(candidate_weight) or not 0.0 <= candidate_weight <= 1.0:
        raise ValueError("candidate_weight must be in [0, 1]")
    candidate = np.asarray(candidate_probability, dtype=np.float64)
    anchor = np.asarray(anchor_probability, dtype=np.float64)
    if candidate.shape != anchor.shape:
        raise ValueError("candidate and anchor shapes must match")
    return np.clip(anchor + candidate_weight * (candidate - anchor), 0.0, 1.0)
