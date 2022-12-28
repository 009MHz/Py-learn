import tkinter

"""Creating the GUI screen"""
screen = tkinter.Tk()

"""Providing window Content"""
# GUI window title
screen.title("Tkinter GUI title")

# GUI window size
screen.minsize(width = 480, height = 500)

# adding window label
win_lab = tkinter.Label(text="Tkinter GUI Label", font=("Lato", 24,"bold"))  # define the content
win_lab.pack()  # showing the label code (at the top center inside the windows = default)

"""Make the screen always visible"""
screen.mainloop()