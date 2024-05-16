from tkinter import *
import time
import tkinter.messagebox

BACKGROUND_COLOR = "#003C43"
MAX_LINE_LENGTH = 35 


instructions = "Don't stop writing or your text will disappear!"
countdown_time = 10


def countdown():
    global timer_running, popup_shown
    time_elapse = int(check_elapsed_time())
    if time_elapse > 5:
        remaining_time = countdown_time - time_elapse
        if remaining_time >= 0:
            time_label.config(text=f"Time Left: {remaining_time:02d}")
        else:
            if not popup_shown:
                popup_shown = True
                prompt_save_or_delete()
            time_label.config(text="Time Left: 00")
            timer_running = False
            return
    else:
        time_label.config(text="Keep it up!")
    window.after(1000, countdown)


def on_key_release(event):
    """ Record the time when a key is released and starts the timer if it's not already running"""
    global last_key_release_time, timer_running, popup_shown
    last_key_release_time = time.time()
    if not timer_running:
        timer_running = True
        popup_shown = False
        countdown()


def on_key_press(event):
    global timer_running, countdown_time
    # Stop the timer when a key is pressed
    timer_running = False


def check_elapsed_time():
    global last_key_release_time
    # Calculate the elapsed time since the last key release
    elapsed_time = time.time() - last_key_release_time
    return elapsed_time


def prompt_save_or_delete():
    text = text_widget.get("1.0", "end-1c")
    text_widget.delete('1.0', END)
    if tkinter.messagebox.askyesno("Time's up!", "Do you want to save your text?"):
        save_text(text)
    else:
        delete_text()


def save_text(text):
    with open("test.txt", "w") as text_file:
        text_file.write(text)


def delete_text():
    with open("test.txt", "w") as text_file:
        text_file.write("")

# Create the main window
window = Tk()
window.title("Mik's Disappearing Text")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create a Text widget
text_widget = Text(window, height=10, width=40,
                   wrap='word', font=("Georgia", 25),
                   bg=BACKGROUND_COLOR, bd=0, fg="#FFF2D7", insertbackground="#FFF2D7")
text_widget.grid(column=0, row=3, rowspan=4, sticky="nsew")
# Bind the text widget to the event for key release
text_widget.bind("<KeyRelease>", on_key_release)
text_widget.bind("<KeyPress>", on_key_press)



# Labels
header_label = Label(text="Disappearing Text",
                     font=("Georgia", 30, "bold"), fg="white",
                     bg=BACKGROUND_COLOR)
header_label.grid(column=0, row=1, pady=5)

instructions_label = Label(text=instructions, font=("Arial", 11),
                           wraplength=text_widget.winfo_reqwidth(),
                           justify="center", fg="white", bg=BACKGROUND_COLOR)
instructions_label.grid(column=0, row=2, pady=5)

time_label = Label(text="Time Left: 06", font=("Arial", 12), fg="white",
                   bg=BACKGROUND_COLOR)
time_label.grid(column=0, row=7, pady=6)


window.mainloop()
