from tkinter import *
import time
from tkinter import messagebox as tmsg
import pyttsx3
import os
import wikipedia
import webbrowser
import datetime
import speech_recognition as sr


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
        self.wishMe()
        query = self.takeCommand().lower()
        print(query)

        if 'wikipedia' in query:
            self.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            self.speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'play music' in query:
            music_dir = ''  # Provide the directory path where your music files are stored
            songs = os.listdir(music_dir)
            if len(songs) > 0:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                self.speak("No music files found in the directory")


class SecuritySystem:
    def __init__(self):
        self.armed = False
        self.door_locked = True
        self.window_locked = True

    def arm(self):
        if not self.armed:
            self.armed = True
            return "🔐 Security system armed."
        else:
            return "🔐 Security system is already armed."

    def disarm(self):
        if self.armed:
            self.armed = False
            return "🔐 Security system disarmed."
        else:
            return "🔐 Security system is already disarmed."

    def lock_door(self):
        if not self.door_locked:
            self.door_locked = True
            return "🚪 Door locked."
        else:
            return "🚪 Door is already locked."

    def unlock_door(self):
        if self.door_locked:
            self.door_locked = False
            return "🚪 Door unlocked."
        else:
            return "🚪 Door is already unlocked."

    def lock_window(self):
        if not self.window_locked:
            self.window_locked = True
            return "🔒 Window locked."
        else:
            return "🔒 Window is already locked."

    def unlock_window(self):
        if self.window_locked:
            self.window_locked = False
            return "🔓 Window unlocked."
        else:
            return "🔓 Window is already unlocked."

    def status(self):
        return (f"System Armed 💻: {'Yes' if self.armed else 'No'}\n"
                f"Door Locked 🚪: {'Yes' if self.door_locked else 'No'}\n"
                f"Window Locked 🪟: {'Yes' if self.window_locked else 'No'}")


