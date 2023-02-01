import tkinter

# main window
window = tkinter.Tk()

# GUI size
window.minsize(width=480, height=640)

# GUI Title
window.title("Tkinter GUI")

# GUI label
win_lab = tkinter.Label(text="Tkinter GUI Label", font=("Century Gothic", 24, "bold"))
win_lab.pack()

# Gui Label Update
win_lab["text"] = "Updated The previous label"
#win_lab.config(text=win_lab["text"])

# Click BUtton
clk_btn = tkinter.Button

# keep the windows open
window.mainloop()
