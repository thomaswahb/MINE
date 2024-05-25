from tkinter import *

root = Tk()
root.geometry("200x200")

button1 = Button(root, text="button1")
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = Button(root, text="button2")
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = Button(root, text="button3")
button3.grid(row=1, column=0, padx=10, pady=10)

button4 = Button(root, text="button4")
button4.grid(row=1, column=1, padx=10, pady=10)

button5 = Button(root, text="button5")
button5.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=10)

root.mainloop()
