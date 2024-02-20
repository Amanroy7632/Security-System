import pyttsx3
import os
import wikipedia
import webbrowser
import datetime
import speech_recognition as sr
import openai
import time
# TODO:==========
# aman Api Key:=== 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
# openai.api_key="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"
# model_engine="gpt-3.5-turbo"
# prompt="hello, how are you today ?"
# completion=openai.ChatCompletion.create(engine=model_engine,
#          messages=[{"role":"user",
        #  "content":"write me a script for hosting a conference on technology"}])
        #  prompt=prompt,
        #  max_tokens=1024,
        #  n=1,
        #  stop=None,
        #  temperature=0.5)
# response(completion.choices[0].text)
# print(completion)

class OptimusPrime:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty('rate', 160)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            self.speak("Good Morning!")
        elif 12 <= hour < 18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")
        self.speak("I am Optimus Prime! How may I help you")

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again...")
            return "None"
        return query

    def run(self):
        # self.wishMe()
        query = self.takeCommand().lower()
        print(query)

        if 'wikipedia' in query:
            self.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            self.speak(results)
        elif 'open youtube' in query:
            self.speak("Opening , youtube")
            webbrowser.open("https://www.youtube.com")
        elif 'chat gpt' in query:
            self.speak("Opening , chat gpt")
            webbrowser.open("https://chat.openai.com")
        elif 'porn' in query:
             self.speak("Bhosdike , aukat me reh lee")
             webbrowser.open("https://pornhub.com")
        elif 'git' in query:
             self.speak("Opening , git hub")
             webbrowser.open("https://github.com")


        elif 'play music' in query:
            music_dir = 'E:\\Aman\\music'  # Provide the directory path where your music files are stored
            songs = os.listdir(music_dir)
            # i=0
            if len(songs) > 0:
                # os.startfile(os.path.join(music_dir, songs[i]))
                for i in range(5):
                    os.startfile(os.path.join(music_dir, songs[i]))
                    time.sleep(10)
                
                    
            else:
                self.speak("No music files found in the directory")

if __name__ == "__main__":
    assistant = OptimusPrime()
    assistant.wishMe()
    while True:
     assistant.run()
