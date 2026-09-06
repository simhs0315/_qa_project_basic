


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By

class InventoryPage : 

    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def __init__(self,driver): #login_page = LoginPage(driver)객체 만들때 이게 실행되서 self라는게 계속해서 driver를 가지고 있게끔 한다
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def add_backpack_to_cart(self):
        #2. Sauce Labs Backpack 상품 Add to cart 버튼 클릭
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()

    def go_to_cart(self):    
        #3. 장바구니 클릭 
        cart_link = self.wait.until(EC.element_to_be_clickable(self.CART_LINK))
        cart_link.click()




