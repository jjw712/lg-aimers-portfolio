"""Dynamic checks for row-independent prediction functions."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Any

import numpy as np
import pandas as pd

Predictor = Callable[[pd.DataFrame], np.ndarray]


def _probability(predict: Predictor, frame: pd.DataFrame) -> np.ndarray:
    probability = np.asarray(predict(frame.copy()), dtype=np.float64).reshape(-1)
    if len(probability) != len(frame):
        raise ValueError("predictor returned the wrong number of rows")
    if not np.isfinite(probability).all():
        raise ValueError("predictor returned NaN or infinity")
    return probability


def _max_abs(left: np.ndarray, right: np.ndarray) -> float:
    if left.shape != right.shape:
        raise ValueError("comparison shapes do not match")
    return float(np.max(np.abs(left - right))) if len(left) else 0.0


def audit_prediction_invariance(
    predict: Predictor,
    frame: pd.DataFrame,
    *,
    row_id_column: str = "row_id",
    batch_sizes: Iterable[int] = (1, 3, 8),
    seed: int = 42,
    atol: float = 1e-12,
) -> dict[str, Any]:
    """Compare the same rows under singleton, batch, shuffle and subset contexts."""
    if len(frame) < 2:
        raise ValueError("the audit requires at least two rows")
    if row_id_column not in frame:
        raise ValueError(f"missing row id column: {row_id_column}")
    if frame[row_id_column].duplicated().any():
        raise ValueError("row ids must be unique")

    baseline = _probability(predict, frame)
    checks: dict[str, float] = {}

    singleton = np.concatenate(
        [_probability(predict, frame.iloc[[position]]) for position in range(len(frame))]
    )
    checks["singleton_vs_full"] = _max_abs(singleton, baseline)

    for batch_size_value in batch_sizes:
        batch_size = int(batch_size_value)
        if batch_size <= 0:
            raise ValueError("batch sizes must be positive")
        chunks = [
            _probability(predict, frame.iloc[start : start + batch_size])
            for start in range(0, len(frame), batch_size)
        ]
        checks[f"batch_{batch_size}_vs_full"] = _max_abs(
            np.concatenate(chunks), baseline
        )

    rng = np.random.default_rng(seed)
    permutation = rng.permutation(len(frame))
    shuffled = _probability(predict, frame.iloc[permutation])
    restored = np.empty_like(shuffled)
    restored[permutation] = shuffled
    checks["shuffle_restore_vs_full"] = _max_abs(restored, baseline)

    subset = np.arange(0, len(frame), 2, dtype=np.int64)
    subset_probability = _probability(predict, frame.iloc[subset])
    checks["other_rows_removed"] = _max_abs(subset_probability, baseline[subset])

    passed = all(value <= atol for value in checks.values())
    return {
        "status": "PASS" if passed else "FAIL",
        "passed": passed,
        "atol": float(atol),
        "row_count": len(frame),
        "checks": checks,
    }
