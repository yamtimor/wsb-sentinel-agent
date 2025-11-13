"""Main entry point for WSB Sentinel Agent."""

import asyncio
from wsb_sentinel_agent.data_fetchers import fetch_reddit_posts, fetch_post_comments
from wsb_sentinel_agent.config.settings import Settings
from wsb_sentinel_agent.utils import extract_tickers_from_text


async def main():
    """Main function to demonstrate Reddit data fetching."""
    print("Fetching top Reddit posts from r/wallstreetbets...")
    posts = await fetch_reddit_posts()
    print(f"Fetched {len(posts)} posts\n")

    # Display top posts
    print("--- Top Posts ---")
    for i, post in enumerate(posts[:10], 1):
        print(f"{i}. [{post.score}↑] {post.title[:80]}")
        if post.url:
            print(f"   URL: {post.url}")
        print()

    # Optionally fetch comments if enabled
    if Settings.FETCH_COMMENTS and posts:
        print("\n--- Fetching Comments for Top Post ---")
        top_post = posts[0]
        if top_post.post_id:
            comments = await fetch_post_comments(top_post.post_id)
            print(f"Fetched {len(comments)} comments for: {top_post.title[:60]}...")
            for i, comment in enumerate(comments[:5], 1):
                print(f"\n{i}. [{comment.score}↑] {comment.body[:100]}...")

    # Demonstrate ticker extraction
    print("\n--- Ticker Extraction Example ---")
    if posts:
        sample_post = posts[0]
        tickers = extract_tickers_from_text(sample_post.title)
        if tickers:
            print(f"Post: {sample_post.title[:80]}")
            print(f"Potential tickers: {', '.join(set(tickers))}")
        else:
            print("No tickers detected in top post title")


if __name__ == "__main__":
    asyncio.run(main())

