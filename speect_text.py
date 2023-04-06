import speech_recognition as sr
r = sr.Recognizer()
import subprocess
def usemic(a,b):
    while True:
        with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print(b ,a)
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    text = text.lower()
                    print(f"the text is {text}")
                    return text
                except sr.UnknownValueError:
                    print("Sorry, I could not understand what you said.")
                except sr.RequestError as e:
                    print("Sorry, could not request results from Google Speech Recognition service; {0}".format(e))


def say(text):
    process = subprocess.Popen(['festival', '--tts'], stdin=subprocess.PIPE)
    process.communicate(text.encode('utf-8'))
