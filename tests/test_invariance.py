import numpy as np
import pandas as pd

from pitch_control.invariance import audit_prediction_invariance


def _frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "row_id": [f"row-{value}" for value in range(12)],
            "feature": np.linspace(-2.0, 2.0, 12),
        }
    )


def test_row_local_predictor_passes_all_contexts():
    def predict(frame: pd.DataFrame) -> np.ndarray:
        value = frame["feature"].to_numpy(float)
        return 1.0 / (1.0 + np.exp(-value))

    result = audit_prediction_invariance(predict, _frame())
    assert result["status"] == "PASS"
    assert all(value == 0.0 for value in result["checks"].values())


def test_batch_dependent_predictor_is_rejected():
    def predict(frame: pd.DataFrame) -> np.ndarray:
        return np.full(len(frame), len(frame) / 100.0)

    result = audit_prediction_invariance(predict, _frame())
    assert result["status"] == "FAIL"
    assert result["checks"]["singleton_vs_full"] > 0.0
