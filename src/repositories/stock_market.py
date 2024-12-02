from src.infra.repository import Repository
from src.models.stock_market import StockMarket
from src.schemas.stock_market import StockMarketDTO
import uuid

class StockMarketRepository(Repository):
    def __init__(self):
        self.data = {}

    def store(self, stock_market: StockMarket):
        self.data[uuid.uuid4().hex] = stock_market

    def update(self, stock_id: str, stock_amount: StockMarketDTO):
        self.data[stock_id].purchased_amount = stock_amount.purchased_amount
    
    def get(self, stock_id: str):
        return self.data[stock_id]
