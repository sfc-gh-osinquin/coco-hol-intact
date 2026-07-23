import streamlit as st
from components import render_session_header, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(5, "CoWork", "3:35 PM", "25 min", "Collaborative AI analysis with CoWork")

render_technologies_used([
    {"name": "Snowflake CoWork", "description": "An AI-powered collaborative workspace inside Snowsight where you can analyze data, generate insights, and share findings.", "icon": "group"},
    {"name": "Data Analysis", "description": "CoWork can query your Snowflake data, generate visualizations, and provide insights without writing SQL.", "icon": "analytics"},
    {"name": "Sharing & Collaboration", "description": "CoWork sessions can be shared with team members for collaborative data exploration.", "icon": "share"},
])

st.markdown("---")

st.markdown("#### :material/open_in_new: Open CoWork")
with st.container(border=True):
    st.markdown("""
In Snowsight, click **CoWork** in the left navigation panel. Start a new conversation.

CoWork discovers your tables in `INSURANCE_AI.OPS` automatically. Paste each question below one at a time.
""")

st.space("small")

st.markdown("#### :material/chat: Questions to ask CoWork")
st.caption("Copy and paste each question into CoWork individually.")

questions = [
    ("Loss Ratio Analysis", "Analyze the loss ratio by region and policy type. Which combinations are most profitable and which are losing money? Show me a breakdown with visualizations."),
    ("Fraud Pattern Detection", "Looking at our claims and fraud investigations data, what patterns can you identify that might indicate fraudulent activity? Consider claim timing, amounts, and policyholder characteristics."),
    ("Broker Performance Scorecard", "Create a broker performance scorecard showing: total premiums written, claims incurred, loss ratio, average policy size, and customer retention (years_as_customer). Rank brokers from best to worst performing."),
    ("Risk Trend Forecasting", "Analyze the risk_scores table to identify seasonal patterns and regional trends. Which regions are showing deteriorating risk profiles? What might be driving the winter spikes in auto risk?"),
    ("Claims Severity Deep Dive", "What are the characteristics of our highest-severity claims (top 10 by amount)? Is there a correlation between policy type, region, and claim severity? What operational changes could reduce severity?"),
]

for title, question in questions:
    with st.container(border=True):
        st.markdown(f"**{title}**")
        st.code(question, language="text", wrap_lines=True)

st.space("small")

render_explanation("How CoWork works", """
**CoWork** is Snowflake's collaborative AI workspace — different from Cortex Code:

| Tool | Best for |
|------|----------|
| Cortex Code | Building infrastructure, creating objects, writing SQL |
| CoWork | Exploring data, generating insights, team collaboration |
| Cortex Agent | End-user Q&A interface (deployed as a product) |
""")

render_key_concepts([
    {"term": "CoWork", "definition": "Snowflake's collaborative AI workspace. Conversational interface that queries data, creates visualizations, and generates insights."},
    {"term": "Context Maintenance", "definition": "CoWork maintains conversation history so follow-up questions build on previous analysis."},
])

render_what_you_built([
    "Explored operations data through conversational AI",
    "Generated visualizations and cross-table analysis",
    "Demonstrated the CoWork collaborative analysis pattern",
])
