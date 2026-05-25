from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temprature = 0,
    api_key = os.getenv("GROQ_API_KEY")
)

def summarizer_node(state: dict)-> dict:
    raw_results = state["raw_results"]
    query = state["query"]

    combined = "\n\n---\n\n".join(raw_results)

    prompt = f"""You are a research summarizer. Given the following search results about "{query}",
    extract and summarize the 5 most important facts. Be concise and factual.

    Seach Results:
    {combined}

    Provide a numbered list of key findings."""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {"summaries": [response.content]}

    
