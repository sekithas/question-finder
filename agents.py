import os

from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv()

from tools import exa_search_tool

llm = LLM(
    model="openrouter/google/gemini-3.1-flash-lite",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    max_tokens = 100,
)

finder = Agent(
    role = "Web Searcher",
    goal = "Search the web for the most possible past paper the question was taken from",
    llm = llm,
    backstory = """You identify the exact source of exam questions. You do not guess.

                PROCESS:
                1. Extract a distinctive 10-15 word phrase including numbers and variables.
                2. Search for ONLY EDEXCEL PAPERS using PhysicsAndMathsTutor, official exam PDFs, SaveMyExams.
                3. If match, return exact past paper. If no match: return UNKNOWN. No explanations. No guessing.
                """,

    tools = [exa_search_tool],
    verbose = True,
    max_rpm = 5,
    max_execution_time = 120,
    max_iter = 2,
)