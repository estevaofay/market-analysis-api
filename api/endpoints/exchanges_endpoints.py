from fastapi import APIRouter, Request
from starlette import status

router = APIRouter()


@router.get("/exchanges", status_code=status.HTTP_200_OK)
async def get_exchanges(request: Request):
    return request.app.state.exchanges_list
