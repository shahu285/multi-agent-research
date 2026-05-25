import streamlit as st
import os
from graph.research_graph import research_graph

os.environ["GROQ_API_KEY"] = st.secrets.get("GROQ_API_KEY", "")
os.environ["TAVILY_API_KEY"] = st.secrets.get("TAVILY_API_KEY", "")

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Multi-Agent Research Assistant")
st.caption("Powered by LangGraph + Groq (Llama 3.3 70B) + Tavily - 100% Free")

with st.sidebar:
    st.header("How it works")
    st.markdown("""
    1. 🔍 **Search Agent** - Searches the web using Tavily
    2. 📝 **Summarizer Agent** - Extracts key findings
    3. ✅ **Critic Agent** - Verifies facts with confidence scores
    4. ✍️ **Writer Agent** - Compiles the final report
    """)
    st.divider()
    st.caption("Built with LangGraph multi-agent orchestration")

query = st.text_input(
    "Enter your research topic",
    placeholder="e.g. What is the current state of fusion energy?",
)

run_button = st.button("🚀 Start Research", type="primary")

if run_button and query:
    with st.status("Running research agents...", expanded=True) as status:
        st.write("🔍 Search agent searching the web...")

        final_state = None

        for step in research_graph.stream({
            "query": query,
            "raw_results": [],
            "summaries": [],
            "verified_facts": "",
            "final_report": ""
        }):
            step_name = list(step.keys())[0]

            if step_name == "search":
                st.write("📝 Summarizer agent processing results...")
            elif step_name == "summarize":
                st.write("✅ Critic agent verifying facts...")
            elif step_name == "critic":
                st.write("✍️ Writer agent compiling report...")
            elif step_name == "writer":
                final_state = step["writer"]

        status.update(label="✅ Research complete!", state="complete")

    if final_state and final_state.get("final_report"):
        st.divider()
        st.subheader(f"📄 Report: {query}")
        st.markdown(final_state["final_report"])

        st.download_button(
            label="📥 Download Report",
            data=final_state["final_report"],
            file_name=f"research_{query[:30].replace(' ', '_')}.txt",
            mime="text/plain"
        )

elif run_button and not query:
    st.warning("Please enter a research topic first.")
