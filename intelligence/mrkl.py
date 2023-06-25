from langchain import OpenAI, LLMMathChain, SerpAPIWrapper, PromptTemplate, LLMChain
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
import chainlit as cl
import os


OPENAI_API_KEY=os.environ["OPENAI_API_KEY"] 
SERPAPI_API_KEY=os.environ["SERPAPI_API_KEY"]


template = """
You are my support system in all aspects emotionally and in terms of knowledge and I want to commit to doing somethig. 
You should provide me a plan for my goals in such a way it's easier for me to take action. 
My Goal is to {goal}.
Give it as a tabular form whenever possible. Also you've follow-up and take the reports from me on my progress. 
You should also provide me with the motivation to continue and review my progess.
In the review, you should add text 'performance: good/bad' to the message based on what you feel about my progess.
Also, focus that I should not be distracted from the goal and catch me if you think I'm lying about my progress. 
I will report my updates with 'Update: text'."""

# The search tool has no async implementation, we fall back to syn

@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["goal"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

    return llm_chain
