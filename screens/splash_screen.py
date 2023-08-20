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

root =Tk()
root.title("Splash screen!")
root.geometry("840x500+340+140")
root.resizable(False, False)
root.config(background=beige)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

cup = Image.open("icons/cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(80, 80))
logo = CTkLabel(root, image=icon, bg_color=transparent, text="",)
logo.place(x=388, y=250)

lbl = Label(root, text='Cafe System',font=(lucida, 40), fg=black,bg=beige,)
lbl.place(x=245,y=150)

root.overrideredirect(True)

def login_screen():
    root.destroy()
    rootLogin = Tk()
    rootLogin.title("Login")
root.after(3000,login_screen)
mainloop()
