import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog


def show():
    global list_box, history
    current = list_box.curselection()
    year_ = list_box.get(current)
    messagebox.showinfo(message=history[year_])


def delete():
    global list_box, history
    current = list_box.curselection()
    year_ = list_box.get(current)
    list_box.delete(current)
    history.pop(year_)
    with open("file.json", "w") as file_:
        json.dump(history, file_, indent=4)
    messagebox.showinfo(message="delete")


"""
add year and information into listbox
"""


def add():
    global list_box, history
    year_ = simpledialog.askstring(None, "enter year")
    information = simpledialog.askstring(None, "enter information")
    # add year  to list_box
    list_box.insert(END, year_)
    # add year and info to history
    history[year_] = information
    # save history to json file
    with open("file.json", "w") as file_:
        json.dump(history, file_, indent=4)


if __name__ == '__main__':

    # window
    window = Tk()
    # dict

    with open("file.json", "r") as file:
        history = json.load(file)

    # frames
    list_box_frame = ttk.Frame(master=window, padding=200)
    button_frame = ttk.Frame(master=window, padding=30)
    list_box_frame.pack()
    button_frame.pack()

    # create list box
    list_box = Listbox(list_box_frame)
    list_box.pack(fill=BOTH)
    for year in history:
        list_box.insert(END, year)

    # create button
    button1 = ttk.Button(button_frame, text="add", command=add)
    button2 = ttk.Button(button_frame, text="show", command=show)
    button3 = ttk.Button(button_frame, text="delete", command=delete)
    button1.pack()
    button2.pack()
    button3.pack()

    # start
    window.mainloop()
