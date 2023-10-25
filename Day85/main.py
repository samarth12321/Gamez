# This is in progress

from tkinter import *
import sys
from tkinter import filedialog
from tkinter import font, colorchooser
from tkinter.font import Font
from PIL import Image, ImageDraw, ImageFont, ImageTk


# Tktinter
window = Tk()
window.title("Mik's Watermark")
window.config(padx=20, pady=20)


# Ask the user to select a file
file_path = filedialog.askopenfilename()
image = Image.open(file_path)

#Canvas
canvas = Canvas(width=800, height=500, highlightthickness=0)
watermark_holder = PhotoImage(file="Watermarkme.png")
image_to_watermark = canvas.create_image(400, 250, image=watermark_holder)  #image=photo_img
watermark_text = canvas.create_text(325, 225, text="", fill="") #adds watermark
canvas.grid(row=0, column=0, columnspan=3, sticky="nsew")


def add_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        max_size = (350, 350)  
        image.thumbnail(max_size) 
        photo_img = ImageTk.PhotoImage(image)
        canvas.itemconfig(image_to_watermark, image=photo_img)
        add_image.photo_img = photo_img


def add_watermark(event):
    if selected_color is not None:  # Check if a color has been selected
        watermark = input.get()
        selected_font_family = clicked.get()
        selected_font_size = 25
        # selected_font_color = selected_color or "black"
        x, y = event.x, event.y  # Get the coordinates of the click  ADDED
        font_specs = Font(family=selected_font_family, size=selected_font_size)
        canvas.itemconfig(watermark_text, text=watermark, fill=selected_color,  font=font_specs)
        canvas.coords(watermark_text, x, y)  # Update the position of the text element  # ADDED
#     print("I got clicked")
    else:
        print("Please choose a color first.")

# Get the available font families
font_families = font.families()
print(type(font_families))
all_fonts = []
for family in font_families:
    all_fonts.append(family)
print(all_fonts)

# Datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set(all_fonts[11])

selected_color = None

# COLORS
def choose_color():
    global selected_color
    color = colorchooser.askcolor()  # This will open a color selection dialog
    if color:
        selected_color = color[1]
        print("Selected color:", selected_color)
       


#Label
label1 = Label(text="Select Image", font=("Arial", 12))
label1.grid(column=0, row=1)
label1.config(padx=5, pady=5)

#Entry
input = Entry(width=30)
input.grid(column=1, row=1)

#Button
button1 = Button(text="Select Image", command=add_image)
button1.grid(column=1, row=1)

button2 = Button(text="Click me", command=add_watermark)
button2.grid(column=2, row=2)

button3 = Button(text="Download Image", command=add_watermark)
button3.grid(column=2, row=3)


window.mainloop()