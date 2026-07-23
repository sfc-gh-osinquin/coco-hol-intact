import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(4, "Cortex Agents", "3:00 PM", "35 min", "Cortex Agent with Analyst + Search + custom tools")

render_technologies_used([
    {"name": "Cortex Agent (CREATE AGENT)", "description": "An orchestrating AI that plans tasks, selects tools, executes them, reflects on results, and generates responses.", "icon": "smart_toy"},
    {"name": "Tool Orchestration", "description": "The Agent automatically routes questions to the right tool: Cortex Analyst for structured data, Cortex Search for documents, custom UDFs for logic.", "icon": "route"},
    {"name": "Custom Tools (UDFs)", "description": "User-defined functions that extend Agent capabilities with custom business logic.", "icon": "build"},
])


PROMPT_4_1 = """In INSURANCE_AI.OPS, create a Cortex Agent called INSURANCE_AGENT.

It should:
- Use auto as the orchestration model
- Have two tools: the INSURANCE_OPERATIONS_VIEW semantic view (for structured data queries) and the INSURANCE_SEARCH Cortex Search service (for unstructured document search)
- Include instructions defining it as the Intact Insurance Operations Assistant, guiding it to use structured data for premium analysis, claims metrics, loss ratios, broker performance, and risk scores and search for claim details, fraud investigation findings, regulatory compliance information, and adjuster notes
- Mention domain context: This agent serves Intact Insurance operations teams analyzing P&C insurance data across Ontario. It can answer questions about policy portfolios, claims experience, fraud patterns, and regulatory compliance.
- Include 3-4 sample questions spanning both tools

Execute and show confirmation."""

render_prompt("Prompt 4.1", "Create the Cortex Agent", PROMPT_4_1)

render_explanation("What this prompt does", """
Creates a **Cortex Agent** combining structured analytics with document search:

- **Structured questions** → routed to Cortex Analyst via the semantic view
- **Unstructured questions** → routed to Cortex Search
- **Mixed questions** → Agent uses both tools and synthesizes
""")


PROMPT_4_2 = """Test our INSURANCE_AGENT with these queries:

1. "What is the loss ratio by region for auto policies?" (structured — Analyst)
2. "What were the findings in the organized tow truck fraud investigation?" (unstructured — Search)
3. "Which regions have the highest claim severity AND what do the adjuster notes say about the most expensive claims in those regions?" (mixed — both tools)

Show the responses and note which tools the agent selected."""

render_prompt("Prompt 4.2", "Test the Agent", PROMPT_4_2)

render_explanation("What this prompt does", """
Tests the agent with structured, unstructured, and mixed queries to validate tool routing.
""")


PROMPT_4_3 = """In INSURANCE_AI.OPS, add a custom tool to the agent:

1. Create a UDF:

CREATE OR REPLACE FUNCTION INSURANCE_AI.OPS.CALCULATE_RISK_PREMIUM(
    base_premium FLOAT,
    risk_tier VARCHAR,
    claim_count INT,
    years_as_customer INT
)
RETURNS VARIANT
LANGUAGE SQL
AS
$$
    SELECT OBJECT_CONSTRUCT(
        'adjusted_premium', base_premium *
            CASE risk_tier
                WHEN 'High' THEN 1.35
                WHEN 'Medium' THEN 1.15
                WHEN 'Low' THEN 0.95
            END *
            CASE
                WHEN claim_count >= 3 THEN 1.25
                WHEN claim_count = 2 THEN 1.10
                WHEN claim_count = 1 THEN 1.05
                ELSE 1.00
            END *
            CASE
                WHEN years_as_customer >= 10 THEN 0.90
                WHEN years_as_customer >= 5 THEN 0.95
                ELSE 1.00
            END,
        'risk_factors', OBJECT_CONSTRUCT(
            'tier_multiplier', CASE risk_tier WHEN 'High' THEN 1.35 WHEN 'Medium' THEN 1.15 ELSE 0.95 END,
            'claims_surcharge', CASE WHEN claim_count >= 3 THEN 1.25 WHEN claim_count = 2 THEN 1.10 WHEN claim_count = 1 THEN 1.05 ELSE 1.00 END,
            'loyalty_discount', CASE WHEN years_as_customer >= 10 THEN 0.90 WHEN years_as_customer >= 5 THEN 0.95 ELSE 1.00 END
        ),
        'recommendation', CASE
            WHEN risk_tier = 'High' AND claim_count >= 3 THEN 'Flag for underwriting review — high risk with frequent claims'
            WHEN risk_tier = 'High' THEN 'Monitor closely — consider risk mitigation requirements'
            WHEN years_as_customer >= 10 AND claim_count = 0 THEN 'Preferred customer — offer loyalty renewal discount'
            ELSE 'Standard renewal'
        END
    )
$$;

2. Recreate INSURANCE_AGENT with CALCULATE_RISK_PREMIUM as an additional tool.

3. Test with: "Calculate the risk-adjusted premium for a High-risk customer with a base premium of $2,500, 2 prior claims, and 3 years as a customer"

Execute all SQL."""

render_prompt("Prompt 4.3", "Agent with Custom Tool", PROMPT_4_3)

render_explanation("What this prompt does", """
Adds a **custom UDF tool** for domain-specific calculations. The Agent can now query data, search documents, AND run custom business logic.
""")


render_key_concepts([
    {"term": "Cortex Agent", "definition": "A Snowflake object that orchestrates LLMs, Analyst, Search, and custom tools to answer complex questions."},
    {"term": "Tool Routing", "definition": "The Agent selects the right tool for each question based on the question type and tool descriptions."},
    {"term": "Custom Tools", "definition": "SQL UDFs registered as Agent tools. Enable domain-specific calculations and business logic."},
])

render_what_you_built([
    "INSURANCE_AGENT — Cortex Agent with Analyst + Search tools",
    "Tested structured, unstructured, and mixed queries",
    "CALCULATE_RISK_PREMIUM as a custom tool",
    "Enhanced agent with three tool types",
])
