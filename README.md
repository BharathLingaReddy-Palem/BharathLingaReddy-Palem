<p align="center">
  <img src="./assets/hero.svg" width="100%" alt="Bharath Linga Reddy Palem — AI systems. Product thinking. AI and ML developer, Hyderabad, India." />
</p>

<p align="center">
  <a href="#the-brief"><strong>THE BRIEF</strong></a> &nbsp; / &nbsp;
  <a href="#portfolio-signal"><strong>PORTFOLIO SIGNAL</strong></a> &nbsp; / &nbsp;
  <a href="#selected-systems"><strong>THE SYSTEMS</strong></a> &nbsp; / &nbsp;
  <a href="#inside-the-builds"><strong>GO DEEPER</strong></a> &nbsp; / &nbsp;
  <a href="#connect"><strong>CONNECT ↗</strong></a>
</p>

## The brief

**I’m Bharath Linga Reddy Palem. I build AI applications around real workflows.**

An AI/ML & Python developer in Hyderabad, studying **B.Tech AI & Data Science at ICFAI Foundation for Higher Education, Hyderabad — class of 2027**. My work connects data, models, APIs, and interfaces: from a dataset to a decision, a PDF to a grounded answer, or a conversation to an action.

<table>
<tr>
<td width="33%" valign="top"><strong>01 / INTELLIGENCE</strong><br /><br />Machine learning, AutoML, retrieval, and language models.</td>
<td width="33%" valign="top"><strong>02 / ENGINEERING</strong><br /><br />Python APIs, persistent data, and connected MCP tools.</td>
<td width="33%" valign="top"><strong>03 / EXPERIENCE</strong><br /><br />React and Streamlit interfaces that make the system usable.</td>
</tr>
</table>

