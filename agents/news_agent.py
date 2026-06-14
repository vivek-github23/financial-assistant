from tools.news_tool import search_news
from tools.sentiment_tool import analyze_sentiment


def news_agent(state):
    if "news" not in state.get("required_agents", []):
        print("⏭️ Skipping News Agent")
        return {}

    query = state["news_query"]

    print(f"📰 Searching {query}")

    news = search_news.invoke({"query": query})

    articles = news.get("articles",[])

    sentiment_scores = []

    for article in articles[:5]:
        score = analyze_sentiment.invoke({"text":article["title"]})
        sentiment_scores.append(score)

    return {"news":articles,"news_sentiment":sentiment_scores}