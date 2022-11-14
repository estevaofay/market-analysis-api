from remote.client.alpha_vantage_remote_client import AlphaVantageRemoteClient
from remote.client.remote_client import RemoteClient
from remote.data_provider.data_provider import DataProvider
from schemas.stock_price_information import StockPriceInformation


class AlphaVantageDataProvider(DataProvider):

    def __init__(self):
        self.client: RemoteClient = AlphaVantageRemoteClient()

    def map_client_response_to_schema(self, client_response_data) -> StockPriceInformation:
        data = {
            "provider": "Alpha Vantage",
            "price": client_response_data['05. price'],
            "ticker": client_response_data['01. symbol']
        }
        return StockPriceInformation(**data)
