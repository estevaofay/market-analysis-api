from pydantic import BaseModel


class StockPriceInformation(BaseModel):
    provider: str
    ticker: str
    currency: str
    price: float

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))
