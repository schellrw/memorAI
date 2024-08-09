from dataclasses import dataclass
from typing import Literal
import streamlit as st
from langchain_pinecone.vectorstores import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.retrievers import MergerRetriever
from dotenv import load_dotenv
import os
from utils import process
from langchain_community.vectorstores import Chroma as LangChainChroma
from pinecone import Pinecone #, ServerlessSpec
import chromadb
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Load environment variables from the .env file
load_dotenv()

# Fetch environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL")
CHAT_MODEL = os.getenv("CHAT_MODEL")

# Supplement with streamlit secrets if None
if None in [PINECONE_API_KEY, PINECONE_INDEX, HUGGINGFACE_API_TOKEN, EMBEDDINGS_MODEL, CHAT_MODEL]:
    PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
    PINECONE_INDEX = st.secrets["PINECONE_INDEX"]
    HUGGINGFACE_API_TOKEN = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
    EMBEDDINGS_MODEL = st.secrets["EMBEDDINGS_MODEL"]
    CHAT_MODEL = st.secrets["CHAT_MODEL"]

# Configure OpenAI API (replace with your chosen LLM API)
openai.api_key = 'your-api-key'

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/generate_mnemonic', methods=['POST'])
def generate_mnemonic():
    data = request.json
    text_to_remember = data['text']
    mnemonic_type = data['type']

    # Here you would call your LLM to generate the mnemonic
    # This is a placeholder for the actual LLM call
    prompt = f"Create a {mnemonic_type} mnemonic for: {text_to_remember}"
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
    
    mnemonic = response.choices[0].text.strip()

    return jsonify({'mnemonic': mnemonic})

@app.route('/upload_document', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Here you would process the document and use it for RAG
        # This is a placeholder for the actual RAG implementation
        return jsonify({'message': 'File uploaded successfully'})
    
    return jsonify({'error': 'File type not allowed'})

if __name__ == '__main__':
    app.run(debug=True)