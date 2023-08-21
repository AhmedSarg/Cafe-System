import sys

sys.path.insert(0, "values")
sys.path.insert(0, "database")
from colors import *
from fonts import *
from tkinter import *
from customtkinter import *
from db_controller import *


class MenuScreen:
    def __init__(self, selection):
        connection = openConnection()

        self.selectedProduct = ""

        self.root = Tk()
        self.root.title("Menu")
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root.config(background=beige)
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()










        categoryFrame = CTkFrame(
            self.root,
            fg_color=darkBlue,
            bg_color=transparent,
            corner_radius=0
        )
        categoryFrame.place(x=0, y=0)

        def hotDrinksCategoryValue():
            getMenu(connection, "Hot Drinks")


        hotDrinksCategoryButton = CTkButton(
            categoryFrame,
            width=170,
            height=80,
            text="Hot Drinks",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=hotDrinksCategoryValue
        )
        hotDrinksCategoryButton.grid(row=1, column=0, pady=((height - 170) / 20), padx=15)

        def coffeeCategoryValue():
            getMenu(connection, "Coffee")

        coffeeCategoryButton = CTkButton(
            categoryFrame,
            width=170,
            height=80,
            text="Coffee",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=coffeeCategoryValue
        )
        coffeeCategoryButton.grid(row=2, column=0, pady=((height - 170) / 20), padx=15)

        def iceCreamCategoryValue():
            getMenu(connection, "Ice Cream")

        IceCreamCategoryButton = CTkButton(
            categoryFrame,
            width=170,
            height=80,
            text="Ice Creams",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=iceCreamCategoryValue
        )
        IceCreamCategoryButton.grid(row=3, column=0, pady=((height - 170) / 20), padx=15)

        def dessertCategoryValue():
            getMenu(connection, "Dessert")

        DessertCategoryButton = CTkButton(
            categoryFrame,
            width=170,
            height=80,
            text="Desserts",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=dessertCategoryValue
        )
        DessertCategoryButton.grid(row=4, column=0, pady=((height - 170) / 20), padx=15)

        def softDrinksCategoryValue():
            getMenu(connection, "Soft Drinks")

        softDrinksCategoryButton = CTkButton(
            categoryFrame,
            width=170,
            height=80,
            text="Soft Drinks",
            hover=True,
            hover_color=cafe,
            text_color=black,
            fg_color=white,
            bg_color=transparent,
            font=(lucida, 17),
            corner_radius=16,
            command=softDrinksCategoryValue
        )
        softDrinksCategoryButton.grid(row=5, column=0, pady=((height - 170) / 20), padx=15)












        productFrame = CTkFrame(
            self.root,
            fg_color=beige,
            bg_color=transparent,
        )
        productFrame.place(x=230, y=30)

        def testOnClick():
            print(self.selectedCategory)

        productItem = CTkButton(
            productFrame,
            width=240,
            height=150,
            text="Drink Hot",
            hover=True,
            hover_color=darkBlue,
            text_color=white,
            fg_color=cafe,
            bg_color=transparent,
            font=(lucida, 25),
            corner_radius=25,
            command=testOnClick
        )
        productItem._text_label.configure(wraplength=240)
        productItem.grid(row=1, column=1)














        quantity_Frame = CTkFrame(
            self.root,
            fg_color=darkBlue,
            bg_color=transparent,
            corner_radius=0,
        )
        quantity_Frame.pack(side="bottom")

        lbl_drink = CTkLabel(
            quantity_Frame,
            text="Drink : ",
            font=(lucida, 20),
            text_color=white,
            height=100,
            bg_color=darkBlue,
            fg_color=darkBlue,
        )
        lbl_drink.grid(row=1, column=1, padx=10)

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

        self.root.mainloop()
        endConnection(connection)

MenuScreen("cafe")
