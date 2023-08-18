from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import time
import os


def login_screen():
    
    splash.destroy()
    
    root = Tk()
    root.title("Login")
    root.resizable(True,True)
    root.config(background="#ffeedb")
    label = Label(root, text = "Login Screen Test")
    label.pack()
    root.state("zoomed")
    root.mainloop()

splash = Tk()
splash.title("Splash screen!")
label = Label(splash, text = "Splash Screen Test")
label.pack()
screen = Tk()
screenWidth = screen.winfo_screenwidth()
screenHeight = screen.winfo_screenheight()
screen.destroy()

splash.resizable(False,False)
splash.config(background="#ffeedb")
splash.state("zoomed")
splash.after(1000,login_screen)
mainloop()