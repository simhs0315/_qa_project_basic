

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By


class CartPage : 

    #1.Cart 페이지의 상품명 요소 위치 정보 /나중에 Locator가 변경되면 밑에서 뒤질필요없이 여기만 수정하면 되겠지?
    ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
      
    def __init__(self,driver): #login_page = LoginPage(driver)객체 만들때 이게 실행되서 self라는게 계속해서 driver를 가지고 있게끔 한다
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #2.그 요소가 보일 때까지 기다리고 실제 텍스트 반환
    def get_item_name(self):
        cart_item_name = self.wait.until(EC.visibility_of_element_located(self.ITEM_NAME))
        return cart_item_name.text