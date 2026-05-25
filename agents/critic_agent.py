from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temprature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

def critic_node(state: dict) ->dict:
    summaries = state ["summaries"]
    query = state["query"]

    summary_text = "\n".join(summaries)

    prompt = f"""You are a critical fact-checker. Review these reaserach findings about "{query}".

    Findings:
    {summary_text}

    Your job:

    1. Flag any claims that seem uncertain or contradictory
    2. Identify what is well-supported vs speculative
    3. Return a verified, cleaned-up version of the facts with confidence labels [HIGH/MEDIUM/LOW]

    Be hones and rigorous."""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {"verified_facts": response.content}

    