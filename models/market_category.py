from pydantic import BaseModel


class MarketCategory(BaseModel):
    code: str
    description: str
