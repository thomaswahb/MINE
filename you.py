from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import threading


root = Tk()
root.title("YouTube Downloader")
root.geometry("600x325")


# browse fun
def browse():
    dir = filedialog.askdirectory(title="Save Video")
    flink.delete(0, "end")
    flink.insert(0, dir)


# down fun
def down():
    status.config(text="Status : Downloading.... ")
    link = ytlink.get()
    folder = flink.get()
    YouTube(link, on_complete_callback=finish).streams.filter(
        progressive=True, file_extension="mp4"
    ).order_by("resolution").desc().first().download(folder)


def finish(stream=None, chunk=None, file_handle=None, remaining=None):
    status.config(text="Status : complete ")


# to be stable
root.resizable(FALSE, FALSE)
# Youtube logo
ytphoto = PhotoImage(file="yt.png")
ytlogo = Label(root, image=ytphoto)
ytlogo.place(relx=0.5, rely=0.25, anchor="center")

# youtube link
ytlabel = Label(root, text="Youtube link")
ytlabel.place(x=25, y=140)

ytlink = Entry(root, width=40)
ytlink.place(x=140, y=150)

# folder link
flabel = Label(root, text="Folder link")
flabel.place(x=25, y=183)

flink = Entry(root, width=50)
flink.place(x=140, y=183)

# Browse Button
browse = Button(root, text="Browse", command=browse)
browse.place(x=455, y=180)

# download button
dbutton = Button(root, text="Download", command=threading.Thread(target=down).start)
dbutton.place(x=280, y=220)

# status bar
status = Label(
    root,
    text="Status ready",
    font="Calibre 10 italic",
    fg="black",
    bg="white",
    anchor="w",
)
status.place(rely=1, anchor="sw", relwidth=1)

root.mainloop()
