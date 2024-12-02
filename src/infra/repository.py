from abc import ABC, abstractmethod
from typing import Optional
from pydantic import BaseModel

class Repository(ABC):
    @abstractmethod
    def store(self, data: BaseModel):
        """Stores stock market data into the database."""
        pass

    @abstractmethod
    def update(self, id: str, data: BaseModel):
        """Updates stock market data into the database."""
        pass

    @abstractmethod
    def get(self, id: str):
        """Retrieves stock market data from the database."""
        pass
