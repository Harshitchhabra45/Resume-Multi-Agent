from google.adk.agents import Agent
from tools.extract_text import extract_pdf_text
from tools.keyword_tools import extract_keywords

resume_parser_agent = Agent(
    name="resume_parser",
    model="gemini-flash-latest"
,
    description="Extract resume text and derive keywords.",
    tools=[extract_pdf_text, extract_keywords],
)
