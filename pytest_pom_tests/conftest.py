
#5. 테스트 프레임워크 > day2 웹브라우저 실행을 위한 기능을 새로운 파일을 만들어 따로 기재.

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()
