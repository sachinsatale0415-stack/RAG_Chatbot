import os
from langchain_community.llms import Ollama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vector_db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2}
)

llm = Ollama(
    model="mistral",
    temperature=0.2,
    num_ctx=2048
)

qa_cache = {}

def ask_question(question):
    
    if question in qa_cache:
        return qa_cache[question]
  
    docs = retriever.get_relevant_documents(question)

    context = "\n\n".join(doc.page_content for doc in docs)
   
    prompt = f"""
Answer the question strictly using the given context.
Do not add extra information.

Context:
{context}

Question:
{question}

Answer:
"""

    
    answer = llm.invoke(prompt)

    
    out_of_context_phrases = [
        "does not mention",
        "does not contain information",
        "cannot be determined",
        "not provided in the context",
        "missing from the provided data"
    ]

    if any(phrase in answer.lower() for phrase in out_of_context_phrases):
        qa_cache[question] = (answer, [])
        return answer, []  

    
    sources = {
        f"{doc.metadata.get('source')} (page {doc.metadata.get('page', 'N/A')})"
        for doc in docs
    }

    
    qa_cache[question] = (answer, sources)

    return answer, sources


def generate_mcqs(topic, num_questions=4):
    
    docs = retriever.get_relevant_documents(topic)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are an exam question generator.

Using ONLY the given context, generate {num_questions} MCQ questions on the topic "{topic}".

STRICT FORMAT (follow exactly):

Q1. Question text
a) option A    b) option B
c) option C    d) option D
Answer: correct option letter

Rules:
- Each question must have exactly 4 options
- Put options a & b on the same line
- Put options c & d on the next line
- Answer must be on a new line
- No extra explanation
- No paragraphs
- No markdown
- No numbering outside Q1, Q2, etc.

Context:
{context}
"""

    
    mcqs = llm.invoke(prompt)

    return mcqs.strip()
