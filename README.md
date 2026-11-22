# QA Automation Project

## 프로젝트 소개

Python, Selenium, pytest, Postman, Newman, GitHub Actions를 활용한 **Web UI 및 API 테스트 자동화 프로젝트**입니다.

Web UI 테스트는 SauceDemo를 대상으로 로그인부터 장바구니 상품 검증까지 자동화하고 있으며, POM(Page Object Model)과 pytest를 적용하여 테스트 구조를 개선했습니다.

API 테스트는 JSONPlaceholder를 대상으로 정상 및 예외 응답을 검증하고, Postman Collection과 Newman CLI를 활용하여 자동 실행 및 HTML 테스트 리포트 생성을 구현했습니다.

GitHub Actions를 활용하여 GitHub 저장소에 Push할 때 Web UI 및 API 테스트가 자동으로 실행되도록 CI 환경을 구축했습니다.

---

## 현재 구현

### Web UI 테스트 자동화

- Selenium 기반 Web UI 자동화
- 로그인 / 장바구니 테스트 자동화
- Explicit Wait 적용
- POM(Page Object Model) 구조 적용
- pytest 테스트 프레임워크 적용
- Fixture / conftest.py를 이용한 WebDriver 관리
- Parametrize를 이용한 반복 테스트
- pytest-html을 이용한 HTML 테스트 리포트 생성
- GitHub Actions 환경에서 Headless Chrome 테스트 실행

### API 테스트 자동화

- Postman을 활용한 REST API 테스트
- GET / POST / PUT 요청 검증
- 정상 및 예외 응답 테스트
- HTTP Status Code 및 Response Body 검증
- Postman Test Script를 이용한 Assertion 작성
- Postman Collection JSON 파일 관리
- Newman CLI 기반 API 테스트 자동 실행
- PowerShell 실행 스크립트 구성
- Newman HTML 테스트 리포트 생성
- Exit Code 기반 테스트 성공 / 실패 판별

### CI 자동화

- GitHub Actions Workflow 구축
- GitHub Push 이벤트 기반 자동 실행
- Ubuntu Runner 기반 테스트 실행
- Python / Node.js 실행 환경 구성
- Selenium + pytest Web UI 테스트 자동 실행
- Postman + Newman API 테스트 자동 실행
- CI 성공 / 실패 상태 확인
- Exit Code 기반 실패 감지 검증
- HTML Report 및 Artifact 업로드 실습 완료

---

## 프로젝트 구조

```text
_qa_project_basic/
│
├─ .github/
│  └─ workflows/
│     └─ ci.yml
│
├─ pytest_pom_pages/
│  ├─ pytest_login_page.py
│  ├─ pytest_inventory_page.py
│  └─ pytest_cart_page.py
│
├─ pytest_pom_tests/
│  ├─ conftest.py
│  ├─ parametrize_test.py
│  ├─ test_pytest_cart_pom.py
│  └─ test_pytest_google.py
│
├─ api_tests/
│  └─ JSONPlaceholder API Test.postman_collection.json
│
├─ scripts/
│  └─ run-newman.ps1
│
├─ reports/
│  ├─ report.html
│  └─ newman-report.html
│
├─ requirements.txt
├─ .gitignore
└─ README.md
```

*기존 학습용 파일 및 폴더는 구조 설명에서 일부 생략했습니다. reports 폴더의 HTML 파일은 로컬 실행 시 생성되며 Git 관리 대상에서 제외됩니다.*

---

## 테스트 실행

프로젝트 루트 디렉터리에서 실행합니다.

### 1. Web UI 테스트 실행

전체 pytest 테스트 실행:

```powershell
python -m pytest .\pytest_pom_tests\ -v
```

장바구니 테스트만 실행:

```powershell
python -m pytest .\pytest_pom_tests\test_pytest_cart_pom.py -v
```

HTML Report 생성:

```powershell
python -m pytest .\pytest_pom_tests\ -v --html=.\reports\report.html --self-contained-html
```

### 2. API 테스트 실행

Node.js 및 Newman, Newman HTML Reporter 설치가 필요합니다.

```powershell
npm install -g newman newman-reporter-html
```

PowerShell 실행 스크립트:

```powershell
.\scripts\run-newman.ps1
```

스크립트는 다음 작업을 수행합니다.

