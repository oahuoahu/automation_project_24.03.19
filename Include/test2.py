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







def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # 스크립트가 관리자 권한으로 실행됩니다.
    # 여기에 실행할 코드를 넣으세요.
    win_prnt = None

    while not win_prnt:
        win_prnt = win32gui.FindWindow(None, '인쇄')
        if not win_prnt:
            print("윈도우 찾는중 잠시 후 다시 시도")
            time.sleep(0.5)
            
    print(win_prnt)
    win32gui.SetForegroundWindow(win_prnt)



    button_handle = win32gui.FindWindowEx(win_prnt, 0, "Button", '확인')

    if button_handle:
        win32gui.SendMessage(button_handle, win32con.BM_CLICK, 0, 0)
        
        win32gui.SendMessage(button_handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
        win32gui.SendMessage(button_handle, win32con.WM_LBUTTONUP, 0, 0)
        print("클릭완료")
    else:
        print("확인 버튼을 찾을 수 없습니다.")


    # print(button_hwnd)
    # win32gui.SetForegroundWindow(button_hwnd)
    # pyautogui.press('enter')
    # print("asdfasdf")


    # win32gui.SendMessage(button_hwnd, win32con.BM_CLICK, 0, 0)

else:
    # 관리자 권한으로 다시 실행합니다.
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)