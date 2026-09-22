# \# Iyuno AI Agent Portfolio

# 

# \## Project

# 

# \### Agentic Knowledge Triage

# 

# 공개된 보안·기술 문서를 기반으로 사용자의 질문에 답변하는  

# AI Agent 시스템을 구현하는 프로젝트입니다.

# 

# \## Goal

# 

# 실제 AI Agent Engineer 채용공고에서 요구하는  

# RAG, Tool Calling, API 연동 및 Evaluation 기능을  

# 작동하는 프로젝트 형태로 구현합니다.

# 

# \## Main Features

# 

# \- Public document collection

# \- Document cleaning

# \- Document chunking

# \- Embedding

# \- Vector search

# \- RAG-based question answering

# \- Document citation

# \- Calculator tool

# \- Tool routing

# \- FastAPI API

# \- Evaluation

# \- Pytest

# \- GitHub Actions CI

# 

# \## Tech Stack

# 

# \- Python

# \- RAG

# \- ChromaDB

# \- Vector Database

# \- FastAPI

# \- Pytest

# \- GitHub Actions

# 

# \## Job Posting

# 

# \### Iyuno AI Agent Engineer

# 

# https://iyuno.wd3.myworkdayjobs.com/careers/job/seoul/ai-agent-engineer\_jr101122

# 

# \## Project Architecture

# 

# User Question  

# ↓  

# FastAPI  

# ↓  

# Agent  

# ↓  

# RAG Retriever / Calculator Tool  

# ↓  

# ChromaDB / Calculator  

# ↓  

# Response + Source

# 

# \## Evaluation

# 

# \### Retrieval Evaluation

# 

# Evaluation Set: 30 questions

# 

# \- Hits: 30

# \- Misses: 0

# \- Recall@3: 1.0

# \- Average Retrieval Latency: approximately 0.20 seconds

# 

# \### Faithfulness Approximation

# 

# \- Evaluation Set: 30 questions

# \- Faithful: 29

# \- Unfaithful: 1

# \- Faithfulness: 96.67%

# 

# Faithfulness 평가는 질문과 검색된 원문 사이의 키워드 겹침을 이용한 간단한 자동 근사 평가입니다.

# 

# 따라서 이 값은 LLM 기반의 정식 Faithfulness 평가 점수가 아니며, 검색된 문서가 질문과 관련된 근거를 포함하는지를 확인하기 위한 보조 지표로 사용했습니다.

# 

# 평가 결과는 다음 파일에 저장되어 있습니다.

# 

# \- `evaluation/results.json`

# \- `evaluation/metrics.json`

# \- `evaluation/faithfulness\_results.json`

# \- `evaluation/faithfulness\_metrics.json`

# 

# \## Testing

# 

# Pytest: 5 passed

# 

# \## Continuous Integration

# 

# GitHub Actions를 이용하여 Push 및 Pull Request 시  

# Pytest가 자동으로 실행되도록 구성했습니다.

# 

# \## Current Progress

# 

# \- \[x] GitHub repository setup

# \- \[x] Collect 20 public documents

# \- \[x] Document cleaning

# \- \[x] Implement document ingestion

# \- \[x] Implement chunking

# \- \[x] Implement embedding

# \- \[x] Implement vector search

# \- \[x] Implement RAG retrieval

# \- \[x] Add document citation

# \- \[x] Add Calculator Tool

# \- \[x] Add Tool routing

# \- \[x] Build FastAPI API

# \- \[x] Add evaluation set

# \- \[x] Evaluate 30 questions

# \- \[x] Measure Recall@3

# \- \[x] Measure retrieval latency

# \- \[x] Add faithfulness approximation evaluation

# \- \[x] Add evaluation graphs

# \- \[x] Add Pytest

# \- \[x] Add GitHub Actions CI

# 

# \- \[ ] LLM-based final answer generation

# \- \[ ] Real LLM Function Calling

# \- \[ ] Search API integration

# \- \[ ] Policy lookup API

# \- \[ ] Feedback loop

# \- \[ ] Streamlit demo

# \- \[ ] Demo video

# \- \[ ] Final retrospective

# 

# \## Limitations

# 

# 현재 RAG 시스템은 검색된 문서와 출처를 반환하는 방식으로 구현되어 있습니다.

# 

# 별도의 LLM을 이용한 최종 자연어 답변 생성 기능은 아직 구현 중입니다.

# 

# 현재 Calculator Tool은 규칙 기반 routing 방식으로 동작하며,  

# 향후 실제 LLM Function Calling 방식으로 확장할 예정입니다.

# 

# 현재 Faithfulness 평가는 LLM 기반 평가가 아닌  

# 질문과 검색 문서의 키워드 겹침을 이용한 간단한 근사 평가 방식입니다.

# 

# \## Future Work

# 

# \- LLM 기반 최종 답변 생성

# \- 실제 Function Calling 기반 Tool Calling

# \- Search API 및 Policy Lookup API 연동

# \- LLM 기반 Faithfulness 평가

# \- Evaluation 그래프 고도화

# \- 사용자 Feedback Loop

# \- Streamlit Demo

# \- Demo 영상 제작

# \- 최종 프로젝트 회고 작성

