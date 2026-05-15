from crewai import Task

from agents import finder

finder_task = Task(
    description="""Find the exact past paper this exam question is from:

                {question_text}

                Search for the exact wording. Verify numbers and structure match exactly.
                If no strong match found, return UNKNOWN.
                """,
    expected_output="One line only: Year, Month, Subject, Unit, Exam Board. Or: UNKNOWN",
    agent=finder,
)