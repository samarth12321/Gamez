from tkinter import *
from tkinter import filedialog, font, colorchooser, messagebox
import pandas
import random

# Global Variables
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 125
BACKGROUND_COLOR = "#16425D"

# Tkinter
window = Tk()
window.title("Mik's Speed Typing Test")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#Canvas
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                highlightthickness=0, bg=BACKGROUND_COLOR)
# typewriter = PhotoImage(file="typewriter.png")
header_text = canvas.create_text(120, 90,
                                 text="Speed Typing Test", fill="#fff",
                                 font=("Georgia", 20, "bold"))
typwriter_background = canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/4,
                                           image=typewriter)
canvas.grid(row=0, column=0)



typed_words = []

def save_entry():
    text = user_entry.get()
    if text:
        typed_words.append(text)
        user_entry.delete(0, END) 

def on_space(event):
    save_entry()

# Bind the Enter key to the save_entry function
user_entry.bind('<space>', on_space)

window.mainloop()