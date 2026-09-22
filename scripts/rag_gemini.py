import chromadb

print("[1] Starting RAG...")

# ChromaDB 연결
chroma_client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = chroma_client.get_collection(
    name="security_documents"
)

print("[2] ChromaDB connected")

# 사용자 질문
question = "How can I improve account security?"

print()
print("Question:", question)

# 관련 문서 검색
results = collection.query(
    query_texts=[question],
    n_results=3
)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

print()
print("[3] Documents retrieved:", len(documents))

# 검색 결과 출력
print()
print("=" * 60)
print("RETRIEVED DOCUMENTS")
print("=" * 60)

for i, (document, metadata, distance) in enumerate(
    zip(documents, metadatas, distances),
    start=1
):
    source = metadata.get(
        "source",
        "Unknown source"
    )

    print()
    print(f"[Document {i}]")
    print("-" * 60)
    print(document)

    print()
    print("Source:", source)
    print("Distance:", round(distance, 4))

# RAG 답변 생성
print()
print("=" * 60)
print("RAG ANSWER")
print("=" * 60)

print()
print("Based on the retrieved security documents,")

print("you can improve account security by:")

print()

for i, (document, metadata) in enumerate(
    zip(documents, metadatas),
    start=1
):
    source = metadata.get(
        "source",
        "Unknown source"
    )

    print(f"{i}. {document}")
    print(f"   Citation: {source}")
    print()

print("=" * 60)
print("RAG pipeline completed successfully!")
print("=" * 60)