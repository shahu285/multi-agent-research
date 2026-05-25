from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

def writer_node(state: dict) -> dict:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        api_key=os.environ.get("GROQ_API_KEY")
    )

    verified_facts = state["verified_facts"]
    query = state["query"]

    prompt = f'''You are a professional research writer. Based on verified facts below, 
    write a comprehensive research report on: "{query}"
    
    Verified Facts:
    {verified_facts}
    
    Write a structured report with:
    - Executive Summary (2-3 sentences)
    - Key Findings (detailed)
    - Conclusion
    - Confidence Note (mention which areas need more research)
    
    Use clear, professional language.'''

    response = llm.invoke([HumanMessage(content=prompt)])

    return {"final_report": response.content}
