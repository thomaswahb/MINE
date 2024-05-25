from tkinter import *
import webbrowser


def buclick():
    link = lin.get()
    webbrowser.open(link)


frame = Tk()
# to change App name
frame.title("App")

# to change App size
frame.geometry("300x300")


# to create a label
mylabel = Label(frame, text=("Web"), font="Helvatica 10 bold")
mylabel.pack(pady=20)


# to get links from user
lin = Entry(frame)
lin.pack(side=LEFT, padx=10, ipadx=10, fill=X, expand=True)

# to create a button
button = Button(
    frame, text="click", fg="red", bg="blue", font="Helvatica 10 bold", command=buclick
)
button.pack(side=LEFT, padx=10, fill=X)

frame.mainloop()
