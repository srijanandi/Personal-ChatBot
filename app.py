import streamlit as st
import requests

from app.config import CHAT_URL, THROUGHPUT_URL, UPLOAD_URL
from app.services.websearch import WebSearch

st.set_page_config(page_title="RAG Chatbot", layout="centered")

st.title("RAG Chatbot POC")
st.subheader("Upload a document and ask questions!")


uploaded_file = st.file_uploader("Upload file", type=["txt", "pdf", "ppt", "pptx", "xls", "xlsx"])
query = st.text_input("Ask a question")

if uploaded_file:
    with st.spinner("Uploading..."):
        response = requests.post(
            UPLOAD_URL,
            files={"file": (uploaded_file.name, uploaded_file, uploaded_file.type)},
        )
    if response.status_code == 200:
        st.success("File uploaded and indexed successfully.")
    else:
        st.write(response.text)
        st.error(f"Upload failed. Status code: {response.status_code}")

use_web = st.checkbox("Include web search")
measure_throughput = st.checkbox("Measure throughput and memory usage")
if st.button("Ask") and query:
    with st.spinner("Thinking..."):
        web_result = ""
        if use_web:
            web_result = WebSearch.web_search(query)
        context = ""
        # To fetch context from backend or keep as is
        if web_result:
            context += f"\nWeb Search Result:\n{web_result}"
        if measure_throughput:
            responseForThroughput = requests.post(THROUGHPUT_URL, data={"query": query})
            if responseForThroughput.status_code == 200:
                st.markdown(f"**Throughput and Memory:** {responseForThroughput.json()['throughput']} queries/sec")
        response = requests.post(CHAT_URL, data={"query": query,"context": context})
    if response.status_code == 200 :
        st.markdown(f"**Answer:** {response.json()['answer']}")
    else:
        st.error("Something went wrong.")