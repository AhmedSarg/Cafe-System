from tkinter import *
from values.colors import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from customtkinter import *
from values.colors import *
from values.fonts import *
from PIL import ImageTk, Image

root_menu =Tk()
root_menu.title('Menu')
width = root_menu.winfo_screenwidth()
height = root_menu.winfo_screenheight()
root_menu.geometry('%dx%d+0+0' %(width,height)) 
root_menu.resizable(False,False)
root_menu.state("zoomed")
root_menu.config(background=beige)

cup = Image.open("icons/cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(50, 50))
logo = CTkLabel(root_menu, image=icon, bg_color=transparent, text="")
logo.place(x=width-60, y=6)

category_Frame = CTkFrame(
    root_menu,
    fg_color=darkBlue,
    bg_color=transparent,
    width=300,
    height=height,
    corner_radius=20,
)
category_Frame.place(x=2, y=55)

titleLabel = Label(
    root_menu,
    font=(lucida, 20),
    text="Menu",
    bg=beige
)
titleLabel.grid(padx=10, pady=10)

cup = Image.open("icons/cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(50, 50))
logo = CTkLabel(root_menu, image=icon, bg_color=transparent, text="")
logo.place(x=width-60, y=6)

cat_button1 = CTkButton(
    category_Frame,
    width=170,
    height=70,
    text="HOT DRINKS",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 17),
    corner_radius=16,
)
cat_button1.grid(row=1, column=1, padx=20, pady=33)

cat_button2 = CTkButton(
    category_Frame,
    width=170,
    height=70,
    text="COLD DRINKS",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 17),
    corner_radius=16,
)
cat_button2.grid(row=2,column=1, pady=33)

cat_button3 = CTkButton(
    category_Frame,
    width=170,
    height=70,
    text="MAIN DISHES",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 17),
    corner_radius=16,
)
cat_button3.grid(row=3,column=1, pady=33)


cat_button4 = CTkButton(
    category_Frame,
    width=170,
    height=70,
    text="SNAKES",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 17),
    corner_radius=16,
)
cat_button4.grid(row=4,column=1, pady=33)


cat_button5 = CTkButton(
    category_Frame,
    width=170,
    height=70,
    text="EXTRAS",
    hover=True,
    hover_color=cafe,
    text_color=black,
    fg_color=white,
    bg_color=transparent,
    font=(lucida, 17),
    corner_radius=16,
)
cat_button5.grid(row=5,column=1, pady=35)
##########================================================================================############
##########================================================================================############
quantity_Frame = CTkFrame(
    root_menu,
    fg_color=darkBlue,
    bg_color=transparent,
    width=width - 2,
    height=80,
    corner_radius=20,
)
quantity_Frame.place(x=2, y=750)

lbl_drink = Label(
    quantity_Frame, 
    text='Drink : ',
    font=(lucida, 20),
    bg=darkBlue,
    fg=white,
)
lbl_drink.grid(row=1,column=1,padx=10,pady=22)


lbl_drinkName = Label(
    quantity_Frame, 
    text='Drink Name',
    font=(lucida, 20),
    bg=darkBlue,
    fg=white,
)
lbl_drinkName.grid(row=1,column=2,padx=10,pady=22)

lbl_quantity = Label(
    quantity_Frame, 
    text='Quantity : ',
    font=(lucida, 20),
    bg=darkBlue,
    fg=white,
)
lbl_quantity.grid(row=1,column=3,padx=50,pady=22)

minus = Image.open("icons/minus.png")
minus = minus.resize((80, 80))
icon = CTkImage(light_image=minus, size=(50, 50))
logo = CTkLabel(quantity_Frame, image=icon, bg_color=transparent, text="")
logo.grid(row=1,column=4)
mainloop()