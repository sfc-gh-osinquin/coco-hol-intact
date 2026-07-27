from pathlib import Path
import streamlit as st

_DIR = Path(__file__).parent.parent

st.title("Getting Started")
st.markdown("Provision a Snowflake account for the workshop")

st.space("small")

st.markdown("#### Step 1: Sign up for a free trial")

with st.container(border=True):
    st.markdown("""
Go to **[signup.snowflake.com](https://signup.snowflake.com/?t=cad5d6e9c8d431c2239aa81694b6b7951bff6edd23f9dc38facae3df7d11f780)** and fill out the registration form with your name, email, and company.

On the **Choose your Snowflake edition** screen, select:

| Setting | Recommended value |
|---------|-------------------|
| **Cloud provider** | Amazon Web Services (AWS) |
| **Edition** | Enterprise |
| **Region** | AWS Canada (Central) or US West (Oregon) |

Enterprise edition is recommended because it includes all the AI/ML features we use in this workshop.
""")

st.space("small")

st.markdown("#### Step 2: Activate your account")

with st.container(border=True):
    st.markdown("""
After submitting the form, Snowflake sends an **activation link** to the email address you provided. Click the link to set your password and log in.

:material/info: The activation email typically arrives within a few minutes. Check your spam folder if you don't see it.
""")

st.space("small")

st.markdown("#### Step 3: Open Cortex Code")

with st.container(border=True):
    st.markdown("""
Once logged in to Snowsight, open **Cortex Code** from the right navigation panel (white star icon in blue square). This is the AI coding assistant where you will paste all prompts from this workshop.

Confirm you are using the **ACCOUNTADMIN** role — you can check and switch roles in the bottom-left of the Snowsight UI.
""")

st.space("small")

st.markdown("#### Step 4: Enable cross-region inference")

with st.container(border=True):
    st.markdown("Several sessions use Cortex LLM models that require cross-region inference. Enable it by pasting the following prompt in CoCo:")
    st.image(str(_DIR / "static" / "coco_cross_region.png"), width=480)

st.space("small")

st.markdown("#### Free trial details")

col1, col2, col3 = st.columns(3)
col1.metric("Duration", "30 days", help="Free trial duration from activation")
col2.metric("Credits", "$400", help="Complimentary Snowflake credits included")
col3.metric("Credit card", "Not required", help="No payment method needed to start")

st.caption("The free trial provides more than enough credits to complete the entire workshop")
