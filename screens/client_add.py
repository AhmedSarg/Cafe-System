from tkinter import *
import sys
from tkinter import messagebox

sys.path.insert(0, "values")
sys.path.insert(0, "classes")
sys.path.insert(0, "database")
from colors import *
from fonts import *
from client import *
from db_controller import *
from customtkinter import *
from PIL import ImageTk, Image


root = Tk()
connection = openConnection()
root.title("Client Add")
root.state("zoomed")
root.resizable(False, False)
root.config(background=beige)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

titleLabel = Label(
    root,
    font=(lucida, 40),
    text="Client Add",
    bg=beige,
)
titleLabel.place(x=10, y=30)

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
    corner_radius=10,
)

nameLabel = CTkLabel(
    nameFrame,
    text="Name",
    font=(lucida, 20),
)
nameLabel.grid(row=0, column=0)

nameEntry = CTkEntry(
    nameFrame,
    width=700,
    height=35,
    corner_radius=10,
    border_width=0,
    fg_color=white,
    text_color=black,
    font=(normal, 16),
    placeholder_text="Name",
    placeholder_text_color=grey,
)
nameEntry.grid(row=1, column=0, columnspan=80)

nameFrame.grid(row=0, column=0, padx=50, pady=20)

addressFrame = CTkFrame(
    mainFrame,
    fg_color=transparent,
    bg_color=transparent,
    width=700,
    height=70,
    corner_radius=10,
)

addressLabel = CTkLabel(
    addressFrame,
    text="Address",
    font=(lucida, 20),
)
addressLabel.grid(row=0, column=0)

addressEntry = CTkEntry(
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
addressEntry.grid(row=1, column=0, columnspan=80)

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

def nextClick():
    name = nameEntry.get()
    address = addressEntry.get()
    phone = phoneEntry.get()
    if name.isspace() or len(name) == 0:
        messagebox.showerror("Failed","Name field is empty")
    elif address.isspace() or len(address) == 0:
        messagebox.showerror("Failed","Address field is empty")
    elif phone.isspace() or not phone.isdigit() or len(phone) == 0:
        messagebox.showerror("Failed","Phone Number is not valid")
    else:
        try:
            addClient(connection, Client(name=name.lower(), address=address.lower(), phone=phone))
            messagebox.showinfo("Success","Client added to database successfully")
        except:
            messagebox.showerror("Failed","Can't add client to database")

buttonNext = CTkButton(
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
    command=nextClick
)
buttonNext.grid(row=0, column=6)


buttonsFrame.grid(row=3, column=0, padx=50, pady=(20, 40))

mainFrame.place(anchor="center", relx=0.5, rely=0.5)

root.mainloop()
endConnection(connection=connection)
