from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from agents.search_agent import search_node
from agents.summarizer_agent import summarizer_node
from agents.critic_agent import critic_node
from agents.writer_agent import writer_node


class ResearchState(TypedDict):
    query: str
    raw_results: List[str]
    summaries: List[str]
    verified_facts: str
    final_report: str


def build_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("search",    search_node)
    graph.add_node("summarize", summarizer_node)
    graph.add_node("critic",    critic_node)
    graph.add_node("writer",    writer_node)

    graph.set_entry_point("search")
    graph.add_edge("search",    "summarize")
    graph.add_edge("summarize", "critic")
    graph.add_edge("critic",    "writer")
    graph.add_edge("writer",    END)

    return graph.compile()


research_graph = build_graph()
