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

cup = Image.open("TeamTest\icons\cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(80, 80))
logo = CTkLabel(root, image=icon, bg_color=transparent, text="")
logo.place(x=screenWidth-100, y=20)

mainFrame = CTkFrame(
    root,
    fg_color=darkBlue,
    bg_color=transparent,
    width=800,
    height=300,
    corner_radius=20,
)

searchFrame = CTkFrame(
    mainFrame,
    fg_color=transparent,
    bg_color=transparent,
    width=670,
    height=70,
)

searchLabel = CTkLabel(
    searchFrame,
    text="Name",
    font=(lucida, 24),
)
searchLabel.grid(row=0, column=0, padx=(0, 0), pady=(0, 10))

searchEntry = CTkEntry(
    searchFrame,
    width=670,
    height=35,
    corner_radius=10,
    border_width=0,
    fg_color=white,
    text_color=black,
    font=(normal, 16),
    placeholder_text="Name",
    placeholder_text_color=grey,
)
searchEntry.grid(row=1, column=0, columnspan=4, padx=100)

searchFrame.grid(rowspan=1, columnspan=6, pady=(40, 0))

buttonAdd = CTkButton(
    mainFrame,
    width=170,
    height=40,
    text="Add Client",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 17),
    corner_radius=16,
)
buttonAdd.grid(row=2, column=1, pady=40)

buttonSearch = CTkButton(
    mainFrame,
    width=170,
    height=40,
    text="Search",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 17),
    corner_radius=16,
)
buttonSearch.grid(row=2, column=4, pady=40)

mainFrame.place(anchor="center", relx=0.5, rely=0.5)

root.mainloop()
