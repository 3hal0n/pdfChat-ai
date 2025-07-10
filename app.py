import streamlit as st
from htmlTemplates import css

def main():
    st.set_page_config(page_title="PDF Chat Pro", page_icon=":books:", layout="wide")
    st.markdown(css, unsafe_allow_html=True)

    st.markdown(
        """
        <h1 style='text-align:center; margin-bottom: 0;'>PDF Chat Pro 📚</h1>
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
                # TODO Add PDF processing logic here
                st.success("PDFs processed! (placeholder)")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.subheader("Ask a question")
        user_question = st.text_input("Type your question here...")
        if user_question:
            # TODO: Replace with real chat logic
            st.markdown(f"<div class='chat-bubble user-bubble'>{user_question}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='chat-bubble bot-bubble'>This is a sample bot response.</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

