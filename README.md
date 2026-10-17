# QA Automation Project

## 프로젝트 소개

Python, Selenium, pytest, Postman, Newman을 활용한 Web UI 및 API 테스트 자동화 프로젝트입니다.

Web UI 테스트는 SauceDemo를 대상으로 로그인부터 장바구니 상품 검증까지 자동화하고 있으며, POM(Page Object Model)과 pytest를 적용하여 테스트 구조를 개선했습니다.

API 테스트는 JSONPlaceholder를 대상으로 정상 및 예외 응답을 검증하고, Postman Collection과 Newman CLI를 활용하여 자동 실행 및 HTML 테스트 리포트 생성을 구현했습니다.

## 현재 구현

### Web UI 테스트 자동화

* Selenium 기반 Web UI 자동화
* 로그인 / 장바구니 테스트 자동화
* Explicit Wait 적용
* POM(Page Object Model) 구조 적용
* pytest 테스트 프레임워크 적용
* Fixture / conftest.py를 이용한 WebDriver 관리
* Parametrize를 이용한 반복 테스트
* pytest-html을 이용한 HTML 테스트 리포트 생성

### API 테스트 자동화

* Postman을 활용한 REST API 테스트
* GET / POST / PUT 요청 검증
* 정상 및 예외 응답 테스트
* HTTP Status Code 및 Response Body 검증
* Postman Test Script를 이용한 Assertion 작성
* Postman Collection JSON 파일 관리
* Newman CLI 기반 API 테스트 자동 실행
* PowerShell 실행 스크립트 구성
* Newman HTML 테스트 리포트 생성
* Exit Code 기반 테스트 성공 / 실패 판별

## 프로젝트 구조

```text
_qa_project_basic/
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
├─ .gitignore
└─ README.md
```

*기존 학습용 파일 및 폴더는 구조 설명에서 일부 생략했습니다.*

## 테스트 실행

프로젝트 루트 디렉터리에서 실행합니다.

### 1. Web UI 테스트 실행

전체 pytest 테스트 실행:

```powershell
python -m pytest .\pytest_pom_tests\ -v
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

* Web UI: `reports/report.html`
* API: `reports/newman-report.html`

리포트 파일은 실행 시 생성되며 Git 관리 대상에서 제외됩니다.

## API 테스트 실행 결과

JSONPlaceholder API Collection 기준:

* Requests: 5
* Assertions: 24
* Failed: 0

검증 항목에는 HTTP 상태 코드, 응답 데이터, 필수 속성, 데이터 타입 및 예외 응답이 포함됩니다.

*위 결과는 프로젝트 개발 과정에서 확인한 실행 결과입니다.*

## 현재 진행 상태

* Selenium Web UI 자동화 완료
* POM 및 pytest 적용 완료
* Fixture / Parametrize 적용 완료
* pytest HTML Report 구현 완료
* Postman API 테스트 작성 완료
* Newman CLI 자동 실행 구현 완료
* PowerShell 실행 스크립트 구성 완료
* Newman HTML Report 구현 완료
* GitHub 업로드 완료

**다음 단계:** GitHub Actions를 활용한 Web UI 및 API 테스트 CI/CD 구축
