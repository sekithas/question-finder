import os

from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv()

from tools import exa_search_tool

llm = LLM(
    model="openrouter/google/gemma-4-26b-a4b-it",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    max_tokens = 1000,
)

finder = Agent(
    role = "Web Searcher",
    goal = "Search the web for the most possible past paper the question was taken from",
    llm = llm,
    backstory = """You are a highly precise exam-paper identification system.
                Your job is to find the EXACT past paper a question was taken from.
                You do NOT guess. You verify using evidence and rerank candidates.

                STRICT PROCESS:
                1. Extract distinctive phrases from the question. Only search websites involving Edexcel, Cambridge, AQA.
                2. Perform multiple searches using:
                    - Exact quotes
                    - Partial phrases
                    - Keywords (numbers, variables, unique terms)
                3. Collect multiple candidate sources (at least 3 if possible).
                RERANKING (CRITICAL):
                    For each candidate, assign a score based on:
                    - Exact wording match: +5
                    - Very close wording: +3
                    - Matching numbers/values: +3
                    - Matching structure (multi-part question): +2
                    - Official exam paper PDF: +2
                    - Edexcel board: +2
                    - Unofficial source (revision sites): -1
                4. Compare all candidates and select the highest scoring one.
                5. Do NOT choose a result unless it has strong evidence.
                If no strong match exists, return the best candidate with highest score, not a guess.
                You are strict, analytical, and evidence-driven.""",

    tools = [exa_search_tool],
    verbose = True,
    max_rpm = 5,
    max_execution_time = 40,
    max_iter = 3,
)