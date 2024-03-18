import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#웹 드라이버 설정
driver = webdriver.Chrome(options=chrome_options)



url = 'https://www.naver.com'
driver.get(url)

#로그인 페이지 이동 버튼 클릭
login_page_btn = driver.find_element(By.XPATH,'//*[@id="account"]/div/a')
login_page_btn.click()



user_id = input('아이디를 입력해주세요 : ')
user_pw = getpass.getpass('비밀번호를 입력해주세요 : ')



# 아이디와 비밀번호를 입력
user_id_input = driver.find_element(By.ID,"id")
user_pw_input = driver.find_element(By.ID,"pw")

user_id_input.send_keys(user_id)
user_pw_input.send_keys(user_pw)

# https://donghodazzi.tistory.com/305
# https://wikidocs.net/91474
# https://donghodazzi.tistory.com/305
# https://github.com/oahuoahu/automation_project_24.03.19

#fhrmdlsqjxms
login_btn = driver.find_element(By.XPATH,'//*[@id="log.login"]')
login_btn.click()