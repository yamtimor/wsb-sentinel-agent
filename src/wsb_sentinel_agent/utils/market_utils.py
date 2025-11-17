"""Utility functions for processing market data."""

from typing import List
from wsb_sentinel_agent.models.market import OhlcBar


def calculate_return(bars: List[OhlcBar]) -> float:
    """
    Calculate simple return from first to last close price.

    Args:
        bars: List of OhlcBar models, sorted by timestamp (oldest first)

    Returns:
        Return as a decimal (e.g., 0.05 for 5% return)
    """
    if not bars or len(bars) < 2:
        return 0.0

    first_close = bars[0].close
    last_close = bars[-1].close

    if first_close == 0:
        return 0.0

    return (last_close - first_close) / first_close


def get_vix_trend(bars: List[OhlcBar]) -> str:
    """
    Determine if VIX is rising or falling based on first vs last close.

    Args:
        bars: List of OhlcBar models, sorted by timestamp (oldest first)

    Returns:
        "rising" if last close > first close, "falling" otherwise
    """
    if not bars or len(bars) < 2:
        return "unknown"

    first_close = bars[0].close
    last_close = bars[-1].close

    if last_close > first_close:
        return "rising"
    else:
        return "falling"
