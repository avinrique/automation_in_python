import pyautogui , subprocess ,os
from time import sleep
def lockscreen():
    pyautogui.keyDown("win")
    pyautogui.press("l")
    pyautogui.keyUp('win')
def unlock_screen():
    password = "20014"
    sleep(0.5)
    pyautogui.press('win')
    sleep(3)
    pyautogui.press('win')
    pyautogui.write(password)
    pyautogui.press('enter')

def bluetooth(state):
    print(state)
    os.system(state)
def shutdown_now():
    os.system("shutdown now")
def shutdown_in_time(text):
    num =  [int(i) for i in text.split() if i.isdigit()]
    if "min" in text:
        os.system(f"shutdown -h -P -t {num[0]}")
    if "sec" in text or "second" in text or "seconds" in text:
        os.system(f"shutdown -h -P -t {num[0]}")