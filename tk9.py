from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Idle")
def myfunc():
    print("TRhis is file")
def help():
    print("Ib will help you")
    #in first string we write the string that appears above the info box and on the second string we write that should be shown on the infobox
    a = tmsg.showinfo("Hello user","was your e")
    #its return value is ok 
def rate():
    print("Rate us")
    a = tmsg.askquestion("Was your experience good")
    if a=="yes":
        msg= "Great","Thankyou"
    else:
        msg="We will contact you"
    tmsg.showinfo("Hello",msg)

root.geometry("655x655")
yourmenu = Menu(root)
def divya():
    ans = tmsg.askretrycancel("Divya se dosti kar lo","Divya apki dost nahi")
    if ans:
          print("Retry mat karo") 
    else:    
        print("Badya cancel kar diya")
m1 = Menu(yourmenu,tearoff=0)
m1.add_command(label="Save",command = myfunc)
m1.add_command(label="New project",command = myfunc)
m1.add_separator()
m1.add_command(label="Save as",command = myfunc)
m1.add_command(label="print",command = myfunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="File",menu=m1)

m2 = Menu(yourmenu,tearoff=0)
m2.add_command(label="cut",command = myfunc)
m2.add_command(label="New ",command = myfunc)
m2.add_separator()
m2.add_command(label="copy",command = myfunc)
m2.add_command(label="pr",command = myfunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="edit",menu=m2)

m3 = Menu(yourmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="rate us",command=rate)
m3.add_command(label="Be friend divya",command=divya)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="Edit",menu=m3)
#for making ssub sub menu
#m4 = Menu(m3,tearoff=0)
#m4.add_command(label="a",command=help)
#root.config(menu=yourmenu)
#m3.add_cascade(label="new",menu=m4)
root.mainloop()