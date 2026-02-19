from google.adk.agents import Agent
from tools.keyword_tools import extract_keywords

jd_parser_agent = Agent(
    name="jd_parser",
    model="gemini-flash-latest",
    description="Extract important job description keywords.",
    tools=[extract_keywords],
)
