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

# Entry
user_entry = Entry(width=30)
user_entry.grid(column=0, row=6, pady=10, ipadx=90, ipady=10)

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

def highlight_words(self):
    word_to_highlight = user_entry.get()
    text_content = self.text_area.get("1.0", END)  #change

def compare_word():
    user_input = user_entry.get().strip().lower()  # Get user input and convert to lowercase for case-insensitive comparison

    if words_to_type and user_input == words_to_type[0]:
        text_area.tag_config("matched", foreground="green")
       
        matched = words_to_type.pop(0) 
        matched_words.append(matched)


    else:
        text_area.tag_config("non_matched", foreground="red")
        non_matched = words_to_type.pop(0)  # Remove the matched word from the list
        non_matched_words.append(non_matched)




window.mainloop()