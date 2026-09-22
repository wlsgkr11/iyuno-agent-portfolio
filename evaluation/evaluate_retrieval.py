import json
import time

import chromadb


DB_DIR = "chroma_db"
COLLECTION_NAME = "security_documents"
QUESTIONS_FILE = "evaluation/questions.json"


print("[1] Starting retrieval evaluation...")


# ChromaDB 연결
client = chromadb.PersistentClient(
    path=DB_DIR
)

collection = client.get_collection(
    name=COLLECTION_NAME
)

print("[2] ChromaDB connected")


# 평가 질문 불러오기
with open(
    QUESTIONS_FILE,
    "r",
    encoding="utf-8"
) as f:
    questions = json.load(f)

print("[3] Questions loaded:", len(questions))


# 평가 설정
k = 3

total = len(questions)
hits = 0

latencies = []

results = []


print()
print("=" * 60)
print("RETRIEVAL EVALUATION")
print("=" * 60)


for item in questions:

    question = item["question"]
    expected_source = item["expected_source"]

    start_time = time.perf_counter()

    search_result = collection.query(
        query_texts=[question],
        n_results=k
    )

    elapsed = time.perf_counter() - start_time

    documents = search_result["documents"][0]
    metadatas = search_result["metadatas"][0]

    retrieved_sources = [
        metadata.get(
            "source",
            "Unknown source"
        )
        for metadata in metadatas
    ]

    hit = expected_source in retrieved_sources

    if hit:
        hits += 1

    latencies.append(elapsed)

    results.append(
        {
            "id": item["id"],
            "question": question,
            "expected_source": expected_source,
            "retrieved_sources": retrieved_sources,
            "hit_at_3": hit,
            "latency_seconds": round(
                elapsed,
                4
            )
        }
    )

    status = "HIT" if hit else "MISS"

    print(
        f"[{status}] "
        f"{item['id']:02d}. "
        f"{question}"
    )


# Recall@3 계산
recall_at_3 = hits / total

# 평균 검색 시간
average_latency = sum(latencies) / total


print()
print("=" * 60)
print("EVALUATION RESULT")
print("=" * 60)

print()
print("Total questions:", total)

print(
    "Hits:",
    hits
)

print(
    "Misses:",
    total - hits
)

print(
    "Recall@3:",
    round(
        recall_at_3,
        4
    )
)

print(
    "Average latency:",
    round(
        average_latency,
        4
    ),
    "seconds"
)


# 결과 저장
output = {
    "total_questions": total,
    "hits": hits,
    "misses": total - hits,
    "recall_at_3": round(
        recall_at_3,
        4
    ),
    "average_latency_seconds": round(
        average_latency,
        4
    ),
    "results": results
}


with open(
    "evaluation/results.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        output,
        f,
        ensure_ascii=False,
        indent=2
    )


print()
print(
    "Saved: evaluation/results.json"
)

print("=" * 60)
print("Evaluation completed!")
print("=" * 60)