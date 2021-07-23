from tkinter import *
from tkinter import ttk


def window():
    root = Tk()
    root.geometry("600x400")
    root.title("V-Top Renamer")

    mainframe = ttk.Frame(root, padding="15 15 15 15")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    
    root.update()
    root.mainloop()