import Tkinter as tk
from Tkinter import *

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