from tkinter import *
root = Tk()
def get():
    print("Submiiting records")
    print(f"{nameval.get()} {phoneval.get()} {genderval.get() }{contactval.get()} {paymentval.get()}")
    try:
     with open("records.txt","a") as f:
        f.write(f"{nameval.get()} {phoneval.get()} {genderval.get()} {contactval.get()} {paymentval.get()}\n")
    except:
        print("not submitted")    
root.geometry("655x655")
Label(root,text = "Welcome to gouransh page",font = "Arial 13 bold").grid()
#TEXT FOR UOR FORM
name = Label(root,text="Name")
phone = Label(root,text="phone")
gender = Label(root,text="gender")
contact = Label(root,text="Emergencycontact")
payment = Label(root,text="payment")

#PACKING FORM
name.grid(row=1,column=0)
phone.grid(row=2,column=0)
gender.grid(row=3,column=0)
contact.grid(row=4,column=0)
payment.grid(row=5,column=0)
#MAKING ENTRIES VARIABLES
nameval = StringVar()
phoneval = StringVar()
genderval = StringVar()
contactval = StringVar()
paymentval = StringVar()

namevalentry = Entry(root,textvariable = nameval)
phonevalentry = Entry(root,textvariable = phoneval)
gendervalentry = Entry(root,textvariable = genderval)
contactvalentry = Entry(root,textvariable = contactval)
paymentvalentry = Entry(root,textvariable= paymentval)
#namevalentry = Entry(root,textvariable)
#PACKING ENTRIES
namevalentry.grid(row=1,column=1)
phonevalentry.grid(row=2,column=1)
gendervalentry.grid(row=3,column=1)
contactvalentry.grid(row=4,column=1)
paymentvalentry.grid(row=5,column=1)
food1 = IntVar()
#CHECKBOX
food = Checkbutton(text="All information are correct",variable=food1).grid(row=6,column=1)
Button(text="Submit",command=get).grid(row=8,column=0)
root.mainloop()

