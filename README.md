# Iyuno AI Agent Portfolio

**Agentic Knowledge Triage**

공개된 보안·기술 문서를 수집하고 검색하여 질문과 관련된 문서를 찾아주는 AI Agent 프로젝트입니다.

Iyuno AI Agent Engineer 채용공고의 RAG, Tool Calling/API Orchestration, Evaluation 요구사항을 참고하여 구현했습니다.

- GitHub Repository: https://github.com/wlsgkr11/iyuno-agent-portfolio
- Job Posting: https://iyuno.wd3.myworkdayjobs.com/careers/job/seoul/ai-agent-engineer_jr101122

---

## 1. Project Goal

사용자가 보안 및 기술 관련 질문을 입력하면 Agent가 질문 유형을 판단하고 적절한 기능을 선택합니다.

### Architecture

User Question  
↓  
FastAPI  
↓  
Agent Router  
↓  
Calculator / Policy Lookup / RAG Retriever  
↓  
Response + Source

---

## 2. Job Posting Requirements Mapping

| Job Requirement | Project Evidence |
|---|---|
| AI Agent 시스템 설계 및 개발 | `app/agent.py` Agent Router |
| RAG 기반 검색 | ChromaDB Vector Search + RAG Retriever |
| Tool Calling / API Orchestration | Calculator + Policy Lookup + Routing |
| Multi-step 실행 흐름 | Question → Router → Tool/RAG → Response |
| Evaluation | 30개 평가셋 + Recall@3 + Latency + Faithfulness |
| API / DB 통합 | FastAPI + ChromaDB |
| 오류 분석 | `evaluation/error_analysis.md` |

> 현재 Tool 기능은 실제 LLM Function Calling이 아니라 규칙 기반 Agent Routing으로 구현되어 있습니다.

---

## 3. Main Features

### Document Processing

- 공개 보안·기술 문서 20개 수집
- 문서 정제
- Document Chunking
- Embedding
- ChromaDB Vector Store 구축

### RAG

- 사용자 질문을 Vector Search로 검색
- 관련 문서 Top-K 검색
- 검색 결과의 Source 표시
- 검색 결과를 기반으로 답변 데이터 제공

### Calculator Tool

간단한 수식을 계산하는 Tool입니다.

Example:

- Question: `What is 120 * 0.15?`
- Result: `18.0`

### Policy Lookup Tool

보안 정책 관련 질문을 분석하여 프로젝트 내부 정책 데이터를 조회합니다.

Example:

- Question: `What is the password policy?`
- Source: `OWASP Password Storage Cheat Sheet`

### Agent Routing

| Question Type | Selected Function |
|---|---|
| Calculation Question | Calculator |
| Policy Question | Policy Lookup |
| Security / Technical Question | RAG Retriever |

---

## 4. Tech Stack

- Python
- FastAPI
- ChromaDB
- LangChain
- BeautifulSoup
- pytest
- GitHub Actions

---

## 5. Project Structure

    iyuno-agent-portfolio/
    ├── app/
    │   ├── agent.py
    │   ├── main.py
    │   ├── tools.py
    │   └── policy.py
    ├── data/
    │   └── public/
    ├── evaluation/
    ├── scripts/
    ├── tests/
    │   └── test_tools.py
    ├── requirements.txt
    └── README.md

---

## 6. Installation

가상환경을 생성하고 필요한 패키지를 설치합니다.

    python -m venv .venv

    .\.venv\Scripts\python.exe -m pip install -r requirements.txt

---

## 7. Run FastAPI

다음 명령어로 FastAPI 서버를 실행할 수 있습니다.

    .\.venv\Scripts\python.exe -m uvicorn app.main:app --reload

실행 후 다음 주소에서 API 문서를 확인할 수 있습니다.

http://127.0.0.1:8000/docs

---

## 8. API Examples

### Calculator

    Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method Post -ContentType "application/json" -Body '{"question":"What is 120 * 0.15?"}'

Expected result:

- type: `tool`
- answer: `18.0`
- source: `calculator`

### Policy Lookup

    Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method Post -ContentType "application/json" -Body '{"question":"What is the password policy?"}'

### RAG

    Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method Post -ContentType "application/json" -Body '{"question":"How can I improve account security?"}'

---

## 9. Evaluation

총 30개의 질문을 사용하여 검색 성능을 평가했습니다.

### Retrieval Evaluation

| Metric | Result |
|---|---:|
| Total Questions | 30 |
| Hits | 30 |
| Misses | 0 |
| Recall@3 | 1.0 |
| Average Retrieval Latency | 0.2014 seconds |

평가 결과 파일:

- `evaluation/results.json`
- `evaluation/metrics.json`

### Faithfulness Approximation

| Metric | Result |
|---|---:|
| Total Questions | 30 |
| Faithful | 29 |
| Unfaithful | 1 |
| Faithfulness | 96.67% |

현재 Faithfulness 평가는 LLM 기반 평가가 아닌 **keyword-overlap 기반 근사 평가**입니다.

