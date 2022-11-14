from fastapi import APIRouter, Depends
from starlette import status

from api.deps import get_data_providers
from remote.data_provider.data_provider import DataProvider
from schemas.stock_price_information import StockPriceInformation
from services import stock_data_service

router = APIRouter()


@router.get("/stocks/{ticker}/quotes", response_model=set[StockPriceInformation], status_code=status.HTTP_200_OK)
async def get_stock_quotes(ticker: str, data_providers: set[DataProvider] = Depends(get_data_providers)):
    return stock_data_service.get_stock_prices(ticker=ticker, data_providers=data_providers)
