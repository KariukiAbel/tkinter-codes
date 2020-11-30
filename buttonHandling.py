from tkinter import *

root = Tk()


def doSomething():
    print("Button was clicked")

    
# the command=doSomething is the actual handler of the button so on clicking the button the doSomething function is executed
button1 = Button(root, text="Click me", command=doSomething)
button1.pack()

root.mainloop()
