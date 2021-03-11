import numpy as np

board_size = 3
board = np.zeros((3, 3), dtype=str)
board_shape = board.shape


def print_board_console():
    print(board)


def check_results():
    for x, y in np.ndindex(board_shape):
        # horizontal match
        if board[x, 0] == board[x, 1] and board[x, 1] == board[x, 2] and board[x, 0] != "":
            return board[x, 0]
        # Vertical match
        if board[0, y] == board[x, 1] and board[1, y] == board[2, y] and board[0, y] != "":
            return board[0, y]
    # Diagonal match
    if np.all(board.diagonal() == board[0, 0]) and board[0, 0] != "":
        return board[0, 0]
    if np.all(np.fliplr(board).diagonal() == board[0, 2]) and board[0, 2] != "":
        return board[0, 2]
