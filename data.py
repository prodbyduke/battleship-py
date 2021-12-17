GAME_NAME = "Battleship"
GUI_BACKGROUND = "LightSkyBlue1"
GRID_SIZE = 10

p1_board = None
p2_board = None

def game_board():
    """
    Defining a new board
    """
    board = [[0 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
    return board


def print_board(board):
    """
    Printing an existing board
    """
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            ttk.Button(frame, text=" ").grid(column=1, row=1)