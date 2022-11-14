import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    DATA_PROVIDERS: str = os.getenv("DATA_PROVIDERS", default="YAHOO")
    ALPHA_VANTAGE_API_KEY: str = os.getenv("ALPHA_VANTAGE_API_KEY", default="")


settings = Settings()
