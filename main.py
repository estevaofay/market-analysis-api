from fastapi import FastAPI

app = FastAPI()


@app.get("/hello/{name}")
async def get_stock_quotes(name: str):
    return {"message": f"Hello {name}"}
