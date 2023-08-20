from tkinter import *
import sys

sys.path.insert(0, "values")
from colors import *
from fonts import *
from customtkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Cash")
root.state("zoomed")
root.resizable(False, False)
root.config(background=beige)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

titleLabel = Label(
    root,
    font=(lucida, 40),
    text="Client Search",
    bg=beige,
)
titleLabel.place(x=10, y=30)

cup = Image.open("icons\cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(80, 80))
logo = CTkLabel(root, image=icon, bg_color=transparent, text="")
logo.place(x=screenWidth - 100, y=20)

price = Label(
    root, text="Reciept :", fg=black, bg=beige, cursor="heart", font=(lucida, 22)
)
price.place(x=screenWidth - 1000, y=35)

number_top = Label(
    root, text="160.5", fg=black, bg=beige, cursor="heart", font=(lucida, 22)
)
number_top.place(x=screenWidth - 500, y=35)
paid_text = Label(
    root, text="Paid", fg=black, bg=beige, cursor="heart", font=(lucida, 22)
)
paid_text.place(x=screenWidth - 1000, y=screenHeight - 650)

paid = CTkEntry(
    root,
    width=600,
    height=50,
    corner_radius=2,
    border_width=1,
    fg_color=white,
    text_color=black,
    border_color=black,
)
paid.place(x=screenWidth - 1000, y=screenHeight - 600)

discount_text = Label(
    root,
    text="Discount",
    fg=black,
    bg=beige,
    cursor="heart",
    font=(lucida, 22),
)
discount_text.place(x=screenWidth - 1000, y=screenHeight - 500)

discount = CTkEntry(
    root,
    width=600,
    height=50,
    corner_radius=2,
    border_width=1,
    fg_color=white,
    text_color=black,
    border_color=black,
)
discount.place(x=screenWidth - 1000, y=screenHeight - 450)
remaining = Label(
    root, text="Remaining :", fg=black, bg=beige, cursor="heart", font=(lucida, 22)
)
remaining.place(x=screenWidth - 1000, y=550)
number_buttom = Label(
    root, text="160.5", fg=black, bg=beige, cursor="heart", font=(lucida, 22)
)
number_buttom.place(x=screenWidth - 500, y=550)
btn_next = CTkButton(
    root,
    width=200,
    height=50,
    text="Next",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=white,
    font=(lucida, 17),
    corner_radius=16,
    border_width=2,
)
btn_next.place(x=750, y=700)
root.mainloop()
