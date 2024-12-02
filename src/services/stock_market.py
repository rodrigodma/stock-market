from src.repositories.stock_market import StockMarketRepository
from src.models.stock_market import StockMarket
from src.schemas.stock_market import StockMarketDTO


class StockMarketService():

    def __init__(self):
        self.repository = StockMarketRepository()

    def update(self, stock_id: str, stock_market: StockMarketDTO):
        self.repository.update(stock_id, stock_market)
    
    def get(self, stock_id: str):
        return self.repository.get(stock_id)
        