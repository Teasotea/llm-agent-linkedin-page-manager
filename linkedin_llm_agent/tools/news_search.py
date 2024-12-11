import os
from newsapi import NewsApiClient

NEWSAPI_API_KEY = os.environ['NEWSAPI_API_KEY']
newsapi = NewsApiClient(api_key=NEWSAPI_API_KEY)

def news_search(query: str, category: str) -> str:
    """
    Searches for news articles based on the given query and category.

    Args:
        query (str): The search query string.
        category (str): The news category. Possible options include
            'business', 'entertainment', 'general', 'health', 'science', 'sports', or 'technology'.

    Returns:
        str: A string containing the retrieved news articles.
    """
    return newsapi.get_everything(q=query, category=category)