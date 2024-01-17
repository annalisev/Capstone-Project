import random
from termcolor import colored


def print_board(board):
    # Function to print the status of the board
    for i in range(6):
        for j in range(7):
            print(board[i][j], "  ", end='')
        print("\n")
    pass


def comp_turn():
    # Function during which the computer takes a turn
    col = 0
    while col == 0:
        num = random.randint(1, 7)
        if height_vals[num-1] != 6:
            col = num
            print(f'The computer is going in column number {col}.')
    return col - 1


def get_col(user):
    # Function which asks which column the user wants to put their counter in then returns this accounting for indexing
    col = 0
    while col == 0:
        try:
            inp = int(input(
                f'{user}, which column would you like to place your counter in? Enter a number between 1 and 7: '))
            if inp >= 1 and inp <= 7:
                if height_vals[inp-1] != 6:
                    col = inp
                else:
                    print('Counter could not be placed, that column is already full!'
                          )
            else:
                print('Out of range, counter cannot be placed.')
        except:
            print('Invalid input')
    return col - 1


board = [['0', '0', '0', '0', '0', '0', '0'],
         ['0', 'X', '0', '0', '0', '0', '0'],
         ['0', 'X', '0', 'X', '0', '0', '0'],
         ['0', 'X', 'X', 'X', 'X', '0', '0'],
         ['0', 'X', '0', 'X', '0', 'X', '0'],
         ['X', 'X', '0', 'X', 'X', 'X', 'X']]


# Many small functions in order to define win_checker function
def diagonal_right(row, col):
    if row <= 2 and col <= 3:
        if (board[row][col] == board[row+1][col+1]) and (board[row][col] == board[row+2][col+2]) and (board[row][col] == board[row+3][col+3]):
            return True
        else:
            return False
    else:
        return False


def diagonal_right_shift1(row, col):
    if row <= 3 and row >= 1 and col <= 4 and col >= 1:
        if (board[row][col] == board[row-1][col-1]) and (board[row][col] == board[row+2][col+2]) and (board[row][col] == board[row+1][col+1]):
            return True
        else:
            return False
    else:
        return False


def diagonal_right_shift2(row, col):
    if row <= 4 and row >= 2 and col <= 5 and col >= 2:
        if (board[row][col] == board[row-2][col-2]) and (board[row][col] == board[row-1][col-1]) and (board[row][col] == board[row+1][col+1]):
            return True
        else:
            return False
    else:
        return False


def diagonal_right_shift3(row, col):
    if row <= 5 and row >= 3 and col >= 3:
        if (board[row][col] == board[row-2][col-2]) and (board[row][col] == board[row-1][col-1]) and (board[row][col] == board[row-3][col-3]):
            return True
        else:
            return False
    else:
        return False


def diagonal_left(row, col):
    if row <= 2 and col >= 3:
        if (board[row][col] == board[row+1][col-1]) and (board[row][col] == board[row+2][col-2]) and (board[row][col] == board[row+3][col-3]):
            return True
        else:
            return False
    else:
        return False


def diagonal_left_shift1(row, col):
    if row <= 3 and row >= 1 and col <= 5 and col >= 2:
        if (board[row][col] == board[row-1][col+1]) and (board[row][col] == board[row+2][col-2]) and (board[row][col] == board[row+1][col-1]):
            return True
        else:
            return False
    else:
        return False


def diagonal_left_shift2(row, col):
    if row <= 4 and row >= 2 and col <= 4 and col >= 1:
        if (board[row][col] == board[row-2][col+2]) and (board[row][col] == board[row-1][col+1]) and (board[row][col] == board[row+1][col-1]):
            return True
        else:
            return False
    else:
        return False


def diagonal_left_shift3(row, col):
    if row <= 5 and row >= 3 and col <= 3:
        if (board[row][col] == board[row-2][col+2]) and (board[row][col] == board[row-1][col+1]) and (board[row][col] == board[row-3][col+3]):
            return True
        else:
            return False
    else:
        return False


def diagonal_checker(row, col):
    return diagonal_right(row, col) or diagonal_right_shift1(row, col) or diagonal_right_shift2(row, col) or diagonal_right_shift3(row, col) or diagonal_left(row, col) or diagonal_left_shift1(row, col) or diagonal_left_shift2(row, col) or diagonal_left_shift3(row, col)


def vertical_checker(row, col):
    if row <= 2:
        if (board[row][col] == board[row+1][col]) and (board[row][col] == board[row+2][col]) and (board[row][col] == board[row+3][col]):
            return True
        else:
            return False
    else:
        return False


def checker_right(row, col):
    if (board[row][col] == board[row][col+1]) and (board[row][col] == board[row][col+2]) and (board[row][col] == board[row][col+3]):
        return True
    else:
        return False


def checker_right_shift1(row, col):
    if (board[row][col] == board[row][col-1]) and (board[row][col] == board[row][col+1]) and (board[row][col] == board[row][col+2]):
        return True
    else:
        return False


def checker_left(row, col):
    if (board[row][col] == board[row][col-1]) and (board[row][col] == board[row][col-2]) and (board[row][col] == board[row][col-3]):
        return True
    else:
        return False


def checker_left_shift1(row, col):
    if (board[row][col] == board[row][col+1]) and (board[row][col] == board[row][col-1]) and (board[row][col] == board[row][col-2]):
        return True
    else:
        return False


