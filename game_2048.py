import random

def new_game(n):    # Initialize a new game by creating a nxn grid with zeros and place two 2s in random positions
    board = [[0] * n for _ in range(n)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):    # adds a 2 to a randomly chosen empty cell on board
    if any(0 in row for row in board):
        x, y = random.choice([(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == 0])
        board[x][y] = 2

def compress(board):    # Shift all non-zero tiles to the left of the board 
    new_mat = [[0]*len(board) for _ in range(len(board))]
    for i in range(len(board)):
        pos = 0
        for j in range(len(board)):
            if board[i][j] != 0:
                new_mat[i][pos] = board[i][j]
                pos += 1
    return new_mat

def merge(board):   # Merge adjacent tiles of the same values towards to the left
    for i in range(len(board)):
        for j in range(len(board)-1):
            if board[i][j] == board[i][j+1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j+1] = 0
    return board

def reverse(board): # Reverses each row of the board (L-R reverse)
    new_mat = []
    for i in range(len(board)):
        new_mat.append([])
        for j in range(len(board)):
            new_mat[i].append(board[i][len(board)-j-1])
    return new_mat

def transpose(board):   # Transpose the board
    new_mat = list(zip(*board))
    return [list(row) for row in new_mat]

def move_left(board):   # Move tiles to the left
    board = compress(board)
    board = merge(board)
    board = compress(board)
    return board

def move_right(board):  # Move tiles to the right
    board = reverse(board)
    board = move_left(board)
    board = reverse(board)
    return board

def move_up(board): # Move tiles upward
    board = transpose(board)
    board = move_left(board)
    board = transpose(board)
    return board

def move_down(board):   # Move tiles downward
    board = transpose(board)
    board = move_right(board)
    board = transpose(board)
    return board

def get_current_state(board):   # Check current board status to determine if game finished
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2048:
                return 'WON'
    if any(0 in row for row in board):
        return 'GAME NOT OVER'
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i][j] == board[i+1][j] or board[i][j] == board[i][j+1]:
                return 'GAME NOT OVER'
    return 'LOST'