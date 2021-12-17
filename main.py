# Libraries
import data
import game
from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()


def init_window():
    """
    Window init.
    """
    root.wm_title(data.GAME_NAME)
    root.configure(background=data.GUI_BACKGROUND)
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    ttk.Label(frame, text=data.GAME_NAME).grid(column=0, row=0)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
    
    data.p1_board = data.game_board
    data.p2_board = data.game_board



def main():
    """
    Main method.
    """
    init_window()


main()
root.mainloop()
