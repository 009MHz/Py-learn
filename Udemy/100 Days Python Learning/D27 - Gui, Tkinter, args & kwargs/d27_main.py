from tkinter import *

# Main Window
gui = Tk()
gui.title("GUI Proto")
gui.minsize(width=480, height=640)

"GUI Control"

# GUI Click Button
def hit_btn():
    print("Hit Button Clicked")
    print(f"Textbox Value: \"{textbox.get()}\"")

# GUI Textbox
def textbox_interact(event):
    if textbox.get() == "Type your text":
        textbox.delete(0, END)
    elif textbox.get() == "":
        textbox.insert(0, "Type your text")

# GUI Multiline Text
def multi_text_interact(event):
    default_text = "Insert your text here."
    if multi_text.get("1.0", "1.end") == default_text:
        multi_text.delete("1.0", END)
    elif multi_text.get("1.0", "1.end") == "":
        multi_text.insert("1.0", default_text)

# GUI Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())

# GUI Scale button
def scale_used(value):  # Called with current scale value.
    print(value)

# GUI Check Button
def checkbutton_used():
    if checked_state.get() == 1:
        print("check_state: True")
    else:
        print("check_state: False")

# GUI Radio button
def radio_used():
    print(f'radio_state = "Option{radio_state.get()}"')


# GUI Listboxes
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


# GUI Components
"GUI label"
lab = Label(text="GUI Label Proto")
lab.config(text="Header Proto")
lab.pack()

"GUI Click Button"
# Calling the button function
button = Button(text="Click Me", command=hit_btn)
button.flash()
button.pack()

"GUI Textbox"
# Creating the textbox widget
textbox = Entry(width=25)
textbox.insert(END, string="Type your text")

# Bind the <Focus> event to call the interact function
textbox.bind("<FocusIn>", textbox_interact)
textbox.bind("<FocusOut>", textbox_interact)
textbox.pack()

"GUI Multiline Text"
# Displaying the Multi-Text Widget
multi_text = Text(height=5, width=20)
default_text = "Insert your text here."
multi_text.insert(END, default_text)

# bind the <FocusIn> event to clear the default text
multi_text.bind("<FocusIn>", multi_text_interact)
multi_text.bind("<FocusOut>", multi_text_interact)

# focus on the widget and pack it
multi_text.focus()
multi_text.pack()

"GUI Spinbox"
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

"GUI Scale button"
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

"GUI Check Button"
checked_state = IntVar()  # variable to store checked state, 0 is off, 1 is on.
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

"GUI Radio button"
radio_state = IntVar()  # Variable to store which radio button value is checked.
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

"GUI Listboxes"
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

"""GUI Appearance"""
gui.mainloop()
