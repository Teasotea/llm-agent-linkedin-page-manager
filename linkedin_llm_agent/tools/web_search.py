import os
from tavily import TavilyClient

TAVILY_API_KEY = os.environ['TAVILY_API_KEY']
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def web_search(query: str) -> str:
    response = tavily_client.search(query)
    return response["results"][0]["title"] + ":\n" + response["results"][0]["content"]