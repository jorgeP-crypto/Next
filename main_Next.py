###############################################################################
# IMPORTING REQUIRED API's #
###############################################################################

import random
import subprocess
import wolframalpha
import pyttsx3
from gtts import gTTS
import googletrans
from googletrans import Translator
from tkinter import *
import json
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
from twilio.rest import Client
from ecapture import ecapture as ec
from urllib.request import urlopen
import randfacts
from newsapi import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys
from os import environ
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import pyautogui





###############################################################################
# SETTING UP GOOGLE VOICE ENGINE
###############################################################################

# creating an engine to take voice input and convert it to text
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


###############################################################################
# name of the project
###############################################################################
name_assistant = "Next"


###############################################################################
# VOICE INPUT FUNCTION #
###############################################################################

# this function processes all audio commands
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.energy_threshold = 10000  # this increasing the hearing threshold to allow the smallest sound to be heard
        r.adjust_for_ambient_noise(source, 1.2)  # this reducing background noise
        r.pause_threshold = 2  # time taken to receive input
        audio = r.listen(source)
        print("Listening...")
        # gui('Listening')

    try:
        print("Recognizing...")
        # gui("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
        # gui(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        # gui("Unable to Recognize your voice.")
        return "None"

    return query



###############################################################################
# GREETINGS #
###############################################################################

# Greetings function
def greeting(name_assistant):
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
        # gui.gui("Good morning")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")
        # gui.gui("Good afternoon")

    else:
        speak("Good evening")
        # gui.gui("Good evening")

    speak("Please, how may I help you?")
    print("Please, how may I help you?")

    print("listening...")



###############################################################################
# DATE FUNCTION #
###############################################################################

