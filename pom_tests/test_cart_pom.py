
#4. 구조 개선 > day2 (tests > 08_test_cart_try_finally파일의 내용을 pom 형식으로 변경하는것)
#test 파일은 테스트시나리오와 판정으로 분리

from selenium import webdriver

from pom_pages.login_page import LoginPage
from pom_pages.inventory_page import InventoryPage
from pom_pages.cart_page import CartPage


driver = webdriver.Chrome()

login_page = LoginPage(driver)
inventory_page = InventoryPage(driver)
cart_page = CartPage(driver)


try:
    driver.get("https://www.saucedemo.com/")

    #1.로그인 *login_page.py
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    #2. Sauce Labs Backpack 상품 Add to cart 버튼 클릭  *inventory_page.py
    inventory_page.add_backpack_to_cart()

    #3. 장바구니 클릭  *inventory_page.py
    inventory_page.go_to_cart()


    #4. 장바구니의 내역이 정상인지 확인  *cart_page.py
    actual_item_name = cart_page.get_item_name()   
    expected_item_name = "Sauce Labs Backpack"

    assert actual_item_name == expected_item_name, (
        f"상품명이 다릅니다. "
        f"기대값: {expected_item_name}, "
        f"실제값: {actual_item_name}"
    )


    input("결과 확인 후 Enter를 누르면 브라우저를 종료합니다.")

finally:
    driver.quit() 

