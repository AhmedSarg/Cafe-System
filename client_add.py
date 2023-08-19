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
    text="Client add",
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
    width=770,
    height=450,
    corner_radius=20,
)



fnameLabel = CTkLabel(
    mainFrame,
    text="first Name",
    font=(lucida, 20),
)

fnameLabel.place(x=30,y=50)

fnameEntry = CTkEntry(
    mainFrame,
    width=300,
    height=35,
    corner_radius=10,
    border_width=0,
    fg_color=white,
    text_color=black,
    font=(normal, 16),
    placeholder_text="First Name",
    placeholder_text_color=grey,
)
fnameEntry.place(x=25,y=90)

lnameLabel = CTkLabel(
    mainFrame,
    text="last Name",
    font=(lucida, 20),
)

lnameLabel.place(x=430,y=50)

lnameEntry = CTkEntry(
    mainFrame,
    width=300,
    height=35,
    corner_radius=10,
    border_width=0,
    fg_color=white,
    text_color=black,
    font=(normal, 16),
    placeholder_text="Last Name",
    placeholder_text_color=grey,
)
lnameEntry.place(x=430,y=90)

AddressLabel = CTkLabel(
    mainFrame,
    text="Address",
    font=(lucida, 20),
)

AddressLabel.place(x=30,y=150)

AddressEntry= CTkEntry(
    mainFrame,
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

AddressEntry.place(x=25,y=185)


phoneLabel = CTkLabel(
    mainFrame,
    text="phone number",
    font=(lucida, 20),
)

phoneLabel.place(x=30,y=240)

phoneEntry= CTkEntry(
    mainFrame,
    width=700,
    height=35,
    corner_radius=10,
    border_width=0,
    fg_color=white,
    text_color=black,
    font=(normal, 16),
    placeholder_text="+20",
    placeholder_text_color=grey,
)

phoneEntry.place(x=25,y=275)


buttonback = CTkButton(
    mainFrame,
    width=170,
    height=40,
    text="Back",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 17),
    corner_radius=16,
)
buttonback.place(x=70,y=360)

buttonnext = CTkButton(
    mainFrame,
    width=170,
    height=40,
    text="Next",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 17),
    corner_radius=16,
)
buttonnext.place(x=470,y=360)

mainFrame.place(anchor="center", relx=0.5, rely=0.5)


root.mainloop()