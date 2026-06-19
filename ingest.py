print("load start..........")
from pathlib import Path
import os 
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

from dotenv import load_dotenv
from langchain_chroma import Chroma
load_dotenv()

DATA_DIR = "data"

print("load khatam..........")
headers_to_split_on = [
    ("#", "h1"),
    ("##", "h2"),
    ("###", "h3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=False,
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

all_chunks = []

for file_path in Path(DATA_DIR).glob("*.md"):
    print(f"Processing: {file_path.name}")

    with open(file_path, "r", encoding="utf-8") as f:
        markdown_text = f.read()

    header_docs = markdown_splitter.split_text(markdown_text)

    chunks = text_splitter.split_documents(header_docs)

    for chunk in chunks:
        chunk.metadata["source"] = file_path.name

    all_chunks.extend(chunks)

print(f"\nTotal Chunks: {len(all_chunks)}")

print("\nSample Chunk:\n")
print(all_chunks[0].page_content[:500])

print("\nMetadata:")
print(all_chunks[0].metadata)

print("model loading starts ...................")

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

print("local embedding model loaded ...................")
from langchain_chroma import Chroma

vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

batch_size = 25

for i in range(0, len(all_chunks), batch_size):
    batch = all_chunks[i:i + batch_size]

    print(f"Adding batch {i} -> {i + len(batch)}")

    vector_store.add_documents(batch)

    import time
    time.sleep(20)

print("Vector DB Created Successfully yeeeh................. ")
