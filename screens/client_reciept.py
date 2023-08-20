from tkinter import *
import sys
sys.path.insert(0, "values")
from colors import *
from fonts import *
from customtkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("client reciept")
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
    text="client reciept",
    bg=beige,
)
titleLabel.grid(padx=10, pady=30)

cup = Image.open("icons\cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(80, 80))
logo = CTkLabel(root, image=icon, bg_color=transparent, text="")
logo.place(x=screenWidth - 100, y=20)

mainFrame=CTkFrame(
    root,
    fg_color=transparent,
    bg_color=transparent,
    corner_radius=20,
    width=200,
    height=150
)

nameLabel = Label(
    mainFrame,
    text="Name : ",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
nameLabel.grid(row=0, column=0 )

shownameLabel = Label(
    mainFrame,
    text="Ahmed Mamdoh ",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
shownameLabel.grid(row=0, column=1 )

addressLabel = Label(
    mainFrame,
    text="address : ",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
addressLabel.grid(row=1, column=0 )

showaddressLabel = Label(
    mainFrame,
    text="banha ",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
showaddressLabel.grid(row=1, column=1 )

phoneLabel = Label(
    mainFrame,
    text="phone number : ",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
phoneLabel.grid(row=2, column=0 )

showphoneLabel =Label(
    mainFrame,
    text="01146872172 ",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
showphoneLabel.grid(row=2, column=1 )

priceLabel = Label(
    mainFrame,
    text="price : ",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
priceLabel.grid(row=3, column=0 )

showpriceLabel = Label(
    mainFrame,
    text="160.5 ",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
showpriceLabel.grid(row=3, column=1 )

paid = Label(
    mainFrame,
    text='Paid  : ',
    fg=black,
    bg=beige,
    font=(lucida, 20)
)
paid.grid(row=4,column=0)

showpaid = Label(
    mainFrame,
    text='200 ',
    fg=black,
    bg=beige,
    font=(lucida, 20)
)
showpaid.grid(row=4,column=1)





mainFrame.place(anchor="center", relx=0.5, rely=0.5)


root.mainloop()