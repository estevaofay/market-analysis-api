from remote.data_provider.alpha_vantage_data_provider import AlphaVantageDataProvider
from remote.data_provider.yahoo_data_provider import YahooDataProvider
from tests.test_utils import ExampleDataProvider

SUPPORTED_DATA_PROVIDERS = {
    "YAHOO": YahooDataProvider(),
    "ALPHA_VANTAGE": AlphaVantageDataProvider(),
    "EXAMPLE_DATA_PROVIDER": ExampleDataProvider(),
}
