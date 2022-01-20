# Imports
import data
import PySimpleGUI as sg
import disconnessione

def main():
    sg.theme('DarkPurple4')  # Choosing Theme
    # Setting pre_window layout
    pre_layout = [[sg.Text('Username')], [sg.InputText()], [sg.Text("Opponent's IP")],
                [sg.InputText()], [sg.Button('Play')], [sg.Button('Ready')]]

    # Ask for name and opponent's IP
    pre_window = sg.Window(data.GAME_NAME, pre_layout)
    while data.ready == False:
        event, values = pre_window.read()

        if event == 'Play':  # User closes main_window
            data.player1.name = values[0]
            data.tempIp = values[1]
            print(data.tempIp)
        if event == 'Ready': # User is ready to accept connection
            data.player1.name = values[0]
            data.available = True
        if data.opponentIP == data.tempIp:
            break
    pre_window.close()

    # Setting main_window layout
    main_layout = [[[sg.Text(data.player2.name)],
                    [sg.Text('Score: ' + str(data.player2.score))],
                    [data.player2.board]],

                [[sg.Text(data.player1.name)],
                    [sg.Text('Score: ' + str(data.player1.score))],
                    [data.player1.board],
                    [sg.Button(ship) for ship in data.SHIPS]],

                [sg.Button('Horizontal', key='HV')], [sg.Button('Quit')]]

    # Instantiating the Window
    main_window = sg.Window(data.GAME_NAME, main_layout,
                            size=data.WINDOW_DEFAULT_SIZE, font=data.DEFAULT_FONT)
    data.busy = True #quando apro la main window vuol dire che sono in gioco e allora sono occupato
    # Main loop
    while True:
        event, values = main_window.read()
        if event == sg.WIN_CLOSED or event == 'Quit':  # User closes main_window or quits
            disconnessione.disconnect(False)
            break
        data.check_gamemode(main_window, event)
        print(data.occupied_points)
    main_window.close()
