from langchain import OpenAI, LLMMathChain, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
import os
import chainlit as cl

os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "70035b12a2500be93964ae7a61a2bfe4a1d98b09f651963376b6c7ae84a9db9d"


# The search tool has no async implementation, we fall back to sync
@cl.langchain_factory(use_async=False)
def load():
    llm = ChatOpenAI(temperature=0, streaming=True)
    llm1 = OpenAI(temperature=0, streaming=True)
    search = SerpAPIWrapper()
    llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="useful for when you need to answer questions about current events. You should ask targeted questions",
        ),
        Tool(
            name="Calculator",
            func=llm_math_chain.run,
            description="useful for when you need to answer questions about math",
        ),
    ]
    return initialize_agent(
        tools, llm1, agent="chat-zero-shot-react-description", verbose=True
    )
