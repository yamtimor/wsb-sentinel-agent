# Minimal production Dockerfile for WSB Sentiment Agent
FROM python:3.11-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy application code
COPY src/ ./src/
COPY main.py ./

# Set Python path
ENV PYTHONPATH=/app/src

# Default command
CMD ["uv", "run", "python", "main.py"]

