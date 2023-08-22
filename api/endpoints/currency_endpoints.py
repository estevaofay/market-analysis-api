from fastapi import APIRouter, status, Request

router = APIRouter()


@router.get("/currencies", status_code=status.HTTP_200_OK)
async def get_currencies(request: Request):
    return request.app.state.currency_list


@router.get("/currencies/{currency_code}", status_code=status.HTTP_200_OK)
async def get_currency(request: Request, currency_code: str):
    return request.app.state.currencies[currency_code]
