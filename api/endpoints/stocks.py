from fastapi import APIRouter

router = APIRouter()


@router.get("/stocks/{name}/price")
async def get_stock_quotes(name: str):
    return {"message": f"Hello {name}"}
