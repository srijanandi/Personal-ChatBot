# RAG Chatbot POC

A Proof-of-Concept Retrieval-Augmented Generation (RAG) chatbot that allows users to upload documents, ask questions, and receive answers generated using both document retrieval and large language models (LLMs). The system supports web search augmentation and provides performance metrics.

---

## Features

- **Document Upload:** Upload `.txt`, `.pdf`, `.ppt`, `.pptx`, `.xls`, `.xlsx` files for indexing.
- **Chunking & Embedding:** Documents are chunked and embedded for efficient retrieval.
- **Vector Search:** Uses FAISS for fast similarity search over document embeddings.
- **LLM Integration:** Answers are generated using an LLM (via Ollama).
- **Web Search Augmentation:** Optionally include web search results in answers.
- **Chat History:** Maintains conversation history in the UI.
- **Performance Metrics:** Measure throughput and memory usage.
- **Streamlit Frontend:** Simple and interactive web UI.

---

## Project Structure

```
├── app/
│   ├── main.py              # FastAPI backend
│   ├── config.py            # Configuration variables
│   ├── services/
│   │   ├── llm_client.py    # LLM interface
│   │   ├── vectordb.py      # FAISS vector DB logic
│   │   └── websearch.py     # Web search integration
│   └── utils/
│       └── helpers.py       # Utility functions
├── app.py                   # Streamlit frontend
├── tests/
│   └── test_integration.py  # Integration tests
├── test.txt                 # Sample document for testing
└── README.md
```

---

## Setup & Installation

1. **Clone the repository:**
   ```
   git clone <repo-url>
   cd rag-chatbot-poc-fixed
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Start the FastAPI backend:**
   ```
   uvicorn app.main:app --reload
   ```

4. **Start the Streamlit frontend:**
   ```
   streamlit run app.py
   ```

---

## Usage

1. Open the Streamlit app in your browser.
2. Upload a document.
3. Enter your question in the chat box.
4. (Optional) Check "Include web search" to augment answers with web results.
5. (Optional) Check "Measure throughput and memory usage" for performance metrics.
6. View answers and chat history.

---

## Testing

- Place a sample file named `test.txt` in the project root.
- Run integration tests:
  ```
  pytest tests/test_integration.py
  ```

---

## Configuration

Edit `app/config.py` to set:
- Model names
- Chunk size
- Vector DB path
- API URLs

---

## Key Libraries Used

- **FastAPI**: Backend API framework
- **Streamlit**: Frontend web UI
- **FAISS**: Vector similarity search
- **Ollama**: LLM inference
- **Hugging Face Transformers**: (optional, for embeddings/LLMs)
- **requests, numpy, pickle, psutil**: Utilities

---

## Notes

- Ensure you have enough system memory for the selected LLM.
- For production, use a smaller LLM or deploy on a machine with more RAM.
- Web search uses DuckDuckGo's Instant Answer API as a demo; replace with a production search API as needed.

---


- [Hugging Face](https://huggingface.co/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
