from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List

class VectorManager:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=80)

    def build_and_save(self, docs: List[Document], save_path="vector_db/faiss_index"):
        chunks = self.splitter.split_documents(docs)
        print(f"Building vector database with {len(chunks)} chunks...")
        vector_db = FAISS.from_documents(chunks, self.embeddings)
        vector_db.save_local(save_path)
        print(f"✅ Index saved to {save_path}")
        return vector_db