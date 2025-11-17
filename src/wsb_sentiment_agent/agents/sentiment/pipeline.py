import asyncio
from .agent import WSBSentimentAgent

async def main():
    agent = WSBSentimentAgent()
    await agent.run(date=None)

if __name__ == "__main__":
    asyncio.run(main())
