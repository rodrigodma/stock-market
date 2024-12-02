from pydantic import BaseModel
from typing import List
from datetime import datetime


class StockValues(BaseModel):
    open: float
    high: float
    low: float
    close: float

class StockPerformance(BaseModel):
    five_days: float
    one_month: float
    three_months: float
    year_to_date: float
    one_year: float

class StockMarketCap(BaseModel):
    currency: str
    value: float

class StockCompetitors(BaseModel):
    name: str
    market_cap: StockMarketCap

class StockMarket(BaseModel):
    status: str
    purchased_amount: float
    purchased_status: str
    request_data: datetime
    company_code: str
    company_name: str
    values: StockValues
    performance_data: StockPerformance
    competitors: List[StockCompetitors]