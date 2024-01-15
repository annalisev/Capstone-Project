
board = [['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', 'X', '0', '0', '0'],
         ['0', '0', '0', '0', 'X', '0', '0'],
         ['0', 'X', '0', 'X', '0', '0', '0'],
         ['X', '0', '0', 'X', 'X', 'X', 'X']]


def win_checker(i, j):
         try:
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
         except:
                 return False


print(win_checker(5, 3))
