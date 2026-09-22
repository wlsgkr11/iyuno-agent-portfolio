from pathlib import Path
import chromadb

DATA_DIR = Path("data/public")
DB_DIR = "chroma_db"
COLLECTION_NAME = "security_documents"

print("[1] Starting document ingestion...")

client = chromadb.PersistentClient(path=DB_DIR)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)

print("[2] ChromaDB connected")

files = list(DATA_DIR.glob("*.md"))

print(f"[3] Documents found: {len(files)}")

total_chunks = 0

for file_path in files:
    print()
    print(f"Processing: {file_path.name}")

    text = file_path.read_text(
        encoding="utf-8"
    )

    raw_chunks = [
        chunk.strip()
        for chunk in text.split("\n\n")
        if chunk.strip()
    ]

    # 너무 짧은 Chunk 제거
    chunks = [
        chunk
        for chunk in raw_chunks
        if len(chunk) >= 80
    ]

    print(f"Chunks: {len(chunks)}")

    ids = []
    documents = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        ids.append(f"{file_path.stem}-{i}")
        documents.append(chunk)
        metadatas.append(
            {
                "source": file_path.name
            }
        )

    if documents:
        collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )

    total_chunks += len(chunks)

print()
print("=" * 60)
print("Document ingestion completed!")
print("Documents:", len(files))
print("Total chunks:", total_chunks)
print("=" * 60)