from selenium import webdriver #Selenium에서 브라우저를 조작하기 위한 webdriver를 가져옴
from selenium.webdriver.common.by import By #웹페이지의 요소를 ID 같은 기준으로 찾기 위한 By를 가져옴

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/") #driver가 조작하고 있는 Chrome에서 해당 주소로 이동함

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

login_button.click()

#지금 브라우저에 떠 있는 현재 주소를 가져옴
current_url = driver.current_url
#터미널창 확인용
print(current_url)

#실제 검증용
assert "inventory" in current_url

input("Enter를 누르면 브라우저를 종료합니다.")

driver.quit()