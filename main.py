import socialcall.all_social_media
import media.youtube
import syscmds , socialmedia, speect_text , google_search , osinfo
import webbrowser , pyautogui , os , sys , subprocess , threading
from time import sleep

z = ["open insta","open instagram","open facebook",'open whatsapp']
count=0
while True:
    speech_input = speect_text.usemic("speak something", "Avin")
    print(f"you said : {speech_input}" )
    text = speech_input.lower()

    if "system" in text or "info" in text :
        osinfo.os_info()
    if "hello" in text:
        subprocess.run(["gnome-terminal"], stdout=subprocess.PIPE)
        sleep(1)
        pyautogui.write("figlet Hello_Avin")
        pyautogui.press("enter")

#Systems commands
    if "activation of" in text:
        while True:
            speech_input = speect_text.usemic("", "").lower()
            text = speech_input.lower()
            if "activation on" in text:
                break

    #lock screen
    if "lock" in text and "screen" in text:
        syscmds.lockscreen()
    if "unlock" in text:
        syscmds.unlock_screen()

    # bluetooth
    if "bluetooth" in text:
        if "on" in text:
            syscmds.bluetooth("rfkill unblock bluetooth")
        if "off" in text:
            syscmds.bluetooth("rfkill block bluetooth")

    #shutdown
    if "shutdown" in text:
        if "now" in text:
            syscmds.shutdown_now()
        res = any(chr.isdigit() for chr in text)
        if res==True:
            syscmds.shutdown_in_time(text)

#apps

    #system monitor
    if "system monitor" in text:
        os.system("gnome-system-monitor")

    #youtube
    if 'open' in text and "youtube" in text:
            #media.youtube.youutube()
            x = speect_text.usemic("which song you want to play","")
            x=x.split()
            print(x)
            xde=""
            count=0
            for i in x:
                len
                if count ==len(x):
                    pass
                else:
                    xde += i + "+"
                count+=1

            print(xde)

            webbrowser.open(f"https://www.youtube.com/results?app=desktop&search_query={xde}")

#social media
    for i in z:
        if i in text:
            socialmedia.socials(text)

    #google search
    if "open google" in text:
        google_search.googlesearch()

#social media call and text
    if "call" in text or "text" in text:
        socialcall.all_social_media.all_media_call_or_text(text)
