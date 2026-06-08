from typing import TypedDict
from typing import Optional

class AgentState(TypedDict):
    question: str
    plan: Optional[str]
    news_query: Optional[str]
    required_agents: Optional[list]
    memories: Optional[list]
    news: Optional[list]
    stocks: Optional[dict]
    analysis: Optional[str]
    critique: Optional[str]