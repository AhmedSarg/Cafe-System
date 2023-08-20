from tkinter import *
import sys
sys.path.insert(0, 'values')
from colors import *
from fonts import *
from customtkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.resizable(False, False)
root.title("Select")
root.state("zoomed")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

root.configure(bg=beige)

cup = Image.open("icons\cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(80, 80))
logo = CTkLabel(root, image=icon, bg_color=transparent, text="")
logo.place(x=screenWidth - 100, y=20)

titleFrame = Frame(root, bg=beige)
titleFrame.grid()

titleLabel = Label(
    titleFrame,
    font=(lucida, 40),
    text="Select Order Type",
    bg=beige,
)
titleLabel.grid(padx=10, pady=30)

buttonsFrame = CTkFrame(
    root, 
    bg_color=transparent,
    fg_color=transparent,
)
buttonCafe = CTkButton(
    buttonsFrame,
    width=500,
    height=250,
    fg_color=white,
    text_color=black,
    border_width=5,
    corner_radius=30,
    border_color=darkBlue,
    text="Cafe",
    font=(lucida, 48),
    hover_color=cafe,
)
buttonCafe.grid(row=0, column=0, padx=(0, 100))

buttonTakeAway = CTkButton(
    buttonsFrame,
    width=500,
    height=250,
    fg_color=white,
    text_color=black,
    border_width=5,
    corner_radius=30,
    border_color=darkBlue,
    text="Take Away",
    font=(lucida, 48),
    hover_color=cafe,
)
buttonTakeAway.grid(row=0, column=1, padx=(100, 50), pady=50)

buttonsFrame.place(anchor="center", relx=0.5, rely=0.5)

root.mainloop()
