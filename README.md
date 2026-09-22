# Iyuno AI Agent Portfolio

## Agentic Knowledge Triage

공개된 보안·기술 문서를 검색하고, 질문 유형에 따라 RAG 또는 Tool을 선택하는 AI Agent 프로젝트입니다.

Iyuno **AI Agent Engineer** 채용공고의 주요 요구사항인 **RAG, Tool/API 연동, Agent Routing, Evaluation, Testing**을 프로젝트에 적용했습니다.

**Repository:** https://github.com/wlsgkr11/iyuno-agent-portfolio  
**Job Posting:** https://iyuno.wd3.myworkdayjobs.com/careers/job/seoul/ai-agent-engineer_jr101122

---

## 🎯 Project Goal

사용자가 보안·기술 관련 질문을 입력하면 Agent가 질문 유형을 판단하고 적절한 기능을 선택합니다.

```text
User Question
      ↓
 FastAPI API
      ↓
 Agent Router
   ↙   ↓    ↘
 RAG  Tool  Policy
   \    |    /
    Response + Source
```

---

## 💼 Job Requirements Mapping

| Job Requirement | Project Implementation |
|---|---|
| AI Agent 시스템 설계 및 개발 | `app/agent.py` Agent Router |
| RAG 기반 검색 | ChromaDB Vector Search + Retriever |
| Tool Calling / API Orchestration | Calculator + Policy Lookup + Routing |
| Multi-step 실행 흐름 | Question → Router → Tool/RAG → Response |
| Evaluation | 30개 질문 + Recall@3 + Latency + Faithfulness |
| API / DB 통합 | FastAPI + ChromaDB |
| 오류 분석 | `evaluation/error_analysis.md` |

> 현재 Tool 기능은 실제 LLM Function Calling이 아니라 **규칙 기반 Agent Routing**으로 구현되어 있습니다.

---

## 🚀 Main Features

### 1. Document Processing

- 공개 보안·기술 문서 20개 수집
- 문서 정제 및 Chunking
- Embedding 생성
- ChromaDB Vector Store 구축

### 2. RAG Retriever

질문과 관련된 문서를 Vector Search로 검색하고 검색 결과의 Source를 함께 제공합니다.

- Top-K 검색
- 관련 문서 검색
- Source 표시
- 검색 결과 기반 응답 데이터 제공

### 3. Calculator Tool

간단한 수식을 계산합니다.

**Example**

```text
Question: What is 120 * 0.15?
Result: 18.0
```

### 4. Policy Lookup Tool

보안 정책 관련 질문을 프로젝트 내부 정책 데이터에서 조회합니다.

**Example**

```text
Question: What is the password policy?
Source: OWASP Password Storage Cheat Sheet
```

### 5. Agent Routing

| Question Type | Selected Function |
|---|---|
| Calculation | Calculator |
| Policy | Policy Lookup |
| Security / Technical | RAG Retriever |

---

## 🛠️ Tech Stack

- Python
- FastAPI
- ChromaDB
- LangChain
- BeautifulSoup
- pytest
- GitHub Actions

---

## 📁 Project Structure

```text
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
```

---

## ⚙️ Installation

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

---

## ▶️ Run FastAPI

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

---

## 🔌 API Examples

### Calculator

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method Post -ContentType "application/json" -Body '{"question":"What is 120 * 0.15?"}'
```

Expected result:

```text
type: tool
answer: 18.0
source: calculator
```

### Policy Lookup

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method Post -ContentType "application/json" -Body '{"question":"What is the password policy?"}'
```