1. Postman Collection JSON 파일 경로 설정
2. Newman을 통한 API 테스트 실행
3. CLI 및 HTML 리포트 생성
4. Exit Code에 따른 성공 / 실패 결과 반환

### 3. 테스트 리포트

- Web UI: `reports/report.html`
- API: `reports/newman-report.html`

리포트 파일은 실행 시 생성되며 Git 관리 대상에서 제외됩니다.

---

## API 테스트 실행 결과

JSONPlaceholder API Collection 기준:

| 항목 | 결과 |
|---|---|
| Requests | 5 |
| Test Scripts | 5 |
| Assertions | 24 |
| Failed | 0 |

검증 항목에는 HTTP 상태 코드, 응답 데이터, 필수 속성, 데이터 타입 및 예외 응답이 포함됩니다.

*위 결과는 프로젝트 개발 과정에서 확인한 실행 결과입니다.*

---

## GitHub Actions CI 자동화

### 1. CI 구성

GitHub Actions를 활용하여 GitHub 저장소에 Push할 때 Web UI 및 API 테스트가 자동 실행되도록 구성했습니다.

**실행 환경**

- GitHub-hosted Ubuntu Runner
- Python 3.13
- Node.js 22
- Selenium + pytest
- Postman + Newman

**Workflow 파일:** `.github/workflows/ci.yml`

### 2. CI 자동 실행 흐름

```text
GitHub Repository
        ↓
Git Push
        ↓
GitHub Actions Workflow
        ↓
Checkout Repository
        ↓
Python 환경 구성
        ↓
Python 라이브러리 설치
        ↓
Selenium + pytest Web UI Test
        ↓
Node.js 환경 구성
        ↓
Newman 설치
        ↓
Postman Collection API Test
        ↓
PASS / FAIL 확인
```

### 3. CI 테스트 실행 결과

| 테스트 | 실행 결과 |
|---|---|
| Web UI (Selenium + pytest) | 1 Passed / 0 Failed |
| API (Postman + Newman) | 5 Requests / 24 Assertions / 0 Failed |
| GitHub Actions Workflow | Success |

GitHub Actions의 Ubuntu Runner에서 Selenium Headless Chrome 테스트와 Newman API 테스트가 정상 실행되는 것을 확인했습니다.

### 4. CI 실패 감지 검증

GitHub Actions가 실행 명령어의 실패를 정상적으로 감지하는지 확인하기 위해 `exit 1` 명령어를 임시로 추가했습니다.

**검증 결과**

1. 정상 Workflow 실행 → Success
2. `exit 1` 명령어 실행 → Failure
3. 실패 로그에서 Exit Code 1 확인
4. 임시 실패 코드 제거
5. Workflow 재실행 → Success

이를 통해 GitHub Actions의 Exit Code 기반 실패 감지 및 정상 복구를 검증했습니다.

*해당 실습은 실제 테스트 Assertion 실패가 아닌 명령어 실패 감지 검증입니다.*

### 5. HTML Report 및 Artifact 실습

GitHub Actions에서 다음 기능을 구현하고 검증했습니다.

- pytest HTML Report 생성
- Newman HTML Report 생성
- `actions/upload-artifact@v4`를 이용한 리포트 업로드
- GitHub Actions에서 Artifact ZIP 다운로드
- Web UI / API HTML 리포트 확인

**현재 Workflow에서는 HTML 리포트 생성 및 Artifact 업로드 기능을 제외하고, 테스트 실행 및 PASS/FAIL 확인 기능만 유지하고 있습니다.**

---

## 현재 진행 상태

- [x] Selenium Web UI 자동화 완료
- [x] POM 및 pytest 적용 완료
- [x] Fixture / Parametrize 적용 완료
- [x] pytest HTML Report 구현 완료
- [x] Postman API 테스트 작성 완료
- [x] Newman CLI 자동 실행 구현 완료
- [x] PowerShell 실행 스크립트 구성 완료
- [x] Newman HTML Report 구현 완료
- [x] GitHub Repository 업로드 완료
- [x] GitHub Actions Workflow 구축 완료
- [x] GitHub Actions 기반 Selenium + pytest 자동 실행 완료
- [x] GitHub Actions 기반 Newman API 테스트 자동 실행 완료
- [x] GitHub Actions HTML Report / Artifact 실습 완료
- [x] CI 실패 감지 및 정상 복구 검증 완료

**다음 단계:** Jenkins를 활용한 CI Pipeline 구축
