from google.adk.agents import Agent
from tools.scoring import match_score

matcher_agent = Agent(
    name="matcher",
    description="Compute match between resume and job keywords.",
    tools=[match_score],
)
