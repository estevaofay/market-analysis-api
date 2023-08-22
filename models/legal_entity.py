from typing import Optional

from pydantic import BaseModel


class LegalEntity(BaseModel):
    name: Optional[str]
    identifier: Optional[str]
