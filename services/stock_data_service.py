from remote.data_provider.data_provider import DataProvider
from schemas.stock_price_information import StockPriceInformation


def get_stock_prices(ticker: str, data_providers: set[DataProvider]) -> set[StockPriceInformation]:
    stock_price_information: set[StockPriceInformation] = set()
    for data_provider in data_providers:
        stock_price_information.add(data_provider.get_stock_price_information(ticker=ticker))
    return stock_price_information
