import io

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import JSONResponse, StreamingResponse

from src.api.depends import get_predict_service
from src.api.schemas import HeartDataRow, PredictionOut
from src.api.service import PredictService
from src.core.config import get_settings

settings = get_settings()

router = APIRouter(prefix=settings.api_str)


@router.post(
        "/predict_csv",
        response_model=list[PredictionOut],
        summary="Predict heart attack risk for patients from a CSV file"
)
async def predict_csv(
    file: UploadFile = File(...),
    predict_service: PredictService = Depends(get_predict_service),
) -> list[dict]:
    try:
        df_pred = predict_service.predict_from_csv(file)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=e.args
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Prediction failed"
        )

    return df_pred.to_dict(orient="records")


@router.post(
        "/predict",
        response_model=PredictionOut,
        summary="Predict heart attack risk for a single patient"
)
async def predict_single(
    data: HeartDataRow,
    predict_service: PredictService = Depends(get_predict_service)
) -> PredictionOut:
    try:
        prediction = predict_service.predict_single(data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=e.args
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Prediction failed"
        )

    return prediction


@router.post(
        "/get_predictions_csv",
        response_class=StreamingResponse,
        responses={
            status.HTTP_200_OK: {
                "content": {"text/csv": {}},
                "description": "CSV file with predictions",
            }
        },
        summary="Predict heart attack risk for patients from a CSV file, return CSV"
)
async def get_predictions_csv(
    file: UploadFile = File(...),
    predict_service: PredictService = Depends(get_predict_service),
) -> StreamingResponse:
    try:
        df_pred = predict_service.predict_from_csv(file)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=e.args
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Prediction failed"
        )

    output = io.StringIO()
    df_pred.to_csv(output, index=False)
    output.seek(0)
    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=predictions.csv"}
    )


@router.get("/health", summary="Service Healthcheck")
async def health_check():
    return JSONResponse(content={"status": "OK"}, status_code=status.HTTP_200_OK)
