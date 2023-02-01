from tkinter import *

# main window
window = Tk()
window.minsize(width=480, height=640)

"GUI Components"
# GUI Title
window.title("Tkinter GUI")

# GUI label
win_lab = Label(text="Tkinter GUI Label", font=("Century Gothic", 24, "bold"))
win_lab.pack()

# GUI Input field
textbox = Entry(width=40)
textbox.pack()

# GUI Click action
def hit_click():
    textbox_value = f"Passed text: '{textbox.get()}'"
    win_lab.config(text=textbox_value, font=("Century Gothic", 12, "bold"))


# GUI Click Button
clk_btn = Button(text="Click Me", command=hit_click)
clk_btn.pack()


"""GUI Appearance"""
window.mainloop()
