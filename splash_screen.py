from tkinter import *
from values.colors import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import time
import os


def login_screen():
    
    root.title("Login")
    splashLabel.destroy()
    label = Label(root, text = "Login Screen Test")
    label.pack()

root = Tk()
root.title("Splash Screen")
root.state("zoomed")
root.resizable(False,False)
root.config(background=beige)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

splashLabel = Label(root, text = "Splash Screen Test")
splashLabel.pack()

root.after(1000,login_screen)
root.mainloop()
