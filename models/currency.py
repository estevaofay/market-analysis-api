from typing import Optional

from pydantic import BaseModel


class Currency(BaseModel):
    code: int
    iata_code: Optional[str]
    country_code: str
    swift_code: str
    inclusion_date: str
    registration_date: str
    gender: str
    name: str
    formatted_name: str
    name_in_singular: str
    name_in_plural: Optional[str]
    acronym: str
    type: str
    symbol: str
    data_source: str = "https://www3.bcb.gov.br/bc_moeda/rest/moeda/data"
