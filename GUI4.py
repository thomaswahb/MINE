from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox


def hello():
    mas = messagebox.showinfo(title="HELLO", message="hello " + enter.get())

#to get name file from user
def myfile():
    file = filedialog.askopenfile(title="open your file")
    enter.insert(0, file)


root = Tk()
root.geometry("200x200")

bu1 = Button(root, text="click1")
bu1.pack()

bu2 = ttk.Button(root, text="click2")
bu2.pack()

opt1 = Radiobutton(root, text="opt1")
opt1.pack()

opt2 = ttk.Radiobutton(root, text="opt2")
opt2.pack()

# to create combo box
combo = ttk.Combobox(root, values=["python", "AI", "english"]).pack()

# to create dilog
button = ttk.Button(root, text="click here", command=hello)
button.pack()

enter = Entry(root)
enter.pack()

root.mainloop()
