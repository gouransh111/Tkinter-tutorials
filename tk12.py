from tkinter import *
import tkinter.messagebox as tmsg 
root = Tk()
def order():
    tmsg.showinfo("Order received",f"We have received your order {var.get()} thanks for ordering")
root.title("Radio buttons")
root.geometry("455x255")

#var = IntVar()
var = StringVar()
#it is complsory to set a initial value otherwise it will take all the arguments
var.set("R")#r is randdomly cchoosen
#set help to initialize the value
#var.set(1)
Label(root,text="What would you like sir",font="lucida 19 bold",justify=LEFT,padx=14).pack()
radio = Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio = Radiobutton(root,text="Edli",padx=14,variable=var,value="Edli").pack(anchor="w")
radio = Radiobutton(root,text="Samosa",padx=14,variable=var,value="Samosa").pack(anchor="w")
radio = Radiobutton(root,text="paratha",padx=14,variable=var,value="Paratha").pack(anchor="w")
                           #or with for
Button(text="Order now",command=order).pack()                           
root.mainloop()
