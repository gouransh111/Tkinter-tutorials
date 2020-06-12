from tkinter import*
import tkinter.messagebox as tmsg
root = Tk()
def getdollar():
    print(f"we have credited {myslider2.get()} to your account")
    tmsg.showinfo("help",f"we have credited {myslider2.get()} to your account")
root.geometry("455x233")
root.title("Slide tutrial")
#It is randomly a vertical slider
#myslider = Scale(root,from_=0,to=455).pack()
Label(root,text="How many dollars you want").pack()
#myslider2 = Scale(root,from_=0,to=455,orient=HORIZONTAL)
#if we want interval
myslider2 = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
# if we wan tits initial position
myslider2.set(34)
myslider2.pack()
Button(root,text="Get dollars",pady = 10,command=getdollar).pack()



root.mainloop()