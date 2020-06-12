
from tkinter import *
def harry(event):
    print(f"you clicked on the button at {event.x} {event.y}")
root = Tk()
root.title("Events")
root.geometry("655x355")

wiget = Button(root,text="Click me please")
wiget.pack()

wiget.bind('<Button-1>',harry)
wiget.bind('<Double-1>',quit)

root.mainloop()