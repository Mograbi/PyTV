from Tkinter import *
import sys
import tkFileDialog, tkMessageBox
# Tkinter
# reference:    https://goo.gl/GYkfrN
root = Tk()
system = None
gui_obj = None

def help():
    tkMessageBox.showinfo("HELP", "")
    return

def create_window(father_window, title):
    t = Toplevel(father_window)
    t.title(title)
    t.geometry(DIMENSIONS)
    grid = init_grid(t)
    return grid

# ======================================================================================================================
# ======================================================================================================================
# MAIN  PROGRAM

# main_grid = init_grid()

root.geometry("180x220")
root.resizable(0, 0)
root.title("Py-TV")
start_y_pos = 35
BUTTON_WIDTH = 80
BUTTON_X_AXIS = 50

loadFileButton = Button(root, text='Load File', command=None)
loadFileButton.place(x=BUTTON_X_AXIS, y=start_y_pos, width=BUTTON_WIDTH, height=25)

helpButton = Button(root, text='Help', command=help)
helpButton.place(x=BUTTON_X_AXIS, y=start_y_pos + 30, width=BUTTON_WIDTH, height=25)

exitButton = Button(root, text='Exit', command=exit)
exitButton.place(x=BUTTON_X_AXIS, y=start_y_pos + 60, width=BUTTON_WIDTH, height=25)

root.mainloop()