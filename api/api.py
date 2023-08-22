from fastapi import APIRouter

from api.endpoints import exchanges_endpoints

api_router = APIRouter()
api_router.include_router(exchanges_endpoints.router, tags=["Exchanges"])
