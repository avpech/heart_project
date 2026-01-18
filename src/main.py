from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.routes import router
from src.core.config import get_settings
from src.core.logger import setup_logging
from src.ml.model import HeartRiskModel

setup_logging()

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    model = HeartRiskModel(model_path=settings.model_path)
    app.state.model = model
    yield
    del app.state.model


app = FastAPI(
    title=settings.app_name,
    description=settings.description,
    docs_url=settings.docs_url,
    lifespan=lifespan
)

app.include_router(router)
