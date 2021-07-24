from tkinter import *
from tkinter import ttk
import base64, os
import rename
from icon import icon
icondata= base64.b64decode(icon)
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
iconfile.write(icondata)
iconfile.close()

def submit():
    file_path = path_var.get()
    new_dir = rename.setup(file_path)
    success_label = Label(mainframe, text="That file path does not exist!")
    success_label.grid(column=0, row=2, columnspan = 2)
    if not new_dir:
        success_label.config(text="That file/folder does not exist!")
        
    else:
        rename.rename(new_dir)
        success_label.config(text="Executed successfully :)")

def make_menu(w):
    global the_menu
    the_menu = Menu(w, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")

def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("Cut",
    command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy",
    command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)


file_path = ''
root = Tk()
root.geometry("450x100")
root.title("V-Top Renamer")
root.wm_iconbitmap(tempFile)
os.remove(tempFile)

make_menu(root)
e1 = Entry(); e1.grid()
e1.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

mainframe = ttk.Frame(root, padding="15 15 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=10)
mainframe.rowconfigure(0, weight=10)
path_var = StringVar()

root_label = Label(mainframe, text="Enter path to zip file or folder: ")
root_label.grid(column=0, row=0)

root_entry = Entry(mainframe, width=40, textvariable=path_var)
root_entry.grid(column=1, row=0)
submit_button = Button(mainframe, text='Submit', command=submit)
submit_button.grid(column=1, row=1)

created_label = Label(root, text="Made by Vishruth Devan", font=("Arial", 7))
created_label.grid(column=0, row=2, sticky=(SW))
root.mainloop()

