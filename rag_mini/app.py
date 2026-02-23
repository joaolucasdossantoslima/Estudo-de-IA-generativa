import streamlit as st
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import HugginFaceHub
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

st.set_page_config(page_title="RAG com Hugging Face", layout="centered")
st.title("📚 RAG com PDF (Hugging Face)")
st.write("Envie um PDF e faça perguntas sobre ele.")

uploaded_file = st.file_uploader("Envie seu PDF", type="pdf")

if uploaded_file is not None:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF carregado com sucesso!")

    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )

    docs = text_splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name= "sentence-transforms/all miniLM - v2")

    vectorstore= chroma.from_documents(
        docs,
        embeddings,
        persist_directory="./cho"
    )

    llm = HugginFaceHub(
        repo_id = "mistralai/Mistral-7B-Instruct-0.1",
        model_kwargs={"temperature":0.3,"max_new_tokens":512},

        HugginFaceHub_api_token=os.getenv("HUGGINFACEHUB_API_TOKEN")
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm
        retriever=vectorstore.as_retriever(serach_kwargs={"k":3})
    )
    