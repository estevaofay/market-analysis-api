from fastapi import APIRouter

from api.endpoints import exchange_endpoints
from api.endpoints import currency_endpoints

api_router = APIRouter()
api_router.include_router(exchange_endpoints.router, tags=["Exchange"])
api_router.include_router(currency_endpoints.router, tags=["Currency"])
