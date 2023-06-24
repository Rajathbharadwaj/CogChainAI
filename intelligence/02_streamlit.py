import os
import streamlit as st

from langchain.chains import ConversationChain
from langchain.llms import OpenAI

# Load the API key from a file
with open("../../OPENAI_API.txt", "r") as f:
    API_KEY = f.read().strip()

os.environ["OPENAI_API_KEY"] = API_KEY

def load_chain():
    """Logic for loading the chain you want to use should go here."""
    llm = OpenAI(temperature=0)
    chain = ConversationChain(llm=llm)
    return chain

chain = load_chain()

# Streamlit UI setup
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

# Initialize conversation history in session_state if not already present
if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = []

# Text input for user message
user_input = st.text_input("You: ", key="user_input")

# Button to send message
send_button = st.button("Send")

# Handle conversation when send button is pressed
if send_button:
    # Run the chain to get the response from the AI agent
    output = chain.run(input=user_input)
    
    # Append user message and AI response to conversation history
    st.session_state["conversation_history"].append(("You: ", user_input))
    st.session_state["conversation_history"].append(("AI: ", output))

    # Clear the text input for the next message
    st.session_state["user_input"] = ""

# Display the conversation history
for sender, message in st.session_state["conversation_history"]:
    st.markdown(f"**{sender}** {message}")
