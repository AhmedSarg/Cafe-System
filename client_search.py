from tkinter import *
from values.colors import *
from values.fonts import *
from tkinter import ttk
from customtkinter import *


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
    font=(lucida, 30),
    text="Client Search",
    bg=beige,
)
titleLabel.grid(padx=50, pady=30)

mainFrame = CTkFrame(
    root,
    fg_color=darkBlue,
    bg_color=transparent,
    width=800,
    height=300,
    corner_radius=20,
)



searchEntry = CTkEntry(
    mainFrame,
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
searchEntry.grid(row=0, column=0, rowspan=1, columnspan=6, pady=(30, 0), padx=100)
buttonAdd = CTkButton(
    mainFrame,
    width=170,
    height=40,
    text="Add Client",
    hover=True,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 17),
    corner_radius=10
)
buttonAdd.grid(row=2, column=1, pady=40)

buttonSearch = CTkButton(
    mainFrame,
    width=170,
    height=40,
    text="Search",
    hover=False,
    text_color=black,
    fg_color=white,
    font=(lucida, 17),
    corner_radius=16,
)
buttonSearch.grid(row=2, column=4, pady=40)

mainFrame.place(anchor="center", relx=0.5, rely=0.5)

root.mainloop()
