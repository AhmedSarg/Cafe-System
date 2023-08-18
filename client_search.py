from tkinter import *

from tkinter import ttk
from customtkinter import *



root = Tk()
root.state("zoomed")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.resizable(False,False)
root.config(background ='#FFEEDB')

frame = Frame(root, bg = '#0d1f2d', border = 100)
mainframe = Frame(root)
mainframe.grid()

titleFrame = Frame(mainframe, width = width, height = height, bg = '#FFEEDB')
titleFrame.grid(row = 0, column = 0)

titleLabel = Label(titleFrame, font = ('Lucida Handwriting', 30), text = 'Client Search', bg = '#FFEEDB', border = 10)
titleLabel.grid(row = 0, column = 0, padx = 50, pady = 30)

labelName = Label(frame, text = 'Name', bg = '#0d1f2d', fg = '#f6f4f6')
labelName.grid(row = 0, column = 0)

txtName = Text(frame, bg = '#f6f4f6', width = 65, height = 2)
txtName.grid(row = 0, column = 1, padx = 10, pady = 10)

buttonSearch = Button(frame, text = 'search', bg = '#f6f4f6', width = 10)
buttonSearch.place(x = 385, y = 70)

buttonAdd = Button(frame, text = 'Add client', bg = '#f6f4f6', width = 10)
buttonAdd.place(x = 120, y = 70)

frame.place(anchor = 'center', relx = 0.5, rely = 0.5)

root.mainloop()
