__author__ = 'ET'
from Tkinter import *
from PIL import Image, ImageTk
import os
import shutil

def rate(i):
    global count
    global path
    global files
    if not os.path.exists(path + str(i) + "/"):
        os.makedirs(path + str(i) + "/")

    if len(files) <= count:
        root.destroy()

    shutil.copy2(path + str(files[count]), path + str(i) + "/" + str(files[count]))

    count += 1

    img = ImageTk.PhotoImage(Image.open(path + str(files[count])))
    root.title(path + str(files[count]))

    root.viewer = Label(root, image=img)
    root.viewer.image = img
    root.viewer.grid(row=0, column=0, columnspan=5)
    return True

def build_windows():
    root = Tk()

    viewer = Label(root, image=img)
    viewer.image = img
    viewer.grid(row=0, column=0, columnspan=5)

    rate1 = Button(root, text="1", width="16", height="5")
    rate1.grid(row=1, column=0)
    rate1["command"] = lambda: rate(1)

    rate2 = Button(root, text="2", width="16", height="5")
    rate2.grid(row=1, column=1)
    rate2["command"] = lambda: rate(2)

    rate3 = Button(root, text="3", width="16", height="5")
    rate3.grid(row=1, column=2)
    rate3["command"] = lambda: rate(3)

    rate4 = Button(root, text="4", width="16", height="5")
    rate4.grid(row=1, column=3)
    rate4["command"] = lambda: rate(4)

    rate5 = Button(root, text="5", width="16", height="5")
    rate5.grid(row=1, column=4)
    rate5["command"] = lambda: rate(5)

    root.mainloop()

if __name__ == "__main__":
    print "please input the image folder path"
    path = raw_input()
    path = os.path.abspath(path)
    print path
    build_windows()