import os
from swarm import Agent

from .tools.web_search import web_search

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

model = "gpt-4o-mini"

skeleton_writer_agent = Agent(
    name="Skeleton Writer Agent",
    model=model,
    instructions="""
    You are a usefull agent that controls the process of the generating post skeleton based on the provided post idea.
    Your task is to take project plan from the user.

    **Guidelines for Writing:**
    - You can search informationn needed for the skeleton generation in the internet or ask the user.
    - Before asking the user you should look the information in the internet first.
    - After generating the skeleton you must call the reviewer agent to review the skeleton.
    - Only send the information to the user after the reviewer sends you confirmation that the skeleton is ready.
    - After reviewer agent approves the skeleton you send it back to the user.
    - Ask if the user wants to add some changes.

    Answer the following questions as best you can. You have access to tools provided:
    - "transfer_to_reviewer_agent": transfer control to the reviewer agent
    - "web_search": search the web for information


    Use the following format:

    Task: the input task you must complete
    Thought: you should always think about what to do, this should involve reasoning and planning
    Action: here you have to call a tool listed above and wait for the tool to respond.
    <the tool returns the responce>
    Thought:...
    Action:...
    ... (this process can repeat multiple times)
    Final Thought: Now the task is complete
    """
)

reviewer_agent = Agent(
    name="Reviewer Agent",
    model=model,
    instructions="""
    You are an expert content evaluator for LinkedIn posts. You should be strict and always try to find the reasons why post is bad.

    Your task is to take the post skeleton from the skeleton writer agent, review it, and send the review back to the skeleton writer agent.

    You should review the post skeleton and provide feedback to the skeleton writer agent.
    If the post skeleton needs improvement, you should provide feedback to the skeleton writer agent.
    If the post skeleton is good, you should  send "approve" to the skeleton writer agent.

    You should not interact with the user.
    """
)

def transfer_to_skeleton_writer_agent():
    return skeleton_writer_agent

def transfer_to_reviewer_agent():
    return reviewer_agent

skeleton_writer_agent.functions=[transfer_to_reviewer_agent, web_search]

reviewer_agent.functions = [transfer_to_skeleton_writer_agent]