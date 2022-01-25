# Problem Statement
# You are given an NxN chessboard, and you are required to place N queens on this chessboard such that no queen is under threat from any other queen.
# As input, your function will take a number n and a list of strings as board.
# n = 4
# board = ["----", 
#          "----",
#          "----",
#          "----"
#          ]

# Your function should return the updated list of strings, board, such that no queen denoted by q shares a row, column, or diagonal with another queen.
# placeNQueens(n, board) = 
#        ["-q--",
#         "---q",
#         "q---",
#         "--q-"
#         ]
def isSafe(i, j, board):
  for c in range(len(board)):
    for r in range(len(board)):
      if board[c][r] == 'q' and i==c and j!=r:
        return False
      elif board[c][r] == 'q' and j==r and i!=c:
        return False
      elif (i+j == c+r or i-j == c-r) and board[c][r] == 'q':
        return False
  return True 

def placeNQueens(n, board):

  '''
  To check whether index i,j is safe to place queen call isSafe(i, j, board)
  True means it is safe, False means it is not
  '''
  return board

l = ['q', 't', 'p', 'i', 'u']
print(isSafe('s', 'm', l))