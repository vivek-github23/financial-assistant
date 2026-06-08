from langgraph.graph import StateGraph

from graph.state import AgentState

from graph.router import (
    route_news,
    route_stocks
)

from agents.planner import planner
from agents.news_agent import news_agent
from agents.stock_agent import stock_agent
from agents.analyst import analyst
from agents.critic import critic


graph = StateGraph(AgentState)

graph.add_node(
    "planner",
    planner
)

graph.add_node(
    "news",
    news_agent
)

graph.add_node(
    "stocks",
    stock_agent
)

graph.add_node(
    "analyst",
    analyst
)

graph.add_node(
    "critic",
    critic
)

graph.set_entry_point(
    "planner"
)

graph.add_conditional_edges(
    "planner",
    route_news
)

graph.add_conditional_edges(
    "planner",
    route_stocks
)

graph.add_edge(
    "news",
    "analyst"
)

graph.add_edge(
    "stocks",
    "analyst"
)

graph.add_edge(
    "analyst",
    "critic"
)

graph.set_finish_point(
    "critic"
)

workflow = graph.compile()