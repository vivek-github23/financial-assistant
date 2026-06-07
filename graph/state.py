from typing import TypedDict, Optional

class AgentState(TypedDict):

    question: str

    plan: Optional[str]

    news: Optional[list]

    stocks: Optional[dict]

    analysis: Optional[str]

    critique: Optional[str]