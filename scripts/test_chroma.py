import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="security_documents"
)

collection.add(
    ids=["test-1"],
    documents=[
        "Multi-factor authentication can provide additional protection."
    ]
)

print("ChromaDB test successful!")
print("Document count:", collection.count())
