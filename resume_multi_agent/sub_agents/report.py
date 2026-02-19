from google.adk.agents import Agent
from google.adk.tools import google_search

report_agent = Agent(
    name="reporter",
    model="gemini-flash-latest",
    description="Generate resume match report and improvement suggestions",
    tools=[google_search],
)
