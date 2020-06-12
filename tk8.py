from tkinter import *
root = Tk()
root.title("Idle")
def myfunc():
    print("TRhis is file")
root.geometry("655x655")

#mymenu = Menu(root)
#mymenu.add_command(label="File",command=myfunc)
#mymenu.add_command(label="Exit",command=quit)
#root.config(menu=mymenu)

yourmenu = Menu(root)
#if we want that a tearoff means a horizontal line with sub menu will not appera we use tearoff
m1 = Menu(yourmenu,tearoff=0)
#else
#m1 = Menu(yourmenu)
m1.add_command(label="Save",command = myfunc)
m1.add_command(label="New project",command = myfunc)
#if we want a line bteween submenu
m1.add_separator()
m1.add_command(label="Save as",command = myfunc)
m1.add_command(label="print",command = myfunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="File",menu=m1)

m2 = Menu(yourmenu,tearoff=0)
m2.add_command(label="cut",command = myfunc)
m2.add_command(label="New ",command = myfunc)
#if we want a line bteween submenu
m2.add_separator()
m2.add_command(label="copy",command = myfunc)
m2.add_command(label="pr",command = myfunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="edit",menu=m2)
root.mainloop()