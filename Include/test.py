import getpass
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


import win32con
import win32gui
import win32api

import pyautogui 
import pyperclip



# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#웹 드라이버 설정
driver = webdriver.Chrome(options=chrome_options)



url = 'https://focus.hanjin.com/login'
driver.get(url)

#로그인 페이지 이동 버튼 클릭
# login_page_btn = driver.find_element(By.XPATH,'//*[@id="account"]/div/a')
# login_page_btn.click()



user_id = '8'
user_pw = 'd'





# 아이디와 비밀번호를 입력
user_id_input = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/section/div[3]/form/div[1]/div/input')
user_pw_input = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/section/div[3]/form/div[2]/div/input')


user_id_input.send_keys(user_id)
user_pw_input.send_keys(user_pw)

# https://donghodazzi.tistory.com/305
# https://wikidocs.net/91474
# https://donghodazzi.tistory.com/305
# https://github.com/oahuoahu/automation_project_24.03.19

#fhrmdlsqjxms
# login_btn = driver.find_element(By.XPATH,'//*[@id="log.login"]')

login_btn = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/section/div[3]/form/div[4]/button')
login_btn.click()




# Dlvry_mngmnt_btn = driver.find_element(By.XPATH,'//*[@id="header"]/nav/ul/li[2]/div/ul/li[2]/a')
# Dlvry_mngmnt_btn.click()


# Dlvry_mngmnt_btn = driver.find_element(By.XPATH,'//*[@id="header"]/nav/ul/li[2]/div/ul/li[2]/a')
# Dlvry_mngmnt_btn.click()

time.sleep(0.1) 
url = 'https://focus.hanjin.com/release/listup'
driver.get(url)




Blk_rgst = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div/section/div[1]/div[1]/div[2]/label')
Blk_rgst.click()


time.sleep(0.5) 
# 윈도우 핸들 찾기
hwnd = win32gui.FindWindow(None, '열기')
time.sleep(0.5) 


# 윈도우가 찾아졌는지 확인
if hwnd != 0:
    print("윈도우가 찾아졌습니다. 핸들:", hwnd)
    file_name = "C:\\Users\\oahuo\\OneDrive\\바탕 화면\\gw.xlsx"
    
    time.sleep(0.5)
    pyperclip.copy("C:\\Users\\oahuo\\OneDrive\\바탕 화면\\gw.xlsx")
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    
    
else:
    print("윈도우를 찾을 수 없습니다.")
    time.sleep(5)
    hwnd = win32gui.FindWindow(None, '열기')
    win32gui.ShowWindow(hwnd, 3)
