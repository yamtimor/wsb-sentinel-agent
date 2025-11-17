"""Reddit data fetcher for r/wallstreetbets."""

import aiohttp
import logging
from typing import List, Optional

from wsb_sentinel_agent.models.reddit import RedditPost, RedditComment
from wsb_sentinel_agent.config.settings import Settings

logger = logging.getLogger(__name__)


async def fetch_reddit_posts() -> List[RedditPost]:
    """
    Fetch top posts from r/wallstreetbets.

    Returns:
        List of RedditPost models representing the top posts.
    """
    url = Settings.get_reddit_posts_url()
    headers = Settings.get_headers()

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            if response.status != 200:
                text = await response.text()
                logger.error(
                    f"Reddit API error fetching posts - Status {response.status}: {text[:200]}"
                )
                raise Exception(
                    f"Reddit API error - Status {response.status}: {text[:200]}"
                )

            data = await response.json()
            posts = data.get("data", {}).get("children", [])
            results = []

            for post in posts:
                post_data = post.get("data", {})
                # Extract post ID from permalink or fullname
                post_id = post_data.get("id")
                permalink = post_data.get("permalink", "")
                if permalink and not post_id:
                    # Extract ID from permalink like "/r/wallstreetbets/comments/abc123/..."
                    parts = permalink.strip("/").split("/")
                    if len(parts) >= 4 and parts[2] == "comments":
                        post_id = parts[3]

                results.append(
                    RedditPost(
                        title=post_data.get("title", ""),
                        score=post_data.get("score", 0),
                        created_utc=post_data.get("created_utc", 0.0),
                        url=post_data.get("url"),
                        author=post_data.get("author"),
                        num_comments=post_data.get("num_comments", 0),
                        post_id=post_id,
                        permalink=permalink,
                    )
                )

            return results


async def fetch_post_comments(post_id: str, limit: Optional[int] = None) -> List[RedditComment]:
    """
    Fetch top-level comments for a specific Reddit post.

    Args:
        post_id: The Reddit post ID (without the 't3_' prefix)
        limit: Maximum number of comments to fetch (defaults to Settings.MAX_COMMENTS_PER_POST)

    Returns:
        List of RedditComment models representing the top comments.
    """
    if limit is None:
        limit = Settings.MAX_COMMENTS_PER_POST

    url = Settings.get_reddit_comments_url(post_id)
    headers = Settings.get_headers()

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            if response.status != 200:
                text = await response.text()
                logger.error(
                    f"Reddit API error fetching comments for post {post_id} - "
                    f"Status {response.status}: {text[:200]}"
                )
                raise Exception(
                    f"Reddit API error - Status {response.status}: {text[:200]}"
                )

            data = await response.json()
            # Reddit comments API returns a list: [post_data, comments_data]
            if len(data) < 2:
                return []

            comments_data = data[1].get("data", {}).get("children", [])
            results = []

            for comment_item in comments_data[:limit]:
                # Skip "more" objects and non-comment items
                if comment_item.get("kind") != "t1":
                    continue

                comment_data = comment_item.get("data", {})
                # Only fetch top-level comments (no parent_id or parent starts with 't3_')
                parent_id = comment_data.get("parent_id", "")
                if parent_id and not parent_id.startswith("t3_"):
                    continue

                results.append(
                    RedditComment(
                        body=comment_data.get("body", ""),
                        score=comment_data.get("score", 0),
                        created_utc=comment_data.get("created_utc", 0.0),
                        author=comment_data.get("author"),
                        comment_id=comment_data.get("id"),
                    )
                )

            return results

