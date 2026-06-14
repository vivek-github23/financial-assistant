from langchain_core.tools import tool
from textblob import TextBlob

@tool(description="Analyze the sentiment of a given text")
def analyze_sentiment(text: str):
    sentiment = TextBlob(text).sentiment

    return {
        "polarity":
        sentiment.polarity
    }