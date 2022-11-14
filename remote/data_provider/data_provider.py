from abc import ABC

from remote.client.remote_client import RemoteClient
from schemas.stock_price_information import StockPriceInformation


class DataProvider(ABC):
    client: RemoteClient

    def get_stock_price_information(self, ticker: str) -> StockPriceInformation:
        api_client_stock_data = self.client.get_stock_price_information(ticker=ticker)
        return self.map_client_response_to_schema(api_client_stock_data)

    def map_client_response_to_schema(self, api_response_data) -> StockPriceInformation:
        raise NotImplementedError()
