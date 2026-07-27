import streamlit as st
from pathlib import Path
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

_DIR = Path(__file__).parent.parent

render_session_header(1, "Data Prep", "1:15 PM", "30 min", "Database, schema, warehouse, and 9 operational tables loaded from CSV")

render_technologies_used([
    {"name": "Database & Schema", "description": "Snowflake's organizational hierarchy for objects. A database contains schemas, and schemas contain tables, views, and other objects.", "icon": "database"},
    {"name": "CSV File Format", "description": "Snowflake can infer schema and load data directly from CSV files using file formats and COPY INTO commands.", "icon": "table_chart"},
    {"name": "Virtual Warehouse", "description": "Snowflake's compute engine. A warehouse provides the CPU and memory to execute queries and load data.", "icon": "memory"},
])


PROMPT_1_1 = """Create the following Snowflake objects for our Intact Insurance AI workshop:

1. A database called INSURANCE_AI
2. A schema called OPS inside that database
3. A stage called DATA in the schema OPS with a directory table and server side encryption
3. A warehouse called INSURANCE_WH (size MEDIUM, auto-suspend after 60 seconds, auto-resume enabled)
4. Set the session context to use these objects

Execute all SQL and confirm each object was created."""

render_prompt("Prompt 1.1", "Create Database, Schema & Warehouse", PROMPT_1_1)

render_explanation("What this prompt does", """
Creates the foundational Snowflake objects:

```sql
CREATE DATABASE INSURANCE_AI;
CREATE SCHEMA INSURANCE_AI.OPS;
CREATE WAREHOUSE INSURANCE_WH
  WAREHOUSE_SIZE = 'MEDIUM'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;

USE DATABASE INSURANCE_AI;
USE SCHEMA OPS;
USE WAREHOUSE INSURANCE_WH;
```
""")


PROMPT_1_2 = """In INSURANCE_AI.OPS, the 9 CSV files have been uploaded to an internal stage called DATA.

For all 9 tables (BROKERS, POLICYHOLDERS, POLICIES, CLAIMS, PAYMENTS, RISK_SCORES, CLAIM_NOTES, FRAUD_INVESTIGATIONS, REGULATORY_FILINGS):

1. Create a file format (CSV with PARSE_HEADER=TRUE, FIELD_OPTIONALLY_ENCLOSED_BY='"')
2. Create the tables with appropriate column types inferred from the data. Ensure to convert the column names to uppercase.
3. Load the data

Use CREATE TABLE with INFER_SCHEMA from a stage and then COPY INTO them. The key requirement is that all 9 tables are created and populated.

Execute all SQL."""

st.markdown("""
**Before running the prompt below, download the CSV files and upload them to the `DATA` stage:**

1. Download the zip file containing all CSVs: [insurance_data.zip](https://github.com/sfc-gh-osinquin/coco-hol-intact/raw/main/workshop_guide/data/insurance_data.zip)
2. Unzip the file on your computer to get the individual CSV files.
3. Using Snowsight, use the Horizon Catalog to browse to the `INSURANCE_AI.OPS.DATA` stage and upload all CSV files.
""")
st.image(str(_DIR / "static" / "stage_upload.png"), width=700)
st.markdown("""
4. Then copy the prompt below into Cortex Code and execute.
""")

render_prompt("Prompt 1.2", "Load and Create Tables from CSV", PROMPT_1_2)

render_explanation("What this prompt does", """
Loads all operational data tables from CSV files uploaded to the internal stage `DATA`:

```sql
CREATE OR REPLACE FILE FORMAT csv_format
  TYPE = CSV
  PARSE_HEADER = TRUE
  FIELD_OPTIONALLY_ENCLOSED_BY = '"';

CREATE OR REPLACE TABLE BROKERS
  USING TEMPLATE (
    SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
    FROM TABLE(INFER_SCHEMA(
      LOCATION => '@INSURANCE_AI.OPS.DATA/brokers.csv',
      FILE_FORMAT => 'csv_format'
    ))
  );

COPY INTO BROKERS
  FROM @INSURANCE_AI.OPS.DATA/brokers.csv
  FILE_FORMAT = csv_format;
```

**The tables**:
| Table | Rows | Description |
|-------|------|-------------|
| BROKERS | 15 | Broker offices across Ontario regions |
| POLICYHOLDERS | 20 | Individual and commercial customers |
| POLICIES | 66 | Insurance policies (auto, property, liability, commercial) |
| CLAIMS | 40 | Filed claims with amounts and status |
| PAYMENTS | 59 | Claim payment disbursements |
| RISK_SCORES | 144 | Regional risk metrics over time |
| CLAIM_NOTES | 40 | Adjuster notes with detailed investigation text |
| FRAUD_INVESTIGATIONS | 12 | Fraud case reports with evidence and outcomes |
| REGULATORY_FILINGS | 20 | OSFI, FSRA, and FINTRAC compliance filings |
""")


PROMPT_1_3 = """Run a query in INSURANCE_AI.OPS that shows every table name and its row count, ordered by row count descending. Format it nicely."""

render_prompt("Prompt 1.3", "Verify All Data Tables", PROMPT_1_3)

render_explanation("What this prompt does", """
A quick verification query. You should see approximately **416 total rows** across 9 tables.
""")


render_key_concepts([
    {"term": "Internal Stage", "definition": "A named Snowflake stage that stores files within Snowflake's managed storage. Files are uploaded via Snowsight UI or PUT command."},
    {"term": "INFER_SCHEMA", "definition": "A Snowflake table function that automatically detects column names and types from files in a stage."},
    {"term": "File Format", "definition": "A named object specifying how to parse files (CSV delimiters, headers, quoting). Created once and reused across multiple COPY INTO operations."},
])

render_what_you_built([
    "INSURANCE_AI database and OPS schema",
    "INSURANCE_WH warehouse (Medium, auto-suspend 60s)",
    "9 operational data tables loaded from CSV (~416 total rows)",
])
