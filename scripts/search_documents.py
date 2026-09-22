import chromadb

DB_DIR = "chroma_db"
COLLECTION_NAME = "security_documents"

client = chromadb.PersistentClient(path=DB_DIR)

collection = client.get_collection(
    name=COLLECTION_NAME
)

question = "How can I improve account security?"

print()
print("Question:", question)
print("=" * 60)

results = collection.query(
    query_texts=[question],
    n_results=3
)

documents = results["documents"][0]
metadatas = results["metadatas"][0]

print("Relevant documents:")
print()

for i, (document, metadata) in enumerate(
    zip(documents, metadatas),
    start=1
):
    print(f"[Result {i}]")
    print(document)
    print(f"Source: {metadata['source']}")
    print("-" * 40)