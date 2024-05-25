from tkinter import *
from tkinter import ttk
import tkcalendar

root = Tk()
root.title("Data entry")
root.geometry("480x480")
# frist creat label data
la = Label(root, text="Data Entry Form", font="Whisper 20 bold")
la.grid(row=0, column=1, columnspan=4, padx=15, pady=10)


# create frist name , last name
fname = Label(root, text="Frist name")
fname.grid(row=1, column=0, padx=10, sticky="w")

frist_entry = Entry(root, width=20)
frist_entry.grid(row=1, column=1, padx=5)

lname = Label(root, text="Last name")
lname.grid(row=1, column=2, padx=10)

last_entry = Entry(root, width=20)
last_entry.grid(row=1, column=3, pady=5)

# create brith date
birth_label = Label(root, text="Birth date")
birth_label.grid(row=2, column=0, sticky="w")

birth_entry = tkcalendar.DateEntry(root)
birth_entry.grid(row=2, column=1, columnspan=3, sticky="we")

# create gender buttom
gender_bu = Label(root, text="Gender")
gender_bu.grid(row=3, column=0, sticky="w")

gender_bu = StringVar()
gender_bu.set("none")

male = Radiobutton(root, text="male", variable=gender_bu, value="male")
male.grid(row=3, column=1, sticky="w")

female = Radiobutton(root, text="female", variable=gender_bu, value="female")
female.grid(row=3, column=2, sticky="w")

# country
country = Label(root, text="Country")
country.grid(row=4, column=0)

country_opt = ttk.Combobox(root, width=20, values=["USA", "UK", "EG", "RU", "UEA"])
country_opt.grid(row=4, column=1, pady=5, columnspan=3, sticky="we")


# create save, clear button
def record():
    fname = frist_entry.get()
    lname = last_entry.get()
    birth_label = birth_entry.get()
    gender_buu = gender_bu.get()
    country = country_opt.get()
    text = (
        fname
        + ","
        + lname
        + ","
        + birth_label
        + ","
        + gender_buu
        + ","
        + country
        + "\n"
    )

    with open(r"C:\Users\Admin\Desktop\PHP.csv", "a") as file:
        file.write(text)


def clear_all():
    frist_entry.delete(0, "end")
    last_entry.delete(0, "end")
    birth_entry.delete(0, "end")
    gender_bu.set("none")
    country_opt.delete(0, "end")
    frist_entry.focus_set()


save = Button(root, text="Save", command=record)
save.grid(row=5, column=0, padx=10, sticky="e", pady=10)

clear = Button(root, text="Clear", command=clear_all)
clear.grid(row=5, column=1, padx=10, sticky="w")

root.mainloop()