따라서 96.67%는 정식 LLM-as-a-Judge 평가 결과가 아니라 현재 검색 결과를 평가하기 위한 실험적 지표입니다.

---

## 10. Error Analysis

Faithfulness 평가에서 1개의 실패 사례가 확인되었습니다.

### Question

`How can I improve account security?`

### Expected Source

`authentication.md`

### Result

`faithful = false`

검색 평가에서는 기대 문서가 검색되었지만 keyword-overlap 방식의 Faithfulness 평가에서 실패로 분류되었습니다.

자세한 분석은 다음 파일에서 확인할 수 있습니다.

`evaluation/error_analysis.md`

### Future Improvements

- LLM 기반 Faithfulness 평가
- Semantic Similarity 평가
- Query Expansion
- Chunking 및 Retrieval 설정 개선

---

## 11. Evaluation Graphs

평가 결과를 시각화했습니다.

- `evaluation/recall_at_3.png`
- `evaluation/latency.png`

---

## 12. Testing

Pytest를 사용하여 Tool 기능을 테스트했습니다.

현재 테스트 결과:

**5 passed**

테스트 파일:

`tests/test_tools.py`

### Test Cases

- Calculator addition
- Calculator multiplication
- Calculator division
- Calculator subtraction
- Invalid expression handling

---

## 13. Continuous Integration

GitHub Actions를 사용하여 Push 및 Pull Request 시 테스트가 자동 실행되도록 구성했습니다.

### CI Flow

GitHub Push  
↓  
GitHub Actions  
↓  
Pytest  
↓  
5 Tests Passed

---

## 14. Data Sources

프로젝트에서는 공개적으로 접근 가능한 보안·기술 문서를 사용했습니다.

### Main Sources

- OWASP Cheat Sheet Series
- OWASP API Security
- OWASP Top 10
- OWASP LLM Security
- 기타 OWASP 보안 관련 공개 문서

### Collection Date

2026-09

각 원문 문서의 이용 조건 및 라이선스는 해당 공식 출처의 라이선스 정보를 따릅니다.

프로젝트에는 개인 정보, 비공개 회사 자료 또는 API Secret을 포함하지 않았습니다.

---

## 15. Limitations

현재 프로젝트에는 다음과 같은 제한사항이 있습니다.

- 현재 RAG는 검색된 문서와 Source를 반환하며 별도의 LLM 최종 답변 생성 단계는 구현하지 않았습니다.
- Tool 기능은 현재 규칙 기반 Routing으로 동작합니다.
- 실제 LLM Function Calling은 아직 구현하지 않았습니다.
- Policy Lookup은 외부 API가 아닌 프로젝트 내부 정책 데이터를 사용합니다.
- Faithfulness 평가는 keyword-overlap 기반 근사 방법입니다.
- Feedback Loop는 아직 구현하지 않았습니다.

---

## 16. Future Work

향후 다음 기능을 추가할 수 있습니다.

- LLM 기반 최종 답변 생성
- 실제 LLM Function Calling
- Search API 및 Policy API 연동
- LLM 기반 Faithfulness 평가
- 사용자 Feedback Loop
- Streamlit Demo
- Demo Video
- 더욱 다양한 Evaluation Dataset
- Retrieval 및 Agent Routing 성능 개선

---

## 17. Current Progress

### Completed

- GitHub Repository
- Public Document Collection
- 20 Public Documents
- Document Cleaning
- Chunking
- Embedding
- Vector Search
- RAG Retrieval
- Source Citation
- Calculator Tool
- Policy Lookup Tool
- Agent Routing
- FastAPI API
- Evaluation Dataset
- 30 Evaluation Questions
- Recall@3
- Retrieval Latency
- Faithfulness Approximation
- Evaluation Graphs
- Error Analysis
- Pytest
- GitHub Actions CI
- Final Retrospective

### Not Yet Implemented

- LLM Final Answer Generation
- Real LLM Function Calling
- Search API
- External Policy API
- Feedback Loop
- Streamlit Demo
- Demo Video

---

## 18. Retrospective

이번 프로젝트를 통해 단순히 LLM을 사용하는 것과 Agent 시스템을 구성하는 것의 차이를 경험했습니다.

특히 문서 수집부터 정제, Chunking, Embedding, Vector Search, RAG, Tool Routing, API, Evaluation, Testing까지 하나의 프로젝트 흐름으로 연결해보면서 각 구성 요소가 어떻게 연결되는지 이해할 수 있었습니다.

또한 30개의 평가 질문을 구성하고 Recall@3와 Latency를 측정하면서 기능 구현뿐만 아니라 결과를 정량적으로 확인하는 과정도 경험했습니다.

Faithfulness 평가에서는 단순한 keyword-overlap 방식의 한계도 확인했습니다. 앞으로는 LLM 기반 평가와 실제 Function Calling, Feedback Loop 등을 추가하여 보다 실제 서비스에 가까운 Agent 시스템으로 발전시키고자 합니다.

---

## License

This project is for educational purposes.

Document licenses and usage conditions follow the original public sources.
