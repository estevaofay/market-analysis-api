from remote.client.yahoo_remote_client import YahooRemoteClient
from remote.data_provider.data_provider import DataProvider
from schemas.stock_price_information import StockPriceInformation


class YahooDataProvider(DataProvider):

    def __init__(self):
        self.client = YahooRemoteClient()

    def map_client_response_to_schema(self, api_response_data) -> StockPriceInformation:
        data = {
            "provider": "Yahoo",
            "price": api_response_data['currentPrice'],
            "ticker": api_response_data['symbol']
        }
        return StockPriceInformation(**data)
