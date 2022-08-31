from tkinter import *
from main import *

def main_screen():
    global screen
    screen = Tk()
    screen.title(name_assistant)
    screen.geometry("700x550")
    screen.iconbitmap('.\app_icon.ico')

    name_label = Label(text=name_assistant, width=300, bg="black", fg="white", font=("Calibri", 13))
    name_label.pack()

    microphone_photo = PhotoImage(file="assistant_logo.png")
    microphone_button = Button(image=microphone_photo, command=Process_audio)
    microphone_button.pack(pady=10)

    info_button = Button(text="Info", command=info)
    info_button.pack(pady=10)

    screen.mainloop()
