from selenium import webdriver  #webdriver : 브라우저를 실행하고 제어
from selenium.webdriver.common.by import By #By：웹페이지의 요소를 어떤 기준으로 찾을지 지정

driver = webdriver.Chrome() # driver : 지금 Chrome을 제어하고 있는 객체

driver.get("https://www.saucedemo.com/")

#1. ID값을 변수에 넣자
username = driver.find_element(By.ID, "user-name") #.find_element() : 현재 페이지에서 요소 하나를 찾아라 By.ID : ID를 기준으로 
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

#2. 계정값을 자동입력해보자
# saucedemo.com 계정 standard_user / secret_sauce
# send_keys : 키보드 입력하듯이 자동입력
username.send_keys("standard_user")
password.send_keys("secret_sauce")

#3.로그인 버튼 자동클릭
login_button.click() 

input("Enter를 누르면 브라우저를 종료합니다.")

driver.quit()
