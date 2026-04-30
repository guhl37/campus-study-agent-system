from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_BASE_URL"),
    model="embedding-2"
)

VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH", "./vector_store")

def create_vector_store(docs, store_name="course_knowledge"):
    store_path = os.path.join(VECTOR_STORE_PATH, store_name)
    os.makedirs(VECTOR_STORE_PATH, exist_ok=True)
    
    if not os.path.exists(store_path):
        vector_store = FAISS.from_documents(docs, embeddings)
        vector_store.save_local(store_path)
    else:
        vector_store = FAISS.load_local(store_path, embeddings, allow_dangerous_deserialization=True)
        vector_store.add_documents(docs)
        vector_store.save_local(store_path)
    
    return vector_store

def load_vector_store(store_name="course_knowledge"):
    store_path = os.path.join(VECTOR_STORE_PATH, store_name)
    if not os.path.exists(store_path):
        raise FileNotFoundError("课程向量库不存在")
    return FAISS.load_local(store_path, embeddings, allow_dangerous_deserialization=True)
