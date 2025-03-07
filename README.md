# Agno Tuts

## Links
[Agno Docs](https://docs.agno.com/get-started/agents)
[GitHub](https://github.com/agno-agi/agno)

## Dependencies

- pipenv
- python 3.12

- agno
- lancedb
- tantivy
- pypdf
- duckduckgo-search
- yfinance

## Agent

```py
groq_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", temperature=0.6),
    instructions=dedent(
        "create 5 articles about what is currently happening in specified place, make sure to output each article in its own paragraph"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    telemetry=False,
    markdown=True,
    stream=False
    )
```
