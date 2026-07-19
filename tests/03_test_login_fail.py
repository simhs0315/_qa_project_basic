# 로그인 실패 케이스를 만들어보자 '2. 로그인 자동화 > Day4'
from selenium import webdriver  
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome() 

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name") 
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# saucedemo.com 계정 standard_user / secret_sauce
username.send_keys("wrong_user")
password.send_keys("wrong_password")

login_button.click() 

input("Enter를 누르면 브라우저를 종료합니다.")

driver.quit()
