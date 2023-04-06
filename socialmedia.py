import webbrowser
def socials(text):
    if 'open insta' in text or "open instagram" in text:
        webbrowser.open("instagram.com")
    if 'facebook' in text:
        webbrowser.open("facebook.com")
    if 'whatsapp' in text:
        webbrowser.open("web.whatsapp.com")

