from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings,
)

query = "Can you tell about the quiesy project that is made by me "

results = vector_store.similarity_search(
    query,
    k=3
)

for i, doc in enumerate(results, start=1):
    print(f"\n{'='*50}")
    print(f"Result {i}")
    print(f"{'='*50}")

    print("\nMetadata:")
    print(doc.metadata)

    print("\nContent:")
    print(doc.page_content[:1000])