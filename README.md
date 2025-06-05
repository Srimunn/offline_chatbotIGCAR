# PDF Knowledge Assistant

A RAG (Retrieval-Augmented Generation) system that allows users to upload PDF documents and ask questions about their content. The system uses Ollama for embeddings and LLM capabilities, along with ChromaDB for vector storage.

## Features

- Upload multiple PDF documents
- Process and index document content
- Ask questions about the uploaded documents
- Get answers with source references
- User-friendly Gradio interface

## Requirements

- Python 3.8+
- Ollama installed with the deepseek-r1 model
- Dependencies listed in requirements.txt

## Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd pdf-knowledge-assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make sure Ollama is installed and the deepseek-r1 model is available:
```bash
ollama pull deepseek-r1
```

4. Run the application:
```bash
python chat.py
```

The application will be available at http://localhost:7860

## Usage

1. Upload one or more PDF files using the file upload interface
2. Click "Initialize System" to process the documents
3. Once the system is ready, type your question in the input box
4. Click "Ask Question" to get an answer based on the document content

## Note

Make sure you have enough system resources as processing large PDF files may require significant memory and computational power. 