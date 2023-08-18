from tkinter import *

from tkinter import ttk
import tkinter.messagebox



root = Tk()
root.state("zoomed")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.resizable(False,False)
root.config(background='#FFEEDB')

frame = Frame(root, bg = '#0d1f2d', border = 100)
mainframe = Frame(root)
mainframe.grid()

#top frame for title
titleFrame = Frame(mainframe, width = width, height = height, bg = '#FFEEDB')
titleFrame.grid(row = 0, column = 0)

titleLabel=Label(titleFrame,font=('Lucida Handwriting',30),text='Client search',bg='#FFEEDB',border=10)
titleLabel.grid(row=0,column=0,padx=10)

lbl_name=Label(frame,text='Name',bg='#0d1f2d',fg='#f6f4f6')
lbl_name.grid(row=0,column=0)

txt_name=Text(frame,bg='#f6f4f6',width=65,height=2)
txt_name.grid(row=0,column=1,padx=10,pady=10)

btn_se=Button(frame,text='search',bg='#f6f4f6',width=10)
btn_se.place(x=385,y=70)

btn_add=Button(frame,text='Add client',bg='#f6f4f6',width=10)
btn_add.place(x=120,y=70)

frame.place(anchor='center',relx=.5,rely=.5 )

root.mainloop()