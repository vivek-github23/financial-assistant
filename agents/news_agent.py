from tools.news_tool import search_news


def news_agent(state):

    query = state.get("news_query")

    print(f"\n📰 Searching: {query}")

    news = search_news.invoke({"query": query})

    articles = news.get("articles",[])

    print(f"Retrieved {len(articles)} articles")

    return {"news": articles}