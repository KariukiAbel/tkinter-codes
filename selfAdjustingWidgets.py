from tkinter import *

root = Tk()

label1 = Label(root, text="First label", bg="Grey", fg="White")

# the fill=X adjusts the size of the label in the horizontal plane with change in the size of the window
label1.pack(fill=X)

label2 = Label(root, text="Second label", bg="Black", fg="White")

# the fill=Y adjusts the size of the label in the vertical plane with change in the size of the window
#  and the side=LEFT makes the widget appear on the left side of the window
label2.pack(side=LEFT, fill=Y)

root.mainloop()
