from fastapi import APIRouter

from api.endpoints import stocks

api_router = APIRouter()
api_router.include_router(stocks.router, tags=["Stocks"])