def horizontal_checker(row, col):
    if col == 0:
        return checker_right(row, col)

    elif col == 1:
        return checker_right(row, col) or checker_right_shift1(row, col)

    elif col == 2:
        return checker_right(row, col) or checker_right_shift1(
            row, col) or checker_left_shift1(row, col)

    elif col == 3:
        return checker_right(row, col) or checker_right_shift1(
            row, col) or checker_left_shift1(row, col) or checker_left(row, col)

    elif col == 4:
        return checker_right_shift1(row, col) or checker_left_shift1(
            row, col) or checker_left(row, col)

    elif col == 5:
        return checker_left_shift1(row, col) or checker_left(row, col)

    elif col == 6:
        return checker_left(row, col)

    else:
        return False


def win_checker(row, col):
    # Function which tells us whether the game is in a win state or not
    return horizontal_checker(row, col) or vertical_checker(row, col) or diagonal_checker(row, col)


def placing_counter(col, board, colour):
    # Function to update the board when a new counter is placed
    height = height_vals[col]
    board[5-height][col] = colour
    height_vals[col] += 1
    return win_checker(5-height, col), colour


# Initialising the board and other values
board = [['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0']]

height_vals = [0, 0, 0, 0, 0, 0, 0]
win_status = False
game_type = 0

while game_type != 'T' and game_type != 'C':
    print('Would you like to play a two-player game or play against the computer?')
    game_type = input(
        'Type T for two-player or C to play against the computer: ').upper()

if game_type == 'C':

    user_colour = 0
    current_player = 0
    player_name = input('What is your name?: ').capitalize()

    # Asking the user which colour they want to be, in a while loop to ensure question gets answered even if user inputs something weird
    while user_colour == 0:
        print('Would you like to be', colored(
            'yellow', 'yellow'), 'or', colored('red', 'red'), ' ?')
        colour_input = input('Please enter either Y or R: ')
        if colour_input.lower() == 'r':
            user_colour = colored("R", 'red')
            player_name = colored(player_name, 'red')
            comp_colour = colored("Y", 'yellow')
            print(
                f'Okay, you are the', colored('Red', 'red'), f' player, you will play with counter {user_colour}!')
        elif colour_input.lower() == 'y':
            user_colour = colored("Y", 'yellow')
            player_name = colored(player_name, 'yellow')
            comp_colour = colored("R", 'red')
            print(
                'Okay, you are the', colored('Yellow', 'yellow'), f' player, you will play with counter {user_colour}!')

    # Seeing who will start
    print('We will flip a coin to see who will start')
    coin = random.randint(0, 1)
    if coin == 0:
        print('Tails, the computer will start.')
    elif coin == 1:
        print('Heads, you will start.')
        print_board(board)
        placing_counter(get_col(player_name), board, user_colour)
        print_board(board)

    while win_status == False:
        win_status, current_player = placing_counter(
            comp_turn(), board, comp_colour)
        print('The board is now:')
        print_board(board)
        if win_status == True:
            break
        win_status, current_player = placing_counter(
            get_col(player_name), board, user_colour)
        print('The board is now:')
        print_board(board)

    print('The game has been won!')
    print(f'Congratulations {current_player} player, you have won!')
    if current_player == user_colour:
        print('Well Done! You have beaten the computer, how clever!')
    else:
        print('Oh no! The computer has beaten you! Better luck next time!')

else:
    user1_name = input("Please enter the first player's name: ").capitalize()
    user2_name = input("Please enter the second player's name: ").capitalize()

    user1_colour = 0
    user2_colour = 0

    while user1_colour == 0:
        print(f'{user1_name} would you like to be', colored(
            'yellow', 'yellow'), 'or', colored('red', 'red'), ' ?')
        colour_input = input('Please enter either Y or R: ')
        if colour_input.lower() == 'r':
            user1_colour = colored("R", 'red')
            user1_name = colored(user1_name, 'red')
            user2_colour = colored("Y", 'yellow')
            user2_name = colored(user2_name, 'yellow')
            print(
                f'Okay, {user1_name}, you are the', colored('Red', 'red'), f' player, you will play with counter {user1_colour}!')
            print(
                f'{user2_name}, you are the', colored('Yellow', 'yellow'), f' player, you will play with counter {user2_colour}!')
        elif colour_input.lower() == 'y':
            user1_colour = colored("Y", 'yellow')
            user1_name = colored(user1_name, 'yellow')
            user2_colour = colored("R", 'red')
            user2_name = colored(user2_name, 'red')
            print(
                f'Okay, {user1_name}, you are the', colored('Yellow', 'yellow'), f' player, you will play with counter {user1_colour}!')
            print(
                f'{user2_name}, you are the', colored('Red', 'red'), f' player, you will play with counter {user2_colour}!')

    current_player = 0

    # Seeing who will start
    print('We will flip a coin to see who will start')
    coin = random.randint(0, 1)
    if coin == 0:
        print(f'Tails, {user2_name} will start.')
        print_board(board)
        placing_counter(get_col(user2_name), board, user2_colour)
        print_board(board)
    elif coin == 1:
        print(f'Heads, {user1_name} will start.')
        print_board(board)

    while win_status == False:
        win_status, current_player = placing_counter(
            get_col(user1_name), board, user1_colour)
        print('The board is now:')
        print_board(board)
        if win_status == True:
            break
        win_status, current_player = placing_counter(
            get_col(user2_name), board, user2_colour)
        print('The board is now:')
        print_board(board)

    print('The game has been won!')
    print(f'Congratulations {current_player} player, you have won!')
    if current_player == user1_colour:
        print(
            f'Well Done {user1_name}! You have beaten {user2_name}, how clever!')
    else:
        print(
            f'Well Done {user2_name}! You have beaten {user1_name}, how clever!')
