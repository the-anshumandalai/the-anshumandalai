from mimetypes import init
from platform import uname
from unicodedata import name
import pyttsx3
import webbrowser
import random
import speech_recognition
import wikipedia
import datetime
import os
import sys

engine = pyttsx3.init()
voices  = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#initializing voice assisstant
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak("Good Morining Sir !")
    elif (hour>=12 and hour<18):
        speak("Good Afternoon Sir !")
    else:
        speak("Good Evening Sir !")
    name = ("Anshuman")
    speak("I am your Assisstant")
    speak(name)

def usrname():
    speak("What should I Call you Sir ?")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)



    speak("How can I help You ?")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User Said:  {query}\n")
    except exception as e:
        print(e)
        print("Could you speak more clearly")
        return "None"
    return query

if (__name__ == '__main__'):
    wishMe()
    usrname()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("Here is what wikipedia says...")
            print(results)
            speak(results)

        elif 'Open youtube' in query:
            speak("Yes Sir")
            webbrowser.Open("youtube.com")

        elif 'Open forum' in query:
            speak("Yes Sir")
            webbrowser.Open("forum.aistudent.community")

        elif 'Open google'in query:
            speak("Here you go to Google\n")
            webbrowser.Open("Yes Sir")

        elif 'open stack overflow' in query:
            speak("Yes Sir")
            webbrowser.Open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "Songs"
            Songs = os.listdir(music_dir)
            print(Songs)
            random = os.startfile(os.path.join(music_dir, Songs[1]))

        elif 'How are you' in query:
            speak("I am Fine, Thank You")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It is good to know that you are fine")

        elif "Change Name" in query:
            speak("What would you like to call me, Sir")
            name = takeCommand()
            speak("Thanks for naming me")

        elif "What's your name" in query or "What is your name" in query:
            speak("My friend call me")
            name = ("Anshuman")
            speak(name)
            print("My friends call me", name)

        elif 'search' in query or 'play' in query:
            query = query.replace("Search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif 'open Document' in query:
            speak("Opening powerpoint presentation")
            word = r"E:\Science Project.docx"
            os.startfile(word)

        elif "Who are you" in query:
            speak("I am your Virtual Assisstant")

        elif "Where is" in query:
            query = query.replace("Where is", "")
            location = query
            speak("User asked to locate")
            speak(location)
            webbrowser.open("https://www.google.come/maps/search/?api=1&" + location + "")

        elif "Write a note" in query:
            speak("What should I write, Sir")
            takeCommand()
            file = open('notes.txt', 'w')
            file.write(note)

        elif "Open Instagram" in query:
            speak("Yes Sir")
            webbrowser.open("Instagram.com")

        elif "Open Facebook" in query:
            speak("Yes Sir")
            webbrowser.open("Facebook.com")

        elif "Open Whatsapp" in query:
            speak("Yes Sir")
            webbrowser.open("web.whatsapp.com")

        elif "Open Discord" in query:
            speak("Yes Sir")
            webbrowser.open("discord.com")

        elif "Tell me my name" in query:
            speak("Your name is")
            speak(uname)

        elif "Show note" in query:
            speak("Yes Sir")
            speak("Showing notes")
            file = open("notes.txt", "r")
            print(file.read())
            print(file.read(6))

        elif "Will you be my friend" in query:
            speak("Sure Sir, why not")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

    
