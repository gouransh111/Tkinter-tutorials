from tkinter import *
def getvals():
    print(f"The user is {uservalue.get()}")
    print(f"The password is {passvalue.get()}")
root =Tk()
root.geometry("655x655")
user = Label(root,text="Username")
password = Label(root,text="password")
user.grid(row=0,column=0)
password.grid(row=1,column=0)
#variable classes in tkinter
#booleanVar,DoubleVar,IntVar,StringVar
uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable = uservalue)
passentry=Entry(root,textvariable = passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

bu = Button(text="Submit",command=getvals).grid()

root.mainloop()
