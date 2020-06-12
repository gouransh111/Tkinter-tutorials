from tkinter import *

root = Tk()
def add():
    global i 
    #Active insert the item above the line that is active
    lbx.insert(ACTIVE, f"{i}")
    i+=1
i = 0    
root.title("List widgets")
root.geometry("455x255")
lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"First item of our listbox")

Button(root,text="add item",command = add).pack()
root.mainloop()