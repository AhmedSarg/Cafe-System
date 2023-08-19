from tkinter import *
from values.colors import *
from values.fonts import *
from customtkinter import *
from PIL import ImageTk, Image
root=Tk()
root.resizable(True,True)
root.title("Select")
root.state("zoomed")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

root.configure(bg=beige)
btn_cafe_image=PhotoImage(file='icons\cafe.PNG')
#image_cafe
btn_takeaway_image=PhotoImage(file='icons\keaway.PNG')
#image_takeaway donot change name image file 

cup = Image.open("icons\cup.png")
cup = cup.resize((80, 80))
icon = CTkImage(light_image=cup, size=(80, 80))
logo = CTkLabel(
    root,
      image=icon,
        bg_color=transparent,
          text=""
          )
logo.place(x=screenWidth-100, y=20)
label_title = Label(
    root,
    text='Selection Order Type ',
    fg=black,
    bg=beige,
      cursor='heart',
      font=(lucida,40)
      )
label_title.place(x=15,y=20)
#title

def onpressed_cafe():
    print('go the next page')
btn_cafe=Button(
    root,
    command=onpressed_cafe,
    image=btn_cafe_image,
    width="700",
    height="400",
    bg=beige,
    borderwidth=0
    )
btn_cafe.place(x=100,y=300)
#button

def onpressed_takeaway():
    print('go the next page')
btn_takeaway=Button(
    root,
    command=onpressed_takeaway,
    image=btn_takeaway_image,
    width="700",
    height="400",
    bg=beige,
    borderwidth=0
    )
btn_takeaway.place(x=800,y=300)

root.mainloop()