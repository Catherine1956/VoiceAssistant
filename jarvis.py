import speech_recognition as sr
from datetime import *
import pyttsx3
import wikipedia
import webbrowser
import os
import subprocess
import ctypes
import time
import pyjokes
import random
from requests import get
from googlesearch import search


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")
engine.setProperty("rate", rate - 25)
engine.setProperty("voice", voices[1].id)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
name = "jarvis"
greetings = [
    "hi",
    "hai",
    "hello",
    "hey",
    "hay",
    "haay",
    "hi " + name,
    "hai " + name,
    "hello " + name,
    "hey " + name,
    "hay " + name,
    "haay " + name,
]
positive_responses = ["s", "yes", "yeah", "sure", "off course"]
negative_responses = ["n", "no", "nah", "not really", "not interested"]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def record():
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        with open("record.wav", "wb") as f:
            f.write(audio.get_wav_data())
        print("Transcript is being created")
        query = r.recognize_google(audio, language="en-in")
        print(f"transcript: {query}\n")
        # speak('Do you want to save the transcript sir')

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"


websites = {
    "youtube": "https://youtube.com",
    "wikipedia": "https://wikipedia.org",
    "google": "https://google.com",
    "whatsapp": "https://web.whatsapp.com",
    "facebook": "https://www.facebook.com/",
    "instagram": "https://www.instagram.com/",
}
subprocesses = ["lock window", "shutdown", "restart", "hibernate", "log off"]

if __name__ == "__main__":

    def clear():
        return os.system("cls")

    # This Function will clean any
    # command before execution of this python file
    clear()
    close = False
    speak(name + " at your service sir")
    while True:
        query = takeCommand().lower()
        try:
            if "wikipedia" in query and "open wikipedia" not in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif "what is the time" in query:
                print(datetime.now())

            elif "play music" in query or "play song" in query:
                speak("Here you go with music")
                music_dir = "C:/Users/nerus/Music"
                songs = [song for song in list(os.listdir(music_dir)) if ".mp3" in song]
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[0]))

            elif "search" in query or "play" in query:
                query = query.replace("search", "")
                query = query.replace("play", "")
                webbrowser.open(query)

            elif "record" in query:
                record()

            # websites
            elif "open" in query:
                for key in websites.keys():
                    if key in query:
                        webbrowser.open(url=websites[key])
                        speak(key + " opened successfully")

            # applications
            elif "open sublime" in query:
                application = "C:/Program Files/Sublime Text 3/sublime_text.exe"
                os.startfile(application)
                speak("sublime text editor is opened")

            elif "open chrome" in query:
                application = chrome_path
                os.startfile(application)
                speak("google chrome opened successfully")

            elif "open edge" in query:
                application = (
                    "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
                )
                os.startfile(application)
                speak("Microsoft edge opened successfully")

            elif "open android studio" in query:
                application = "C:/Program Files/Android/Android Studio/bin/studio64.exe"
                os.startfile(application)
                speak("sublime text editor opened successfully")

            elif "open vs code" in query:
                application = (
                    "C:/Users/nerus/AppData/Local/Programs/Microsoft VS Code/Code.exe"
                )
                os.startfile(application)
                speak("VS Code editor opened successfully")

            # subprocesses

            elif "lock window" in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif "shutdown" in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call(["shutdown", "/s", "/f"])

            elif "restart" in query:
                subprocess.call(["shutdown", "/r"])

            elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                subprocess.call(["shutdown", "/h"])

            elif "log off" in query or "sign out" in query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif "don't listen" in query or "stop listening" in query:
                speak(
                    "for how much time you want to stop jarvis from listening commands (Specify time in minutes)"
                )
                a = int(takeCommand())
                time.sleep(a * 60)
                print(a)

            # conversation
            elif query in greetings:
                speak(random.choice(greetings[:3]) + " sir")

            elif "how are you" in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif "fine" in query or "good" in query:
                speak("It's good to know that your fine")

            elif "change my name to" in query:
                query = query.replace("change my name to", "")
                name = query

            elif "change name" in query:
                speak("What would you like to call me, Sir ")
                name = takeCommand()
                speak("Thanks for naming me")

            elif "what's your name" in query or "What is your name" in query:
                speak("My friends call me")
                speak(name)
                print("My friends call me", name)

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by Catherine.")

            elif "joke" in query:
                speak(pyjokes.get_joke())

            elif "exit" in query or "break" in query:
                speak("Thanks for giving me your time")
                close = True
                exit()

            else:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
        except:
            if close:
                exit()
            print("Unable to Recognize your Command.")
            speak("Unable to Recognize your Command.")

"""
pyttsx3.drivers
pyttsx3.drivers.sapi5
"""
