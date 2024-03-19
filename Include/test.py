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
import pandas as pd
import os
import glob
import ctypes
import sys

#관리자권한으로 실행.
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if is_admin():
    # 브라우저 꺼짐 방지 옵션
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    #웹 드라이버 설정
    driver = webdriver.Chrome(options=chrome_options)

    url = 'https://focus.hanjin.com/login'
    driver.get(url)

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

    # 로그인버튼 클릭
    login_btn = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/section/div[3]/form/div[4]/button')
    login_btn.click()

    #접속시간 약간 기다림
    time.sleep(0.1)  

    #출력페이지로 이동
    url = 'https://focus.hanjin.com/release/listup'
    driver.get(url)

    #엑셀파일로 일괄등록 클릭.
    Blk_rgst = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div/section/div[1]/div[1]/div[2]/label')
    Blk_rgst.click()


    time.sleep(0.5) 
    # 윈도우 핸들 찾기
    hwnd = win32gui.FindWindow(None, '열기')
    time.sleep(0.5) 


    # 파일주소를 입력할 윈도우가 찾아졌는지 확인
    if hwnd != 0:
        print("윈도우가 찾아졌습니다. 핸들:", hwnd)

        #파일주소셋팅및 복붙후 엔터해서 파일을 연다.
        file_name = "C:\\Users\\oahuo\\OneDrive\\바탕 화면\\gw.xlsx"
        time.sleep(0.5)
        pyperclip.copy("C:\\Users\\oahuo\\OneDrive\\바탕 화면\\gw.xlsx")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        
        
        
        #오류체크 버튼 클릭
        err_check = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div/section/div[1]/div[1]/div[2]/button[1]')
        err_check.click()
        
        
        #오류체크 완료의 확인 버튼 클릭.
        time.sleep(0.5)
        cnfrm_btn = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/button')
        cnfrm_btn.click()
        
        
        #운송장 즉시출력 버튼 클릭
        time.sleep(0.5)
        Inv_prt = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div/section/div[1]/div[1]/div[2]/button[5]')
        Inv_prt.click()
        #로딩이 좀 필요하다.
        time.sleep(2)
        
        
        #프린터 바로 출력 버튼 클릭.
        Immdt_prt = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div/section/div[11]/div/div[2]/div[2]/table/tbody/tr[2]/td/div/div[3]/button[1]')
        Immdt_prt.click()
        
        
        
        
        win_prnt = None
        #윈도우가 프린터창이 인식될때까지 반복
        while not win_prnt:
            win_prnt = win32gui.FindWindow(None, '인쇄')
            if not win_prnt:
                print("윈도우 찾는중 잠시 후 다시 시도")
                time.sleep(0.5)
                
        print(win_prnt)
        time.sleep(2)    
        button_hwnd = win32gui.FindWindowEx(win_prnt, 0, "Button", '확인')
        win32gui.SendMessage(button_hwnd, win32con.BM_CLICK, 0, 0)


        
        #즉시출력창을 닫는다.
        close_btn = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div/section/div[11]/div/div[1]/button')
        close_btn.click()
        
        #엑셀파일로 다운로드 버튼 클릭
        dwn_xls = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/main/div/section/div[1]/div[3]/div[1]/div[1]/div[2]/button[3]')
        dwn_xls.click()
        
        
        
        
        time.sleep(2)   
        #다운로드 폴더를 찾아서 가장 최신파일을 열어본다
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        latest_file = max(glob.glob(download_folder + '/*'), key=os.path.getctime)
        os.startfile(latest_file)



    else:
        print("윈도우를 찾을 수 없습니다.")
        time.sleep(5)
        hwnd = win32gui.FindWindow(None, '열기')
        win32gui.ShowWindow(hwnd, 3)

else:
    # 관리자 권한으로 다시 실행합니다.
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)