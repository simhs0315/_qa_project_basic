#Python에서 운영체제의 환경변수를 읽기 위해 사용
import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():

    options = webdriver.ChromeOptions() #Chrome 브라우저의 실행 옵션을 설정하는 기능

    # GitHub Actions에서 실행할 때만 Headless 모드 적용
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new") #Chrome 창을 화면에 띄우지 않고 실행

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()