from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from swarm import Swarm

from linkedin_llm_agent.post_generation import skeleton_writer_agent

client = Swarm()
STARTING_AGENT = skeleton_writer_agent

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

if "agent" not in st.session_state:
    st.session_state.agent = STARTING_AGENT

def display_assistant_message(message):
    with st.chat_message(message["role"]):
        st.subheader(message["sender"])
        st.markdown(message["content"])

        if message["tool_calls"] is not None:
            for tool_call in message["tool_calls"]:
                with st.expander(f"🔧 Tool Call: {tool_call['function']['name']}"):
                    st.code(tool_call['function']['arguments'], language="json")

def display_tool_message(message):
    with st.chat_message(message["role"], avatar="🔧"):
        with st.expander("Tool Output: " + message["tool_name"]):
            st.markdown(message["content"])

def display_user_message(message):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def display_error_message(message):
    with st.chat_message("ERROR"):
        st.markdown("Unknown sender with the message content:\n" + message["content"])

def display_message(message):
    if message["role"] == "assistant":
        display_assistant_message(message)
    elif message["role"] == "tool":
        display_tool_message(message)
    elif message["role"] == "user":
        display_user_message(message)
    else:
        display_error_message(message)

# Function to run the agent
def run_agent(user_prompt):
    history = st.session_state.history
    response = client.run(
        agent=st.session_state.agent,
        messages=history,
    )
    return response

def add_response_to_history(response):
    for message in response.messages:
        st.session_state.history.append(message)
        display_message(message)

st.title("Chat with Agentify!")

# Display chat history
for message in st.session_state.history:
    display_message(message)

# React to user input
if prompt := st.chat_input():
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.history.append({"role": "user", "content": prompt})

    response = run_agent(prompt)
    st.session_state.agent = response.agent
    add_response_to_history(response)