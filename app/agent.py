import re

import chromadb

from app.tools import calculator
from app.policy import policy_lookup


chroma_client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = chroma_client.get_collection(
    name="security_documents"
)


def search_documents(question, n_results=3):
    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    return documents, metadatas, distances


def use_calculator(question):
    match = re.search(
        r"\d+(?:\.\d+)?\s*[+\-*/]\s*\d+(?:\.\d+)?",
        question
    )

    if not match:
        return None

    expression = match.group().strip()

    return calculator(expression)


def use_policy_lookup(question):
    policy_keywords = [
        "policy",
        "password policy",
        "authentication policy",
        "session policy",
        "logging policy",
        "보안 정책",
        "비밀번호 정책",
        "인증 정책",
        "세션 정책",
        "로그 정책"
    ]

    question_lower = question.lower()

    for keyword in policy_keywords:
        if keyword in question_lower:
            return policy_lookup(question)

    return None


def agent(question):
    print()
    print("=" * 60)
    print("AGENT")
    print("=" * 60)
    print()
    print("Question:", question)

    # 1. Calculator Tool
    calculation_result = use_calculator(question)

    if calculation_result is not None:
        print()
        print("[Tool Selected]")
        print("Calculator")

        print()
        print("Calculation Result:")
        print(calculation_result)

        return {
            "type": "tool",
            "answer": calculation_result,
            "source": "calculator"
        }

    # 2. Policy Lookup Tool
    policy_result = use_policy_lookup(question)

    if policy_result is not None:
        print()
        print("[Tool Selected]")
        print("Policy Lookup")

        print()
        print("Policy Title:")
        print(policy_result["title"])

        print()
        print("Description:")
        print(policy_result["description"])

        print()
        print("Source:")
        print(policy_result["source"])

        return {
            "type": "policy",
            "answer": policy_result["description"],
            "source": policy_result["source"]
        }

    # 3. RAG Retriever
    print()
    print("[Tool Selected]")
    print("RAG Retriever")

    documents, metadatas, distances = search_documents(
        question
    )

    print()
    print("[Retrieved Documents]")

    sources = []

    for i, (document, metadata, distance) in enumerate(
        zip(documents, metadatas, distances),
        start=1
    ):
        source = metadata.get(
            "source",
            "Unknown source"
        )

        sources.append(source)

        print()
        print(f"[Result {i}]")
        print(document)
        print("Source:", source)
        print("Distance:", round(distance, 4))

    return {
        "type": "rag",
        "documents": documents,
        "sources": sources
    }


if __name__ == "__main__":
    print()
    print("Iyuno AI Agent")
    print("Agentic Knowledge Triage")

    agent("How can I improve account security?")

    agent("What is 120 * 0.15?")

    agent("What is the password policy?")