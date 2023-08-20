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
titleLabel.grid(padx=10, pady=20)

cup = Image.open("icons\cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(80, 80))
logo = CTkLabel(root, image=icon, bg_color=transparent, text="")
logo.place(x=screenWidth - 100, y=15)

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
    text="Ahmed Mamdouh ",
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



productFrame=CTkFrame(
    root,
    fg_color=transparent,
    bg_color=transparent,
    corner_radius=20,
    width=200,
    height=150
)

nameproductLabel = Label(
    productFrame,
    text="Name  ",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
nameproductLabel.grid(row=0, column=0 )

shownameproductLabel = Label(
    productFrame,
    text="coffe ",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
shownameproductLabel.grid(row=1, column= 0)

priceproductLabel = Label(
    productFrame,
    text="Price  ",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
priceproductLabel.grid(row=0, column=1)

showpriceproductLabel = Label(
    productFrame,
    text="25",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
showpriceproductLabel.grid(row=1, column= 1)

countproductLabel = Label(
    productFrame,
    text=" Count ",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
countproductLabel.grid(row=0, column=2)

showpriceproductLabel = Label(
    productFrame,
    text="2",
    font=(lucida, 20),
    fg=black,
    bg=beige,
)
showpriceproductLabel.grid(row=1, column= 2)

buttonnext = CTkButton(
    root,
    width=250,
    height=50,
    text="print",
    hover=True,
    hover_color=cafe,
    text_color=white,
    fg_color=darkBlue,
    bg_color=transparent,
    font=(lucida, 22),
    corner_radius=16,
)
buttonnext.place(x=500,y=600)

buttonnext = CTkButton(
    root,
    width=250,
    height=50,
    text="return",
    hover=True,
    hover_color=cafe,
    text_color=white,
    fg_color=darkBlue,
    bg_color=transparent,
    font=(lucida, 22),
    corner_radius=16,
)
buttonnext.place(x=800,y=600)





productFrame.place(x=600,y=350)

mainFrame.place(x=500,y=100)


root.mainloop()