from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.tools import DuckDuckGoSearchRun

llm = ChatOpenAI(model="gpt-4o-mini")

search = DuckDuckGoSearchRun()

tools = [
    Tool(name="Search", func=search.run, description="Search internet")
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

print(agent.run("Latest AI news"))
