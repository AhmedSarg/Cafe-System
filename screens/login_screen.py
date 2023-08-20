from tkinter import *
import sys

sys.path.insert(0, "values")
from colors import *
from fonts import *
from customtkinter import *
from PIL import ImageTk, Image

root = Tk()
root.resizable(False, False)
root.title("Login")
root.state("zoomed")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.configure(bg=darkBlue)
loginframe = Frame(width=screenWidth - 420, height=screenHeight - 98, background=beige)
loginframe.place(x=500, y=18)
label_title = Label(
    loginframe,
    text="Cafe System",
    fg=black,
    bg=beige,
    cursor="heart",
    font=(lucida, 70),
)
label_title.place(x=250, y=180)
cup = Image.open("icons\cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(130, 130))
logo = CTkLabel(loginframe, image=icon, text="")
logo.place(x=500, y=320)
titleLabel = Label(root, font=(lucida, 40), text="System Login", bg=darkBlue, fg=beige)
titleLabel.place(x=35, y=40)
searchLabel = CTkLabel(
    root,
    text="Username",
    font=(lucida, 20),
)
searchLabel.place(x=45, y=175)

username = CTkEntry(
    root,
    width=400,
    height=35,
    corner_radius=10,
    border_width=0,
    fg_color=white,
    text_color=black,
    font=(normal, 16),
    placeholder_text="Username",
    placeholder_text_color=grey,
)
username.place(x=45, y=210)
searchLabel = CTkLabel(
    root,
    text="Password",
    font=(lucida, 20),
)
searchLabel.place(x=45, y=300)
password = CTkEntry(
    root,
    width=400,
    height=35,
    corner_radius=10,
    border_width=0,
    fg_color=white,
    text_color=black,
    font=(normal, 16),
    placeholder_text="Password",
    placeholder_text_color=grey,
)
password.place(x=45, y=335)
btn_login = CTkButton(
    root,
    width=180,
    height=40,
    text="Login",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(normal, 17),
    corner_radius=16,
)
btn_login.place(x=135, y=500)
root.mainloop()
