from remote.client.remote_client import RemoteClient
from remote.data_provider.data_provider import DataProvider
from schemas.stock_price_information import StockPriceInformation

SAMPLE_TICKER = "TESTAMZN"
SAMPLE_PRICE = 1337
SAMPLE_CURRENCY = "USD"
STOCK_QUOTES_ENDPOINT = "/stocks/{}/quotes"


class TestClient(RemoteClient):
    def get_stock_price_information(self, ticker: str):
        return {"provider": "ExampleDataProvider", "ticker": ticker, "currency": SAMPLE_CURRENCY, "price": SAMPLE_PRICE}


class ExampleDataProvider(DataProvider):
    def __init__(self):
        self.client = TestClient()

    def map_client_response_to_schema(self, api_response_data) -> StockPriceInformation:
        return StockPriceInformation(**api_response_data)
