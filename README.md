Smart Resume Analyzer (Multi-Agent ADK System)
Overview
Smart Resume Analyzer is a multi-agent system built using Google ADK that analyzes a candidate’s resume against a job description (JD).
It extracts keywords, compares skills, computes a match score, and highlights missing skills to improve resume alignment.

Architecture
Root Agent:

resume_analyzer_root → orchestrates workflow
Sub-Agents:

resume_parser_agent → extracts resume keywords
jd_parser_agent → extracts job description keywords
matcher_agent → computes match score & missing skills
report_agent → generates final analysis report
Custom Tools:

extract_text → reads resume/JD text
keyword_tools → extracts keywords
match_score → calculates match percentage
Setup
Create virtual environment and install dependencies:

pip install -r requirements.txt
Create .env file in project root:

GOOGLE_API_KEY=your_api_key_here
Run
From project root:

adk run .
Example Usage
User input:

Compare resume skills python sql excel tableau 
with job skills python sql powerbi statistics machine learning
Output:

Match Score: 40%
Missing Keywords: powerbi, statistics, machine learning
Problem Solved
✔ Resume–JD skill comparison
✔ Keyword gap identification
✔ Resume optimization insights
✔ Multi-agent orchestration using ADK

Tech Stack
Python
Google ADK
Gemini Flash model
Custom keyword & scoring tools
Author
Harshit Chhabra
