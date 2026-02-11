import streamlit as st
from rag_backend import ask_question

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="centered"
)


st.markdown("<h1 style='text-align:center;'>🤖 RAG Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Ask questions from your documents</p>", unsafe_allow_html=True)

st.divider()


question = st.text_area(
    "Enter your question",
    height=80,
    placeholder="e.g. What is Big Data?"
)


ask_button = st.button("Ask", use_container_width=True)


if ask_button:
    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            answer, sources = ask_question(question)

        st.success("Answer")
        st.write(answer)

        st.divider()

        st.markdown("### Sources")
        for s in sources:
            st.write(f"- {s}")
