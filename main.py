# Imports
import data
import game
from player import player
from tkinter import *
from tkinter import ttk
from tkinter import font
import numpy as np

root = Tk()


def init_window():
    """
    Window init.
    """
    root.wm_title(data.GAME_NAME)
    root.configure(background=data.GUI_BACKGROUND)
    data.main_frame = ttk.Frame(root, padding=1)
    data.main_frame.grid()
    ttk.Label(data.main_frame, text=data.GAME_NAME).grid(column=0, row=0)
    ttk.Button(data.main_frame, text="Quit",
               command=root.destroy).grid(column=1, row=0)
    data.print_button_board(data.main_frame, game.player1.board)


def main():
    """
    Main method.
    """
    init_window()


main()
root.mainloop()
