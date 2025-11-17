"""Utility functions for processing Reddit data."""

import re
from typing import List

# Pattern to detect potential stock tickers (2-5 uppercase letters)
TICKER_PATTERN = r"\b[A-Z]{2,5}\b"


def extract_tickers_from_text(text: str) -> List[str]:
    """
    Extract potential stock tickers from text.

    This is a simple pattern-based extraction that finds uppercase words
    of 2-5 characters. It may produce false positives.

    Args:
        text: The text to search for tickers.

    Returns:
        List of potential ticker symbols found in the text.
    """
    return re.findall(TICKER_PATTERN, text)

