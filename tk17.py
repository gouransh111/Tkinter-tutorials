from tkinter import *
root = Tk()
#for changing the feather icon on top left
root.wm_iconbitmap("E:/games photos/bird.png")
root.title("Title of my gui")
root.geometry("655x444")
#for changing the background
root.configure(background="red")
#for taking width and height of the window that is running
width =  root.winfo_screenwidth()
height = root.winfo_screenheight()
print(width,height)
#it close the window
Button(text="Close",command = root.destroy).pack()
root.mainloop()