# WSB Sentinel Agent

A modern, clean backend foundation for AI-agent development, focused on Reddit WallStreetBets data ingestion.

## Overview

This project provides a minimal, well-structured backend skeleton designed to be extended with AI-agent capabilities. It currently includes clean data ingestion utilities for fetching Reddit WSB posts and comments, with a modular architecture ready for future enhancements.

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
│       ├── data_fetchers/          # External API clients
│       │   ├── __init__.py
│       │   └── reddit_fetcher.py
│       ├── models/                 # Data models
│       │   ├── __init__.py
│       │   └── reddit.py
│       └── utils/                  # Utility functions
│           ├── __init__.py
│           └── reddit_utils.py
├── tests/                          # Test directory (empty for now)
├── main.py                         # Root entry point
├── pyproject.toml                  # Project configuration (uv)
├── Dockerfile                      # Minimal production Dockerfile
└── README.md
```

## Features

- **Reddit WSB Data Fetching**: Fetch top posts from r/wallstreetbets
- **Optional Comment Fetching**: Configurable comment retrieval per post
- **Clean Architecture**: Modular design with clear separation of concerns
- **Type Safety**: Pydantic models for data validation
- **Async/Await**: Modern async patterns with aiohttp
- **Configuration Management**: Centralized settings with environment variable support

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
   git clone <repository-url>
   cd wsb-sentinel-agent
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

## Usage

### Basic Usage

Run the main script to fetch and display top Reddit posts:

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
uv run black src/
```

### Linting

```bash
uv run ruff check src/
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
- **Minimal Dependencies**: Only essential packages (aiohttp, pydantic)

## Future Enhancements

This foundation is designed to be extended with:
- AI-agent modules
- Additional data sources
- Data processing pipelines
- API endpoints
- Database integration

## License

[Add your license here]
