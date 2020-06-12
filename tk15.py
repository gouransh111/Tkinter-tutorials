from tkinter import *
root = Tk()
def upload():
    statusvar.set("Busy...")
    sbar.update()#if we dont write this busy will not displayed but ready now will displayed
    import time
    time.sleep(2)
    statusvar.set("Ready Now")
root.title("status bar ")
root.geometry("455x255")
statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="upload",command=upload).pack()
root.mainloop()