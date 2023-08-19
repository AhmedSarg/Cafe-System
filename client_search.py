from tkinter import *
from values.colors import *
from tkinter import ttk
from customtkinter import *


root = Tk()
root.state("zoomed")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.resizable(False, False)
root.config(background="#FFEEDB")

frame = Frame(root, bg="#0d1f2d", border=100)
mainframe = Frame(root)
mainframe.grid()

titleFrame = Frame(mainframe, width=width, height=height, bg="#FFEEDB")
titleFrame.grid(row=0, column=0)

titleLabel = Label(
    titleFrame,
    font=("Lucida Handwriting", 30),
    text="Client Search",
    bg="#FFEEDB",
    border=10,
)
titleLabel.grid(row=0, column=0, padx=50, pady=30)

labelName = Label(frame, text="Name", bg="#0d1f2d", fg="#f6f4f6")
labelName.grid(row=0, column=0)
labelName.location

txtName = CTkEntry(
    frame,
    width=600,
    height=35,
    corner_radius=50,
    fg_color=white,
    text_color=black,
    font=("Lucida Handwriting", 14),
    placeholder_text="Name",
    placeholder_text_color="#AAAAAA",
)
txtName.grid(row=1, column=0, padx=10, pady=10)

buttonAdd = CTkButton(
    frame,
    height=40,
    text="Add Client",
    hover=False,
    text_color=black,
    fg_color=white,
    font=("Lucida Handwriting", 17),
    corner_radius=10
)
buttonAdd.place(x=120, y=70)

buttonSearch = CTkButton(
    frame,
    height=40,
    text="Search",
    hover=False,
    text_color=black,
    fg_color=white,
    font=("Lucida Handwriting", 17),
    corner_radius=16
)
buttonSearch.place(x=385, y=70)

frame.place(anchor="center", relx=0.5, rely=0.5)

root.mainloop()
