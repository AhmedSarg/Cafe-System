from tkinter import *
import sys

sys.path.insert(0, "values")
from colors import *
from fonts import *
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
logo.place(x=screenWidth - 100, y=20)

mainFrame = CTkFrame(
    root,
    fg_color=darkBlue,
    bg_color=transparent,
    corner_radius=20,
)

toolsFrame = CTkFrame(
    mainFrame,
    fg_color=transparent,
    bg_color=transparent,
    width=700,
    height=200,
)

searchFrame = CTkFrame(
    toolsFrame,
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
searchLabel.grid(row=0, column=0, padx=(50, 0), pady=(0, 10))

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

searchFrame.grid(row=0, column=0, rowspan=1, columnspan=8, pady=(40, 0))

buttonAdd = CTkButton(
    toolsFrame,
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
    toolsFrame,
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

toolsFrame.grid(row=0, column=0, padx=20)

detailsframe = CTkFrame(
    mainFrame,
    fg_color=darkBlue,
    bg_color=transparent,
    corner_radius=20,
)

idLabel = CTkLabel(
    detailsframe,
    text="Id",
    font=(lucida, 20),
    width=40,
)
idLabel.grid(row=0, column=1, pady=(20, 0))

nameLabel = CTkLabel(
    detailsframe,
    text="Name",
    font=(lucida, 20),
    width=240,
)
nameLabel.grid(row=0, column=2, pady=(20, 0))

addressLabel = CTkLabel(
    detailsframe,
    text="Address",
    font=(lucida, 20),
    width=340,
)
addressLabel.grid(row=0, column=3, pady=(20, 0))

buttonTempLabel = CTkLabel(
    detailsframe,
    text="",
    font=(lucida, 20),
    fg_color=transparent,
    bg_color=transparent,
    width=80,
)
buttonTempLabel.grid(row=0, column=4, pady=(20, 0))

# showIdLabel = CTkLabel(
#     detailsframe,
#     text="1",
#     font=(normal, 20),
#     text_color=white,
# )
# showIdLabel.grid(row=1, column=1)

# showNameLabel = CTkLabel(
#     detailsframe,
#     text="Ahmed Essam Eliwa",
#     font=(normal, 16),
#     text_color=white,
# )
# showNameLabel.grid(row=1, column=2)

# showaddressLabel = CTkLabel(
#     detailsframe,
#     text="EQalyoubia - Shoubra - Basos - B7b7",
#     font=(normal, 16),
#     text_color=white,
# )
# showaddressLabel.grid(row=1, column=3)

# buttonSelect = CTkButton(
#     detailsframe,
#     width=60,
#     height=30,
#     text="Select",
#     hover=True,
#     hover_color=cafe,
#     text_color=black,
#     fg_color=white,
#     bg_color=transparent,
#     font=(lucida, 16),
#     corner_radius=10,
# )
# buttonSelect.grid(row=1, column=4, padx=20)

detailsframe.grid(row=1, column=0, padx=(20, 0), pady=(0, 40))

mainFrame.place(anchor="center", relx=0.5, rely=0.5)

root.mainloop()
