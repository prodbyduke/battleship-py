import random
from player import player
import PySimpleGUI as sg
import numpy as np

GAME_NAME = "Battleship"
GRID_SIZE = 10
DEFAULT_FONT = 'Verdana 12'
WINDOW_DEFAULT_SIZE = (300, 725)

SHIPS = {
    "Carrier": 5,
    "Battleship": 4,
    "Destroyer": 3,
    "Submarine": 3,
    "Patrol Boat": 2
}

player1 = player(GRID_SIZE)
player2 = player(GRID_SIZE)


def connect(IP):
    # Connecting with opponent
    return None


def shoot(window: sg.Window, event):
    # Send shot info to opponent
    # THIS METHOD IS STILL NOT DEVELOPED
    result = random.randint(-1, 1)  # -1: missed | 0: hit | 1: drowned
    match result:
        case -1:
            color = 'grey'
        case 0:
            color = 'IndianRed3'
        case 1:
            color = 'IndianRed4'

    window[event].update(player2.board[event[0]][event[1]],
                         button_color=(color, color))
    window[event].update('', disabled=True)
