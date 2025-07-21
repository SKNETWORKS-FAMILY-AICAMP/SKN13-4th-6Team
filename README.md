
# 💳 신용카드 추천 챗봇 (LLM 기반 RAG 시스템)


## 🧑‍💻 팀원 소개
| 항목 | 최성장 | 고범석 | 지형우 | 안수민 | 김동욱 |
|----|----|----|----|----|----|
| 이미지 | <img src="" width="100" height="100"> | <img src="" width="120" height="100"> | <img src="" width="100" height="100"> | <img src="" width="100" height="100"> | <img src="" width="100" height="100"> |
| 이메일 | [GrowingChoi](https://github.com/GrowingChoi) | <p align='center'>[](https://github.com/)</p> | <p align='center'>[](https://github.com/)</p> | <p align='center'>[](https://github.com/)</p> |  |


---

# 1. 프로젝트 주제
## "사용자 질문에 따라 맞춤형 신용카드를 추천하고 설명하는 LLM 기반 챗봇 시스템"

### 기존의 정해진 응답만 제공하는 챗봇을 넘어, 이 시스템은 사용자 질문을 LLM이 직접 이해하고, 카드 추천 및 설명을 위해 필요한 도구(예: 벡터 검색, 프롬프트 생성, 카드 필터링) 등을 자동 호출하는 Tool-Calling 기반 추천 시스템입니다.

---

# 2. 주제 선정 이유
## 신용카드 선택은 복잡하고 조건이 다양함

## 사용자마다 연회비, 혜택, 라이프스타일이 다름

## 기존 챗봇은 정해진 QnA만 제공 → 사용자의 세부 질문에는 대응이 불가능함

## 벡터 검색 + LLM 활용으로 해결 가능

## 카드 정보를 벡터로 임베딩하여 빠르게 필터링 가능

## 사용자의 질문을 이해하고, 맞춤형 응답 제공 가능

## FAQ, 카드 설명, 사용자 조건까지 통합 분석 가능

## 대화형 인터페이스로 카드 선택 UX 개선

## 사용자는 단순히 "해외 결제 좋은 카드 추천해줘"처럼 자연어로 물으면 됨

---

3. 주요 기능 요약
| 기능                | 설명                                                      |
| ----------------- | ------------------------------------------------------- |
| 🔐 사용자 인증         | 로그인 기능을 통해 접근 제어                                        |
| 💬 챗봇 UI          | `chat.html` 기반의 채팅 인터페이스 제공                             |
| 🧠 LLM 기반 카드 추천   | 사용자 질문 분석 → 조건 필터링 → FAISS 검색 → 프롬프트 생성 → 답변 생성         |
| 🔎 유사 질문 FAQ 검색   | 유사한 FAQ 벡터 검색으로 빠른 응답                                   |
| 🧰 모듈화된 추천 파이프라인  | `formatter`, `prompt_builder`, `recommender` 등 역할 분리 구조 |
| 📦 FAISS 기반 벡터 검색 | 사전 벡터화된 카드 정보 인덱스에서 밀리초 단위 검색 수행                        |
| 🧱 Django 기반 백엔드  | Django 앱 구조로 관리 및 확장 용이                                 |

---

4. 기술 스택
| 구분              | 사용 기술                            |
| --------------- | -------------------------------- |
| Language        | Python                           |
| Web Framework   | Django                           |
| Embedding Model | `sentence-transformers`          |
| Vector DB       | FAISS                            |
| LLM Integration | OpenAI GPT                       |
| Frontend        | HTML + JavaScript                |
| 기타              | `langchain`, `torch`, `dotenv` 등 |

5. 프로젝트 구조
```bash
chat_project/
├── accounts/                # 로그인 관련 기능
├── chatbot/                 # 챗봇 UI + API
├── recommendation/          # 추천 알고리즘 로직
│   ├── formatter.py
│   ├── model_manager.py
│   ├── prompt_builder.py
│   ├── query_filter.py
│   └── recommender.py
├── embedding/               # FAISS 기반 벡터 검색 로직
│   └── EmbeddingCardInfo.py
├── templates/
│   ├── base.html
│   ├── accounts/login.html
│   ├── accounts/home.html
│   └── chatbot/chat.html
├── chat_project/            # Django 설정
│   ├── settings.py
│   ├── urls.py
├── manage.py
└── requirements.txt
└── documents                # 산출물
```

---

6. 시스템 아키텍처 및 흐름
```bash
[사용자 질문] 
     ↓
[chat.html → GET /api/chat_message/ 호출]
     ↓
[chatbot.views → recommendation.recommender 호출]
     ↓
[사용자 조건 파악 → 카드 필터링]
     ↓
[벡터 임베딩 → FAISS 인덱스 검색]
     ↓
[검색 결과 포맷팅 → LLM 프롬프트 생성]
     ↓
[OpenAI API 호출 → 마크다운 응답 생성]
     ↓
[HTML 채팅 UI에 실시간 스트리밍 출력]
```
7. 실행 방법
1. 의존성 설치
```bash
pip install -r requirements.txt
```
2. FAISS 인덱스 생성
```bash
# 필요한 경우 EmbeddingCardInfo.py 실행 or vector 인덱스 생성 스크립트 실행
```
3. Django 서버 실행
```bash
python manage.py runserver
```
4. 접속
```ruby
http://127.0.0.1:8000/accounts/login/
```
로그인 후 /chatbot/으로 이동하여 챗봇 사용 가능


## 한 줄 회고

| 이름 | 회고 |
|-------|----|
|최성장   |  |
|고범석   |  |
|지형우   |  |
|김동욱   |  |
|안수민   |  |
