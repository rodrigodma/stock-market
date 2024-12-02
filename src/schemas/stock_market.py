from typing import Optional
from pydantic import BaseModel, Field

class StockMarketDTO(BaseModel):
    purchased_amount: Optional[float] = Field(None)