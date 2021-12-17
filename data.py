from tkinter import *
from tkinter import ttk
from tkinter import font
import numpy as np

GAME_NAME = "Battleship"
GUI_BACKGROUND = "LightSkyBlue1"
GRID_SIZE = 10

main_frame = None


def print_button_board(frame: Frame, board: np.array):
    """
    Printing an existing board
    """
    x = 0
    for row in board:
        y = 0
        for cell in row:
            cell = ttk.Button(text=" ", width=10)
            cell.grid(column=y, row=x)
            y += 1
        x += 1