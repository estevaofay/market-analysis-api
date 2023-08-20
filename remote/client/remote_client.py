from abc import ABC, abstractmethod


class RemoteClient(ABC):
    @abstractmethod
    def get_stock_price_information(self, ticker: str):
        raise NotImplementedError()
