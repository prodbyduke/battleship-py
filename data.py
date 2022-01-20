import socket
from player import player
import PySimpleGUI as sg
import comunicazione as comm


ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
GAME_NAME = "Battleship"
GRID_SIZE = 10
DEFAULT_FONT = 'Verdana 9'
WINDOW_DEFAULT_SIZE = (475, 950)
MISSED_COLOR = 'grey'
HIT_COLOR = 'IndianRed3'
DROWNED_COLOR = 'IndianRed4'
SHIP_COLOR = 'DarkGreen'
SENDPORT = 6969
LISTENPORT = 12345
LOCALIP = "127.0.0.1" 
BUFFERSIZE = 1024

SHIPS = {
    "CARRIER": 5,
    "BATTLESHIP": 4,
    "DESTROYER": 3,
    "SUBMARINE": 3,
    "PATROL BOAT": 2
}

player1 = player(GRID_SIZE, 1)
player2 = player(GRID_SIZE, 2)
current_gamemode = "Idle"
current_ship = None
current_direction = 0
occupied_points = []
available = False #variabile per capire se siamo occupati
ready = False # Connection established
turn = 0 #il turno, se è 0 è avversario se è 1 è il nostro turno
opponentIP = None
UDPServerSocket = None
tempIp = ""


def creaSocket():
    global UDPServerSocket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((LOCALIP, LISTENPORT))

def changeTurn():
    #questo fa vedere graficamente di chi è il turno 
    #portremmo fare che quando non è il nostro turno i bottoni per mandare l'attacco sono disabilitati
    return 0 

def shootResult(coordinate):
    risultato = 2
    #se le coordinate che ci hanno passato corrispondono a una nave allora manderemo 0, se la nave è stata affondata 1 se hanno missato -1
    return risultato
    
def shoot(window: sg.Window, event):    
    # Send shot info to opponent    
    # -1: missed | 0: hit | 1: drowned
    if(comm.sendAttack(event)):
        result = shootResponse() # Receive result from shotResponse()
        if result == -1:
            color = MISSED_COLOR
        elif result == 0:
            color = HIT_COLOR
            player1.add_score(1)
        elif result == 1:
            color = DROWNED_COLOR
            player1.add_score(5)

        window[event].update(window[event],
                            button_color=(color, color))
        window[event].update('', disabled=True)

def shootResponse(): 
    # get shot response
    risposta = comm.waitResponse()
    splittedMsg = risposta.split(", ")
    if(splittedMsg[0] == "RH"):
        rispostaColpo = splittedMsg[1] #-1, 1 o 0 
    return rispostaColpo

def place_ship(ship, coordinate, direction: int):
    # Place a ship on the board
    # Direction - 0: Horizontal | 1: Vertical
    length = SHIPS[ship]
    if(direction == 0):
        for column in range(length):
            player1.board[int(coordinate[1:(len(coordinate)) - 1]) - 1][column + ALPHABET.index(coordinate[0:1])].update(button_color=(SHIP_COLOR, SHIP_COLOR))
            occupied_points.append(player1.board[int(coordinate[1:(len(coordinate)) - 1]) - 1][column + ALPHABET.index(coordinate[0:1])].Key)
    elif(direction == 1):
        for row in range(length):
            player1.board[row + int(coordinate[1:(len(coordinate)) - 1]) - 1][ALPHABET.index(coordinate[0:1])].update(button_color=(SHIP_COLOR, SHIP_COLOR))
            occupied_points.append(player1.board[row + int(coordinate[1:(len(coordinate)) - 1]) - 1][ALPHABET.index(coordinate[0:1])].Key)
    return None

def receive_shot(coords):
    # Receive shot from opponent and respond
    if coords in occupied_points:
        result = 0
    return

def is_in_board(event):
    # Check if the pressed button is in a board
    check = False
    board_ids = []
    for number in range(GRID_SIZE):
        for letter in range(GRID_SIZE):
            if(event[0:(len(event) - 1)] == (ALPHABET[letter] + str(number + 1))):
                check = True
                break
    return check


def get_event_type(event):
    # Get what type of button has been pressed
    if(is_in_board(event)):
        return 'Board'
    elif(event in SHIPS):
        return 'SelectShip'
    elif(event == 'HV'):
        return 'SwitchDirection'


def check_gamemode(window: sg.Window, event):
    # Check what to do after a pressed button
    global current_gamemode, current_ship, current_direction, player1, player2
    if(get_event_type(event) == 'Board' and current_gamemode == "Shoot"):
        shoot(window, event)
        return
    elif(get_event_type(event) == 'Board' and current_gamemode == "Place"):
        place_ship(current_ship, event, current_direction)
        window[current_ship].update(disabled=True)
        current_gamemode = "Shoot"
        disable_board(player1)
        enable_board(player2)
        return
    elif(get_event_type(event) == 'SelectShip'):
        current_ship = event
        current_gamemode = "Place"
        disable_board(player2)
        enable_board(player1)
        return
    elif(get_event_type(event) == 'SwitchDirection'):
        if(current_direction == 0):
            current_direction = 1
            window[event].update('Vertical')
        elif(current_direction == 1):
            current_direction = 0
            window[event].update('Horizontal')
        return

def closeGame():
    return ""

def disable_board(player: player):
    # Disable the specified board
    for column in range(GRID_SIZE):
        for row in range(GRID_SIZE):
            player.board[column][row].update(disabled=True)


def enable_board(player: player):
    # Enable the specified board
    for column in range(GRID_SIZE):
        for row in range(GRID_SIZE):
            player.board[column][row].update(disabled=False)