# this is the date function
def date():
    now = datetime.datetime.now()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    ordinal_names = ['1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    speak("Today is " + month_names[month_name - 1] + " " + ordinal_names[day_name - 1] + '.')
    print("Today is " + month_names[month_name - 1] + " " + ordinal_names[day_name - 1] + '.')
    # gui.gui("Today is " + month_names[month_name - 1] + " " + ordinal_names[day_name - 1] + '.')


###############################################################################
# EMAIL FUNCTION
###############################################################################

# this function is used is to send email function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('gantwiagyei58@gmail.com', 'rogue@A656')
    server.sendmail('gantwiagyei58@gmail.com', to, content)
    server.close()



###############################################################################
#                # WEATHER REPORT FUNCTION #                                          #
###############################################################################

def weather(city):
    # city = "Kumasi"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    print(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")
    speak(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")
    # gui.gui(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")


###############################################################################
#                # TRANSLATOR FUNCTION #                                          #
###############################################################################

def translategl(text):
    speak("SURE SIR")
    # print(googletrans.LANGUAGES)
    translator = Translator()
    speak("In which language should I translate to?")
    lang = input("To_Lang :- ")   
    text_to_translate = translator.translate(text,src = "auto",dest= lang,)
    translated_text = text_to_translate.text
    try : 
        # speakgl = gTTS(text=text, lang=b, slow= False)
        # speakgl.save("voice.mp3")
        # playsound("voice.mp3")
        speak(translated_text)
        
        time.sleep(5)
        # os.remove("voice.mp3")
    except:
        print("Unable to translate")
        speak(" Unable to translate")



###############################################################################
#                # ALARM FUNCTION #                                          #
###############################################################################

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")




###############################################################################
#                # CALCULATOR FUNCTION #                                          #
###############################################################################
def WolfRamAlpha(query):
    apikey = "XV3L68-YK29VUH7V9"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("Next","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")








###############################################################################
#                # DRIVER FUNCTION #                                          #
###############################################################################

# this is the main driver function

def Process_audio():
    if __name__ == '__main__':
        
            # This Function will clean any command before execution of this python file
            # clear = lambda: os.system('cls')

            # clear()
        global name_assistant
        greeting(name_assistant)
        while True:

            # app_string = ["open word", "open powerpoint", "open excel", "open Photoshop", "open notepad", "open Access"]
            # app_link = [r'Microsoft Office Word 2007.lnk', r'Microsoft Office PowerPoint 2007.lnk',
                            # r'Microsoft Office Excel 2007.lnk', r'\Zoom.lnk', r'Notepad.lnk', r'Google Chrome.lnk']
            # app_desktop = r'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs'

                # All the commands said by user will be stored here in 'query' and will be converted to lower case for
                # easily recognition of command
            query = takeCommand().lower()

                ###############################################################################
                # GREETING MESSAGES #
                ###############################################################################
            #print(name_assistant)
            if ("Good" and "Morning") in query or ("Good" and "Afternoon") in query or ("Good" and "evening") in query:
                # gui.gui(f"A warm {query}")
                speak("A warm" + query)
                speak("How are you?")
                speak(name_assistant)

            elif "hello" in query: 
                # in query or name_assistant 
                # greeting(name_assistant)
                speak("Next at your service.")

            elif "How are you" in query:
                speak("Hello sir, how are you ?")
                if "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")


            elif "who i am" in query:
                speak("If you talk then definitely you're a human.")

            elif "why are you in the world" in query or "why are you here" in query:
                speak("I was created by George.")

            elif 'who are you' in query or 'what can you do' in query:
                speak('I am ' + name_assistant + 'your personal assistant. I am programmed to minor tasks like opening '
                        'youtube, google chrome, gmail and search wikipedia etcetra')

            elif 'reason for you' in query:
                speak("I was created as a mini project by George.")

                # this changes the name of the personal assistant to a customised one
            elif "change my name_assistant to" in query:
                query = query.replace("change my name_assistant to", "")
                name_assistant = query

            elif "change name" in query or 'change your name' in query or 'change assistants name' in query:
                speak("What would you like to call me")
                name_assistant = takeCommand()
                speak("Thanks for naming me")

            elif "what's your name" in query or "What is your name" in query:
                speak("My friends call me")
                speak(name_assistant)
                print("My friends call me", name_assistant)
                # gui.gui("My friends call me", name_assistant)

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by George.")
                # gui.gui("I have been created by George.")



                ###############################################################################
                # OPENING WEBSITES OF INTEREST #
                ###############################################################################

                # this opens YouTube
            # elif 'open' and 'youtube' in query:
            #     speak("Here you go to Youtube\n")
            #     webbrowser.open("https://www.youtube.com")

            #     # this opens Google
            # elif 'open' and 'google' in query:
            #     speak("Here you go to Google\n")
            #     webbrowser.open("https://www.google.com")

            # elif 'open gmail' in query:
            #     webbrowser.open_new_tab("https://www.mail.google.com")
            #     speak("Google Mail open now")
            #     time.sleep(5)

            # elif 'open netflix' in query:
            #     webbrowser.open_new_tab("https://www.netflix.com/browse")
            #     speak("Netflix open now")

            # elif 'open stackoverflow' in query:
            #     speak("Here you go to Stack Over flow.Happy coding")
            #     webbrowser.open("https://www.stackoverflow.com")



                ###############################################################################
                # WIKIPEDIA SEARCH #
                ###############################################################################

                # This searches a word and opens wikipedia.
            # elif 'search ' and 'wikipedia' in query:
            #     try:
            #         speak("What word should I search?")
            #         word = takeCommand()
            #             # query = query.replace("wikipedia", "")
            #         speak('Searching Wikipedia...')
            #         results = wikipedia.summary(word, sentences=3)
            #         speak("According to Wikipedia")
            #         print(results)
            #         # gui.gui(results)
            #         speak(results)
            #     except:
            #         speak("Sorry, couldn't find the word")

            # elif "open wikipedia" in query:
            #     speak("Opening Wikipedia.")
            #     # gui.gui("Opening Wikipedia.")
            #     webbrowser.open("wikipedia.com")

            elif "google" in query:
                from SearchWord import searchGoogle
                searchGoogle(query)
                
                
            elif "youtube" in query:
                from SearchWord import searchYoutube
                searchYoutube(query)
            
            
            elif "wikipedia" in query:
                from SearchWord import searchWikipedia
                searchWikipedia(query)



                ###############################################################################
                # OPENING WEBSITES OF INTEREST #
                ###############################################################################

                # this opens YouTube
            elif 'open' and 'youtube' in query:
                speak("Here you go to Youtube\n")
                webbrowser.open("https://www.youtube.com")

                # this opens Google
            elif 'open' and 'google' in query:
                speak("Here you go to Google\n")
                webbrowser.open("https://www.google.com")

            elif 'open gmail' in query:
                webbrowser.open_new_tab("https://www.mail.google.com")
                speak("Google Mail open now")
                time.sleep(5)

            elif 'open netflix' in query:
                webbrowser.open_new_tab("https://www.netflix.com/browse")
                speak("Netflix open now")

            elif 'open stackoverflow' in query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("https://www.stackoverflow.com")




                ###############################################################################
                # TIME AND DATE FUNCTION #
                ###############################################################################

                # this tells the time
            elif ('what is' and 'the time') in query or 'the time' in query:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {str_time}")

                # this tells the date
            elif 'date' in query or "what is today's date" in query or "today's date" in query:
                date()




                ###############################################################################
                # OPENING APPS #
                ###############################################################################





            elif 'open firefox' in query:
                app_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
                os.startfile(app_path)

            # elif app_string[0] in query:
            elif "Open" and "word" in query:
                # os.startfile(app_desktop + app_link[0])
                app_path = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                os.startfile(app_path)

                speak("Microsoft office Word is opening now")

            # elif app_string[1] in query:
            elif "Open" and "powerpoint" in query:
                # os.startfile(app_desktop + app_link[1])
                app_path = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
                os.startfile(app_path)
                speak("Microsoft office PowerPoint is opening now")

            # elif app_string[2] in query:
            elif "Open" and "excel" in query:
                # os.startfile(app_desktop + app_link[2])
                app_path = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
                os.startfile(app_path)
                speak("Microsoft office Excel is opening now")

            # elif app_string[3] in query:
            elif "Open" and "photoshop" in query:
                app_path = r"C:\Program Files\\Adobe\\Adobe Photoshop CC 2019\Photoshop.exe"
                os.startfile(app_path)
                speak("Photoshop is opening now")

            # elif app_string[4] in query:
            elif "Open" and "notepad" in query:
                app_path = r"%windir%\system32\notepad.exe"
                os.startfile(app_path)
                speak("Notepad is opening now")
                
            
            # elif app_string[5] in query:
            elif "Open" and "access" in query:
                app_path = r"C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE"
                os.startfile(app_path)
                speak("Microsoft Access is opening now")
                
            elif "open" and "dictionary" in query:
                app_path = r"C:\Program Files (x86)\WordWeb\wweb32.exe"
                os.startfile(app_path)
                speak("Dictionary is opening now")



            elif "open" in query:   #EASY METHOD
                query = query.replace("open","")
                query = query.replace("Next","")
                pyautogui.press("super")
                pyautogui.typewrite(query)
                pyautogui.sleep(2)
                pyautogui.press("enter") 


                ###############################################################################
                # SENDING MAIL #
                ###############################################################################

                # this sends a mail to any recipient with an email address
            elif 'send a mail' in query:
                try:
                    speak("to whom should I send")
                    # gui.gui("to whom should I send ")
                    to = input()
                    speak("What should I say?")
                    # gui.gui("What should I say?")
                    content = takeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent !")
                    # gui.gui("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
                    # gui.gui("I am not able to send this email")




                ###############################################################################
                # PERFORMING MATHEMATICAL CALCULATIONS #
                ###############################################################################

                # this is used for mathematical calculations
            elif "calculate" in query:
                
                query = query.replace("calculate","")
                query = query.replace("Next","")
                Calc(query)
                
                # app_id = "XV3L68-YK29VUH7V9"
                # client = wolframalpha.Client(app_id)
                # indx = query.lower().split().index('calculate')
                # query = query.split()[indx + 1:]
                # res = client.query(' '.join(query))
                # answer = next(res.results).text
                # print("The answer is " + answer)
                # # gui.gui("The answer is " + answer)
                # speak("The answer is " + answer)


                ###############################################################################
                # TRIVIA #
                ###############################################################################

            elif 'search' in query or 'play' in query:
                query = query.replace("search", "")
                query = query.replace("play", "")
                webbrowser.open(query)

                # this tells any random fact when asked
            elif 'fact' in query or 'facts' in query:
                fact = randfacts.get_fact()
                print("Did you know that, " + fact)
                # gui.gui("Did you know that, " + fact)
                speak("Did you know that, " + fact)

                # this tells random jokes
            elif 'joke' in query:
                joke_now = pyjokes.get_fact()
                speak(joke_now)
                # gui.gui(joke_now)




                ###############################################################################
                # READING NEWS #
                ###############################################################################

                # this reads news headlines from the Times of India
            elif 'news' in query:
                try:
                    json_obj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey
                            =\\a86773864b3349258e2d86fea732018b\\''')
                    data = json.load(json_obj)
                    i = 1

                    speak('here are some top news from the times of india')
                    print('''=============== TIMES OF INDIA ============''' + '\n')
                    # gui.gui('''=============== TIMES OF INDIA ============''' + '\n')

                    for item in data['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        # gui.gui(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        # gui.gui(item['description'] + '\n')
                        speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                except Exception as e:

                    print(str(e))





                ###############################################################################
                # PERFORMING OS FUNCTIONS #
                ###############################################################################

                # changes the background of your windows
            elif 'change background' in query:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
                speak("Background changed successfully")

                # this locks the window of your device
            elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

                # this shuts down your machine
            elif "shutdown the system" in query:
                speak("Are You sure you want to shutdown?")
                # shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                shutdown = takeCommand()
                if shutdown == "yes":
                    os.system("shutdown /s /t 1")

                elif shutdown == "no":
                    # break
                    pass

                # this restarts your device
            elif "restart" in query:
                subprocess.call(["shutdown", "/r"])

                # this puts your device to sleep
            elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                subprocess.call("shutdown / h")

                # this signs you out of your current device
            elif "log off" in query or "sign out" in query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

                # this empties recycle bin
            elif 'empty recycle bin' in query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")

                # this puts your personal assistant to sleep
            elif "don't listen" in query or "stop listening" in query or "sleep" in query:
                speak("for how much time you want to stop Next from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)
                # gui.gui(a)




                ###############################################################################
                # SET ALARM #
                ###############################################################################
                
                
                
            elif "set an alarm" in query:
                speak("What time please? Example: 10 and 10 and 10")
                print("input time example:- 10 and 10 and 10")
                # speak("Set the time")
                # a = input("Please tell the time :- ")
                a = takeCommand()
                alarm(a)
                speak("Alarm set")




                ###############################################################################
                # LOCATION SEARCH #
                ###############################################################################

                # this searches for the location of a place
            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                # gui.gui("WHich plcae do you want to locate?")
                speak("Which plcae do you want to locate?")
                speak(location)
                webbrowser.open("https://www.google.nl/maps/place/" + location + "")





                ###############################################################################
                # TAKES PICTURE #
                ###############################################################################
                # takes a picture
            elif "camera" in query or "take a photo" in query:
                # gui.gui("Opening camera")
                speak("Opening camera")
                image = ec.capture(0, "Camera ", "img.jpg")
                ec.show(image)





                ###############################################################################
                # WRITING NOTE USING NOTEPAD #
                ###############################################################################

                # this writes a note in notepad
            elif "write a note" in query:
                # gui.gui("What should i write, please")
                speak("What should i write, please")
                note = takeCommand()
                file = open('next.txt', 'w')
                # gui.gui("Please, Should i include date and time")
                speak("Please, Should i include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    str_time = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(str_time)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif "show note" in query:
                speak("Showing Notes")
                file = open("note.txt", "r")
                print(file.read())
                # gui.gui(file.read())
                speak(file.read(6))




                ###############################################################################
                # WEATHER REPORT #
                ###############################################################################

                # Gives a report on the weather using the Openweathermap api
            elif "weather" in query:
                print("Which city do you want to know it's weather?")
                # gui.gui("Which city do you want to know it's weather?")
                speak("Which city do you want to know it's weather?")
                city_name = takeCommand()
                # gui.gui(city_name)
                weather(city_name)
            

            # elif "send message " in query:
            #         # You need to create an account on Twilio to use this service
            #     account_sid = 'Account Sid key'
            #     auth_token = 'Auth token'
            #     client = Client(account_sid, auth_token)

            #     message = client.messages.create(body=takeCommand(), from_='Sender No', to='Receiver No')
            #     print(message.sid)
            #     gui.gui(message.sid)

                # these are some of the most asked question from Google Assistant
            elif "will you be my gf" in query or "will you be my bf" in query:
                # gui.gui("I'm not sure about, may be you should give me some time")
                speak("I'm not sure about, may be you should give me some time")

            elif "how are you" in query:
                # gui.gui("I'm fine")
                speak("I'm fine")

            elif "i love you" in query:
                # gui.gui("It's hard to understand")
                speak("It's hard to understand")

                # Answers questions based on "what is"
            elif "what is" in query or "who is" in query:
                client = wolframalpha.Client("XV3L68-YK29VUH7V9")
                res = client.query(query)

                try:
                    print(next(res.results).text)
                    # gui.gui(next(res.results).text)
                    speak(next(res.results).text)
                
                except StopIteration:
                    print("I can't find what you're asking for.")
                    # gui.gui("I can't find what you're asking for.")
                    speak("I can't find what you're asking for.")

            elif "translate" in query:
                
                query = query.replace("Next","")
                query = query.replace("translate","")
                translategl(query)



                # this exits the application
            elif 'exit' in query or 'bye-bye' in query or 'bye' in query:
                # gui.gui("Thanks for giving me your time")
                speak("Thanks for giving me your time")
                
                exit()
                
                
                
########################################################################################
#               GUI                 #
########################################################################################


class MainThread(QThread):
    
    def __init__(self):
        super(MainThread, self).__init__()
        

    def run(self):
        Process_audio()



startExe = MainThread()



class Ui_Next(object):

    def setupUi(self, Next):
        Next.setObjectName("Next")
        Next.resize(730, 485)
        self.centralwidget = QtWidgets.QWidget(Next)
        self.centralwidget.setObjectName("centralwidget")
        self.bg1 = QtWidgets.QLabel(self.centralwidget)
        self.bg1.setGeometry(QtCore.QRect(-190, -170, 1171, 811))
        # self.bg1.setText("")
        self.bg1.setPixmap(QtGui.QPixmap("C:/Users/Fibre/projectNext/Next/pic/Black_Template.jpg"))
        self.bg1.setObjectName("bg1")

        # create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -60, 601, 451))
        self.label.setMinimumSize(QtCore.QSize(600, 600))
        self.label.setMaximumSize(QtCore.QSize(600, 600))
        self.label.setObjectName("label")
        
        Next.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Next)
        self.statusbar.setObjectName("statusbar")
        Next.setStatusBar(self.statusbar)

        # add label to main window
        Next.setCentralWidget(self.centralwidget)

        # set qmovie as label
        self.movie = QMovie("C:/Users/Fibre/projectNext/Next/pic/Aqua.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        
        
        startExe.start()


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

suppress_qt_warnings()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_Next()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

# Process_audio()


