import pytest

from remote.data_provider.data_provider import DataProvider
from tests.test_utils import TestClient


def test_map_client_response_to_schema_has_no_default_implementation():
    provider: DataProvider = DataProvider()
    provider.client = TestClient()
    with pytest.raises(NotImplementedError):
        provider.map_client_response_to_schema(api_response_data={})
