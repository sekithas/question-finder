import os

from crewai_tools import EXASearchTool
from dotenv import load_dotenv

load_dotenv()

os.environ["EXA_API_KEY"] = os.getenv("EXA_API_KEY")

exa_search_tool = EXASearchTool(
    num_results=3,
    include_text=False,
    use_autoprompt=True,
)