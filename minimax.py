import numpy as np
import math

board_size = 3
board = np.zeros((3, 3), dtype=str)
board_shape = board.shape
players = ["X", "O"]
human = players[0]
ai = players[1]
count = 0


def print_board_console():
    print(board)


def make_move_human(x: int, y: int):
    board[x, y] = human
    print_board_console()
    winner = check_winner()
    if winner == "":
        print("AI made a move:")
        make_best_move_ai()
    elif winner == "tie":
        print("Game tied!")
    else:
        print(winner, "has won the game!")


def make_best_move_ai():
    best_score = -math.inf
    best_move = {'x': 0, 'y': 0}
    for x, y in np.ndindex(board_shape):
        if board[x, y] == "":
            board[x, y] = ai
            score = alpha_beta_pruning(current_board=board, level=0,
                                       alpha=-math.inf, beta=math.inf,
                                       maximizing_player=False)
            board[x, y] = ""
            # print("score", score)
            if score > best_score:
                best_score = score
                best_move = {'x': x, 'y': y}
                # print('updated best score:', best_score)
                # print('best move:', best_move)
    board[best_move['x'], best_move['y']] = ai
    print_board_console()
    winner = check_winner()
    if winner == "tie":
        print("Game tied!")
    elif winner != "":
        print(winner, "has won the game!")


def check_winner():
    # global count
    # print(count)
    # count += 1
    winner = ""
    for x, y in np.ndindex(board_shape):
        # Horizontal match
        if board[x, 0] == board[x, 1] and board[x, 1] == board[x, 2] and board[x, 0] != "":
            # print(board)
            # print("horizontal match:", x, 0)
            winner = board[x, 0]
        # Vertical match
        if board[0, y] == board[1, y] and board[1, y] == board[2, y] and board[0, y] != "":
            # print(board)
            # print("vertical match:", 0, y)
            winner = board[0, y]
    # Diagonal match
    if np.all(board.diagonal() == board[0, 0]) and board[0, 0] != "":
        # print(board)
        # print("left diagonal match:", 0, 0)
        winner = board[0, 0]
    if np.all(np.fliplr(board).diagonal() == board[0, 2]) and board[0, 2] != "":
        # print(board)
        # print("left diagonal match:", 0, 2)
        winner = board[0, 2]
    open_spots = 0
    for x, y in np.ndindex(board_shape):
        if board[x, y] == "":
            open_spots += 1
    if winner == "" and open_spots == 0:
        # print("returning tie")
        return "tie"
    else:
        # print(board)
        # print("returning winner:", winner)
        return winner


def get_scores(player: str):
    # Human = -1
    if player == human:
        return -1
    # AI = 1
    elif player == ai:
        return 1
    # Tie = 0
    elif player == "tie":
        return 0


def alpha_beta_pruning(current_board: np.ndarray, level: int, alpha, beta, maximizing_player: bool):
    global count
    count += 1
    winner = check_winner()  # returns X or O or ""
    # print("winner", winner)
    # print("winner scores", get_scores(winner))
    if winner != "":
        return get_scores(winner)  # returning the game value
    if maximizing_player:
        max_score = -math.inf
        for x, y in np.ndindex(board_shape):
            if current_board[x, y] == "":
                current_board[x, y] = ai
                score = alpha_beta_pruning(current_board=current_board, level=level + 1,
                                           alpha=alpha, beta=beta,
                                           maximizing_player=False)
                # print(board)
                # print("current score", score)
                current_board[x, y] = ""  # taking the move back because we want to find the best move first
                max_score = max(max_score, score)
                # print("max score", max_score)
                alpha = max(alpha, score)
                if alpha > beta:
                    break
        return max_score
    else:
        min_score = math.inf
        for x, y in np.ndindex(board_shape):
            if current_board[x, y] == "":
                current_board[x, y] = human
                score = alpha_beta_pruning(current_board=current_board, level=level + 1,
                                           alpha=alpha, beta=beta,
                                           maximizing_player=True)
                # print(board)
                # print("current score", score)
                current_board[x, y] = ""  # taking the move back because we want to find the best move first
                min_score = min(min_score, score)
                # print("min score", min_score)
                beta = min(beta, score)
                if alpha > beta:
                    break
        return min_score
