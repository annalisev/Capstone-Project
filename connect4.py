import random


def print_board(board):
    for i in range(6):
        print(board[i])
    pass


def comp_turn():
    col = 0
    while col == 0:
        num = random.randint(1, 7)
        if height_vals[num-1] != 6:
            col = num
            print(f'The computer is going in column number {col}.')
    return col - 1


def get_col():
    col = 0
    while col == 0:
        inp = int(input(
            'Which column would you like to place your counter in? Enter a number between 1 and 7: '))
        if height_vals[inp-1] != 6:
            col = inp
        else:
            print('Counter could not be placed, that column is already full!'
                  )
    return col - 1


def win_checker(i, j):
    if board[i][j] == board[i-1][j+1] and board[i][j] == board[i-2][j+2] and board[i][j] == board[i-3][j+3]:
        return True
    elif board[i][j] == board[i-1][j-1] and board[i][j] == board[i-2][j-2] and board[i][j] == board[i-3][j-3]:
        return True
    elif board[i][j] == board[i][j+1] and board[i][j] == board[i][j+2] and board[i][j] == board[i][j+3]:
        return True
    elif board[i][j] == board[i-1][j] and board[i][j] == board[i-2][j] and board[i][j] == board[i-3][j]:
        return True
    else:
        return False


def placing_counter(col, board, colour):
    height = height_vals[col]
    board[5-height][col] = colour
    height_vals[col] += 1
    win_status = win_checker(5-height, col)


board = [['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0']]

height_vals = [0, 0, 0, 0, 0, 0, 0]
win_status = False
user_colour = 0
while user_colour == 0:
    colour_input = input(
        'Would you like to be yellow or red? Please enter either Y or R: ')
    if colour_input.lower() == 'r':
        user_colour = "R"
        comp_colour = "Y"
    elif colour_input.lower() == 'y':
        user_colour = "Y"
        comp_colour = "R"

print('We will flip a coin to see who will start')
coin = random.randint(0, 1)
'''if coin == 0:
    print('Tails, the computer will start.')
elif coin == 1:'''
print('Heads, you will start.')
placing_counter(get_col(), board, user_colour)
print_board(board)

while win_status == False:
    placing_counter(comp_turn(), board, comp_colour)
    print('The board is now:')
    print_board(board)
    placing_counter(get_col(), board, user_colour)
    print('The board is now:')
    print_board(board)

print('The game has been won!')
print_board(board)
