"""Market data fetcher using yfinance."""

import asyncio
import logging
from typing import List
from datetime import datetime, timedelta

import yfinance as yf
import pandas as pd

from wsb_sentiment_agent.models.market import OhlcBar

logger = logging.getLogger(__name__)


async def fetch_ohlc(symbol: str, days: int = 30) -> List[OhlcBar]:
    """
    Fetch OHLC data for a given symbol.

    Args:
        symbol: Stock symbol (e.g., "SPY", "^VIX")
        days: Number of days of history to fetch

    Returns:
        List of OhlcBar models representing the OHLC data.
    """
    logger.info(f"Fetching {days} days of OHLC data for {symbol}")

    # Run yfinance in executor since it's synchronous
    loop = asyncio.get_event_loop()
    ticker = await loop.run_in_executor(None, lambda: yf.Ticker(symbol))

    # Fetch historical data
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    def _fetch_data():
        hist = ticker.history(start=start_date, end=end_date)
        return hist

    df = await loop.run_in_executor(None, _fetch_data)

    if df.empty:
        logger.warning(f"No data returned for symbol {symbol}")
        return []

    # Convert DataFrame to list of OhlcBar models
    results = []
    for timestamp, row in df.iterrows():
        # Handle both DatetimeIndex and regular datetime
        if isinstance(timestamp, pd.Timestamp):
            dt = timestamp.to_pydatetime()
        else:
            dt = timestamp

        results.append(
            OhlcBar(
                timestamp=dt,
                open=float(row["Open"]),
                high=float(row["High"]),
                low=float(row["Low"]),
                close=float(row["Close"]),
                volume=int(row["Volume"]),
                symbol=symbol,
            )
        )

    logger.info(f"Fetched {len(results)} bars for {symbol}")
    return results


async def fetch_spy_history(days: int = 30) -> List[OhlcBar]:
    """
    Fetch SPY (S&P 500 ETF) historical data.

    Args:
        days: Number of days of history to fetch

    Returns:
        List of OhlcBar models for SPY.
    """
    return await fetch_ohlc("SPY", days=days)


async def fetch_vix_history(days: int = 30) -> List[OhlcBar]:
    """
    Fetch VIX (Volatility Index) historical data.

    Args:
        days: Number of days of history to fetch

    Returns:
        List of OhlcBar models for VIX.
    """
    return await fetch_ohlc("^VIX", days=days)
