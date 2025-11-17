# WSB Sentinel Agent

A backend foundation for an AI-driven "sentinel" that monitors WallStreetBets crowd behavior and market regime data (SPY & VIX). This project provides the data layer that will power future AI Agent analysis of WSB sentiment versus market volatility regimes.

## Overview

**wsb-sentinel-agent** is a backend and data layer that fetches Reddit WallStreetBets activity and basic market data (SPY & VIX). In later phases, this will power an AI Agent that analyzes crowd sentiment versus market volatility regimes.

### Current Implementation

- **Reddit WSB Data Fetching**: Fetch top posts from r/wallstreetbets with optional comment retrieval
- **Market Data Fetching**: Fetch historical OHLC data for SPY (S&P 500 ETF) and VIX (Volatility Index) using yfinance
- **Data Models**: Pydantic models for Reddit posts/comments and market OHLC bars
- **Basic Utilities**: Ticker extraction from text, simple return calculations, VIX trend detection

### Future Implementation

- **AI Agent Layer**: LLM-powered analysis that interprets WSB sentiment vs SPY/VIX regime
- **Market Regime Analysis**: Advanced metrics and classification of market conditions
- **Sentiment Analysis**: Integration of WSB crowd sentiment with market context

## Project Structure

```
wsb-sentinel-agent/
├── src/
│   └── wsb_sentinel_agent/
│       ├── __init__.py
│       ├── main.py                 # Main entry point
│       ├── config/                 # Configuration module
│       │   ├── __init__.py
│       │   └── settings.py
│       ├── data_fetchers/          # External data fetching
│       │   ├── __init__.py
│       │   ├── reddit_fetcher.py   # Reddit WSB data
│       │   └── market_fetcher.py   # SPY/VIX market data
│       ├── models/                 # Data models
│       │   ├── __init__.py
│       │   ├── reddit.py           # RedditPost, RedditComment
│       │   └── market.py           # OhlcBar
│       └── utils/                  # Utility functions
│           ├── __init__.py
│           ├── reddit_utils.py     # Ticker extraction
│           └── market_utils.py     # Return calc, trend detection
├── tests/                          # Unit tests
├── main.py                         # Root entry point
├── pyproject.toml                  # Project configuration (uv)
├── Dockerfile                      # Minimal production Dockerfile
└── README.md
```

### Future Modules (Not Yet Implemented)

- `agent/` - AI Agent reasoning layer
- `analysis/` - Advanced market regime analysis
- `api/` - REST API endpoints (if needed)

## Features

- **Reddit WSB Data Fetching**: Fetch top posts from r/wallstreetbets
- **Optional Comment Fetching**: Configurable comment retrieval per post
- **Market Data**: Fetch SPY and VIX historical OHLC data
- **Clean Architecture**: Modular design with clear separation of concerns
- **Type Safety**: Pydantic models for data validation
- **Async/Await**: Modern async patterns with aiohttp and yfinance
- **Configuration Management**: Centralized settings with environment variable support
- **Logging**: Professional logging setup for diagnostics

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager

## Installation

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/yamtimor/wsb-sentinel-agent.git
   cd wsb-sentinel-agent
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

## Usage

### Basic Usage

Run the main script to fetch and display Reddit posts and market data:

```bash
uv run python main.py
```

### Fetching Reddit Posts

```python
from wsb_sentinel_agent.data_fetchers import fetch_reddit_posts

posts = await fetch_reddit_posts()
for post in posts:
    print(f"{post.title} - Score: {post.score}")
```

### Fetching Comments

```python
from wsb_sentinel_agent.data_fetchers import fetch_post_comments

comments = await fetch_post_comments(post_id="abc123", limit=10)
for comment in comments:
    print(f"{comment.body} - Score: {comment.score}")
```

### Fetching Market Data

```python
from wsb_sentinel_agent.data_fetchers import fetch_spy_history, fetch_vix_history
from wsb_sentinel_agent.utils import calculate_return, get_vix_trend

# Fetch SPY data
spy_bars = await fetch_spy_history(days=30)
spy_return = calculate_return(spy_bars)
print(f"SPY 30d return: {spy_return * 100:.2f}%")

# Fetch VIX data
vix_bars = await fetch_vix_history(days=30)
vix_trend = get_vix_trend(vix_bars)
print(f"VIX trend: {vix_trend}")
```

### Configuration

Configure behavior via environment variables:

- `FETCH_COMMENTS`: Set to `"true"` to enable comment fetching (default: `false`)
- `MAX_COMMENTS_PER_POST`: Maximum comments to fetch per post (default: `10`)

Or modify `src/wsb_sentinel_agent/config/settings.py` directly.

## Development

### Running Tests

```bash
uv run pytest
```

### Code Formatting

```bash
uv run black src/ tests/
```

### Linting

```bash
uv run ruff check src/ tests/
```

## Docker

Build and run with Docker:

```bash
docker build -t wsb-sentinel-agent .
docker run wsb-sentinel-agent
```

## Architecture Decisions

- **Package Structure**: Uses `src/` layout for better import clarity
- **Models**: Pydantic BaseModel for type safety and validation
- **Data Fetchers**: Async/await pattern with proper error handling
- **Configuration**: Centralized in config module, environment-aware
- **Minimal Dependencies**: Only essential packages (aiohttp, pydantic, yfinance, pandas)
- **Logging**: Structured logging for diagnostics and monitoring

## Roadmap

### Phase 1: Backend + Data (Current)
- ✅ Reddit WSB data fetching (posts, comments)
- ✅ Market data fetching (SPY, VIX)
- ✅ Basic data models and utilities
- ✅ Logging and code quality improvements

### Phase 2: Market Regime Analysis & Metrics
- Market regime classification (low vol, high vol, trending, etc.)
- Advanced metrics and indicators
- Correlation analysis between WSB activity and market movements

### Phase 3: AI Agent / LLM Reasoning Layer
- LLM integration for sentiment analysis
- AI-powered interpretation of WSB crowd behavior vs market regime
- Decision support and alerting capabilities

## License

[Add your license here]
