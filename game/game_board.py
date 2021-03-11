import numpy as np

board_size = 3
board = np.zeros((3, 3), dtype=str)
board_shape = board.shape
players = ["X", "O"]


def print_board_console():
    print(board)
    # board_length = len(board)
    # for x in range(board_length):
    #     if (x + 1) % board_size == 0:
    #         print(board[x], end="\n")
    #     else:
    #         print(board[x], end=", ")


def make_move(player: str, board_index: int):
    board[board_index] = player


def check_results():
    winner = ""
    for x, y in np.ndindex(board):
        if board[x, 0] == board[x, 1] and board[x, 1] == board[x, 2] and board[x, 0] != "":
            return
    # board_length = len(board)
    # horizontal_count = 0
    # horizontal_current_player = ""
    # for x in range(board_length):
    #     print("x: ", x)
    #     # setting the current player
    #     if x % board_size == 0 and board[x] != " ":
    #         horizontal_current_player = board[x]
    #     # checking horizontal matches
    #     if board[x] == horizontal_current_player:
    #         horizontal_count += 1
    #     if (x + 1) % board_size == 0:
    #         if horizontal_count == board_size and board[x] == horizontal_current_player:
    #             winner = board[x]
    #             return winner
    #         else:
    #             horizontal_count = 0
    return winner
