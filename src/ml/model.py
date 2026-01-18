import logging
from pathlib import Path

import dill
import pandas as pd
from sklearn.pipeline import Pipeline

logger = logging.getLogger(__name__)


class HeartRiskModel:

    def __init__(
            self,
            model_path: str | Path,
    ) -> None:
        self._model_path = Path(model_path)
        self._model = self._load_model()

    def _load_model(self) -> Pipeline:
        """Load model from file."""

        if not self._model_path.exists():
            raise FileNotFoundError(f"Model file not found: {self._model_path}")
        try:
            with open(self._model_path, "rb") as file:
                model = dill.load(file)
        except Exception as e:
            raise RuntimeError(f"Failed to load model from {self._model_path}: {e}")

        if not isinstance(model, Pipeline):
            raise RuntimeError(f"The loaded object is not a Pipeline, but {type(model)}")

        return model

    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        """Predict class."""
        if df.empty:
            raise ValueError("Input DataFrame is empty")

        try:
            predictions = self._model.predict(df)
        except Exception as e:
            logger.error("Prediction failed", exc_info=True)
            raise RuntimeError("Prediction failed") from e
        return pd.DataFrame({
            "id": df["id"],
            "prediction": predictions,
        })
