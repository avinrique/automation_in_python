import webbrowser , pyautogui
from time import sleep
import speect_text
def youutube():
    webbrowser.open("youtube.com")
    song_video = speect_text.usemic("which song or video do you want to listen/watch", "")
    print(song_video)
    sleep(5)
    pyautogui.press('tab', presses=4)
    sleep(0.2)
    pyautogui.write(song_video)
    pyautogui.press("enter")
    sleep(2)
    pyautogui.press("enter")