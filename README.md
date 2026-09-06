# QA Automation Project

## 프로젝트 소개

Python, Selenium, pytest를 활용한 Web UI 테스트 자동화 프로젝트입니다.

SauceDemo를 대상으로 로그인부터 장바구니 상품 검증까지 자동화하고 있으며,
POM(Page Object Model)과 pytest를 적용하여 테스트 구조를 개선하고 있습니다.

## 현재 구현

- Selenium 기반 Web UI 자동화
- 로그인 / 장바구니 테스트 자동화
- Explicit Wait 적용
- POM(Page Object Model) 구조 적용
- pytest 테스트 프레임워크 적용
- Fixture / conftest.py를 이용한 WebDriver 관리
- Parametrize를 이용한 반복 테스트
- pytest-html을 이용한 HTML 테스트 리포트 생성

## 프로젝트 구조

```text
qa_project_basic/
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
├─ reports/
│  └─ report.html
│
├─ .gitignore
└─ README.md
```

## 테스트 실행

전체 테스트 실행:

```powershell
python -m pytest .\pytest_pom_tests\ -v
```

HTML Report 생성:

```powershell
python -m pytest .\pytest_pom_tests\ -v --html=.\reports\report.html --self-contained-html
```

## 현재 진행 상태

Selenium → POM → pytest → Fixture → Parametrize → HTML Report까지 구현 완료