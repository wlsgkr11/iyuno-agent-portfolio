import json
import re
import chromadb

QUESTIONS_FILE = "evaluation/questions.json"
OUTPUT_FILE = "evaluation/faithfulness_results.json"
METRICS_FILE = "evaluation/faithfulness_metrics.json"

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection(name="security_documents")

with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
    questions = json.load(f)

results = []
faithful_count = 0

for item in questions:
    question = item["question"]
    expected_source = item["expected_source"]

    result = collection.query(
        query_texts=[question],
        n_results=3
    )

    documents = result["documents"][0]
    metadatas = result["metadatas"][0]

    matched_document = None

    for document, metadata in zip(documents, metadatas):
        source = metadata.get("source", "")
        if source == expected_source:
            matched_document = document
            break

    if matched_document:
        question_words = set(
            re.findall(r"[a-zA-Z]{4,}", question.lower())
        )

        document_words = set(
            re.findall(r"[a-zA-Z]{4,}", matched_document.lower())
        )

        overlap = question_words.intersection(document_words)

        faithful = len(overlap) > 0
    else:
        faithful = False

    if faithful:
        faithful_count += 1

    results.append({
        "id": item["id"],
        "question": question,
        "expected_source": expected_source,
        "faithful": faithful
    })

total = len(results)
faithfulness = faithful_count / total if total else 0

metrics = {
    "evaluation_set_size": total,
    "faithful_answers": faithful_count,
    "unfaithful_answers": total - faithful_count,
    "faithfulness": round(faithfulness, 4),
    "evaluation_method": "keyword overlap between question and retrieved source document"
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

with open(METRICS_FILE, "w", encoding="utf-8") as f:
    json.dump(metrics, f, ensure_ascii=False, indent=2)

print("Faithfulness evaluation completed.")
print(f"Total questions: {total}")
print(f"Faithful: {faithful_count}")
print(f"Unfaithful: {total - faithful_count}")
print(f"Faithfulness: {faithfulness:.4f}")
print(f"Saved: {OUTPUT_FILE}")
print(f"Saved: {METRICS_FILE}")
