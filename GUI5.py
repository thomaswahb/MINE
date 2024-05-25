from tkinter import *

root = Tk()
root.geometry("500x500")
bu1 = Button(root, text="button")
bu1.place(x=200, y=50)

bu2 = Button(root, text="button")
bu2.place(relx=0.5, rely=0.5, anchor="center")
root.mainloop()
