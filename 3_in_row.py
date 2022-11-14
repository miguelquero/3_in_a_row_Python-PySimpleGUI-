import PySimpleGUI as sg

button_size = (7, 3)

PLAYER_ONE = "X"
PLAYER_TWO = "O"

winner_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

layout = [[
                sg.Button("", key="-0-", size=button_size),
                sg.Button("", key="-1-", size=button_size),
                sg.Button("", key="-2-", size=button_size)
          ],
          [
                sg.Button("", key="-3-", size=button_size),
                sg.Button("", key="-4-", size=button_size),
                sg.Button("", key="-5-", size=button_size)
          ],
          [
                sg.Button("", key="-6-", size=button_size),
                sg.Button("", key="-7-", size=button_size),
                sg.Button("", key="-8-", size=button_size)
          ],
          [sg.Button("He terminado", key="-end-"), sg.Button("Revancha", key="-again-")]]


def close_program(event):
    if event == sg.WIN_CLOSED or event == "-end-":
        close = True
        return close


def winner_player(deck):
    for winner_play in winner_plays:
        if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
            if deck[winner_play[0]] == PLAYER_ONE:
                sg.Popup("El jugador 1 (X) ha ganado")
                game_end = True
                return game_end
            else:
                sg.Popup("El jugador 2 (O) ha ganado")
                game_end = True
                return game_end
    if 0 not in deck:
        sg.Popup("Juego terminado, nadie gano")


def again(event, window, deck, game_end):
    if event == "-again-":
        if 0 in deck and not game_end:
            sg.Popup("Para la revancha primero tiene que ganar alguien")
        else:
            window.Element("-0-").Update(text="")
            window.Element("-1-").Update(text="")
            window.Element("-2-").Update(text="")
            window.Element("-3-").Update(text="")
            window.Element("-4-").Update(text="")
            window.Element("-5-").Update(text="")
            window.Element("-6-").Update(text="")
            window.Element("-7-").Update(text="")
            window.Element("-8-").Update(text="")
            new_game = True
            return new_game


def round(event, window, current_player, deck, game_end):
    if window.Element(event).ButtonText == "" and not game_end:
        index = int(event.replace("-", ""))
        deck[index] = current_player
        window.Element(event).Update(text=current_player)
        turn = True
        return turn


def main():
    current_player = PLAYER_ONE
    game_end = False
    deck = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]
    window = sg.Window("Demo", layout)

    while True:
        event, value = window.read()
        close = close_program(event)
        if close:
            break

        turn = round(event, window, current_player, deck, game_end)
        if not game_end:
            win = winner_player(deck)
            if win:
                game_end = True
            if turn:
                if current_player == PLAYER_ONE:
                    current_player = PLAYER_TWO
                else:
                    current_player = PLAYER_ONE

        new_game = again(event, window, deck, game_end)
        if new_game:
            current_player = PLAYER_ONE
            game_end = False
            deck = [0, 0, 0,
                    0, 0, 0,
                    0, 0, 0]

    window.close()

if __name__ == "__main__":
    main()