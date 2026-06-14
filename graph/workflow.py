from langgraph.graph import StateGraph, END

from graph.state import AgentState

from agents.planner import planner
from agents.supervisor import supervisor
from agents.news_agent import news_agent
from agents.stock_agent import stock_agent
from agents.macro_agent import macro_agent
from agents.analyst import analyst
from agents.critic import critic
from agents.revision import revision
from agents.evidence_collector import evidence_collector
from agents.sentiment_agent import sentiment_agent

from memory.memory_agent import memory_agent

from graph.router import reflection_router

graph = StateGraph(AgentState)

graph.add_node("planner", planner)
graph.add_node("supervisor", supervisor)
graph.add_node("memory", memory_agent)
graph.add_node("news", news_agent)
graph.add_node("stocks", stock_agent)
graph.add_node("macro", macro_agent)
graph.add_node("sentiment", sentiment_agent)
graph.add_node("evidence_collector", evidence_collector)
graph.add_node("analyst", analyst)
graph.add_node("critic", critic)
graph.add_node("revision", revision)

graph.set_entry_point("planner")

graph.add_edge("planner", "supervisor")
graph.add_edge("supervisor", "memory")
graph.add_edge("memory", "news")
graph.add_edge("news", "stocks")
graph.add_edge("stocks", "macro")
graph.add_edge("macro", "sentiment")
graph.add_edge("sentiment", "evidence_collector")
graph.add_edge("evidence_collector", "analyst")
graph.add_edge("analyst", "critic")
graph.add_conditional_edges("critic",reflection_router,{"revision": "revision",END: END})
graph.add_edge("revision", "analyst")

workflow = graph.compile()