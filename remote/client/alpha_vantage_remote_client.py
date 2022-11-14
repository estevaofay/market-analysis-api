from alpha_vantage.timeseries import TimeSeries

from core.environment_variables import settings
from remote.client.remote_client import RemoteClient


class AlphaVantageRemoteClient(RemoteClient):

    def __init__(self):
        self.api_key = settings.ALPHA_VANTAGE_API_KEY

    def get_stock_price_information(self, ticker: str):
        time_series: TimeSeries = TimeSeries(key=settings.ALPHA_VANTAGE_API_KEY)
        data, _ = time_series.get_quote_endpoint(symbol=ticker)
        return data
