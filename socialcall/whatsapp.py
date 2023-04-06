import pyautogui as p
from time import sleep
import speect_text
import webbrowser
def call():

    speect_text.say("whatsApp app is not in your system, so unable to call")
def message():
    webbrowser.open("web.whatsapp.com")
    sleep(15)
    p.press("tab" , presses=5)
    person_name = speect_text.usemic("who do you want to send message", "")
    p.write(person_name)
    p.press("down")
    p.press('tab' , 6)
    p.press('enter')

# 5 tabs for search
# search
# down
# tab 6
#enter