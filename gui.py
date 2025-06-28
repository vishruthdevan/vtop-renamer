from tkinter import *
from tkinter import ttk
from functools import partial

file_path = ''

def window():
    root = Tk()
    root.geometry("400x100")
    root.title("V-Top Renamer")
    mainframe = ttk.Frame(root, padding="15 15 15 15")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=10)
    mainframe.rowconfigure(0, weight=10)
    path_var = StringVar()
    
    root_label = Label(mainframe, text="Enter path to zip folder: ")
    root_label.grid(column=0, row=0)
    
    root_entry = Entry(mainframe, width=40, textvariable=path_var)
    root_entry.grid(column=1, row=0)

    submit_button = Button(mainframe, text='Submit', command=lambda: submit(path_var.get()))
    submit_button.grid(column=1, row=1)
    root.mainloop()


def submit(path):
    file_path = path

window()