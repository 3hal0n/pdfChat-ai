import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from transformers import pipeline
from htmlTemplates import css

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text and len(page_text.strip()) > 50:  # skip very short/empty pages
                text += page_text
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,  # increased chunk size for fewer chunks
        chunk_overlap=100,  # keep overlap moderate
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    pipe = pipeline("text2text-generation", model="google/flan-t5-large")
    llm = HuggingFacePipeline(pipeline=pipe)
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.warning("Please upload and process your PDFs first!")
        return

    # Prepend a friendly system prompt to the user's question
    friendly_prompt = (
        "You are a helpful assistant. Please answer in a friendly, clear, and concise way.\n\n"
        f"User question: {user_question}"
    )
    response = st.session_state.conversation.invoke({'question': friendly_prompt})
    # Try to get the answer from the response
    answer = response.get('answer', '') or response.get('result', '') or ''

    # Store chat history as a list of (user, bot) tuples
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    st.session_state.chat_history.append((user_question, answer.strip()))

    # Display chat history
    for user_msg, bot_msg in st.session_state.chat_history:
        st.markdown(f"<div class='chat-bubble user-bubble'>{user_msg}</div>", unsafe_allow_html=True)
        user_friendly_answer = f"🤖 Here’s what I found for you:\n\n{bot_msg}"
        st.markdown(f"<div class='chat-bubble bot-bubble'>{user_friendly_answer}</div>", unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="PDF Chat AI", page_icon=":books:", layout="wide")
    st.markdown(css, unsafe_allow_html=True)

    st.markdown(
        """
        <h1 style='text-align:center; margin-bottom: 0;'>PDF Chat AI📚</h1>
        <p style='text-align:center; color:#a5b4fc; margin-top:0;'>Chat with your documents in style!</p>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.markdown("<div class='stFileUploader'>", unsafe_allow_html=True)
        st.subheader("Upload PDFs")
        pdf_docs = st.file_uploader("Select PDF files", accept_multiple_files=True, type=["pdf"])
        if st.button("Process"):
            with st.spinner("Processing..."):
                #get pdf text
                raw_text = get_pdf_text(pdf_docs)

                #get the text chunks
                text_chunks = get_text_chunks(raw_text)

                #create vector store
                vectorstore = get_vectorstore(text_chunks)

                #create conversation chain
                st.session_state.conversation = get_conversation_chain(
                    vectorstore)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.subheader("Ask a question")
        user_question = st.text_input("Type your question here...")
        if user_question:
            handle_userinput(user_question)

if __name__ == "__main__":
    main()
