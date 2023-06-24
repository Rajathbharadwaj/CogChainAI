import os
import time
from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl

# read text from file: ../../OPENAI_API.txt
with open("../../OPENAI_API.txt", "r") as f:
    API_KEY = f.read().strip()

os.environ["OPENAI_API_KEY"] = API_KEY

template = """You are a companion to the user who wants to commit to doing somethig. It will be discussed in the next message with the user. You should provide a plan for the user to follow and take the reports from the user on the progress. You should also provide the user with the motivation to continue. In the review, you should add text 'performance: good/bad ' to the message. Also, focus that the user should not be distracted from the goal. and is not lying about the progress. User will report with 'Update: text'."""
prompt_template = template


@cl.action_callback("action_button")
async def on_action(action):
    await cl.Message(content=f"Executed {action.name}").send()
    # Optionally remove the action button from the chatbot user interface
    await action.remove()


@cl.on_message
async def main(message: str):
    # Your custom logic goes here...

    # ping google.com using os
    response = os.system("ping www.google.com")
    # and then check the response...
    if response == 0:
        txt_ = "Internet connection is up"
    else:
        txt_ = "Internet connection is down"

    # Create a new chain

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {txt_}",
    ).send()
