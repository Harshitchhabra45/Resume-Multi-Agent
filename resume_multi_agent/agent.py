from google.adk.agents import Agent
from sub_agents.matcher import matcher_agent

root_agent = Agent(
    name="resume_analyzer_root",
    description="Root agent for resume matching.",
    sub_agents=[matcher_agent],
)
