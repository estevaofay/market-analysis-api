from fastapi import FastAPI

from api.api import api_router
from core.config.lifespan import lifespan


def include_routes(application: FastAPI):
    application.include_router(api_router)


def start_app() -> FastAPI:
    application = FastAPI(lifespan=lifespan)
    include_routes(application)
    return application


app = start_app()
