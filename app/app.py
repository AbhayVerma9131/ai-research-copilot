import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.pdf_loader import extract_text_from_pdf
from src.summarizer import summarize_text
from src.qa_engine import answer_question

st.title("📄 AI Research Copilot")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("📌 Summary")
    summary = summarize_text(text)
    st.write(summary)

    st.subheader("❓ Ask a Question")
    question = st.text_input("Enter your question")

    if question:
        answer = answer_question(question, text)
        st.write("Answer:", answer)
