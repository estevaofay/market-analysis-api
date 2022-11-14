import os

from pydantic import BaseSettings

from remote.data_provider.yahoo_data_provider import YahooDataProvider
from tests.test_utils import ExampleDataProvider


class Settings(BaseSettings):
    DATA_PROVIDERS: str = os.getenv("DATA_PROVIDERS", default="YAHOO")


SUPPORTED_DATA_PROVIDERS = {
    "YAHOO": YahooDataProvider(),
    "EXAMPLE_DATA_PROVIDER": ExampleDataProvider(),
}

settings = Settings()