**Open to AI/ML & Python internships.** [Start a conversation →](https://www.linkedin.com/in/bharath-linga-reddy-palem-523a6b449/)

## Portfolio signal

<a href="https://github.com/BharathLingaReddy-Palem?tab=repositories">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="./assets/portfolio-signal-light.svg" />
    <img src="./assets/portfolio-signal.svg" width="100%" alt="Public project dashboard: repository count, primary language distribution, and cumulative repository creation timeline. Values and refresh date are included in the graphic." />
  </picture>
</a>

<sub>Real public GitHub data. The profile repository and forks are excluded. Language shares count repositories by their primary language; they are not skill ratings. Charts refresh weekly. <a href="./data/repositories.json">Data</a> · <a href="./.github/workflows/refresh-profile.yml">Refresh workflow</a></sub>

## Selected systems

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/BharathLingaReddy-Palem/data-agent-generative-ai"><img src="./assets/data-agent.svg" alt="01 — Data Agent: explore, clean, train, report." width="100%" /></a>
<h3><a href="https://github.com/BharathLingaReddy-Palem/data-agent-generative-ai">Data Agent ↗</a></h3>
<p><strong>The decision layer for a dataset.</strong> Explore and clean data, compare models, make predictions, and export reports from one workspace.</p>
<p><code>FastAPI</code> <code>React</code> <code>scikit-learn</code></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/BharathLingaReddy-Palem/expense_tracker"><img src="./assets/expense-mcp.svg" alt="02 — Expense MCP: conversation, action, persistent data." width="100%" /></a>
<h3><a href="https://github.com/BharathLingaReddy-Palem/expense_tracker">Expense Tracker MCP ↗</a></h3>
<p><strong>Finance tools inside a conversation.</strong> Categorize expenses, track budgets, manage reminders, and export records through MCP.</p>
<p><code>FastMCP</code> <code>PostgreSQL</code> <code>NVIDIA NIM</code></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/BharathLingaReddy-Palem/Multimodal-RAG-LoRA-Fine-Tuned-Educational-LLM"><img src="./assets/educational-rag.svg" alt="03 — Educational RAG: documents, retrieval, language models." width="100%" /></a>
<h3><a href="https://github.com/BharathLingaReddy-Palem/Multimodal-RAG-LoRA-Fine-Tuned-Educational-LLM">College PDF Intelligence ↗</a></h3>
<p><strong>Study material becomes a knowledge interface.</strong> Exploring PDF extraction, vector retrieval, and LoRA fine-tuning workflows.</p>
<p><code>RAG</code> <code>ChromaDB</code> <code>Llama</code> <code>LoRA</code></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/BharathLingaReddy-Palem/retail-demand-forecasting"><img src="./assets/retail-forecast.svg" alt="04 — Retail Forecasting: historical sales and future demand." width="100%" /></a>
<h3><a href="https://github.com/BharathLingaReddy-Palem/retail-demand-forecasting">Retail Demand Forecasting ↗</a></h3>
<p><strong>Better context for the next restock.</strong> Exploring demand estimation and inventory planning with historical sales and machine learning.</p>
<p><code>Python</code> <code>pandas</code> <code>scikit-learn</code></p>
</td>
</tr>
</table>

## Inside the builds

<details>
<summary><strong>01 / Open the Data Agent architecture</strong> — data → analysis → models → reports</summary>

### From raw files to a working analytical workflow

<a href="./assets/data-agent-architecture.svg"><img src="./assets/data-agent-architecture.svg" width="100%" alt="Data Agent architecture: files flow through profiling and cleaning into model comparison, prediction, interpretation, and reports." /></a>

**Engineering choices:** versioned data cleaning, validation-based model selection, saved runs, and interfaces built around the workflow. The implementation computes statistics before requesting LLM interpretations.

[Read the implementation and its limitations →](https://github.com/BharathLingaReddy-Palem/data-agent-generative-ai)

</details>

<details>
<summary><strong>02 / Open the Expense MCP architecture</strong> — a conversation becomes an application action</summary>

<a href="./assets/expense-mcp-architecture.svg"><img src="./assets/expense-mcp-architecture.svg" width="100%" alt="Expense MCP architecture: an assistant calls FastMCP tools, validates input, and connects to PostgreSQL and categorization." /></a>

**Engineering choices:** persistent records, batch operations, recoverable expense deletion, CSV export, and a tool interface the assistant can call.

[Inspect the tools →](https://github.com/BharathLingaReddy-Palem/expense_tracker/blob/main/expense_tracker.py)

</details>

<details>
<summary><strong>03 / Open the learning lab</strong> — retrieval, forecasting, and recommendation</summary>

| Experiment | Question I’m exploring | Repository |
| :--- | :--- | :--- |
| **Educational RAG + LoRA** | How can retrieval and adaptation help a model work with course material? | [Explore →](https://github.com/BharathLingaReddy-Palem/Multimodal-RAG-LoRA-Fine-Tuned-Educational-LLM) |
| **Retail forecasting** | How can past sales inform future inventory decisions? | [Explore →](https://github.com/BharathLingaReddy-Palem/retail-demand-forecasting) |
| **Music recommendation** | What can content similarity tell us about the next song? | [Explore →](https://github.com/BharathLingaReddy-Palem/Music-recommendation-system) |
| **Image classification** | What does it take to turn visual data into useful labels? | [Explore →](https://github.com/BharathLingaReddy-Palem/Cat_dog_classification) |

</details>

<details>
<summary><strong>04 / Open the toolkit</strong> — the technologies behind the work</summary>

| Layer | Tools I work with |
| :--- | :--- |
| **Data & models** | Python · pandas · scikit-learn · PyTorch |
| **Language & retrieval** | RAG · ChromaDB · LoRA · LLM APIs |
| **Applications** | FastAPI · React · Streamlit |
| **Connected systems** | MCP · FastMCP · PostgreSQL · Git |

**My operating principles:** start with a real question, make the evidence visible, and finish the interface.

</details>

## Connect

**A useful problem. A thoughtful team. Something worth building.**

I’m open to AI/ML & Python internships and conversations about practical AI applications.

<p>
<a href="https://www.linkedin.com/in/bharath-linga-reddy-palem-523a6b449/"><img src="./assets/linkedin.svg" alt="Connect on LinkedIn" height="42" /></a>
&nbsp;
<a href="https://x.com/bharath3702"><img src="./assets/x.svg" alt="Follow @bharath3702 on X" height="42" /></a>
&nbsp;
<a href="https://github.com/BharathLingaReddy-Palem?tab=repositories"><img src="./assets/github.svg" alt="Explore all public projects on GitHub" height="42" /></a>
</p>

<sub><strong>Bharath Linga Reddy Palem</strong> · Hyderabad, India · Learn with curiosity. Build with intent.</sub>

