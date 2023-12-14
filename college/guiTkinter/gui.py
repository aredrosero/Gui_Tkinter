import tkinter as tk 
from tkinter import font as font
import os
from PIL import ImageTk
from tkinter import simpledialog
import sqlite3
from numpy import random

# Colors
bg_color = "#3D59AB"
fg_color = "#CAFF70"

script_directory = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(script_directory, "credit family", "credit river.otf")

# Create a new window
window = tk.Tk()
window.title("B&B Caffe")
window.eval("tk::PlaceWindow . center")

myFont = font.Font(family="abadiFamily")

# create a frame widgets
frame1 = tk.Frame(window, width=500, height=600, bg=bg_color)
frame2 = tk.Frame(window, bg=bg_color)
frame3 = tk.Frame(window, bg=bg_color)
frame4 = tk.Frame(window, bg=bg_color)
# place frame widgets in window
#for frame in (frame1, frame2):
#  frame.grid(row=0, column=0, sticky="nesw")

# Configure the rows and columns of the window to expand with the window size
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_frame1():
    clear_widgets(frame2)
    frame1.grid(row=0, column=0, sticky="nesw")
    frame1.pack_propagate(False)  # Prevent frame1 from shrinking
    frame1.tkraise()  # Raise frame1 to the top

    # Button en Frame 1
    tk.Button(
        frame1,
        text="Guest access",
        font=myFont,
        bg="#3D59AB",
        fg="white",
        cursor="hand2",
        activebackground="#b0c4de",
        activeforeground="black",
        command=load_frame2
    ).pack(pady=9)

    tk.Button(
        frame1,
        text="Login/Register",
        font=myFont,
        bg="#3D59AB",
        fg="white",
        cursor="hand2",
        activebackground="#b0c4de",
        activeforeground="black"
    ).pack(pady=9)

def load_frame2():
    clear_widgets(frame1)
    clear_widgets(frame3)
    clear_widgets(frame4)
    frame2.grid(row=0, column=0, sticky="nesw")
    frame2.pack_propagate(False)  # Prevent frame2 from shrinking
    frame2.tkraise()  # Raise frame2 to the top

    # Button en Frame 2
    tk.Button(
        frame2,
        text="Food",
        font=myFont,
        bg="#3D59AB",
        fg="white",
        cursor="hand2",
        activebackground="#b0c4de",
        activeforeground="black"
    ).pack(pady=9)

    tk.Button(
        frame2,
        text="Drink",
        font=myFont,
        bg="#3D59AB",
        fg="white",
        cursor="hand2",
        activebackground="#b0c4de",
        activeforeground="black"
    ).pack(pady=9)
    
    tk.Button(
        frame2,
        text="Book a Table",
        font=myFont,
        bg="#3D59AB",
        fg="white",
        cursor="hand2",
        activebackground="#b0c4de",
        activeforeground="black",
        command=booking
    ).pack(pady=9)

    tk.Button(
        frame2,
        text="Lesson Booking",
        font=myFont,
        bg="#3D59AB",
        fg="white",
        cursor="hand2",
        activebackground="#b0c4de",
        activeforeground="black",
        command=lesson
    ).pack(pady=9)

    tk.Button(
        frame2,
        text="Back",
        font=myFont,
        bg="#3D59AB",
        fg="white",
        cursor="hand2",
        activebackground="#b0c4de",
        activeforeground="black",
        command=load_frame1
    ).pack(pady=9)
    
    


def create_input_box(frame, label_text, input_type='entry', options=None):
    # Create a label for the input box
    label = tk.Label(frame, text=label_text, font=myFont, bg="#3D59AB", fg="white")
    label.pack(pady=(5, 0))  # Add some vertical padding

    if input_type == 'entry':
        # Create the input box
        input_box = tk.Entry(frame, font=myFont, bg="#3D59AB", fg="white", cursor="hand2")
        input_box.pack(pady=(0, 10))  # Add some vertical padding
    elif input_type == 'option_menu':
        # Create the option menu
        input_box = tk.StringVar(frame)
        input_box.set(options[0])  # Set the default option
        tk.OptionMenu(frame, input_box, *options).pack(pady=(0, 10))

    return input_box

    
def booking():
    clear_widgets(frame2)
    frame3.grid(row=0, column=0, sticky="nesw")
    frame3.pack_propagate(False)  # Prevent frame2 from shrinking
    frame3.tkraise()  # Raise frame2 to the top
    # Create a frame for the input boxes
    #input_frame = tk.Frame(frame3)
    #input_frame.pack(pady=10)
    locations = ["Harrogate", "Leeds", "Knaresborough Castle"]
    # Create input boxes
    name_input = create_input_box(frame3, "Name:").pack(pady=10)
    people_input = create_input_box(frame3, "People (Qty):").pack(pady=10)
    tlphNumber_input = create_input_box(frame3, "T. Number +44 ").pack(pady=10)
    time_input = create_input_box(frame3, "Morning-Noon-Afternoon").pack(pady=10)
    location_input = create_input_box(frame3, "Location", input_type='option_menu', options=locations)
    # Add more input boxes as needed
    
    
    tk.Button(
        frame3,
        text="Submit Booking",
        font=myFont,
        bg="#3D59AB",
        fg="white",
        cursor="hand2",
        activebackground="#b0c4de",
        activeforeground="black"
        #command=submit_form
    ).pack(pady=30)
    
    tk.Button(
        frame3,
        text="Back",
        font=myFont,
        bg="#3D59AB",
        fg="white",
        cursor="hand2",
        activebackground="#b0c4de",
        activeforeground="black",
        command=load_frame2
    ).pack(pady=40)
    
def lesson():
    clear_widgets(frame2)
    frame4.grid(row=0, column=0, sticky="nesw")
    frame4.pack_propagate(False)  # Prevent frame2 from shrinking
    frame4.tkraise()  # Raise frame2 to the top
    # Create a frame for the input boxes
    #input_frame = tk.Frame(frame3)
    #input_frame.pack(pady=10)
    locations = ["Harrogate", "Leeds", "Knaresborough Castle"]
    # Create input boxes
    name_input = create_input_box(frame4, "Name:").pack(pady=10)
    tlphNumber_input = create_input_box(frame4, "T. Number +44 ").pack(pady=10)
    time_input = create_input_box(frame4, "Morning-Noon-Afternoon").pack(pady=10)
    location_input = create_input_box(frame4, "Location", input_type='option_menu', options=locations)
    # Add more input boxes as needed
    
    
    tk.Button(
        frame4,
        text="Submit Booking",
        font=myFont,
        bg="#3D59AB",
        fg="white",
        cursor="hand2",
        activebackground="#b0c4de",
        activeforeground="black"
        #command=submit_form
    ).pack(pady=30)
    
    tk.Button(
        frame4,
        text="Back",
        font=myFont,
        bg="#3D59AB",
        fg="white",
        cursor="hand2",
        activebackground="#b0c4de",
        activeforeground="black",
        command=load_frame2
    ).pack(pady=40)


# load the first frame
load_frame1()

window.mainloop()
