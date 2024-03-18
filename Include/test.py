from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#웹 드라이버 설정
driver = webdriver.Chrome(options=chrome_options)



url = 'https://www.naver.com'
driver.get(url)