class HouseGUI(Tk):
    def __init__(self):
        self.securityObj = SecuritySystem()
        self.optimus = OptimusPrime()
        super().__init__()
        self.geometry("1920x1080")
        self.title("Security System")
        self.photox = PhotoImage(file="backgr.png")
        Label(image=self.photox).pack()
        self.head_frame = Frame(self, borderwidth=7, relief=SUNKEN, padx=281, bg="grey5").place(
            x=0, y=0, width=1535, height=80)
        self.heading_label = Label(text="🏠 House Security System", font=(
            "Courier New", 20, "bold"), bg="grey5", fg="white").place(x=450, y=7, width=500, height=50)
        def get_time():
            timeVar = time.strftime("%I:%M:%S %p")
            self.clock.config(text=timeVar)
            self.clock.after(200, get_time)
        self.clock = Label(self.head_frame, font=(
            "Courier New", 18), bg="grey5", fg="white")
        self.clock.place(x=10, y=12, width=170, height=60)
        get_time()
        self.dates = Label(self.head_frame, bg="grey5", fg="white", font=(
            "Courier New", 18), text=datetime.datetime.now().strftime('%d %b,%Y'))
        self.dates.place(x=1370, y=12, height=60)
        self.heading = Label(text="Security System", font=(
            "times new roman", 20, "bold")).pack()
        self.UserId = StringVar(self)
        self.Password = StringVar(self)
        # =============frame for userid or password=============

        def arm(self):
            if (self.securityObj.armed):
                self.optimus.speak(
                    "Sorry Cheif ! House arm has already activated")
                message = self.securityObj.arm()
            else:
                self.optimus.speak("Are you sure cheif ! activate the arm")
                result = tmsg.askyesno("Optimus Prime", "Are you Sure")
                if (result):
                    message = self.securityObj.arm()
                    self.optimus.speak("House arm activated successfully")
                else:
                    self.optimus.speak("Okay,cheif")
            self.status_label.config(text=message)

        def create_widgets(self):
            self.status_label = Label(self.login_frame, text="", font=(
                "Helvetica", 14, "bold"), fg="white", bg="black")
            self.status_label.place(x=560, y=500)
        self.login_frame = Frame(self, borderwidth=7, relief=SUNKEN, padx=281, bg="grey5").place(
            x=430, y=200, width=630, height=500)
        button_arm = Button(self.login_frame, text="🦾 Arm System", font=("Courier New", 17, "bold"),
                            bg="blue", fg="white", command=lambda: arm(self)).place(x=500, y=220, width=230, height=35)
        button_disarm = Button(self.login_frame, text="✿ Disarm System", font=("Courier New", 17, "bold"),
                               bg="red", fg="white", command=lambda: disarm(self)).place(x=760, y=220, width=230, height=35)
        button_lock_door = Button(self.login_frame, text="🔒 Lock Door", font=("Courier New", 17, "bold"),
                                  bg="red", fg="white", command=lambda: lock_door(self)).place(x=500, y=270, width=230, height=35)
        button_unlock_door = Button(self.login_frame, text="🔓 Unlock Door", font=(
            "Courier New", 17, "bold"), fg="green", command=lambda: unlock_door(self)).place(x=760, y=270, width=230, height=35)
        button_lock_window = Button(self.login_frame, text="🪟 Lock Window", font=(
            "Courier New", 17, "bold"), fg="blue", command=lambda: lock_window(self)).place(x=500, y=320, width=230, height=35)
        button_unlock_window = Button(self.login_frame, text="🪟 Unlock Window", font=(
            "Courier New", 17, "bold"), bg="blue", fg="white", command=lambda: unlock_window(self)).place(x=760, y=320, width=230, height=35)
        button_status = Button(self.login_frame, text="⚧️ Status", command=lambda: get_status(self), font=(
            "Courier New", 17, "bold"), bg="blue", fg="white").place(x=500, y=370, width=230, height=35)
        button_quit = Button(self.login_frame, text="⬅️ Quit", command=lambda: closeProgram(self), font=(
            "Courier New", 17, "bold"), bg="blue", fg="white").place(x=760, y=370, width=230, height=35)
        create_widgets(self)
        self.lineframe = Frame(self.login_frame).place(
            x=430, y=420, width=630, height=6)
        Label(self.login_frame, text="Displaying the Tasks: ", font=("Courier New",
              17, "bold"), bg="black", fg="cyan").place(x=550, y=430, width=400, height=30)

        def closeProgram(self):
            self.status_label.config(text="🎙️ Recognizing...")
            self.optimus.speak("Cheif ! Are you sure want to exit")
            query = self.optimus.takeCommand()
            print(query)
            query = query.lower()
            if ('n' in query):
                self.status_label.config(text="Ok Cheif..")
                self.optimus.speak("Ok Cheif")
            else:
                self.optimus.speak("Bye Cheif ! have a good day")
                self.destroy()

        def clearAction(self):
            self.status_label.config(text="")

        def disarm(self):
            if (not self.securityObj.armed):
                self.optimus.speak(
                    "Sorry Cheif ! House arm is already deactivated")
                message = self.securityObj.disarm()
            else:
                self.optimus.speak(
                    "Are you sure cheif ! deactivate the house arm")
                result = tmsg.askyesno("Are you Sure")
                if (result):
                    self.optimus.speak("House arm deactivating")
                    time.sleep(1)
                    message = self.securityObj.disarm()
                    self.optimus.speak(
                        "House arm has been deactivated successfully")
                else:
                    self.optimus.speak("Thanks , cheif")
            self.status_label.config(text=message)

        def lock_door(self):
            if (self.securityObj.door_locked):
                self.optimus.speak("Sorry Cheif ! door has already locked")
                message = self.securityObj.lock_door()
            else:
                self.optimus.speak("Are you sure cheif ! lock the door")
                result = tmsg.askyesno("Bot", "Are you Sure")
                if (result):
                    message = self.securityObj.lock_door()
                    self.optimus.speak("door locked successfully")
                else:
                    self.optimus.speak("Thanks ! cheif")
            self.status_label.config(text=message)

        def unlock_door(self):
            if (not self.securityObj.door_locked):
                self.optimus.speak("Sorry Cheif ! door is already unlocked")
                message = self.securityObj.unlock_door()
            else:
                self.optimus.speak("Are you sure cheif ! unlock the door")
                result = tmsg.askyesno("Are you Sure")
                if (result):
                    self.optimus.speak("door Lock deactivating")
                    time.sleep(1)
                    message = self.securityObj.unlock_door()
                    self.optimus.speak(
                        "Door lock has been deactivated successfully")
                else:
                    self.optimus.speak("Thanks ! cheif")
            self.status_label.config(text=message)

        def lock_window(self):
            if (self.securityObj.window_locked):
                self.optimus.speak("Sorry Cheif ! window is already locked")
                message = self.securityObj.lock_window()
            else:
                self.optimus.speak("Are you sure cheif ! lock the Window")
                result = tmsg.askyesno("Are you Sure")
                if (result):
                    message = self.securityObj.lock_window()
                    self.optimus.speak("Window locked successfully")
                else:
                    self.optimus.speak("Thanks ! cheif")
            self.status_label.config(text=message)

        def unlock_window(self):
            if (not self.securityObj.window_locked):
                self.optimus.speak("Sorry Cheif ! window is already unlocked")
                message = self.securityObj.unlock_window()
            else:
                self.optimus.speak("Are you sure cheif ! unlock the Window")
                result = tmsg.askyesno("Are you Sure")
                if (result):
                    message = self.securityObj.unlock_window()
                    self.optimus.speak("Window lock deactivating")
                    time.sleep(1)
                    self.optimus.speak(
                        "Window lock has been deactivated successfully")
                else:
                    self.optimus.speak("Thanks ! cheif")
            self.status_label.config(text=message)

        def get_status(self):
            if (self.securityObj.armed and self.securityObj.door_locked and self.securityObj.window_locked):

                self.optimus.speak(
                    "All Seems to good cheif , House armed is activated")
            elif (not self.securityObj.door_locked and not self.securityObj.window_locked):
                self.optimus.speak(
                    "cheif , House Window and Doors are unlocked")
            elif (not self.securityObj.door_locked):
                self.optimus.speak("cheif , House  Doors are unlocked")
            elif (not self.securityObj.window_locked):
                self.optimus.speak("cheif , House  windows are unlocked")
            message = self.securityObj.status()
            self.status_label.config(text=message)


