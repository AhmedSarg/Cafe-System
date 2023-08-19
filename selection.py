from tkinter import *
from values.colors import *
from values.fonts import *
from customtkinter import *
from PIL import ImageTk, Image
root=Tk()
root.resizable(True,True)
root.title("Select")
root.state("zoomed")
root.resizable(False, False)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

root.configure(bg=beige)
btn_cafe_image=PhotoImage(file='icons\cafe.PNG')
#image_cafe
btn_takeaway_image=PhotoImage(file='icons\keaway.PNG')
#image_takeaway donot change name image file 

label_title = Label(root,text='Selecion Ordwe Type ',fg=black,bg=beige, cursor='heart' ,font=(font_style,45))
label_title.place(x=15,y=10)
#title

def onpressed_cafe():
    print('go the next page')
btn_cafe=Button(root,command=onpressed_cafe,image=btn_cafe_image,width="700",height="400",bg=beige,borderwidth=0)
btn_cafe.place(x=100,y=300)
#button

def onpressed_takeaway():
    print('go the next page')
btn_takeaway=Button(root,command=onpressed_takeaway,image=btn_takeaway_image,width="700",height="400",bg=beige,borderwidth=0)
btn_takeaway.place(x=800,y=300)

root.mainloop()