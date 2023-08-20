from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from customtkinter import *
import sys
sys.path.insert(0, 'values')
from fonts import *
from colors import *
from PIL import ImageTk, Image
import time
import os


##Splash Screen...

splash =Tk()
splash.title("Splash screen!")
splash.geometry("840x500+340+140")
splash.resizable(False, False)
splash.config(background="#ffeedb")
lbl = Label(splash, text='Cafe System',font=(lucida, 40), fg=black,bg=beige)
lbl.place(x=245,y=150)

cup = Image.open("icons/cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(80, 80))
logo = CTkLabel(splash, image=icon, bg_color=transparent, text="")
logo.place(x=388, y=250)


#hide the title bar..
splash.overrideredirect(True)

def login_screen():
    splash.destroy()
    root = Tk()
    root.title("Login")
splash.after(3000,login_screen)
mainloop()
