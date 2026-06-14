from typing import TypedDict, Optional

class AgentState(TypedDict, total=False):
    question: str
    plan: str
    news_query: str
    required_agents: list

    memories: list
    news: list
    news_sentiment: list
    companies: list
    countries: list

    stocks: dict
    macro_data: dict
    market_sentiment: str

    evidence: dict

    analysis: dict
    critique: str
    score: float
    iterations: int