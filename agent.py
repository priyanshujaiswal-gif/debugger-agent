import os
from crewai import Agent, Task, Crew, LLM


def debug(code):
    debugger = Agent(
        role="Python Debugger",
        goal="Find the bug in the code you are given",
        backstory="You read code carefully and explain exactly what is wrong.",
        llm=LLM(model="gpt-4o-mini", api_key=os.environ["OPENAI_API_KEY"]),
    )

    task = Task(
        description=f"Find the bug in this Python code and show the fix:\n\n{code}",
        expected_output="What the bug is, why it's wrong, and the corrected line.",
        agent=debugger,
    )

    return str(Crew(agents=[debugger], tasks=[task]).kickoff())
