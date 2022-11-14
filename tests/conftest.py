from typing import Generator

import pytest
from fastapi.testclient import TestClient

from core.environment_variables import settings
from main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="function")
def example_data_provider():
    settings.DATA_PROVIDERS = "EXAMPLE_DATA_PROVIDER"
    yield settings
