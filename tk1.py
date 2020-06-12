from tkinter import *
ro1 = Tk()
from PIL import Image, ImageTk
#gui logic
# width x height

ro1.geometry("644x434")

#width,height
ro1.minsize(200,100)
ro1.maxsize(800,800)

#label
rohit = Label(text = "Shakibb is a good boy and this is his gui")
rohit.pack()

#Important label option
'''text - adds the text
bg - background
1.font -  sets the font
2.font="comicsansms 19 bold"
fg - foreground
padx - x padding
pady - y pafding
relief - border styling - SUNKEN,RAISED,GROOVE,RIDGE
'''

#title
ro1.title("My gui with gourav")
title_label = Label(text = "HEy this is my learning in tk so i am writing it for testing",bg = "red",fg ="white",padx=40,pady=40,font=("comicsansms",19,"bold"),borderwidth=3,relief=GROOVE)
title_label.pack()

#IMPORTANT pack options

  #title_label.pack(anchor="ne")
  #IF we want it in the south
#title_label.pack(side=BOTTOM,anchor= "se")

#fill
#title_label.pack(side=BOTTOM,anchor = "se",fill=X)#for y we use capital Y
'''#image
#for jpg
im = Image.open("E:\Snake game\gallery\sprites\snk.jpg")
photo = ImageTk.PhotoImage(im)
image = Label(image=photo)
image.pack()

#for other image
photo = ImageTk.PhotoImage(#here we have to write the path)
image = Label(image=photo)
image.pack()'''

ro1.mainloop()
