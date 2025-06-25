# AI 챗봇 프로젝트

FastAPI + Streamlit + LangGraph를 사용한 AI 챗봇 프로젝트입니다.

## 🆕 최신 업데이트
- PR 테스트를 위한 업데이트
- GitHub Actions 자동화 기능 추가
- 자동 라벨링 및 댓글 시스템 구현

## 프로젝트 구조

```
├── backend/                 # FastAPI 백엔드
│   ├── app/                # 애플리케이션 코드
│   │   ├── models/         # 데이터 모델
│   │   └── routers/        # API 라우터
│   ├── tests/              # 테스트 코드
│   └── requirements.txt    # Python 의존성
├── frontend/               # Streamlit 프론트엔드
│   ├── app.py             # 메인 애플리케이션
│   └── requirements.txt   # Python 의존성
├── docs/                  # 문서
├── .github/workflows/     # GitHub Actions
└── .cursor/rules/         # 개발 규칙
```

## 기술 스택

### 백엔드
- **FastAPI**: 웹 프레임워크
- **LangGraph**: AI Agent 프레임워크
- **Gemini-2.5-flash**: LLM 모델
- **DuckDuckGo Search**: 웹 검색 도구

### 프론트엔드
- **Streamlit**: 웹 인터페이스

### DevOps
- **GitHub Actions**: CI/CD
- **pytest**: 테스트 프레임워크

## 설치 및 실행

### 백엔드 실행
```bash
cd backend
pip install -r requirements.txt
python run.py
```

### 프론트엔드 실행
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## GitHub Actions

이 프로젝트는 다음과 같은 자동화 기능을 제공합니다:

### PR 자동화
- 자동 댓글 등록
- 자동 할당자 지정
- 자동 라벨링
- 자동 코드 리뷰

### 이슈 자동화
- 자동 댓글 등록
- 자동 할당자 지정
- 자동 라벨링

### 테스트 자동화
- 코드 푸시/PR 시 자동 테스트 실행
- 코드 커버리지 측정

## 개발 가이드

- TDD(Test-Driven Development) 원칙 준수
- SOLID 원칙 및 Clean Architecture 적용
- 모든 PR은 리뷰 필수
- 테스트 코드 작성 필수

## 🚀 특별 기능

### AI 기반 상품 검색
- 자연어로 상품 검색 가능
- 실시간 웹 검색 결과 제공
- 개인화된 추천 시스템