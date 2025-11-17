class WSBSentimentAgent:
    """
    Agent 1:
    Fetch top WSB sentiment data and prepare it for later correlation.
    """

    def __init__(self, logger=None):
        self.logger = logger

    async def run(self, date=None):
        """
        Entrypoint for the agent.
        """
        raise NotImplementedError("Agent logic will be implemented step by step.")
