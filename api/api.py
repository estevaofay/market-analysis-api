from fastapi import APIRouter
from fastapi_healthcheck import healthCheckRoute

from api.endpoints import stocks
from core.health.healthcheck_factory import health_checks

api_router = APIRouter()
api_router.include_router(stocks.router, tags=["Stocks"])
api_router.add_api_route("/health", endpoint=healthCheckRoute(factory=health_checks), tags=["Health"])
