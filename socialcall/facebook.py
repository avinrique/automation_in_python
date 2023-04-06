import webbrowser
from time import sleep
import pyautogui as p
import speect_text as sp
import tkinter as tk
def call():
    webbrowser.open("facebook.com")
    sleep(10)
    p.press("tab",  presses=10)
    p.press("enter")
    p.press("tab", presses=4)
    person_name = sp.usemic("who do you want to call" , "avin")
    p.write(person_name)
    p.press("down")
    p.press("enter")
def message():
    webbrowser.open("facebook.com")
    sleep(10)
    p.press("tab", presses=10)
    p.press("enter")
    p.press("tab", presses=4)
    person_name = sp.usemic("who do you want to send", "avin")
    print(person_name)
    p.write(person_name)
    p.press("down")
    p.press("enter")
    message_send = sp.usemic("what message you want to send", "avin")
    p.write(message_send)
    p.press('tab', presses=2)
    p.press("enter")



