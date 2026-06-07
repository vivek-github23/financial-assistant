from data.news import get_news

def news_agent(state):

    print("📰 News Agent")

    news_response = get_news()

    articles = news_response.get(
        "articles",
        []
    )

    print(
        f"Retrieved {len(articles)} articles"
    )

    return {
        "news": articles
    }