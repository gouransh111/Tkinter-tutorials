from tkinter import *
root = Tk()
root.geometry("655x655")
def hello():
    print("hello tkinter buttons")
def name():
    print("Name is gouransh")
    
frame = Frame(root,borderwidth=6,bg = "grey",relief = SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1 = Button(frame,fg="red",text="Print now",command=hello)#in commad we have to give only function name we shoulf not use ()
b1.pack(side=LEFT,padx=10)

b2 = Button(frame,fg="red",text="Print now",command=name)
b2.pack(side=LEFT,padx=10)

b3 = Button(frame,fg="red",text="Print now")
b3.pack(side=LEFT,padx=10)

b4 = Button(frame,fg="red",text="Print now")
b4.pack(side=LEFT,padx=10)

root.mainloop()