class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.title("Login")
        self.photox = PhotoImage(file="backgr.png")
        Label(image=self.photox).pack()
        self.photo_icon = PhotoImage(
            file="C:\\Users\\yadav\\Documents\\project\\group.png")
        self.iconphoto(True, self.photo_icon)
        self.UserId = StringVar(self)
        self.Password = StringVar(self)

        self.login_frame = Frame(self, borderwidth=7, relief=SUNKEN, padx=281, bg="grey5").place(
            x=430, y=300, width=600, height=300)
        button = Button(self.login_frame, command=lambda: self.destroy(), text="🔙 Exit", font=(
            "times new roman", 12, "bold"), bg="grey5", fg="white smoke").place(x=430, y=300, width=100)
        user_id = Label(self.login_frame, text="Enter user ID:", background="grey5", fg="white smoke", font=(
            "ariel", 14, "bold"), pady=20).place(x=540, y=308, width=380)
        user_id_entry = Entry(self.login_frame, width=25, font=(
            "ariel", 12, "bold"), textvariable=self.UserId).place(x=490, y=360, width=500)
        user_password = Label(self.login_frame, text="Password:", background="grey5",
                              fg="white smoke", pady=10, font=("ariel", 14, "bold")).place(x=440, y=400, width=580)
        # TODO:Shwoing star in entry field
        entery1 = Entry(self.login_frame, show="*", width=25,
                        textvariable=self.Password, font=("ariel", 12, "bold"))
        entery1.place(x=490, y=445, width=500)

        # TODO==================Activating of Button==== yaha pe ek ek charcater check ho raha hai recursively=============

        def check_button(*args):  # used variable length of arguments
            if (len(self.Password.get()) > 2) and (len(self.UserId.get()) > 0):
                submit_button.config(state=NORMAL)
            else:
                submit_button.config(state=DISABLED)
        self.UserId.trace('w', check_button)
        self.Password.trace('w', check_button)

        def lib():
            obj1 = OptimusPrime()
            name = self.UserId.get().lower()
            if name == "aman" or name == "ankita" or name == "anish" or name == "anurag" and self.Password.get() == "123":
                tmsg.showinfo("Sucess", f"Welcome 😊\n{self.UserId.get()}")
                self.destroy()
                obj = HouseGUI()
                obj1.wishMe()
                obj.mainloop()
            else:
                obj1.speak("Wrong User , ID or ,Password")
                obj1.speak("What are you doing nowadays")
                query = obj1.takeCommand()
                if ('nothing' in query or 'coding' in query):
                    obj1.speak("Welcome , cheif")
                    tmsg.showinfo("Sucess", f"Welcome 😊\n{self.UserId.get()}")
                    self.destroy()
                    obj = HouseGUI()
                    obj1.wishMe()
                    obj.mainloop()

        def Hide_password():
            if entery1.cget('show') == '*':
                entery1.config(show='')
            else:
                entery1.config(show='*')
        check = Checkbutton(self.login_frame, bg="grey5", fg="blue", text="Show Password", font=(
            "times new roman", 12, "bold"), pady=5, command=Hide_password)
        check.place(x=850, y=470)
        submit_button = Button(self.login_frame, text="Submit", bg="blue", state=DISABLED,
                               fg="white", padx=20, pady=5, font=("times new roman", 12, "bold"), command=lib)
        submit_button.place(x=680, y=500)


print("AI is activating Security System \n\n\tPlease Wait ", end="")
for i in range(4):
    print(".", end="")
    time.sleep(0.4)
obj = OptimusPrime()
obj.speak(
    "Welcome Everyone ! presenting smart House security system , powered by , Atrificial intelligence ")
obj = Login()
obj.mainloop()
    # answer=obj.takeCommand()
    # answer=answer.lower()
    # print(answer)
    # if('who' in answer):
    #   obj.speak("Mister , Aman Roy , is my cheif")
    # elif ('nind' in answer):
    #   obj.speak("Okay cheif ! you can sleep ! i will handle it")
    # elif(answer=="nothing"):
    #   x=HouseGUI()
    #   OptimusPrime().wishMe()
    #   x.mainloop()
    # else:
    #   obj.speak("sorry cheif ! wrong code")
