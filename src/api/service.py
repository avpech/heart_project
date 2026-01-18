import pandas as pd
from fastapi import UploadFile

from src.api.schemas import HeartDataRow, PredictionOut
from src.api.validators import validate_csv_dataframe
from src.ml.model import HeartRiskModel


class PredictService:

    def __init__(self, model: HeartRiskModel):
        self.model = model

    def predict_from_csv(self, file: UploadFile) -> pd.DataFrame:
        try:
            df = pd.read_csv(file.file)
        except Exception as e:
            raise ValueError(f"Failed to read CSV: {e}")

        if df.empty:
            raise ValueError("Uploaded CSV is empty")

        df = validate_csv_dataframe(df)
        return self.model.predict(df)

    def predict_single(self, row: HeartDataRow) -> PredictionOut:
        df = pd.DataFrame([row.model_dump()])
        df_pred = self.model.predict(df)
        return PredictionOut(
            id=int(df_pred["id"].iloc[0]),
            prediction=int(df_pred["prediction"].iloc[0])
        )
