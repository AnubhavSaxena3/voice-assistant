import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
from News import *
import randfacts
from jokes import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)  # we can set the speed of voice by this
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello sir or ma'am, I am Freddy the voice assistant, how are you.")
    

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, 1.2)
        audio = r.listen(source)
        # text = r.recognize_google(audio)
        # print(text)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('yourmail@gmail.com', 'your-password')
#     server.sendmail('yourmail@gmail.com', to, content)
#     server.close()


if __name__ == "__main__":

    while True:
        # if 1:
        wishMe()
        query = takeCommand().lower()

        if 'what' and 'about' in query:
            speak('I am also having a fantastic day sir.')
            speak('tell me, how can i help you?')

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("Opening youtube please wait...")
            speak("Opening youtube please wait")
            webbrowser.open("youtube.com")
       
        elif 'open google' in query:
            print("Opening google please wait...")
            speak("Opening google please wait")
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            print("Opening stackoverflow please wait")
            speak("Opening stackoverflow please wait")
            webbrowser.open("stackoverflow.com")

        elif 'weather' in query:
            print("please wait it's coming")
            speak("please wait it's coming")
            webbrowser.open("https://www.google.com/search?q=weather&rlz=1C1JJTC_enIN1019IN1019&oq=weather&aqs=chrome..69i59j69i57j0i131i433i512j0i131i433i457i512j0i402i650l2j0i131i433i512l2j46i131i433i512j0i512.4564j1j15&sourceid=chrome&ie=UTF-8")

        elif 'play music' in query:
            music_dir = "C:\\Users\\Dell\\Music\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        # elif 'open code' in query:
        #     codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)

        # elif 'email to anubhav' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "yourmail@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend Anubhav . I am not able to send this email currently because maybe you are not enabled less secured app")

        elif 'news' in query:
            print("Sure sir , now i will read news for you.")
            speak("Sure sir , now i will read news for you.")
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])

        elif 'facts' in query:
            x = randfacts.get_fact()
            print(x)
            speak("Did you know that, " + x)

        elif 'joke' in query:
            speak("sure sir, get ready for some chuckles")
            ar = joke()
            print(ar[0])
            speak(ar[0])
            print(ar[1])
            speak(ar[1])

        if 'exit' in query:
            speak("exited")
            exit()
