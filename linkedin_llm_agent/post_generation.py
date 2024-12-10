from swarm import Agent

from .prompts import content_writer_agent_prompt, content_evaluator_agent_prompt
from .prompts import skeleton_writer_agent_prompt, reviewer_agent_prompt
from .tools.web_search import web_search

model = "gpt-4o-mini"

skeleton_writer_agent = Agent(
    name="Skeleton Writer Agent",
    model=model,
    instructions=skeleton_writer_agent_prompt
)

reviewer_agent = Agent(
    name="Reviewer Agent",
    model=model,
    instructions=reviewer_agent_prompt
)

content_writer_agent = Agent(
    name="Content Writer Agent",
    model=model,
    instructions=content_writer_agent_prompt
)

content_evaluator_agent = Agent(
    name="Content Evaluator Agent",
    model=model,
    instructions=content_evaluator_agent_prompt
)

def transfer_to_skeleton_writer_agent():
    return skeleton_writer_agent

def transfer_to_reviewer_agent():
    return reviewer_agent

def transfer_to_content_writer_agent():
    return content_writer_agent

def transfer_to_content_evaluator_agent():
    return content_evaluator_agent

skeleton_writer_agent.functions=[transfer_to_reviewer_agent, web_search, transfer_to_content_writer_agent]
reviewer_agent.functions = [transfer_to_skeleton_writer_agent]

content_writer_agent.functions=[transfer_to_content_evaluator_agent]
content_evaluator_agent.functions=[transfer_to_content_writer_agent]