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
textbox.insert(END, "Insert your text here.")
print(textbox.get())
textbox.pack()

# GUI Click Button
def hit_click():  # Click action
    textbox_value = f"Passed text: '{textbox.get()}'"
    if textbox.get() == "Insert your text here.":
        textbox_value = f"Button Clicked with empty value"
    else:
        textbox_value = f"Passed text: '{textbox.get()}'"
    win_lab.config(text=textbox_value, font=("Century Gothic", 12, "bold"))


clk_btn = Button(text="Click Me", command=hit_click)
clk_btn.pack()

# # GUI Multiline Text
# text = Text(height=5, width=30)
# text.focus()  # Puts cursor in textbox.
# text.insert(END, "Example of multi-line text entry.")
# print(text.get("1.0", END))  # Get current value in textbox at line 1, character 0
# text.pack()
#
# # GUI Spinbox
# def spinbox_used():
#     # gets the current value in spinbox.
#     print(spinbox.get())
#
#
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# # GUI Scale button
# def scale_used(value):  # Called with current scale value.
#     print(value)
#
#
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # GUI Check Button
# def checkbutton_used():
#     print(checked_state.get())  # Prints 1 if On button checked, otherwise 0.
#
#
# checked_state = IntVar()  # variable to store checked state, 0 is off, 1 is on.
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# # GUI Radio button
# def radio_used():
#     print(radio_state.get())
#
#
# radio_state = IntVar()  # Variable to store which radio button value is checked.
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# # GUI Listboxes
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()


"""GUI Appearance"""
window.mainloop()
