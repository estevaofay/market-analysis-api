from fastapi.testclient import TestClient
from requests import Response

from tests.test_utils import STOCK_QUOTES_ENDPOINT, SAMPLE_TICKER


def test_get_stock_quotes(client: TestClient, example_data_provider):
    url: str = STOCK_QUOTES_ENDPOINT.format(SAMPLE_TICKER)
    response: Response = client.get(url=url)
    assert response.status_code == 200
    response_json = response.json()
    assert 1 == len(response_json)
    for stock_info in response_json:
        assert "provider" in stock_info
        assert "price" in stock_info
        assert "ticker" in stock_info
