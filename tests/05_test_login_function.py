# 2.로그인 자동화 > Day6 자동화 함수로 만들어보자
from selenium import webdriver
from selenium.webdriver.common.by import By 

#1. 로그인 받을 계정을 저장할 함수 입력
def login(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/") 

#2_1. 성공 케이스의 계정 테스트
login(driver, "standard_user", "secret_sauce")
#2_2. 실패 로그인 계정으로 테스트
#login(driver, "wrong_user", "wrong_password")

current_url = driver.current_url
print(current_url)

#3. 화면에 뜨는 에러 코드의 id값을 가져오려 했으나 id값이 없어서 By.CSS_SELECTOR 사용 후에 data-test='error'값을가져옴
# error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
# print(error_message.text)

# #4. 아래 명령어가 나와서 true일때만 다름으로 넘어가라
# assert "Username and password do not match" in error_message.text

assert "inventory" in current_url

add_to_cart = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")

print(add_to_cart)

input("Enter를 누르면 브라우저를 종료합니다.")

driver.quit()