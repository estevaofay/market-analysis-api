"""
Stock exchange Schema based on ISO 10383 found on
https://www.iso20022.org/sites/default/files/media/file/ISO10383_MIC_Release_2_0_Factsheet_v2.pdf
"""

from typing import Optional

from pydantic import BaseModel, ConfigDict

from models.legal_entity import LegalEntity
from models.market_category import MarketCategory


class Exchange(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    market_name: str
    market_identifier_code: str
    operating_market_identifier_code: str
    operating_or_segment: str
    operating: bool
    segment: bool
    legal_entity: LegalEntity
    market_category: Optional[MarketCategory]
    acronym: Optional[str]
    country: str
    city: str
    status: str
    active: bool
    creation_date: str
    last_update_date: Optional[str]
    last_validation_date: Optional[str]
    expiry_date: Optional[str]
    website: Optional[str]
    comments: Optional[str]
    data_source: str = "https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.csv"

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))
