from pathlib import Path
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
load_dotenv()

DATA_DIR = "data"

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

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("local embedding model loaded ...................")
vector_store = Chroma.from_documents(
    documents=all_chunks,
    embedding=embeddings,
    persist_directory="./chroma_db",
)

print("Vector DB Created Successfully yeeeh................. ")
