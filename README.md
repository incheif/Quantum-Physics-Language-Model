# Quantum-Physics-Language-Model
This project leverages advanced language model capabilities to facilitate the analysis of quantum physics research papers. Users can interact with the system by asking questions, and the model generates responses both with and without context from uploaded documents. This application utilizes LangChain, Groq, and Google Generative AI Embeddings to streamline research and analysis workflows.

Features

Document Embedding and Retrieval:

Converts research papers into vector embeddings using Google Generative AI Embeddings.

Organizes documents into a FAISS vector store for efficient retrieval.

Interactive Question-Answering:

Answers user queries using both document-based context and general model knowledge.

Displays relevant document excerpts for context-based answers.

Customizable Prompt Templates:

Utilizes structured templates to tailor the language model's responses.

Streamlit Interface:

Provides an intuitive and user-friendly interface for question input and answer display.

Supports real-time interactions and visualizes relevant document excerpts.

Installation and Setup

Prerequisites

Ensure you have the following installed:

Python 3.8+

pip or conda

Streamlit

Dependencies

Install required Python libraries:

pip install streamlit langchain langchain-google-genai langchain-community langchain-groq faiss-cpu

API Keys

The application requires API keys for Google Generative AI and Groq.

Set your API keys in the environment variables:

export GOOGLE_API_KEY="your_google_api_key"
export groq_api_key="your_groq_api_key"

Alternatively, directly modify the keys in the os.environ section of the code:

os.environ["GOOGLE_API_KEY"] = "your_google_api_key"
os.environ["groq_api_key"] = "your_groq_api_key"

Data Preparation

Save your research papers as PDFs in a folder named data at the root of the project directory.

Usage

Run the Application:
Launch the Streamlit app:

streamlit run app.py

Initialize Embedding:

Click the "Initialize Document Embedding" button to process and store embeddings of your uploaded documents.

Ask Questions:

Enter a question in the input box and click submit to receive answers with and without document context.

View Results:

The application displays context-based responses alongside the relevant document excerpts.

General responses (without context) are also provided.

Upload Screenshots:

Add screenshots of the application interface for reference in the screenshots/ directory and mention them in the relevant sections below.

File Structure

quantum-physics-research-analysis/
├── app.py               # Main application file
├── data/                # Directory for storing research papers (PDF format)
├── screenshots/         # Directory for storing application screenshots
├── README.md            # Documentation for the project
├── requirements.txt     # Python dependencies

Key Components

Technologies Used

LangChain: Framework for building applications with LLMs.

Groq: LLM provider for high-performance inference.

Google Generative AI: Embedding model for document vectorization.

FAISS: Library for efficient similarity search.

Streamlit: Frontend framework for interactive UI.

Main Functions

initialize_vector_store:
Loads PDF documents, splits them into chunks, and converts them into embeddings stored in a FAISS vector database.

create_retrieval_chain_with_context:
Establishes a document retrieval chain for generating context-aware answers.

handle_user_question:
Manages user queries and provides both context-based and general responses.

Example Workflow

Upload quantum physics research papers into the data directory.

Initialize embeddings through the Streamlit interface.

Ask a question (e.g., "Explain quantum entanglement").

Receive answers with and without relevant document excerpts.

Screenshots

Include relevant screenshots of the application interface here. Place all screenshots in the screenshots/ directory and reference them using markdown syntax:

![Screenshot Description](screenshots/example.png)

Future Enhancements

Integration with additional embedding models for broader compatibility.

Support for more file formats (e.g., Word documents, text files).

Enhanced UI with visualization of embeddings.

Fine-tuning LLMs on specific quantum physics datasets.

License

This project is licensed under the MIT License. See the LICENSE file for details.
