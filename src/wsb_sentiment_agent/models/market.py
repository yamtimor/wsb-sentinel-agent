"""Market data models."""

from pydantic import BaseModel
from datetime import datetime


class OhlcBar(BaseModel):
    """Model representing an OHLC (Open, High, Low, Close) bar for market data."""

    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int
    symbol: str

    class Config:
        """Pydantic configuration."""

        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
