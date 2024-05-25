from tkinter import *

root = Tk()

button1 = Button(root, text="click").pack()

# to create multe opt
# line 7 (لتعريف المتغير mysys على انه متغير تابع الى  tkinter)
mysys = StringVar()
opt1 = Radiobutton(root, text="opt 1", variable="mysys", value="check0").pack()
opt2 = Radiobutton(root, text="opt 2", variable="mysys", value="check1").pack()

# to create check button
check = Checkbutton(root, text="check me").pack()


# to create list
opt = Listbox(root)
opt.pack()
opt.insert(1, 2, 3, "ali", "mhmd")


root.mainloop()
