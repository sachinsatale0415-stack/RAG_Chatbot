# 🚀 LLM-Powered Multimodal RAG Chatbot

An intelligent **Retrieval-Augmented Generation (RAG) based chatbot** that answers user queries by retrieving relevant information from documents and generating responses strictly grounded in the retrieved context — minimizing hallucinations and improving answer accuracy.

👨‍💻 **Developed by:** Sachin Satale  

🎓 **Guided by:** Prof. Veena Sarda  


## 🌟 Overview

This project implements a Multimodal RAG (Retrieval-Augmented Generation) pipeline that enhances LLM responses with external knowledge retrieval.

Instead of relying only on the model’s memory, the chatbot:

1. Extracts knowledge from documents (PDF, TXT, Images)

2. Converts them into embeddings

3. Stores them in a vector database

4. Retrieves relevant chunks during queries

5. Generates grounded answers using an LLM


## ✅ Key Benefits

✔ Reduces hallucinations

✔ Context-aware answers

✔ Supports multiple file formats

✔ Scalable for enterprise use

✔ Works on private/custom datasets


## ✨ Features

• 📄 PDF / TXT document ingestion

• 🔎 Semantic search with vector embeddings

• 🧠 LLM-powered answer generation

• 💬 Conversational memory (chat history aware)

• ⚡ Fast retrieval using vector database

• 🌐 Web UI chatbot interface

## 🏗️ Architecture

User Query
   ↓
Retriever (Vector DB)
   ↓
Relevant Context
   ↓
LLM (RAG Prompting)
   ↓
Generated Answer


## Detailed Flow

1. Documents uploaded

2. Text extraction (PDF/OCR)

3. Chunking

4. Embedding generation

5. Stored in Vector DB

6. User query → embedding

7. Top-K similarity search

8. Context + Query → LLM

9. Final grounded answer
