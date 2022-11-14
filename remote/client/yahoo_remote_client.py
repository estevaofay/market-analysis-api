import yfinance as yf

from remote.client.remote_client import RemoteClient


class YahooRemoteClient(RemoteClient):
    def get_stock_price_information(self, ticker: str):
        return yf.Ticker(ticker).info
