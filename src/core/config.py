from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Heart Health"
    api_str: str = "/api"
    description: str = "Heart health predictions project"
    docs_url: str = "/docs"
    model_path: str = "artifacts/heart_risk_model.pkl"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
