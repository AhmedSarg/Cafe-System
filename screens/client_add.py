from tkinter import *
import sys
sys.path.insert(0, "values")
from colors import *
from fonts import *
from customtkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Client Add")
root.state("zoomed")
root.resizable(False, False)
root.config(background=beige)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

titleFrame = Frame(root, bg=beige)
titleFrame.grid()

titleLabel = Label(
    titleFrame,
    font=(lucida, 40),
    text="Client add",
    bg=beige,
)
titleLabel.grid(padx=10, pady=30)

cup = Image.open("icons\cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(80, 80))
logo = CTkLabel(root, image=icon, bg_color=transparent, text="")
logo.place(x=screenWidth - 100, y=20)


mainFrame = CTkFrame(
    root,
    fg_color=darkBlue,
    bg_color=transparent,
    corner_radius=20,
)

nameFrame = CTkFrame(
    mainFrame,
    fg_color=transparent,
    bg_color=transparent,
    width=700,
    height=70,
    corner_radius=20,
)

fnameLabel = CTkLabel(
    nameFrame,
    text="First Name",
    font=(lucida, 20),
)
fnameLabel.grid(row=0, column=0, padx=(0, 30))

fnameEntry = CTkEntry(
    nameFrame,
    width=320,
    height=35,
    corner_radius=10,
    border_width=0,
    fg_color=white,
    text_color=black,
    font=(normal, 16),
    placeholder_text="First Name",
    placeholder_text_color=grey,
)
fnameEntry.grid(row=1, column=0, columnspan=40, padx=(0, 30))

lnameLabel = CTkLabel(
    nameFrame,
    text="Last Name",
    font=(lucida, 20),
)

lnameLabel.grid(row=0, column=40, padx=(30, 0))

lnameEntry = CTkEntry(
    nameFrame,
    width=320,
    height=35,
    corner_radius=10,
    border_width=0,
    fg_color=white,
    text_color=black,
    font=(normal, 16),
    placeholder_text="Last Name",
    placeholder_text_color=grey,
)
lnameEntry.grid(row=1, column=40, columnspan=40, padx=(30, 0))

nameFrame.grid(row=0, column=0, padx=50, pady=(40, 20))

addressFrame = CTkFrame(
    mainFrame,
    fg_color=transparent,
    bg_color=transparent,
    width=700,
    height=70,
    corner_radius=10,
)

AddressLabel = CTkLabel(
    addressFrame,
    text="Address",
    font=(lucida, 20),
)
AddressLabel.grid(row=0, column=0)

AddressEntry = CTkEntry(
    addressFrame,
    width=700,
    height=35,
    corner_radius=10,
    border_width=0,
    fg_color=white,
    text_color=black,
    font=(normal, 16),
    placeholder_text="Address",
    placeholder_text_color=grey,
)
AddressEntry.grid(row=1, column=0, columnspan=80)

addressFrame.grid(row=1, column=0, padx=50, pady=20)

phoneFrame = CTkFrame(
    mainFrame,
    fg_color=transparent,
    bg_color=transparent,
    width=700,
    height=70,
    corner_radius=10,
)

phoneLabel = CTkLabel(
    phoneFrame,
    text="Phone Number",
    font=(lucida, 20),
)
phoneLabel.grid(row=0, column=0)
# phoneLabel.place(x=30,y=240)

phoneEntry = CTkEntry(
    phoneFrame,
    width=700,
    height=35,
    corner_radius=10,
    border_width=0,
    fg_color=white,
    text_color=black,
    font=(normal, 16),
    placeholder_text="Phone Number",
    placeholder_text_color=grey,
)
phoneEntry.grid(row=1, column=0, columnspan=80)
# phoneEntry.place(x=25,y=275)

phoneFrame.grid(row=2, column=0, padx=50, pady=20)

buttonsFrame = CTkFrame(
    mainFrame,
    fg_color=transparent,
    bg_color=transparent,
    width=700,
    height=70,
    corner_radius=10,
)

tmp = CTkLabel(
    buttonsFrame,
    text="",
    width=700,
    height=0,
    bg_color=transparent,
    fg_color=transparent,
)
tmp.grid(row=0, column=0, columnspan=8)

buttonback = CTkButton(
    buttonsFrame,
    width=250,
    height=50,
    text="Back",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 22),
    corner_radius=16,
)
buttonback.grid(row=0, column=1)

buttonnext = CTkButton(
    buttonsFrame,
    width=250,
    height=50,
    text="Next",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 22),
    corner_radius=16,
)
buttonnext.grid(row=0, column=6)

buttonsFrame.grid(row=3, column=0, padx=50, pady=(20, 40))

mainFrame.place(anchor="center", relx=0.5, rely=0.5)


root.mainloop()
