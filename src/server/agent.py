from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import initialize_agent, AgentType

from src.server.tools import search_tool

def create_agent(model: str,api_key: str,):
    llm = ChatGoogleGenerativeAI(
        model=model,
        api_key=api_key
    )

    agent = initialize_agent(
        llm=llm,
        tools=[search_tool],
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True

    )

    return agent
