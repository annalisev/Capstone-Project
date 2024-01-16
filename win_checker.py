
board = [['0', '0', '0', '0', '0', '0', '0'],
         ['0', 'X', '0', '0', '0', '0', '0'],
         ['0', 'X', '0', 'X', '0', '0', '0'],
         ['0', 'X', 'X', 'X', 'X', '0', '0'],
         ['0', 'X', '0', 'X', '0', 'X', '0'],
         ['X', 'X', '0', 'X', 'X', 'X', 'X']]


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
    return horizontal_checker(row, col) or vertical_checker(row, col) or diagonal_checker(row, col)


print(win_checker(4, 2))
