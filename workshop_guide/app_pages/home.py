import streamlit as st

st.title("Intact Insurance AI Workshop")
st.markdown("Building Intelligence for Canada's Leading Property & Casualty Insurer with Snowflake Cortex")

st.space("small")

col1, col2, col3 = st.columns(3)
col1.metric("Sections", "6", help="Hands-on lab sections")
col2.metric("Prompts", "16", help="Total prompts across all tools")
col3.metric("Duration", "3.5 hrs", help="Total workshop time")

st.space("medium")

st.markdown("#### How this workshop works")

st.markdown("""
Each section has **numbered prompts** that you copy and paste into the appropriate tool:

- **Cortex Code** — for building infrastructure, creating objects, and writing SQL/Python
- **Cortex Analyst** — for testing natural language queries against your semantic view
- **Snowflake CoWork** — for collaborative data exploration and analysis

All prompts build on each other sequentially — run them in order throughout the afternoon.
""")

st.space("small")

st.markdown("#### The scenario")
with st.container(border=True):
    st.markdown("""
Intact Financial Corporation is Canada's largest provider of property and casualty insurance, serving individuals and businesses through a network of over 1,800 brokers across Ontario. With millions of active policies spanning auto, property, liability, and commercial lines, the operations team needs intelligent tools to analyze claims patterns, detect fraud, assess risk, and ensure regulatory compliance.

We'll build a complete AI platform covering:

| Data type | Examples |
|-----------|---------|
| **Structured** | Policies, claims, payments, broker performance |
| **Unstructured** | Claim adjuster notes, fraud investigation reports, regulatory filings |
| **Time series** | Regional risk scores, claims frequency, severity trends |
""")

st.space("small")

st.markdown("#### What we're building")

with st.container(border=True):
    st.markdown("""
In 3.5 hrs, we build a complete AI-powered operations platform:

**1. Data Foundation** — Load structured and unstructured operations data into Snowflake from pre-generated CSV files.

**2. Natural Language Analytics** — Create a Semantic View over operational tables and query them with plain English via Cortex Analyst.

**3. Intelligent Search** — Build a Cortex Search service over claim notes, fraud investigations, and regulatory filings for hybrid semantic + keyword search.

**4. AI Agents** — Create a Cortex Agent that orchestrates structured data queries AND document search through a single conversational interface.

**5. Collaborative AI** — Use CoWork to collaboratively analyze data with AI assistance.

**6. Operations Dashboard** — Deploy a Streamlit app with live KPIs, charts, and an AI chat interface.
""")

st.space("small")

st.markdown("#### Prerequisites")
with st.container(border=True):
    st.markdown("""
- Snowflake account with **ACCOUNTADMIN** role — see **Getting Started** in the sidebar to provision a free trial
- **Cortex Code** open in Snowsight and connected to your account
- Cross-region inference enabled (for Cortex LLM functions)
""")

st.space("medium")
st.caption("Built for the July 29, 2026 workshop  :material/location_on:  Intact Insurance Office, 2020 Blvd Robert-Bourassa Ste 100, Montréal, QC H3A 2A5")
