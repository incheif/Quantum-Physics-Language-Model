import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import time

# Set API keys directly
google_api_key = "GOOGLE_API_KEY"
groq_api_key = "GROQ_API_KEY"

os.environ["GOOGLE_API_KEY"] = google_api_key
os.environ["groq_api_key"] = groq_api_key

st.title("Quantum Physics Research Analysis: Using Large Language Model")

# Initialize LLM
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192", max_tokens=2048)

# Define prompt template
prompt_template = ChatPromptTemplate.from_template(
    """
    <context>
    {context}
    <context>
    Questions: {input}
    """
)

def initialize_vector_store(data_path="./data"):
    """Initialize vector embeddings and FAISS vector store."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    loader = PyPDFDirectoryLoader(data_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_documents = text_splitter.split_documents(documents[:20])  # Limit for performance
    vectors = FAISS.from_documents(final_documents, embeddings)
    return vectors

def create_retrieval_chain_with_context(llm, vectors):
    """Create a retrieval chain using the LLM and vector store."""
    retriever = vectors.as_retriever()
    document_chain = create_stuff_documents_chain(llm, prompt_template)
    return create_retrieval_chain(retriever, document_chain)

def handle_user_question(question, retrieval_chain):
    """Handle user question and generate responses with and without context."""
    responses = {}

    # With context
    start = time.process_time()
    try:
        response_with_context = retrieval_chain.invoke({'input': question})
        responses['with_context'] = {
            "response_time": time.process_time() - start,
            "answer": response_with_context.get('answer', "No answer generated."),
            "context": response_with_context.get('context', [])
        }
    except Exception as e:
        st.error(f"Error during context-based response: {e}")
        responses['with_context'] = {"response_time": None, "answer": "Error generating response.", "context": []}

    # Without context
    prompt_without_context = f"Answer the following question as accurately as possible: {question}"
    start = time.process_time()
    try:
        raw_response = llm.invoke(prompt_without_context)
        response_text = raw_response.content if hasattr(raw_response, 'content') else "No response content."
        responses['without_context'] = {
            "response_time": time.process_time() - start,
            "answer": response_text
        }
    except Exception as e:
        st.error(f"Error during general response: {e}")
        responses['without_context'] = {"response_time": None, "answer": "Error generating response."}

    return responses

# Streamlit UI
st.subheader("Interactive Q&A")
question = st.text_input("Enter your question:")

if st.button("Initialize Document Embedding"):
    if "vectors" not in st.session_state:
        st.session_state.vectors = initialize_vector_store()
        st.write("Vector store initialized successfully.")

if question and "vectors" in st.session_state:
    st.session_state.retrieval_chain = create_retrieval_chain_with_context(llm, st.session_state.vectors)
    responses = handle_user_question(question, st.session_state.retrieval_chain)

    if 'with_context' in responses:
        st.subheader("Response with Context:")
        st.text_area("Answer", responses['with_context']['answer'], height=600)
        with st.expander("Relevant Documents:"):
            for doc in responses['with_context']['context']:
                st.write(doc.page_content)
                st.write("--------------------------------")

    if 'without_context' in responses:
        st.subheader("Response without Context:")
        st.text_area("General Answer", responses['without_context']['answer'], height=600)
