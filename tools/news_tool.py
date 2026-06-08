from langchain_core.tools import tool

from data.news import get_news


@tool
def search_news(query: str):

    """
    Search financial news.
    """

    result = get_news(
        query=query
    )

    return result