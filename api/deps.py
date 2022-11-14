from typing import Generator

from core.environment_variables import settings
from core.supported_data_providers import SUPPORTED_DATA_PROVIDERS
from remote.data_provider.data_provider import DataProvider


def get_data_providers() -> Generator:
    data_providers: set[DataProvider] = set()
    stock_data_providers = settings.DATA_PROVIDERS
    stock_data_providers = stock_data_providers.split(", ")
    for data_provider in stock_data_providers:
        if data_provider in SUPPORTED_DATA_PROVIDERS.keys():
            data_providers.add(SUPPORTED_DATA_PROVIDERS[data_provider])
    yield data_providers
