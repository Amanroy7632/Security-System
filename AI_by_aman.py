import pyttsx3
import os
import wikipedia
import webbrowser
# import py_audio
from googletrans import Translator
import datetime
import speech_recognition as sr



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',160)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Optimus Prime! How may i help you")  
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again...")
        return "None"
    return query  
# def takecommand():
#     # it takes microphone as input and return string as output 
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listning...")
#         r.pause_threshold=1
#         audio=r.listen(source)
#     try:
#         print("Recognizing...")
#         query=r.Recognize_google(audio,Language='en-in')
#         print(f"User said: {query}\n")
#     except Exception as a:
#         print("Say that again..")
#         return "None"
#     return query 




if __name__=="__main__":
    # speak("Aman")
      wishMe()
    # while True:
      query=takecommand().lower()
      if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query=query.replace("wikipwdia","")
        results=wikipedia.summary(query,sentences=2)
        speak(result)
      elif 'open youtube' in query:
        webbeowser.open("youtube.com")

      elif'play music' in query:
        music_dir=''
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(music_dir,songs[0])
        




