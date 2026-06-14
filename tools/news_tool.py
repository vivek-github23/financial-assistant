from langchain_core.tools import tool
from data.news import get_news

@tool(description="Search financial news articles")
def search_news(query: str):
    """Search for news articles related to the query."""
    result = get_news(query=query)
    return result