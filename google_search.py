import webbrowser ,pyautogui
from time import sleep
import speect_text
def googlesearch():
    webbrowser.open("google.com")
    sleep(2)
    google_search = speect_text.usemic("what do you want to search" , "")
    pyautogui.write(google_search)
    pyautogui.press("enter")
    speect_text.say(google_search)
