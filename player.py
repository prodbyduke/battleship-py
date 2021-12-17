# This class defines the player
import data
import numpy as np


class player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.board = np.array([
            ["" for x in range(data.GRID_SIZE)],
            ["" for y in range(data.GRID_SIZE)]
        ])  # Creating a square matrix NxN where N = data.GRID_SIZE

    def add_score(self, score):
        self.score += score