"""Pipeline entrypoint for WSB Sentiment Agent."""

import asyncio
from .agent import WSBSentimentAgent


async def main():
    """Main entrypoint for the sentiment agent pipeline."""
    agent = WSBSentimentAgent()
    data = await agent.run()
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
