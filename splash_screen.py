from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import time
import os

splash = Tk()
splash.title("Splash screen!")

screen = Tk()
screenWidth = screen.winfo_screenwidth()
screenHeight = screen.winfo_screenheight()
screen.destroy()

splash.resizable(False,False)
splash.config(background="#ffeedb")
splash.attributes('-fullscreen', True)
splash


def login_screen():
    
    splash.destroy()
    
    root=Tk()
    root.title("Login")
    # root.geometry(f"{screenWidth}x{screenHeight}")
    root.resizable(True,True)
    root.config(background="#ffeedb")
    root.attributes('-fullscreen', True)
    #Splash timer...
splash.after(1000,login_screen)
mainloop()