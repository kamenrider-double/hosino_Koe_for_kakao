# Copilot Instructions for hosino_Koe_for_kakao

## 프로젝트 개요
- 이 프로젝트는 OpenAI API를 활용하여 챗봇 또는 AI 어시스턴트 기능을 제공합니다.
- 주요 파일: `sei.py` (OpenAI API 호출 및 메시지 처리)

## 주요 구조 및 동작
- `sei.py`는 환경 변수(`GITHUB_TOKEN`)를 통해 인증 토큰을 받아 OpenAI API에 요청을 보냅니다.
- API 엔드포인트와 모델명(`openai/gpt-5-nano`)은 코드 내에 하드코딩되어 있습니다.
- 메시지 포맷은 OpenAI의 Chat API와 동일하게 `messages` 리스트로 구성됩니다.
- 출력은 콘솔에 바로 표시됩니다.

## 개발 워크플로우
- Python 3.x 환경에서 동작하며, 주요 의존성은 `openai`, `langchain_community`입니다.
- 패키지 설치 예시:
  ```bash
  pip install openai langchain_community
  ```
- 실행 예시:
  ```bash
  python sei.py
  ```
- 환경 변수 `GITHUB_TOKEN`이 반드시 필요합니다.

## 확장 및 통합
- 외부 텍스트 파일 로딩 시 `langchain_community.document_loaders.TextLoader`를 사용할 수 있습니다.
- 추가적인 모델, 엔드포인트, 메시지 포맷 변경 시 `sei.py`를 직접 수정해야 합니다.

## 프로젝트 관례
- 모든 주요 설정(토큰, 엔드포인트, 모델명)은 코드 상단에 명시합니다.
- 메시지 프롬프트는 한국어로 작성하는 것이 기본입니다.
- 외부 패키지 추가 시 `pip install` 명령어를 README 또는 본 문서에 명확히 남깁니다.

## 예시 코드 패턴
- OpenAI API 호출 및 메시지 구성은 `sei.py` 참고
- 텍스트 파일 로딩 및 전처리는 `langchain_community` 활용 가능

## 참고 파일
- `sei.py`: 핵심 로직 및 API 연동 예시
- `README.md`: 프로젝트 간단 소개

---
이 문서는 AI 코딩 에이전트가 프로젝트 구조와 관례를 빠르게 파악하고, 일관성 있게 코드를 작성할 수 있도록 돕기 위한 가이드입니다.
