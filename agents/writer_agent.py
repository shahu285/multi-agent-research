from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os 
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temprature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)

def writer_node(state:dict) -> dict:
    verified_facts = state["verified_facts"]
    query = state["query"]

    prompt = f"""You are a professional research write. Based on verfied facts below, write a comprehensive research report on: "{query}"

    Verified Facts:
    {verified_facts}

    Write a structured report with:
    - Executive summary (2-3 sentences)
    - Key Findings (detailed)
    - Conclusion
    - Confidence Note (mention which areas need more research)

    Use clear, professional language. """

    response = llm.invoke ([HumanMessage(content=prompt)])

    return {"final_report": response.content}