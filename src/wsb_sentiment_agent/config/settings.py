"""Application settings and configuration."""

import os
from typing import Optional


class Settings:
    """Application configuration settings."""

    # Reddit API Configuration
    REDDIT_BASE_URL: str = "https://www.reddit.com"
    REDDIT_SUBREDDIT: str = "wallstreetbets"
    REDDIT_POST_LIMIT: int = 50
    REDDIT_TIME_FILTER: str = "day"  # hour, day, week, month, year, all
    REDDIT_USER_AGENT: str = "wsb-sentiment-agent/0.1.0 by wsb-sentiment-agent"

    # Optional: Fetch comments for posts
    FETCH_COMMENTS: bool = os.getenv("FETCH_COMMENTS", "false").lower() == "true"
    MAX_COMMENTS_PER_POST: int = int(os.getenv("MAX_COMMENTS_PER_POST", "10"))

    @classmethod
    def get_reddit_posts_url(cls) -> str:
        """Get the URL for fetching top Reddit posts."""
        return (
            f"{cls.REDDIT_BASE_URL}/r/{cls.REDDIT_SUBREDDIT}/top.json"
            f"?limit={cls.REDDIT_POST_LIMIT}&t={cls.REDDIT_TIME_FILTER}"
        )

    @classmethod
    def get_reddit_comments_url(cls, post_id: str) -> str:
        """Get the URL for fetching comments for a specific post."""
        return (
            f"{cls.REDDIT_BASE_URL}/r/{cls.REDDIT_SUBREDDIT}/comments/{post_id}.json"
        )

    @classmethod
    def get_headers(cls) -> dict:
        """Get HTTP headers for Reddit API requests."""
        return {"User-Agent": cls.REDDIT_USER_AGENT}

