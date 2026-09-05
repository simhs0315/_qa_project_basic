
#4. 구조 개선 > day2(tests > 08_test_cart_try_finally파일의 로그인 영역 내용을 pom 형식으로 변경하는것
# Page 파일에는 Selenium으로 실제 화면을 조작하거나 값을 가져오는 코드로 분리

from selenium.webdriver.common.by import By

class LoginPage : 

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    #login_page = LoginPage(driver)객체 만들때 이게 실행되서 self라는게 계속해서 driver를 가지고 있게끔 한다
    def __init__(self,driver): 
        self.driver = driver


    def login(self, username, password):
        username_input = self.driver.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(username)

        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()