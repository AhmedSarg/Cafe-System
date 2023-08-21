import sys

sys.path.insert(0, "values")
from colors import *
from fonts import *
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from customtkinter import *


class MenuScreen:
    def __init__(self, selection):
        self.root = Tk()
        self.root.title("Menu")
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root.config(background=beige)
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        category_Frame = CTkFrame(
            self.root,
            fg_color=darkBlue,
            bg_color=transparent,
            width=300,
            height=height,
        )
        category_Frame.place(x=0, y=0)

        def button1():
            cat_button2.destroy()
            cat_button3.destroy()
            cat_button4.destroy()
            cat_button5.destroy()
            drink_button1 = CTkButton(
                drink_Frame,
                width=210,
                height=150,
                text="Drink Hot",
                hover=True,
                hover_color=darkBlue,
                text_color=white,
                fg_color=cafe,
                bg_color=transparent,
                font=(lucida, 25),
                corner_radius=25,
            )
            drink_button1.grid(row=1, column=3, padx=50, pady=33)

        cat_button1 = CTkButton(
            category_Frame,
            width=170,
            height=80,
            text="HOT DRINKS",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=button1,
        )
        cat_button1.grid(row=1, column=1, padx=20, pady=33)

        def button2():
            cat_button1.destroy()
            cat_button3.destroy()
            cat_button4.destroy()
            cat_button5.destroy()
            drink_button1 = CTkButton(
                drink_Frame,
                width=210,
                height=150,
                text="Drink cold",
                hover=True,
                hover_color=darkBlue,
                text_color=white,
                fg_color=cafe,
                bg_color=transparent,
                font=(lucida, 25),
                corner_radius=25,
            )
            drink_button1.grid(row=1, column=3, padx=50, pady=33)

        cat_button2 = CTkButton(
            category_Frame,
            width=170,
            height=80,
            text="COLD DRINKS",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=button2,
        )
        cat_button2.grid(row=2, column=1, pady=33)

        def button3():
            cat_button1.destroy
            cat_button2.destroy
            cat_button4.destroy
            cat_button5.destroy
            drink_button1 = CTkButton(
                drink_Frame,
                width=210,
                height=150,
                text="Drink main",
                hover=True,
                hover_color=darkBlue,
                text_color=white,
                fg_color=cafe,
                bg_color=transparent,
                font=(lucida, 25),
                corner_radius=25,
            )
            drink_button1.grid(row=1, column=3, padx=50, pady=33)

        cat_button3 = CTkButton(
            category_Frame,
            width=170,
            height=80,
            text="MAIN DISHES",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=button3,
        )
        cat_button3.grid(row=3, column=1, pady=33)

        def button4():
            cat_button1.destroy()
            cat_button2.destroy()
            cat_button3.destroy()
            cat_button5.destroy()
            drink_button1 = CTkButton(
                drink_Frame,
                width=210,
                height=150,
                text="Drink snakes",
                hover=True,
                hover_color=darkBlue,
                text_color=white,
                fg_color=cafe,
                bg_color=transparent,
                font=(lucida, 25),
                corner_radius=25,
            )
            drink_button1.grid(row=1, column=3, padx=50, pady=33)

        cat_button4 = CTkButton(
            category_Frame,
            width=170,
            height=80,
            text="SNAKES",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=button4,
        )
        cat_button4.grid(row=4, column=1, pady=33)

        def button5():
            cat_button1.destroy()
            cat_button2.destroy()
            cat_button4.destroy()
            cat_button3.destroy()
            drink_button1 = CTkButton(
                drink_Frame,
                width=210,
                height=150,
                text="Drink extra",
                hover=True,
                hover_color=darkBlue,
                text_color=white,
                fg_color=cafe,
                bg_color=transparent,
                font=(lucida, 25),
                corner_radius=25,
            )
            drink_button1.grid(row=1, column=3, padx=50, pady=33)

        cat_button5 = CTkButton(
            category_Frame,
            width=170,
            height=80,
            text="EXTRAS",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=button5,
        )
        cat_button5.grid(row=5, column=1, pady=50)

        quantity_Frame = CTkFrame(
            self.root,
            fg_color=darkBlue,
            bg_color=transparent,
            width=width - 2,
            height=80,
            corner_radius=0,
        )
        # quantity_Frame.place(x=2, y=750)
        quantity_Frame.pack(side="bottom")

        lbl_drink = Label(
            quantity_Frame,
            text="Drink : ",
            font=(lucida, 20),
            bg=darkBlue,
            fg=white,
        )
        lbl_drink.grid(row=1, column=1, padx=10, pady=22)

        lbl_drinkName = Label(
            quantity_Frame,
            text="Drink Name",
            font=(lucida, 20),
            bg=darkBlue,
            fg=white,
        )
        lbl_drinkName.grid(row=1, column=2, padx=10, pady=22)

        lbl_quantity = Label(
            quantity_Frame,
            text="Quantity : ",
            font=(lucida, 20),
            bg=darkBlue,
            fg=white,
        )
        lbl_quantity.grid(row=1, column=3, padx=(100, 10), pady=22)

        # minus = ImageTk.PhotoImage(Image.open('icons/minus.png'))
        # minus = minus.resize((80, 80))

        min_button = CTkButton(
            quantity_Frame,
            width=50,
            height=50,
            text="-",
            text_color=darkBlue,
            hover_color=cafe,
            fg_color=white,
            bg_color=darkBlue,
            font=(normal, 30, "bold"),
            corner_radius=20,
        )
        min_button.grid(row=1, column=5, padx=5)

        lbl_quantityNum = Label(
            quantity_Frame,
            text=" 5 ",
            font=(lucida, 20),
            bg=darkBlue,
            fg=white,
        )
        lbl_quantityNum.grid(row=1, column=6, padx=30, pady=22)

        plus_button = CTkButton(
            quantity_Frame,
            width=50,
            height=50,
            text="+",
            text_color=darkBlue,
            hover_color=cafe,
            fg_color=white,
            bg_color=darkBlue,
            font=(normal, 30, "bold"),
            corner_radius=20,
        )
        plus_button.grid(row=1, column=7, padx=5)

        lbl_price = Label(
            quantity_Frame,
            text="Total Price :  ",
            font=(lucida, 20),
            bg=darkBlue,
            fg=white,
        )
        lbl_price.grid(row=1, column=8, padx=(100, 10), pady=22)

        lbl_priceNum = Label(
            quantity_Frame,
            text="Price",
            font=(lucida, 20),
            bg=darkBlue,
            fg=white,
        )
        lbl_priceNum.grid(row=1, column=9, padx=25, pady=22)

        def toNextScreen():
            price = 250
            self.root.destroy()
            if selection == "takeaway":
                from e1_client_search_screen import ClientSearchScreen
                ClientSearchScreen(price, selection)
            elif selection == "cafe":
                from f_cash_screen import CashScreen
                CashScreen(price, selection)

        next_button = CTkButton(
            quantity_Frame,
            width=50,
            height=50,
            text="→",
            text_color=darkBlue,
            hover_color=cafe,
            fg_color=white,
            bg_color=darkBlue,
            font=(normal, 30, "bold"),
            corner_radius=20,
            command=toNextScreen,
        )
        next_button.grid(row=1, column=10, padx=100)

        drink_Frame = CTkFrame(
            self.root,
            fg_color=beige,
            bg_color=transparent,
            width=width - 20,
            height=height - 100,
        )
        drink_Frame.place(x=210, y=0)

        self.root.mainloop()
