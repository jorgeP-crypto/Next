###############################################################################
# IMPORTING REQUIRED API's #
###############################################################################
import random
import subprocess
import tkinter

import wolframalpha
import pyttsx3
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
# import shutil
from twilio.rest import Client
from ecapture import ecapture as ec
from urllib.request import urlopen
import randfacts

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
        r.pause_threshold = 1  # time taken to receive input
        audio = r.listen(source)
        print("Listening...")

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


###############################################################################
# GREETINGS #
###############################################################################

# Greetings function
def greeting():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good evening")

    speak("My name is {}, your personal assistant.".format(name_assistant))
    print(f"My name is {name_assistant}, your personal assistant.")
    speak("Please, how may I help you?")
    print("Please, how may i help you?")
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

# CALLING THE GREETING FUNCTION
greeting()


###############################################################################
#                # DRIVER FUNCTION #                                          #
###############################################################################

# this is the main driver function
def Process_audio():
    if __name__ == '__main__':

        # This Function will clean any command before execution of this python file
        # clear = lambda: os.system('cls')

        # clear()
        # greeting()

        while True:

            app_string = ["open word", "open powerpoint", "open excel", "open zoom", "open notepad"]
            app_link = [r'\Microsoft Office Word 2007.lnk', r'\Microsoft Office PowerPoint 2007.lnk',
                        r'\Microsoft Office Excel 2007.lnk', r'\Zoom.lnk', r'\Notepad.lnk', r'\Google Chrome.lnk']
            app_desktop = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'

            # All the commands said by user will be stored here in 'query' and will be converted to lower case for
            # easily recognition of command
            query = takeCommand().lower()

            ###############################################################################
            # GREETING MESSAGES #
            ###############################################################################

            if "Good Morning" in query:
                speak("A warm" + query)
                speak("How are you Mister")
                speak(name_assistant)

            elif "hello" or name_assistant in query:
                greeting()

            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in query or "good" in query:
                speak("It's good to know that your fine")

            elif "who i am" in query:
                speak("If you talk then definitely you're a human.")

            elif "why you came to world" in query:
                speak("I was created by George.")

            elif 'who are you' in query or 'what can you do' in query:
                speak('I am ' + name_assistant + 'your personal assistant. I am programmed to minor tasks like opening '
                        'youtube, google chrome, gmail and search wikipedia etcetra')

            elif 'reason for you' in query:
                speak("I was created as a mini project by George.")

            # this changes the name of the personal assistant to a customisoed one
            elif "change my name_assistant to" in query:
                query = query.replace("change my name_assistant to", "")
                name_assistant = query

            elif "change name" or 'change your name' or 'change assistants name' in query:
                speak("What would you like to call me, Sir ")
                name_assistant = takeCommand()
                speak("Thanks for naming me")

            elif "what's your name" in query or "What is your name" in query:
                speak("My friends call me")
                speak(name_assistant)
                print("My friends call me", name_assistant)

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by George.")



            ###############################################################################
            # WIKIPEDIA SEARCH #
            ###############################################################################

            # This searches a word and opens wikipedia.
            elif 'search ' and 'wikipedia' in query:
                try:
                    speak("What word should I search?")
                    word = takeCommand()
                    # query = query.replace("wikipedia", "")
                    speak('Searching Wikipedia...')
                    results = wikipedia.summary(word, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except:
                    speak("Sorry, couldn't find the word")

            elif "open wikipedia" in query:
                webbrowser.open("wikipedia.com")



            ###############################################################################
            # OPENING WEBSITES OF INTEREST #
            ###############################################################################

            # this opens YouTube
            elif 'open youtube' in query:
                speak("Here you go to Youtube\n")
                webbrowser.open("youtube.com")

            # this opens Google
            elif 'open google' in query:
                speak("Here you go to Google\n")
                webbrowser.open("google.com")

            elif 'open gmail' in query:
                webbrowser.open_new_tab("mail.google.com")
                speak("Google Mail open now")
                time.sleep(5)

            elif 'open netflix' in query:
                webbrowser.open_new_tab("netflix.com/browse")
                speak("Netflix open now")

            elif 'open stackoverflow' in query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")

            ###############################################################################
            # TIME AND DATE FUNCTION #
            ###############################################################################

            # this tells the time
            elif ('what is' and 'the time') in query or 'the time' in query:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {str_time}")

            # this tells the date
            elif 'date' in query or "what is today's date" in query or "today's date" in query:
                date()

            ###############################################################################
            # OPENING APPS #
            ###############################################################################

            elif 'open firefox' in query:
                app_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
                os.startfile(app_path)

            if app_string[0] in query:
                os.startfile(app_desktop + app_link[0])

                speak("Microsoft office Word is opening now")

            if app_string[1] in query:
                os.startfile(app_desktop + app_link[1])
                speak("Microsoft office PowerPoint is opening now")

            if app_string[2] in query:
                os.startfile(app_desktop + app_link[2])
                speak("Microsoft office Excel is opening now")

            if app_string[3] in query:
                os.startfile(app_desktop + app_link[3])
                speak("Zoom is opening now")

            if app_string[4] in query:
                os.startfile(app_desktop + app_link[4])
                speak("Notepad is opening now")

            ###############################################################################
            # SENDING MAIL #
            ###############################################################################

            # this sends a mail to any recipient with an email address
            elif 'send a mail' in query:
                try:
                    speak("to whom should i send")
                    to = input()
                    speak("What should I say?")
                    content = takeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            ###############################################################################
            # PERFORMING MATHEMATICAL CALCULATIONS #
            ###############################################################################

            # this is used for mathematical calculations
            elif "calculate" in query:
                app_id = "XV3L68-YK29VUH7V9"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            elif 'search' in query or 'play' in query:
                query = query.replace("search", "")
                query = query.replace("play", "")
                webbrowser.open(query)

            # this tells any random fact when asked
            elif 'fact' or 'facts' in query:
                fact = randfacts.get_fact()
                print(fact)
                speak("Did you know that, " + fact)

            # this tells random jokes
            elif 'joke' in query:
                speak(pyjokes.get_joke())

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

                    for item in data['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
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
            elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

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

            ###############################################################################
            # LOCATION SEARCH #
            ###############################################################################

            # this searches for the location of a place
            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl/maps/place/" + location + "")

            ###############################################################################
            # TAKES PICTURE #
            ###############################################################################
            # takes a picture
            elif "camera" in query or "take a photo" in query:
                image = ec.capture(0, "Camera ", "img.jpg")
                ec.show(image)

            ###############################################################################
            # WRITING NOTE USING NOTEPAD #
            ###############################################################################

            # this writes a note in notepad
            elif "write a note" in query:
                speak("What should i write, please")
                note = takeCommand()
                file = open('next.txt', 'w')
                speak("Sir, Should i include date and time")
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
                speak(file.read(6))

            ###############################################################################
            # WEATHER REPORT #
            ###############################################################################

            # Gives a report on the weather using the Openweathermap api
            elif "weather" in query:

                # Google Open weather website to get API of Open weather
                api_key = "56c5f7d9be5e74534aa8a4aeb839f785"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                speak(" City name_assistant ")
                print("City name_assistant : ")
                city_name = takeCommand()
                complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                response = requests.get(complete_url)
                x = response.json()

                if x["code"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in kelvin unit) = " + str(
                        current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                        current_pressure) + "\n humidity (in percentage) = " + str(
                        current_humidiy) + "\n description = " + str(weather_description))

                else:
                    speak(" City Not Found ")

            elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)

                message = client.messages.create(body=takeCommand(), from_='Sender No', to='Receiver No')
                print(message.sid)

            # these are some of the most asked question from Google Assistant
            elif "will you be my gf" in query or "will you be my bf" in query:
                speak("I'm not sure about, may be you should give me some time")

            elif "how are you" in query:
                speak("I'm fine")

            elif "i love you" in query:
                speak("It's hard to understand")

            # Answers questions based on "what is"
            elif "what is" in query or "who is" in query:

                client = wolframalpha.Client("XV3L68-YK29VUH7V9")
                res = client.query(query)

                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No results")

            # this exits the application
            elif 'exit' in query:
                speak("Thanks for giving me your time")
                exit()


def info():
    info_screen = Toplevel(screen)
    info_screen.title("Info")
    info_screen.iconbitmap('app_icon.ico')

    creator_label = Label(info_screen, text="Created by George Antwi")
    creator_label.pack()

    age_label = Label(info_screen, text=" at the age of 12")
    age_label.pack()

    for_label = Label(info_screen, text="For Makers-pace")
    for_label.pack()


def main_screen():
    global screen
    screen = Tk()
    screen.title(name_assistant)
    screen.geometry("700x550")
    screen.iconbitmap('app_icon.ico')

    name_label = Label(text=name_assistant, width=300, bg="black", fg="white", font=("Calibri", 13))
    name_label.pack()

    microphone_photo = PhotoImage(file="assistant_logo.png")
    microphone_button = Button(image=microphone_photo, command=Process_audio)
    microphone_button.pack(pady=10)

    info_button = Button(text="Info", command=info)
    info_button.pack(pady=10)

    screen.mainloop()


main_screen()


