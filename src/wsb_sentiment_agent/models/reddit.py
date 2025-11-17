"""Reddit data models."""

from pydantic import BaseModel
from typing import Optional, List


class RedditPost(BaseModel):
    """Model representing a Reddit post from r/wallstreetbets."""

    title: str
    score: int
    created_utc: float  # Unix timestamp
    url: Optional[str] = None
    author: Optional[str] = None
    num_comments: Optional[int] = None
    post_id: Optional[str] = None
    permalink: Optional[str] = None


class RedditComment(BaseModel):
    """Model representing a Reddit comment."""

    body: str
    score: int
    created_utc: float  # Unix timestamp
    author: Optional[str] = None
    comment_id: Optional[str] = None

