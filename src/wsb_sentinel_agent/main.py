"""Main entry point for WSB Sentinel Agent."""

import asyncio
import logging
from wsb_sentinel_agent.data_fetchers import (
    fetch_reddit_posts,
    fetch_post_comments,
    fetch_spy_history,
    fetch_vix_history,
)
from wsb_sentinel_agent.config.settings import Settings
from wsb_sentinel_agent.utils import extract_tickers_from_text, calculate_return, get_vix_trend

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


async def main():
    """Main function to demonstrate Reddit data fetching."""
    logger.info("Starting WSB Sentinel Agent data fetch")
    print("Fetching top Reddit posts from r/wallstreetbets...")
    posts = await fetch_reddit_posts()
    logger.info(f"Successfully fetched {len(posts)} posts from Reddit")
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
        logger.info("Comment fetching enabled, fetching comments for top post")
        print("\n--- Fetching Comments for Top Post ---")
        top_post = posts[0]
        if top_post.post_id:
            comments = await fetch_post_comments(top_post.post_id)
            logger.info(f"Fetched {len(comments)} comments for post: {top_post.post_id}")
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

    # Fetch and display market data
    print("\n--- Market Data (SPY & VIX) ---")
    logger.info("Fetching market data for SPY and VIX")
    
    try:
        days = 10
        spy_bars = await fetch_spy_history(days=days)
        vix_bars = await fetch_vix_history(days=days)
        
        if spy_bars:
            spy_return = calculate_return(spy_bars)
            spy_return_pct = spy_return * 100
            print(f"SPY last {days}d return: {spy_return_pct:.2f}%")
            print(f"SPY current close: ${spy_bars[-1].close:.2f}")
            logger.info(f"SPY {days}d return: {spy_return_pct:.2f}%")
        else:
            print("No SPY data available")
            logger.warning("No SPY data returned")
        
        if vix_bars:
            vix_trend = get_vix_trend(vix_bars)
            latest_vix = vix_bars[-1].close
            print(f"VIX current level: {latest_vix:.2f}")
            print(f"VIX trend (last {days}d): {vix_trend}")
            logger.info(f"VIX level: {latest_vix:.2f}, trend: {vix_trend}")
        else:
            print("No VIX data available")
            logger.warning("No VIX data returned")
    except Exception as e:
        logger.error(f"Error fetching market data: {str(e)}", exc_info=True)
        print(f"Error fetching market data: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())

