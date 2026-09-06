
#5. 테스트 프레임워크 > day2 , pytest를 동작해보기 위해서 새로운 폴더 및 파일을 복사하여 진행

from pytest_pom_pages.pytest_login_page import LoginPage
from pytest_pom_pages.pytest_inventory_page import InventoryPage
from pytest_pom_pages.pytest_cart_page import CartPage


def test_cart(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)


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


    # pytest를 진행하며 테스트 자동화가 실행되는데 사람이 직접 눌러줘서 종료되면 안되니 삭제처리
    # input("결과 확인 후 Enter를 누르면 브라우저를 종료합니다.")      

