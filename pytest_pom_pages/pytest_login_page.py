


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