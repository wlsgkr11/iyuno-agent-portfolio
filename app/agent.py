import re

import chromadb

from app.tools import calculator


# --------------------------------------------------
# ChromaDB 설정
# --------------------------------------------------

chroma_client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = chroma_client.get_collection(
    name="security_documents"
)


# --------------------------------------------------
# RAG 검색
# --------------------------------------------------

def search_documents(question, n_results=3):

    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    return documents, metadatas, distances


# --------------------------------------------------
# Calculator Tool
# --------------------------------------------------

def use_calculator(question):

    # 계산식이 포함된 질문인지 확인
    match = re.search(
        r"\d+(?:\.\d+)?\s*[+\-*/]\s*\d+(?:\.\d+)?",
        question
    )

    if not match:
        return None

    expression = match.group().strip()

    return calculator(expression)


# --------------------------------------------------
# Agent
# --------------------------------------------------

def agent(question):

    print()
    print("=" * 60)
    print("AGENT")
    print("=" * 60)

    print()
    print("Question:", question)

    # 계산 관련 질문인지 확인
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

    # 계산이 아니면 RAG 검색
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


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    print()
    print("Iyuno AI Agent")
    print("Agentic Knowledge Triage")

    # 테스트 1: RAG
    agent(
        "How can I improve account security?"
    )

    # 테스트 2: Calculator
    agent(
        "What is 120 * 0.15?"
    )