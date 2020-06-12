from tkinter import *
root = Tk()
canva_width = 800
canva_height = 400


root.geometry(f"{canva_width}x{canva_height}")
can_widget = Canvas(root,width=canva_width,height=canva_height)
can_widget.pack()
root.title("canva")
#The line goesv from the point x1,y1 to x2,y2

can_widget.create_line(0,0,800,200)
can_widget.create_line(0,0,800,300,fill = "red")
#to create a rectangle specify the parameters in this nordersb - coordinates of top leftv corner and coorss of bottom right corner
 #can_widget.create_rectangle(3,5,700,300,fill="blue")

can_widget.create_text(200,200,text="bd")

#the coordinates are same as rectangle
can_widget.create_oval(344,233,244,355)
#in circle we give square coordinates
root.mainloop()