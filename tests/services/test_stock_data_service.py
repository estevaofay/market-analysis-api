from remote.data_provider.data_provider import DataProvider
from schemas.stock_price_information import StockPriceInformation
from services import stock_data_service
from tests.test_utils import ExampleDataProvider, SAMPLE_TICKER, SAMPLE_PRICE


def test_get_stock_prices():
    data_providers: set[DataProvider] = {ExampleDataProvider()}
    stock_price_information: set[StockPriceInformation] = stock_data_service.get_stock_prices(
        ticker=SAMPLE_TICKER,
        data_providers=data_providers
    )
    assert 1 == len(stock_price_information)
    stock_price_information: StockPriceInformation = stock_price_information.pop()
    assert SAMPLE_TICKER == stock_price_information.ticker
    assert SAMPLE_PRICE == stock_price_information.price
    assert hasattr(stock_price_information, "provider")
