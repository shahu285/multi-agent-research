from tavily import TavilyClient
import os

def search_node(state: dict) -> dict:
    tavily = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))

    query = state["query"]

    results = tavily.search(
        query=query,
        max_results=5,
        search_depth="advanced"
    )

    raw_results = [r["content"] for r in results["results"]]

    return {"raw_results": raw_results}
