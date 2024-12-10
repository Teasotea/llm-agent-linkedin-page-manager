import os
from newsapi import NewsApiClient

NEWSAPI_API_KEY = os.environ['NEWSAPI_API_KEY']
newsapi = NewsApiClient(api_key=NEWSAPI_API_KEY)

def news_search(query: str, category: str) -> str:
    """
    :param query: search query
    :param category: news category. Possible options: business, entertainment, general, health, science, sports, technology

    :return: news articles
    """
    return newsapi.get_everything(q=query, category=category)