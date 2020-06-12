from tkinter import *
root = Tk()

root.title("Scrool bar")
root.geometry("455x255")
#for connecting scrool bar to a widget
#1.widget(yscrollcommand = scrollbar.set)
#2. scrollbar.config(command=widget.yview)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
listbox = Listbox(root,yscrollcommand = scrollbar.set)
#for i in range(344):
 #   listbox.insert(END,f"Item {i}")
#listbox.pack(fill=BOTH,padx=22)
#scrollbar.config(command=listbox.yview)
text=Text(root,yscrollcommand = scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)    

root.mainloop()