from fastapi import FastAPI

from api.api import api_router


def include_routes(application: FastAPI):
    application.include_router(api_router)


def start_app() -> FastAPI:
    application = FastAPI()
    include_routes(application)
    return application


app = start_app()
