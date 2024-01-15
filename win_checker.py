
board = [['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', 'X', '0', '0', '0'],
         ['0', '0', '0', '0', 'X', '0', '0'],
         ['0', 'X', '0', 'X', '0', '0', '0'],
         ['X', '0', '0', 'X', 'X', 'X', 'X']]


def win_checker(row, col):
    if row <= 2:
        if col >= 3:
            if board[row][col] == board[row+1][col-1] and board[row][col] == board[row+2][col-2] and board[row][col] == board[row+3][col-3]:
                return True
            elif board[row][col] == board[row+1][col] and board[row][col] == board[row+2][col] and board[row][col] == board[row+3][col]:
                return True
        if col <= 3:
            if board[row][col] == board[row+1][col+1] and board[row][col] == board[row+2][col+2] and board[row][col] == board[row+3][col+3]:
                return True
        elif board[row][col] == board[row+1][col] and board[row][col] == board[row+2][col] and board[row][col] == board[row+3][col]:
            return True

    elif col >= 3:
        if board[row][col] == board[row][col-1] and board[row][col] == board[row][col-2] and board[row][col] == board[row][col-3]:
            return True

    elif col <= 3:
        print('here1')
        if board[row][col] == board[row][col+1] and board[row][col] == board[row][col+2] and board[row][col] == board[row][col+3]:
            print('here2')
            return True

    else:
        return False


print(win_checker(5, 3))
