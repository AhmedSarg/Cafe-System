from tkinter import *
from values.colors import *
from values.fonts import *
from customtkinter import *
from PIL import ImageTk, Image
root=Tk()
root.resizable(True,True)
root.title("Select")
root.state("zoomed")
root.resizable(False, False)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

root.configure(bg=beige)

cup = Image.open("icons\cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(80, 80))
logo = CTkLabel(
    root,
      image=icon,
        bg_color=transparent,
          text=""
          )
logo.place(x=screenWidth-100, y=20)


title = Label(
    root,
    text='Reciept',
    fg=black,
    bg=beige,
      cursor='heart',
      font=(lucida,40)
      )
title.place(x=15,y=20)

price = Label(
    root,
    text='Reciept :',
    fg=black,
    bg=beige,
      cursor='heart',
      font=(lucida,22)
      )
price.place(x=screenWidth-1000,y=35)

number_top = Label(
    root,
    text='160.5',
    fg=black,
    bg=beige,
      cursor='heart',
      font=(lucida,22)
      )
number_top.place(x=screenWidth-500,y=35)
root.mainloop()