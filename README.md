프로젝트명
QA Automation Project

현재 구현
- Selenium 기반 Web UI 자동화
- 로그인 자동화
- 장바구니 추가
- Cart 이동
- 상품명 Assertion
- Explicit Wait
- try-finally 종료 처리
- POM 구조 적용

현재 구조
pom_pages/
  login_page.py
  inventory_page.py
  cart_page.py

pom_tests/
  test_cart_pom.py

다음 단계
- pytest 적용
- Postman API 테스트
- Newman
- GitHub Actions