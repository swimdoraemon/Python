from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")


def msg():
    messagebox.askretrycancel("Alert", "stop! virus Found.")

button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

root.mainloop()