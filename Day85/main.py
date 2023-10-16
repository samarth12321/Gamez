# This is in progress

from tkinter import *
import sys
from PIL import Image, ImageDraw, ImageFont

# Tktinter
window = tkinter.Tk()
window.title("Mik's Watermark")
window.minsize(width=800, height=500)
window.config(padx=20, pady=20)


#Canvas
canvas = Canvas(width=650, height=450, highlightthickness=0)
burger_img = PhotoImage(file="hamburger.png")
canvas.create_image(325, 225, image=burger_img)
watermark_text = canvas.create_text(325, 225, text="", fill="white", font=("Arial", 35)) #adds watermark
canvas.grid(column=0, row=0, columnspan=2)


def add_watermark():
    watermark = input.get()
    canvas.itemconfig(watermark_text, text=watermark)


#Label
my_label = Label(text="Add name", font=("Arial", 14))
my_label.grid(column=0, row=1)

#Entry
input = Entry(width=30)
input.grid(column=1, row=1)


window.mainloop()