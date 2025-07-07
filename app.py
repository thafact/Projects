import streamlit as st
from utils import extract_text_from_pdf, check_scuML_with_gemini

st.set_page_config(page_title="SCUML Checker AI", layout="centered")
st.title("SCUML Checker AI (Gemini-powered)")

st.markdown(
    "Upload the first 2–3 pages of your company's Memorandum of Association (MoA). "
    "This tool uses Google's Gemini AI to determine if SCUML registration is required."
)

uploaded_file = st.file_uploader("Upload MoA (PDF only)", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading and analyzing your document..."):
        text = extract_text_from_pdf(uploaded_file)
        result = check_scuML_with_gemini(text)

    st.subheader("Extracted Business Objectives")
    st.text_area("Text Preview", text[:2000], height=200)

    st.subheader("SCUML Registration Status")
    st.success(f"SCUML Status: {result['status']}")
    st.info(result["explanation"])

    if result["keywords"]:
        st.subheader("AI-Detected Keywords")
        st.write(", ".join(result["keywords"]))
