import os
from tavily import TavilyClient

TAVILY_API_KEY = os.environ['TAVILY_API_KEY']
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def web_search(query: str) -> str:
    """
    Searches the web for a given query and returns the title and content of the top result.

    Args:
        query (str): The search query string.

    Returns:
        str: A formatted string containing the title and content of the top search result.
    """
    response = tavily_client.search(query)
    return response["results"][0]["title"] + ":\n" + response["results"][0]["content"]