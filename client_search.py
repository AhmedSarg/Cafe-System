from tkinter import *
from values.colors import *
from values.fonts import *
from customtkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Client Search")
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
    text="Client Search",
    bg=beige,
)
titleLabel.grid(padx=10, pady=30)

cup = Image.open("icons\cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(80, 80))
logo = CTkLabel(root, image=icon, bg_color=transparent, text="")
logo.place(x=screenWidth-100, y=20)

mainFrame = CTkFrame(
    root,
    fg_color=darkBlue,
    bg_color=transparent,
    corner_radius=20,
)

detailsframe=CTkFrame(
    root,
    fg_color=darkBlue,
    bg_color=transparent,
    corner_radius=20,
)


searchFrame = CTkFrame(
    mainFrame,
    fg_color=transparent,
    bg_color=transparent,
    width=700,
    height=70,
)

searchLabel = CTkLabel(
    searchFrame,
    text="Phone Number",
    font=(lucida, 24),
)
searchLabel.grid(row=0, column=0,padx=(50, 0), pady=(0, 10))

searchEntry = CTkEntry(
    searchFrame,
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
searchEntry.grid(row=1, column=0, columnspan=80, padx=50)

searchFrame.grid(rowspan=1, columnspan=8, pady=(40, 0))

buttonAdd = CTkButton(
    mainFrame,
    width=250,
    height=50,
    text="Add Client",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 22),
    corner_radius=16,
)
buttonAdd.grid(row=2, column=2, pady=40)

buttonSearch = CTkButton(
    mainFrame,
    width=250,
    height=50,
    text="Search",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 22),
    corner_radius=16,
)
buttonSearch.grid(row=2, column=5, pady=40)



idLabel = CTkLabel(
    detailsframe,
    text="Id",
    font=(lucida, 20),
)
idLabel.grid()

nameLabel = CTkLabel(
    detailsframe,
    text="Name",
    font=(lucida, 20),
)
nameLabel.grid()

addressLabel = CTkLabel(
    detailsframe,
    text="Address",
    font=(lucida, 20),
)
addressLabel.grid()

buttonclose = CTkButton(
    detailsframe,
    width=75,
    height=50,
    text="close",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 22),
    corner_radius=16,
)
buttonclose.grid()

showIdLabel = CTkLabel(
    detailsframe,
    text=" ",
    font=(lucida, 20),
)
showIdLabel.grid()

shownameLabel = CTkLabel(
    detailsframe,
    text=" ",
    font=(lucida, 20),
)
shownameLabel.grid()

showaddressLabel = CTkLabel(
    detailsframe,
    text=" ",
    font=(lucida, 20),
)
showaddressLabel.grid()



detailsframe.place(anchor="center", relx=0.5, rely=0.5)


mainFrame.place(anchor="center", relx=0.5, rely=0.5)

root.mainloop()
