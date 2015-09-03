__author__ = 'ET'
from Tkinter import *
from PIL import Image, ImageTk
import os
import shutil

rating = {}

def get_imgs(path):
    result = []
    for root, dirs, files in os.walk(path):
        for image in files:
            result.append(os.path.join(root, image))
    return result

def rate(root, i):
    if len(files) > 0:
        print files[0]
        rating[files[0]] = i

        img = ImageTk.PhotoImage(Image.open(files[0]))
        root.title(files[0])

        root.viewer = Label(root, image=img)
        root.viewer.image = img
        root.viewer.grid(row=0, column=0, columnspan=5)
        files.remove(files[0])
    else:
        root.destroy()
    return True

def build_windows():
    root = Tk()

    img = ImageTk.PhotoImage(Image.open(files[0]))
    viewer = Label(root, image=img)
    viewer.grid(row=0, column=0, columnspan=5)

    rate1 = Button(root, text="1", width="16", height="5")
    rate1.grid(row=1, column=0)
    rate1["command"] = lambda: rate(root, 1)

    rate2 = Button(root, text="2", width="16", height="5")
    rate2.grid(row=1, column=1)
    rate2["command"] = lambda: rate(root, 2)

    rate3 = Button(root, text="3", width="16", height="5")
    rate3.grid(row=1, column=2)
    rate3["command"] = lambda: rate(root, 3)

    rate4 = Button(root, text="4", width="16", height="5")
    rate4.grid(row=1, column=3)
    rate4["command"] = lambda: rate(root, 4)

    rate5 = Button(root, text="5", width="16", height="5")
    rate5.grid(row=1, column=4)
    rate5["command"] = lambda: rate(root, 5)

    root.mainloop()

if __name__ == "__main__":
    path = os.path.abspath(sys.argv[1])
    files = get_imgs(path)
    build_windows()