from typing import List
from langchain_core.documents import Document
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

class PageSummarizer:
    def __init__(self, api_key: str):
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile", 
            groq_api_key=api_key,
            temperature=0
        )
        self.prompt = ChatPromptTemplate.from_template(
            "Analyze the following PDF page content carefully. "
            "Provide a detailed summary (around 50-80 words) highlighting the main concepts, "
            "technical directions, and any key takeaways. "
            "If it's a cover or empty, just say 'Empty or OCR-unreadable page':\n\n{content}"
                )
        self.chain = self.prompt | self.llm

    def summarize(self, text: str) -> str:
        if not text.strip() or len(text.strip()) < 50:
            return "Empty or OCR-unreadable page"
        try:
            return self.chain.invoke({"content": text}).content.strip()
        except Exception as e:
            return f"Groq Error: {e}"

def add_llm_metadata(docs: List[Document], api_key: str) -> List[Document]:
    summarizer = PageSummarizer(api_key=api_key)
    print(f"Generating Groq (Llama3) summaries for {len(docs)} pages...")
    for doc in docs:
        doc.metadata["page_description"] = summarizer.summarize(doc.page_content)
    return docs