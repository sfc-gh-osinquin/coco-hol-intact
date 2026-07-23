import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(2, "Cortex Analyst & Semantic Views", "1:45 PM", "30 min", "Semantic view with relationships, metrics, and natural language queries")

render_technologies_used([
    {"name": "Cortex Analyst", "description": "Snowflake's text-to-SQL engine that converts natural language questions into SQL queries using a semantic view to understand your data's business meaning.", "icon": "chat"},
    {"name": "Semantic View", "description": "A first-class Snowflake object (CREATE SEMANTIC VIEW) that describes your data in business terms: tables, relationships, facts, dimensions, metrics, and synonyms.", "icon": "description"},
    {"name": "AI_SQL_GENERATION", "description": "Custom instructions embedded in the semantic view that guide how Cortex Analyst generates SQL — providing domain context and disambiguation hints.", "icon": "auto_fix_high"},
])


PROMPT_2_1 = """/semantic_studio In INSURANCE_AI.OPS, create a semantic view called INSURANCE_OPERATIONS_VIEW for use with Cortex Analyst. It should cover these tables: BROKERS, POLICYHOLDERS, POLICIES, CLAIMS, PAYMENTS, RISK_SCORES.

Include:
- Relationships between the tables following these rules:
  - Do NOT specify join_type — omit it entirely (the proto enum doesn't accept string values like many_to_one)
  - Convention: left_table = fact/many side, right_table = dimension/one side (put the table with many rows as left_table)
  - Define primary_key.columns on dimension tables (BROKERS, POLICYHOLDERS) so the engine knows the "one" side
  - Use this template for each relationship:
    relationships:
      - name: <descriptive_name>
        left_table: <FACT_TABLE>
        right_table: <DIMENSION_TABLE>
        relationship_columns:
          - left_column: <FK_COLUMN>
            right_column: <PK_COLUMN>
  - Relationships needed: POLICIES→BROKERS (broker_id), POLICIES→POLICYHOLDERS (policyholder_id), CLAIMS→POLICIES (policy_id), PAYMENTS→CLAIMS (claim_id)
- Facts for key numeric columns: premium_amount, coverage_limit, deductible, claim_amount, net_payout, payment amount, risk_score, claims_frequency, severity_index
- Dimensions for categorical columns: policy_type, claim_status, claim_type, region, broker_name, payment_type, risk_tier, policyholder_type
- Add useful SYNONYMS (premium=insurance cost/rate, policyholder=customer/insured/client, claim=loss report/incident, broker=agent/intermediary)
- Metrics: loss_ratio (sum of claim_amount / sum of premium_amount), average_claim_value (avg claim_amount), claim_frequency_rate (count claims / count policies), severity_ratio (avg net_payout / avg premium_amount)
- An AI_SQL_GENERATION instruction with domain context: This is a P&C (property and casualty) insurance dataset for Intact Insurance in Ontario, Canada. Key concepts: loss ratio measures claims cost vs premium income (lower is better for the insurer), severity measures average claim cost, frequency measures how often claims occur. Policy types include Auto, Property, Commercial, and Liability lines. Regions are Ontario sub-regions (Greater Toronto, Central, Eastern, Southwestern, Northern, Southern Ontario). When asked about profitability, use loss_ratio. When asked about risk, reference risk_scores table.

Execute the SQL and confirm with DESCRIBE SEMANTIC VIEW."""

render_prompt("Prompt 2.1", "Create the Semantic View", PROMPT_2_1)

render_explanation("What this prompt does", """
Creates a **semantic view** — a first-class Snowflake object that enables natural language to SQL.

Key insurance concepts mapped:
- **Loss ratio** = Claims paid ÷ Premiums earned (the fundamental P&C profitability metric)
- **Severity** = Average cost per claim (how expensive claims are)
- **Frequency** = Number of claims per policy (how often claims happen)
- **Combined ratio** = Loss ratio + Expense ratio (overall underwriting profitability)
""")


PROMPT_2_2 = """Ask Cortex Analyst these questions using INSURANCE_AI.OPS.INSURANCE_OPERATIONS_VIEW:

1. "What is the total premium revenue by policy type?"
2. "Which region has the highest loss ratio?"
3. "Show me the top 5 brokers by total claims paid out"
4. "What is the average claim amount for commercial vs personal policies?"

Show the generated SQL and results for each."""

render_prompt("Prompt 2.2", "Test with Natural Language Queries", PROMPT_2_2)

st.info("""
:material/lightbulb: **You can also test these in the Cortex Analyst UI!**

In Snowsight, navigate to **AI & ML → Cortex Analyst** in the left sidebar. Select your `INSURANCE_OPERATIONS_VIEW` semantic view, and you'll see a playground where you can type natural language questions interactively.
""")

render_explanation("What this prompt does", """
Tests Cortex Analyst across different question types to validate the semantic view definitions.

1. **Aggregation by dimension** — validates policy_type dimension and premium_amount fact
2. **Calculated metric** — validates loss_ratio metric and region dimension
3. **Multi-table join** — validates relationships between claims, policies, and brokers
4. **Conditional aggregation** — validates filtering by policyholder_type
""")


PROMPT_2_3 = """Now expand our INSURANCE_OPERATIONS_VIEW in INSURANCE_AI.OPS:

1. Add a new metric called "retention_risk_score" that calculates the average risk_score for each region weighted by premium volume
2. Add a metric called "claim_severity_trend" that shows average claim_amount by month
3. Add synonyms: "high risk" = risk_tier = 'High', "profitable" = loss_ratio < 0.6, "unprofitable" = loss_ratio > 1.0

Execute all SQL."""

render_prompt("Prompt 2.3", "Expand the Semantic View", PROMPT_2_3)

render_explanation("What this prompt does", """
Demonstrates iterative semantic view development — adding calculated metrics.

- **retention_risk_score** helps identify regions where high-value customers may be at risk
- **claim_severity_trend** enables time-series analysis of claim costs
- **Synonyms** map business language to technical conditions
""")


render_key_concepts([
    {"term": "Cortex Analyst", "definition": "Snowflake's text-to-SQL engine. Converts natural language to SQL using a semantic view for context."},
    {"term": "Semantic View", "definition": "A first-class Snowflake object mapping tables to business concepts. Contains relationships, facts, dimensions, metrics, synonyms, and AI instructions."},
    {"term": "AI_SQL_GENERATION", "definition": "Custom instructions guiding SQL generation. Essential for domain-specific terminology."},
])

render_what_you_built([
    "INSURANCE_OPERATIONS_VIEW semantic view with domain-specific metrics",
    "Natural language queries validated against the view",
    "Expanded view with calculated metrics",
])
