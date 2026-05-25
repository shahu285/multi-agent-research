from tavily import TavilyClient
import os 
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_node(state: dict) -> dict:
    query = state["query"]

    results = tavily.search(
        query = query,
        max_results=5,
        search_depth="advanced"
    )

    raw_results = [r["content"] for r in results["results"]]

    return {"raw_results": raw_results}