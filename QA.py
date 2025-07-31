# from http import client
# from langchain.vectorstores import FAISS
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# # Embed and store transcript
# def build_vector_store(text):
#     splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#     chunks = splitter.split_text(text)
#     embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#     vectordb = FAISS.from_texts(chunks, embeddings)
#     return vectordb


# def answer_question(question, vectordb):
#     docs = vectordb.similarity_search(question, k=3)
#     context = "\n".join([doc.page_content for doc in docs])
#     prompt = f"Context:\n{context}\n\nAnswer the question: {question}"
#     completion = client.chat.completions.create(
#         messages=[{"role": "user", "content": prompt}],
#         model="llama3-8b-8192"
#     )
#     return completion.choices[0].message.content



from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_vector_store(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = FAISS.from_texts(chunks, embeddings)
    return vectordb

def answer_question(question, vectordb):
    docs = vectordb.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"Context:\n{context}\n\nAnswer the question: {question}"
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192"
    )
    return completion.choices[0].message.content
