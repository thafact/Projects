import streamlit as st
from utils import extract_text_from_pdf, check_scuML_keywords

st.set_page_config(page_title="SCUML Checker AI", layout="centered")
st.title("SCUML Checker AI")

st.markdown("Upload the first 2–3 pages of your company’s Memorandum of Association (MoA). We will check if SCUML registration is required.")

uploaded_file = st.file_uploader("Upload MoA (PDF only)", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading document..."):
        text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Business Objectives")
    st.text_area("Text Preview", text[:2000], height=200)

    with st.spinner("Analyzing..."):
        result = check_scuML_keywords(text)

    st.subheader("SCUML Registration Status")
    st.success(f"SCUML Status: {result['status']}")
    st.info(result["explanation"])

    if result["matched_keywords"]:
        st.markdown("Detected Keywords:")
        for kw in result["matched_keywords"]:
            st.markdown(f"- {kw}")
