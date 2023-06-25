import os
from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl

os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "70035b12a2500be93964ae7a61a2bfe4a1d98b09f651963376b6c7ae84a9db9d"

template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

    return llm_chain
