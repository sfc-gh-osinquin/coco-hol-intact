import streamlit as st

st.title("Workshop agenda")

AGENDA = [
    ("12:45 PM", "Arrival & Coffee", None, None),
    ("1:00 PM", "Welcome & Workshop Overview", None, None),
    ("1:15 PM", "Session 1: Data Prep", "30 min", "1"),
    ("1:45 PM", "Session 2: Cortex Analyst & Semantic Views", "30 min", "2"),
    ("2:15 PM", "Session 3: Cortex Search", "30 min", "3"),
    ("2:45 PM", ":orange-badge[BREAK]", None, None),
    ("3:00 PM", "Session 4: Cortex Agents", "35 min", "4"),
    ("3:35 PM", "Session 5: CoWork", "25 min", "5"),
    ("4:00 PM", "Session 6: Streamlit", "30 min", "6"),
]

for time, title, duration, session_num in AGENDA:
    if session_num:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f":material/play_circle: **{title}** :gray-badge[{duration}]")
    elif "BREAK" in title:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f"{title}")
    else:
        col1, col2 = st.columns([1, 4])
        col1.markdown(f"**{time}**")
        col2.markdown(f":gray[{title}]")

st.space("medium")

st.markdown("##### What you'll build by end of session")
st.markdown("""
| Object Type | Count | Examples |
|-------------|-------|---------|
| **Tables** | 9 | Claims, policies, risk scores, fraud investigations |
| **Cortex Search Services** | 1 | INSURANCE_SEARCH |
| **Semantic Views** | 1 | INSURANCE_OPERATIONS_VIEW with relationships, metrics, and AI instructions |
| **Cortex Agents** | 1 | INSURANCE_AGENT with Analyst + Search + custom tools |
| **Streamlit Apps** | 1 | Operations dashboard with AI chat |
""")

st.space("small")

st.markdown("##### Location")
with st.container(border=True):
    st.markdown("""
:material/location_on: **Intact Insurance Office, Toronto, ON**

July 29, 2026 — 1:00 PM to 5:00 PM
""")
