# 🔬 MultiThesis - Multi-Agent Research Assistant

> An AI-powered research tool that deploys multiple specialized agents to search the web, summarize findings, verify facts, and produce structured research reports — all in real time.

🚀 **Live Demo** → [multi-agent1.streamlit.app](https://multi-agent1.streamlit.app/)

---

## 📌 What It Does

Enter any research topic and 4 specialized AI agents collaborate in a pipeline to deliver a comprehensive, fact-verified research report in under 60 seconds.

**Example queries:**
- "What is the current state of quantum computing?"
- "Latest developments in fusion energy 2025"
- "How is AI impacting the Indian job market?"

---

## 🏗️ Architecture

```
User Query
    │
    ▼
┌─────────────────────────────────────────────┐
│              LangGraph Orchestrator          │
│                                             │
│  ┌──────────┐    ┌────────────┐             │
│  │  Search  │───▶│ Summarizer │             │
│  │  Agent   │    │   Agent    │             │
│  └──────────┘    └─────┬──────┘             │
│   Tavily API           │                    │
│                        ▼                    │
│                  ┌──────────┐               │
│                  │  Critic  │               │
│                  │  Agent   │               │
│                  └─────┬────┘               │
│                        │                    │
│                        ▼                    │
│                  ┌──────────┐               │
│                  │  Writer  │               │
│                  │  Agent   │               │
│                  └──────────┘               │
└─────────────────────────────────────────────┘
    │
    ▼
Final Research Report (Streamlit UI)
```

---

## 🤖 Agent Breakdown

### 1. 🔍 Search Agent
- Uses the **Tavily API** to perform deep web searches
- Fetches top 5 most relevant results for the query
- Returns raw content for downstream agents to process

### 2. 📝 Summarizer Agent
- Powered by **Llama 3.3 70B via Groq**
- Reads all raw search results
- Extracts the 5 most important findings
- Returns a clean, numbered list of key facts

### 3. ✅ Critic Agent
- Powered by **Llama 3.3 70B via Groq**
- Reviews the summarized findings for accuracy
- Flags uncertain or contradictory claims
- Labels each fact with a confidence score: `[HIGH]`, `[MEDIUM]`, or `[LOW]`

### 4. ✍️ Writer Agent
- Powered by **Llama 3.3 70B via Groq**
- Takes the verified facts and writes a structured report
- Output includes: Executive Summary, Key Findings, Conclusion, and Confidence Notes
- Report is downloadable as a `.txt` file

---

## 🧠 How LangGraph Powers This

LangGraph is used to define a **stateful directed graph** where each node is an agent and edges define the flow of information between them.

```python
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
```

A shared `ResearchState` object is passed between all agents, allowing each agent to read previous outputs and write its own:

```python
class ResearchState(TypedDict):
    query: str
    raw_results: List[str]
    summaries: List[str]
    verified_facts: str
    final_report: str
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **LangGraph** | Multi-agent orchestration and state management |
| **LangChain** | LLM abstraction and message handling |
| **Groq API** | Ultra-fast inference with Llama 3.3 70B (free tier) |
| **Tavily API** | Real-time web search (free tier) |
| **Streamlit** | Frontend UI and deployment |
| **Python** | Core language |

---

## 📁 Project Structure

```
multi-agent-research/
│
├── agents/
│   ├── __init__.py
│   ├── search_agent.py       # Tavily web search
│   ├── summarizer_agent.py   # Key findings extraction
│   ├── critic_agent.py       # Fact verification
│   └── writer_agent.py       # Report generation
│
├── graph/
│   ├── __init__.py
│   └── research_graph.py     # LangGraph pipeline definition
│
├── app.py                    # Streamlit UI
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.10+
- A free [Groq API key](https://console.groq.com)
- A free [Tavily API key](https://app.tavily.com)

### Installation

```bash
# Clone the repository
git clone https://github.com/shahu285/multi-agent-research.git
cd multi-agent-research

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your-groq-key-here
TAVILY_API_KEY=your-tavily-key-here
```

### Run the App

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🚀 Deployment

This app is deployed on **Streamlit Community Cloud** (free).

To deploy your own instance:
1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Add your API keys under **Advanced Settings → Secrets**
5. Deploy

---

## 💡 Key Concepts Demonstrated

- **Multi-agent orchestration** with LangGraph
- **Stateful graph execution** with shared state between agents
- **Tool integration** — connecting LLMs to real-world APIs (Tavily)
- **Prompt engineering** for specialized agent roles
- **Production deployment** on Streamlit Cloud
- **Secrets management** for API keys in deployment

---

## 📈 Future Improvements

- [ ] Add chat history to store past research sessions
- [ ] Display source citations with URLs under the report
- [ ] Export report as a formatted PDF
- [ ] Add a feedback loop — critic can send summarizer back to re-search if confidence is low
- [ ] Support multiple search queries per topic for broader coverage

---

## 👤 Author

**Shahu Ugale** | AI Engineer

Connect on [LinkedIn](#) | [GitHub](https://github.com/shahu285)

---

## 📄 License

MIT License — free to use, modify, and distribute.
