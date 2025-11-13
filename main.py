"""Root entry point - delegates to package main."""

from wsb_sentinel_agent.main import main
import asyncio

if __name__ == "__main__":
    asyncio.run(main())