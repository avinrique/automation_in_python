import socialcall.whatsapp , socialcall.instagram , socialcall.facebook
def all_media_call_or_text(text):
    if "whatsapp" in text:
        if "call" in text:
            socialcall.whatsapp.call()
        if "text" in text:
            socialcall.whatsapp.message()
    if "messenger" in text:
        if "call" in text:
            socialcall.facebook.call()
        if "text" in text:
            socialcall.facebook.message()
    if "instagram" in text:
        if "call" in text:
            socialcall.instagram.call()

        if "text" in text:
            socialcall.instagram.message()
