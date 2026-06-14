def sentiment_agent(state):
    print("😊 Sentiment Agent")
    data = state.get("news_sentiment", [])
    scores = [x['polarity'] for x in data]
    if not scores:
        return {"market_sentiment": "Neutral"}

    avg = sum(scores) / len(scores)

    if avg > 0.2:
        sentiment = "Bullish"
    elif avg < -0.2:
        sentiment = "Bearish"
    else:
        sentiment = "Neutral"

    return {"market_sentiment": sentiment}