import tkinter as tk
# from tkinter import *
# from main import *

# from distutils import core
import dearpygui.dearpygui as dpg


sample = "Kofi is a boy"

def print_function(text):
    # print(dpg.get_value(text))    
    return text
    
dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

with dpg.window(label="Example Window", width=600, height=300):
    # dpg.add_text("Hello, world")
    # dpg.add_button(label="Save")
    # dpg.add_text(print_function(sample))
    # dpg.add_combo(print_function(sample))
    
    dpg.add_text(print_function(sample))
    
    # dpg.add_input_text(label="Output", callback=sample)
    # dpg.add_input_text(label="string", default_value="Quick brown fox", multiline=True,)
    # dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
    

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()



# def main_screen():
#     global screen
#     screen = tk.Tk()
#     screen.title("name_assistant")
#     screen.geometry("700x550")
#     screen.iconbitmap('.\app_icon.ico')

#     name_label = tk.Label(text="name_assistant", width=300, bg="black", fg="white", font=("Calibri", 13))
#     name_label.pack()

#     # microphone_photo = PhotoImage(file="assistant_logo.png")
#     # microphone_button = Button(image=microphone_photo, command=Process_audio)
#     # microphone_button.pack(pady=10)

#     # info_button = Button(text="Info", command=info)
#     # info_button.pack(pady=10)

#     screen.mainloop()



# root= tk.Tk()

# root.title("Next")
# root.geometry("600x300")

# label = tk.Label(root, text=print_function(sample), width=600, height=300)

# label.pack

# root.mainloop




