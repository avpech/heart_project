from fastapi import Depends, Request

from src.api.service import PredictService
from src.ml.model import HeartRiskModel


def get_model(request: Request) -> HeartRiskModel:
    """Return the HeartRiskModel instance from app state."""
    return request.app.state.model


def get_predict_service(model: HeartRiskModel = Depends(get_model)) -> PredictService:
    """Return a PredictService instance using the provided model."""
    return PredictService(model=model)
