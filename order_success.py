from tkinter import *
from values.colors import *
from values.fonts import *
from customtkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Success')
root.state("zoomed")
root.resizable(False, False)
root.config(background=beige)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

titleFrame = Frame(root, bg=beige)
titleFrame.grid()

frame=Frame(root,bg=beige)
cup = Image.open("icons\cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(80, 80))
logo = CTkLabel(root, image=icon, bg_color=transparent, text="")
logo.place(x=screenWidth-100, y=20)

successLabel =Label(
    frame,
    text="Order Success",
    font=(lucida,60 ),
    bg=beige
)
successLabel.grid(row=0,column=0,pady=30)

cup = Image.open("icons\checkmark.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(150,150))
logo = CTkLabel(frame, image=icon, bg_color=transparent, text="")
logo.grid(row=1,column=0)

frame.place(anchor="center", relx=0.5, rely=0.5)

root.mainloop()