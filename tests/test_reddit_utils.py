"""Tests for Reddit utility functions."""

import pytest
from wsb_sentiment_agent.utils.reddit_utils import extract_tickers_from_text


def test_extract_tickers_simple():
    """Test extracting tickers from simple text."""
    text = "I'm buying AAPL and TSLA today"
    result = extract_tickers_from_text(text)
    assert "AAPL" in result
    assert "TSLA" in result


def test_extract_tickers_multiple():
    """Test extracting multiple tickers."""
    text = "MSFT GOOGL AMZN are all great stocks"
    result = extract_tickers_from_text(text)
    assert "MSFT" in result
    assert "GOOGL" in result
    assert "AMZN" in result


def test_extract_tickers_no_tickers():
    """Test text with no tickers."""
    text = "This is just regular text with no stock symbols"
    result = extract_tickers_from_text(text)
    assert result == []


def test_extract_tickers_empty_string():
    """Test empty string."""
    result = extract_tickers_from_text("")
    assert result == []


def test_extract_tickers_case_sensitive():
    """Test that only uppercase tickers are detected."""
    text = "I like aapl but not AAPL"
    result = extract_tickers_from_text(text)
    assert "aapl" not in result
    assert "AAPL" in result


def test_extract_tickers_length_filter():
    """Test that tickers are 2-5 characters."""
    text = "A is too short, ABCDEF is too long, but TSLA is perfect"
    result = extract_tickers_from_text(text)
    assert "A" not in result
    assert "ABCDEF" not in result
    assert "TSLA" in result


def test_extract_tickers_with_punctuation():
    """Test ticker extraction with punctuation."""
    text = "Buy $AAPL and TSLA! Now."
    result = extract_tickers_from_text(text)
    assert "AAPL" in result
    assert "TSLA" in result
