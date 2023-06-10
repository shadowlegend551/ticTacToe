from tkinter import Tk, Button, DISABLED
from collections import Counter


# All winning coordinate combinations are on this list.
win_cond = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]




# This function sets the board and checks for winners.
def game():
    global Xwin
    global Owin
    global turn
    global screen
    global buttons
    
    buttons = {}  # A dictionary for buttons and their coordinates.
    Xwin = []  # Player X's pressed buttons' coordinates are stored here.
    Owin = []  # Player O's pressed buttons' coordinates are stored here
    win = False
    turn = True
    wait = True
    try:
        screen.destroy()
    except:
        pass
    screen = Tk()
    screen.title('Tic Tac Toe')
    screen.focus_force()
    screen.bind('r', lambda event: game())
    x = 0
    y = 0

    # Makes the buttons.
    for coord in range(9):

        button = Button(
            text='',
            command=lambda coord=coord: markup(coord),  # Calls markup().
            width=16,
            height=8,
        )

        button.grid(column=x, row=y)
        buttons[coord] = button
        x = x + 1
        if x == 3:
            x = 0
            y = y + 1


# When a button is pressed, this function marks the right symbol and calls check_for_win().
def markup(coord):
    global Owin
    global Xwin
    global turn
    global win

    if turn:
        buttons[coord]['text'] = u'\u274C'
        buttons[coord]['command'] = DISABLED
        Xwin.insert(0, convert_int(coord))
        Xwin.sort(reverse=False)
    else:
        buttons[coord]['text'] = u'\u25EF'
        buttons[coord]['command'] = DISABLED
        Owin.insert(0, convert_int(coord))
        Owin.sort(reverse=False)

    check_for_win(Xwin, Owin)
    turn = not turn


# Converts needed value from dictionary 'buttons' to int.
def convert_int(coord):
    removable_char = '.!buton'
    fin_int = str(buttons[coord])

    for char in removable_char:
        fin_int = fin_int.replace(char, '')
    if fin_int == '':
        fin_int = 1
    return int(fin_int)


def disable():
    for child in screen.winfo_children():
        child.configure(state='disable')  # Disables all buttons so the game doesn't go on forever.


# Checks who won by comparing lists 'Xwin' and 'Owin' to sublists of win_cond
def check_for_win(Xwin, Owin):
    global win_cond
    global turn

    if not turn:
        check = Counter(Owin)
    elif turn:
        check = Counter(Xwin)

    win = any(len(Counter(e) - check) == 0 for e in win_cond)

    if win and turn:
        screen.title('X won!')
        print('X won')
        disable()
    elif win and not turn:
        screen.title('O won!')
        print('O won')
        disable()


if __name__ == '__main__':
    game()
    screen.mainloop()
