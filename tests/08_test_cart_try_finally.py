# 3. 장바구니 자동화 > Day7
# #오류가 나도 브라우저를 종료 할 수 있도록. try-finally 추가해보자

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #몇초 동안 기다릴지
from selenium.webdriver.support import expected_conditions as EC #무엇이 될때 까지 기다릴지 별칭은 EC

#1. 브라우저 실행 및 사이트 접속
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10) #9. 최대 10초를 기다린다. 10초를 다 기다리는 것이 아니라 버튼 나타나면 10초안에 처리됨. 단, 10초가 지나 간다면 timeoutexception 발생  

try:
    driver.get("https://www.saucedemo.com/")


    #2. id 입력창 찾기
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    #3. 비밀번호 입력창 찾기
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    #4. 로그인 버튼 클릭
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    #10. sauce labs backpack 상품 add to cart 버튼 눌러서 장바구니 +1되는지 확인 + 10초안에 기다리고 처리하도록 코드 수정
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    #13. 코드 수정해서 10초 이상되게 : add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "wrong-add-to-cart-button")))
    #wait.until:내가 원하는 조건이 될때까지, EC.element_to_be_clickable(...):클릭할 수 있는 상태가 될 때까지(화면에 보이고, 비활성화되어 있지 않은 상태), By.ID, "add-to-cart-sauce-labs-backpack"):튜플
    add_to_cart_button.click()

    #7. 장바구니 클릭하기
    #11. 장바구니에 내가 원하는 상품명이 들어왔는지 확인하기 (성공케이스) + Explicit Wait을 추가
    cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='shopping-cart-link']")))
    cart_link.click()

    #12. 장바구니에 내가 원하는 상품명이 들어왔는지 확인하기 (성공케이스) + Explicit Wait을 추가 
    cart_item_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='inventory-item-name']")))
    #상품명은 클릭 대상이 아닌 화면에 보이는 텍스트 그대로 이기 때문에 EC.visibility_of_element_located 사용

    actual_item_name = cart_item_name.text
    expected_item_name = "Sauce Labs Backpack"
    # 아래 f"상품명이 다릅니다. 나오게 하기 : expected_item_name = "Sauce Labs Backpack11"

    assert actual_item_name == expected_item_name, (
        f"상품명이 다릅니다. "
        f"기대값: {expected_item_name}, "
        f"실제값: {actual_item_name}"
    )

    #5.브라우저 안꺼지도록 유지
    input("결과 확인 후 Enter를 누르면 브라우저를 종료합니다.")

finally:
    driver.quit() #오류가 나도 브라우저를 종료 할 수 있도록.

