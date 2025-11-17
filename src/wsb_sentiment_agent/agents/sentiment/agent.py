"""WSB Sentiment Agent for collecting Reddit sentiment data."""

from typing import List
from wsb_sentiment_agent.data_fetchers import fetch_reddit_posts
from wsb_sentiment_agent.models.reddit import RedditPost


class WSBSentimentAgent:
    """
    Agent 1:
    Fetch top WSB sentiment data and prepare it for later correlation.
    """

    def __init__(self, logger=None):
        self.logger = logger

    async def collect_sentiment(self) -> List[RedditPost]:
        """
        Collect sentiment data from WSB using internal Reddit fetcher.
        
        Returns:
            List[RedditPost]: Raw Reddit posts data from r/wallstreetbets
        """
        posts = await fetch_reddit_posts()
        return posts

    async def run(self, date=None) -> List[RedditPost]:
        """
        Entrypoint for the agent.
        
        Args:
            date: Optional date parameter for future use
            
        Returns:
            List[RedditPost]: Collected sentiment data
        """
        data = await self.collect_sentiment()
        return data
