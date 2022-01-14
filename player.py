# This class defines the player
import PySimpleGUI as sg
import numpy as np
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class player:
    def __init__(self, GRID_SIZE, n: int):
        self.name = ""
        self.score = 0
        self.board = [[
            sg.Button(ALPHABET[j] + str(i + 1), key=ALPHABET[j] + str(i + 1) + str(n), size=(4, 2),
                      pad=(0.1, 0.1), font='Verdana 9', disabled=True)
            for j in range(GRID_SIZE)
        ] for i in range(GRID_SIZE)]  # Creating a square board

    def add_score(self, score):
        self.score += score
