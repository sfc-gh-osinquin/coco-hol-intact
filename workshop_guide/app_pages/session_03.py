import streamlit as st
from components import render_session_header, render_prompt, render_explanation, render_technologies_used, render_key_concepts, render_what_you_built

render_session_header(3, "Cortex Search", "2:15 PM", "30 min", "Knowledge base, Cortex Search service, and RAG query pattern")

render_technologies_used([
    {"name": "Cortex Search Service", "description": "A managed hybrid search engine combining vector (semantic) and keyword search with automatic reranking. Created with a single SQL statement.", "icon": "search"},
    {"name": "RAG (Retrieval Augmented Generation)", "description": "A pattern that retrieves relevant documents first, then passes them as context to an LLM for grounded answer generation.", "icon": "hub"},
    {"name": "SEARCH_PREVIEW", "description": "SQL function to query a Cortex Search Service. Supports text queries, column selection, filtering, and result limits.", "icon": "preview"},
])


st.info("""
:material/add_circle: **Tip: start a new chat before this session.**

To reduce token consumption and avoid context rot, it is good practice to start a new chat whenever your work is not related to previous prompts.

Before getting into Cortex Search, click on the **+** icon at the top of the CoCo panel and start a new chat.
""")

PROMPT_3_1 = """In INSURANCE_AI.OPS:

1. First, create a unified text table for search called INSURANCE_KNOWLEDGE_BASE that combines:
   - CLAIM_NOTES: use note_id as doc_id, 'claim_note' as doc_type, content as content, note_type as metadata_category, 'standard' as metadata_priority, note_date as doc_date
   - FRAUD_INVESTIGATIONS: use investigation_id as doc_id, 'fraud_investigation' as doc_type, evidence_summary as content, fraud_type as metadata_category, investigation_status as metadata_priority, open_date as doc_date
   - REGULATORY_FILINGS: use filing_id as doc_id, 'regulatory_filing' as doc_type, summary as content, filing_type as metadata_category, status as metadata_priority, filing_date as doc_date

2. Then create a Cortex Search Service:
   CREATE OR REPLACE CORTEX SEARCH SERVICE INSURANCE_SEARCH
     ON content
     ATTRIBUTES metadata_category, metadata_priority, doc_type
     WAREHOUSE = INSURANCE_WH
     TARGET_LAG = '1 hour'
     EMBEDDING_MODEL = 'snowflake-arctic-embed-l-v2.0'
     AS (
       SELECT doc_id, doc_type, content, metadata_category, metadata_priority, doc_date
       FROM INSURANCE_KNOWLEDGE_BASE
     );

Execute all SQL. Then verify with SHOW CORTEX SEARCH SERVICES."""

render_prompt("Prompt 3.1", "Create Cortex Search Service", PROMPT_3_1)

render_explanation("What this prompt does", """
Builds a unified knowledge base from unstructured text sources and creates a hybrid search service.

The search service automatically embeds, indexes, and serves results with auto-refresh when source data changes.
""")


PROMPT_3_2 = """In INSURANCE_AI.OPS, query our INSURANCE_SEARCH service using SEARCH_PREVIEW:

1. Search for "water damage basement flooding" — should find relevant claim notes
2. Search for "ransomware cyber breach" — should find the cyber incident investigation
3. Search for "OSFI capital adequacy" — should find regulatory filings about MCT ratios
4. Search for "organized fraud ring GTA" — should find fraud investigation reports

Execute all searches and show results."""

render_prompt("Prompt 3.2", "Query the Search Service", PROMPT_3_2)

render_explanation("What this prompt does", """
Tests different search capabilities across the document corpus:

1. **Semantic match** — finds water damage claims even without exact keyword match
2. **Technical terminology** — validates search across cyber/IT security domain
3. **Regulatory context** — tests retrieval of compliance documents
4. **Investigative content** — searches fraud case files for pattern recognition
""")


PROMPT_3_3 = """In INSURANCE_AI.OPS, implement a RAG pattern:

1. Question: "What are the most common fraud patterns in our portfolio, what are their root causes, and what detection methods have been most effective?"

2. Retrieve top 5 documents from INSURANCE_SEARCH, then pass to SNOWFLAKE.CORTEX.COMPLETE() with instructions to answer ONLY from the provided documents, cite doc_ids, and structure the answer with: 1) Common fraud types, 2) Detection indicators, 3) Investigation outcomes, 4) Recommendations for prevention.

Use claude-sonnet-4-6 as the model. Execute and show the RAG response."""

render_prompt("Prompt 3.3", "RAG Pattern: Search + Generate", PROMPT_3_3)

render_explanation("What this prompt does", """
Implements the full **RAG** pattern: retrieve relevant documents, then generate a grounded answer with citations.
""")


render_key_concepts([
    {"term": "Cortex Search Service", "definition": "A managed hybrid search engine created with SQL. Handles embedding, indexing, reranking, and auto-refresh automatically."},
    {"term": "RAG", "definition": "Retrieval Augmented Generation: retrieve documents, include as context in LLM prompt, generate grounded answer."},
    {"term": "Hybrid Search", "definition": "Combining vector search (semantic similarity) with keyword search (exact matching). Better than either alone."},
])

render_what_you_built([
    "INSURANCE_KNOWLEDGE_BASE — unified document table",
    "INSURANCE_SEARCH — Cortex Search service with hybrid search",
    "Search queries across multiple document types",
    "Full RAG pipeline for grounded Q&A",
])
