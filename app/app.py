import streamlit as st

st.set_page_config(page_title="AI Research Copilot")

st.title("📄 AI Research Copilot")
st.write("Upload a research paper and ask questions!")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    st.success("File uploaded successfully!")
