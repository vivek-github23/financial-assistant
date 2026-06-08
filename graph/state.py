from typing import TypedDict, Optional

class AgentState(TypedDict):

    question: str
    history: list
    plan: Optional[str]
    news_query: Optional[str]
    required_agents: Optional[list]
    news: Optional[list]
    stocks: Optional[dict]
    analysis: Optional[str]
    critique: Optional[str]