import os
from dotenv import load_dotenv

load_dotenv()

from src.loaders import load_pdf_pages
from src.metadata import add_llm_metadata

BOOK_PATH = "/mnt/c/BooksForRag/andrew-ng-machine-learning-yearning.pdf"

def main():
    print("--- Reading PDF and Adding Metadata (GROQ CLOUD MODE) ---")
    
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("No Groq Key found in environment. Please set GROQ_API_KEY in your .env file.")
        return

    documents = load_pdf_pages(BOOK_PATH)[:10]
    
    enriched_docs = add_llm_metadata(documents, api_key)
    
    print("\n" + "="*30)
    print("SUMMARIZATION TEST RESULTS")
    print("="*30)
    for doc in enriched_docs:
        print(f"Page {doc.metadata['page_number']}: {doc.metadata['page_description']}")
        print("-" * 30)

if __name__ == "__main__":
    main()