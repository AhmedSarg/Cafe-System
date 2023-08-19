from tkinter import *
from values.colors import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import time
import os

##Splash Screen...

splash =Tk()
splash.title("Splash screen!")
splash.geometry("840x500+340+140")
splash.resizable(False,False)
splash.config(background="#ffeedb")




#hide the title bar..
splash.overrideredirect(True)

def login_screen():
    
    root.title("Login")
    root.geometry("840x470+340+140")
    root.resizable(False,False)
    root.config(background="#ffeedb")
    #Splash timer...
splash.after(1000,login_screen)
mainloop()