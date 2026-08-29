import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Create Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

# Page configuration
st.set_page_config(
    page_title="AI Health Analyzer",
    page_icon="🩸",
    layout="wide"
)

# Title
st.title("🩸 AI Health Analyzer")

# Two-column layout
left_col, right_col = st.columns([1, 1])

# LEFT SIDE
with left_col:
    st.subheader("Blood Work Report")

    blood_report = st.text_area(
        "Paste your blood report",
        height=500,
        placeholder="Paste your blood work report here...",
        label_visibility="collapsed"
    )

    analyze_clicked = st.button(
        "Analyze Report",
        type="primary",
        use_container_width=True
    )

# RIGHT SIDE
with right_col:

    st.subheader("Health Analysis")

    health_box = st.container(border=True)

    with health_box:
        health_placeholder = st.empty()

    st.subheader("Suggested Diet Plan")

    diet_box = st.container(border=True)

    with diet_box:
        diet_placeholder = st.empty()


# ANALYSIS
if analyze_clicked:

    if not blood_report.strip():

        st.warning(
            "Please paste a blood work report before analyzing."
        )

    else:

        with st.spinner("Analyzing your blood report..."):

            final_prompt = f"""
You are a medical report analysis assistant.

Analyze the blood report provided below.

IMPORTANT RULES:
- Use only the information and reference ranges provided in the report.
- Do not diagnose any disease.
- Keep the explanation simple and concise.
- If a reference range is not provided for a test, do not guess one.

Perform the following tasks:

1. Identify the important blood test values.
   Mention whether each relevant value is HIGH, LOW, or NORMAL
   according to the reference range given in the report.

2. Write a short health summary in 2-3 lines explaining the
   important findings in simple language.

3. Give a short practical Indian diet plan.

The diet plan must contain ONLY these two sections:
- Food to avoid
- Food to eat more of

Return your response EXACTLY in the following format:

HEALTH ANALYSIS:

Important Values:
- Test Name: Value | Status: HIGH/LOW/NORMAL | Reference: Range

Summary:
<2-3 line simple health summary>

DIET PLAN:

Food to avoid:
- item
- item
- item

Food to eat more of:
- item
- item
- item


Blood Report:

{blood_report}
"""

            try:

                final_response = llm.invoke(final_prompt)

                result = final_response.text

                # Separate health analysis and diet plan
                if "DIET PLAN:" in result:

                    health_part, diet_part = result.split(
                        "DIET PLAN:",
                        1
                    )

                    health_part = health_part.replace(
                        "HEALTH ANALYSIS:",
                        ""
                    ).strip()

                    diet_part = diet_part.strip()

                else:
                    # Fallback in case Gemini changes formatting
                    health_part = result
                    diet_part = (
                        "Diet plan could not be separated "
                        "from the response."
                    )

                # Display results
                health_placeholder.markdown(
                    health_part
                )

                diet_placeholder.markdown(
                    diet_part
                )

            except Exception as e:

                st.error(
                    f"Something went wrong while analyzing "
                    f"the report: {e}"
                )