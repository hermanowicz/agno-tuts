from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

groq_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True)


run: RunResponse = groq_agent.run("Tell me about a breaking news story from New York.")
print(run.content)

# agent = Agent(
#     model=OpenAIChat(id="gpt-4o"),
#     description="You are an enthusiastic news reporter with a flair for storytelling!",
#     tools=[DuckDuckGoTools()],
#     show_tool_calls=True,
#     markdown=True
# )

# print direct to console
#  ---------------------
# agent.print_response(
#     "Tell me about a breaking news story from New York.", stream=True)
