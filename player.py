# This class defines the player
import PySimpleGUI as sg
import numpy as np


class player:
    def __init__(self, GRID_SIZE):
        self.name = ""
        self.score = 0
        self.ip = ""
        self.board = [[
            sg.Button('', size=(2, 1), key=(i, j), pad=(0.1, 0.1))
            for j in range(GRID_SIZE)
        ] for i in range(GRID_SIZE)]  # Creating a square board

    def add_score(self, score):
        self.score += score
