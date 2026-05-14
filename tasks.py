from crewai import Task

from agents import finder

finder_task = Task(
    description = """You are given the following exam question:
                    {question_text}
                    Steps you MUST follow:
                        1. Extract key phrases from the question.
                        2. Search using multiple query variations.
                        3. Collect at least 3 candidate sources.
                        4. For each candidate:
                        - Compare wording, numbers, and structure
                        - Assign a score based on the scoring rules
                        5. Select the candidate with the highest score.
                    """,
    expected_output = """Output ONLY the final answer in this format:
                    (Year), (Month), (Subject), (Unit), (Certificate), (Examination Board)
                Example:
                    2019 June Physics Unit 2 IAL, Edexcel
                    """,
    agent = finder,
)