### RAG

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method Post -ContentType "application/json" -Body '{"question":"How can I improve account security?"}'
```

---

## 📊 Evaluation

총 **30개의 질문**으로 검색 성능을 평가했습니다.

### Retrieval

| Metric | Result |
|---|---:|
| Questions | 30 |
| Hits | 30 |
| Misses | 0 |
| Recall@3 | 1.00 |
| Average Retrieval Latency | 0.2014 sec |

### Faithfulness Approximation

| Metric | Result |
|---|---:|
| Questions | 30 |
| Faithful | 29 |
| Unfaithful | 1 |
| Faithfulness | 96.67% |

> Faithfulness는 현재 **keyword-overlap 기반 근사 평가**입니다. 따라서 96.67%는 LLM-as-a-Judge 방식의 정식 평가 결과가 아닙니다.

### Evaluation Files

- `evaluation/results.json`
- `evaluation/metrics.json`
- `evaluation/error_analysis.md`
- `evaluation/recall_at_3.png`
- `evaluation/latency.png`

---

## 🧪 Testing & CI

Pytest를 사용하여 Tool 기능을 테스트했습니다.

**Current Result: 5 passed**

Test cases:

- Calculator addition
- Calculator multiplication
- Calculator division
- Calculator subtraction
- Invalid expression handling

GitHub Actions를 통해 Push 및 Pull Request 시 테스트가 자동 실행됩니다.

```text
GitHub Push
    ↓
GitHub Actions
    ↓
Pytest
    ↓
5 Tests Passed
```

---

## 📚 Data Sources

공개적으로 접근 가능한 보안·기술 문서를 사용했습니다.

주요 출처:

- OWASP Cheat Sheet Series
- OWASP API Security
- OWASP Top 10
- OWASP LLM Security
- 기타 OWASP 공개 보안 문서

**Collection Date:** 2026-09

원문 문서의 이용 조건 및 라이선스는 각 공식 출처의 정책을 따릅니다.

프로젝트에는 개인 정보, 비공개 회사 자료 또는 API Secret을 포함하지 않았습니다.

---

## ⚠️ Limitations

현재 프로젝트에는 다음과 같은 제한사항이 있습니다.

- RAG는 검색된 문서와 Source를 반환하며 LLM 최종 답변 생성은 구현하지 않았습니다.
- Tool은 규칙 기반 Routing으로 동작합니다.
- 실제 LLM Function Calling은 아직 구현하지 않았습니다.
- Policy Lookup은 외부 API가 아닌 프로젝트 내부 데이터를 사용합니다.
- Faithfulness는 keyword-overlap 기반 근사 평가입니다.
- 사용자 Feedback Loop는 아직 구현하지 않았습니다.

---

## 🔮 Future Work

향후 다음 기능을 추가할 예정입니다.

- LLM 기반 최종 답변 생성
- 실제 LLM Function Calling
- Search API 및 Policy API 연동
- LLM 기반 Faithfulness 평가
- 사용자 Feedback Loop
- Streamlit Demo
- Demo Video
- 더 다양한 Evaluation Dataset
- Retrieval 및 Agent Routing 성능 개선

---

## 📈 Current Progress

### Completed

- GitHub Repository
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
- 30 Evaluation Questions
- Recall@3
- Retrieval Latency
- Faithfulness Approximation
- Evaluation Graphs
- Error Analysis
- Pytest
- GitHub Actions CI

### Not Yet Implemented

- LLM Final Answer Generation
- Real LLM Function Calling
- Search API
- External Policy API
- Feedback Loop
- Streamlit Demo
- Demo Video

---

## 📝 Retrospective

이번 프로젝트를 통해 단순히 LLM을 사용하는 것과 Agent 시스템을 구성하는 것의 차이를 경험했습니다.

문서 수집부터 정제, Chunking, Embedding, Vector Search, RAG, Tool Routing, API, Evaluation, Testing까지 하나의 프로젝트 흐름으로 연결하면서 각 구성 요소가 어떻게 연결되는지 이해할 수 있었습니다.

또한 30개의 평가 질문을 구성하고 Recall@3와 Latency를 측정하면서 기능 구현뿐만 아니라 결과를 정량적으로 확인하는 과정도 경험했습니다.

Faithfulness 평가에서는 keyword-overlap 방식의 한계도 확인했습니다. 앞으로 실제 LLM 기반 평가와 Function Calling, Feedback Loop 등을 추가하여 보다 실제 서비스에 가까운 Agent 시스템으로 발전시키고자 합니다.

---

## 📄 License

This project is for educational purposes.

Document licenses and usage conditions follow the original public sources.
