from fastapi import FastAPI, Path, Query

from src.services.stock_market import StockMarketService
from src.schemas.stock_market import StockMarketDTO

app = FastAPI()

stock_market_service = StockMarketService()

@app.post("/stock/{stock_symbol}")
def save_stock_market(stock_symbol: str, stock_market: StockMarketDTO):
    stock_market_service.store(stock_symbol, stock_market)
    return stock_market

@app.get("/stock/{stock_symbol}")
def get_stock_market_data(stock_symbol: str):
    result = stock_market_service.get(stock_symbol)
    return result