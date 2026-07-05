from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

input("Enter를 누르면 브라우저를 종료합니다.")

driver.quit()

# 그래서 실무 습관은 프로젝트를 만들면 거의 항상 마지막 줄에
# driver.quit() 을 넣는 습관을 들여.