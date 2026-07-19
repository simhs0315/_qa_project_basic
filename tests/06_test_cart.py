# 3.장바구니 자동화 > Day3 
# 로그인후 장바구니에 +1 자동으로 하기 #3~#6 

# 3. 장바구니 자동화 > Day4
# +1된 장바구니 클릭하기 #7~#8-1

from selenium import webdriver
from selenium.webdriver.common.by import By

#1. 브라우저 실행 및 사이트 접속
driver = webdriver.Chrome()
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

#6. sauce labs backpack 상품 add to cart 버튼 눌러서 장바구니 +1되는지 확인
add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart_button.click()

#7. 장바구니 클릭하기
cart_link = driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
cart_link.click()

#8. 장바구니에 내가 원하는 상품명이 들어왔는지 확인하기 (성공케이스)
cart_item_name = driver.find_element(By.CSS_SELECTOR,"[data-test='inventory-item-name']")

actual_item_name = cart_item_name.text
print('actual_item_name = ' + actual_item_name)

expected_item_name = "Sauce Labs Backpack"
print('expected_item_name = ' + expected_item_name)

assert actual_item_name == expected_item_name
print("장바구니 상품 검증 성공")

# #8-1. 실패 케이스(문구를 임의로 수정 Sauce Labs Backpack111")
# cart_item_name = driver.find_element(By.CSS_SELECTOR,"[data-test='inventory-item-name']")
# actual_item_name = cart_item_name.text
# print('actual_item_name = ' + actual_item_name)

# expected_item_name = "Sauce Labs Backpack111"
# print('expected_item_name = ' + expected_item_name)

# #아래 명령어는 pass시에 다음으로 넘어가니 장바구니 상품 검증 성공 이건 안나오겠지
# assert actual_item_name == expected_item_name
# print("장바구니 상품 검증 성공") 

#5.브라우저 안꺼지도록 유지
input("결과 확인 후 Enter를 누르면 브라우저를 종료합니다.")
driver.quit()

