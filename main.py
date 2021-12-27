# Imports
import data
from player import player
import PySimpleGUI as sg
import numpy as np

sg.theme('DarkPurple4')  # Choosing Theme
# Setting pre_window layout
pre_layout = [[sg.Text('Username')], [sg.InputText()], [sg.Text("Opponent's IP")],
              [sg.InputText()], [sg.Button('Play')]]

# Ask for name and opponent's IP
pre_window = sg.Window(data.GAME_NAME, pre_layout)
while True:
    event, values = pre_window.read()
    if event == 'Play':  # User closes main_window
        data.player1.name = values[0]
        data.connect(values[1])
        break
pre_window.close()

# Setting main_window layout
main_layout = [[[sg.Text(data.player1.name)],
                [sg.Text('Score: ' + str(data.player1.score))],
                [data.player1.board]],
                
                [[sg.Text(data.player2.name)],
                [sg.Text('Score: ' + str(data.player2.score))],
                [data.player2.board]],

                [sg.Button('Quit')]]

# Instantiating the Window
main_window=sg.Window(data.GAME_NAME, main_layout,
                        size = data.WINDOW_DEFAULT_SIZE, font = data.DEFAULT_FONT)
# Main loop
while True:
    event, values=main_window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':  # User closes main_window or quits
        ## SEND DISCONNECTION ##
        break
    data.shoot(main_window, event)
main_window.close()
