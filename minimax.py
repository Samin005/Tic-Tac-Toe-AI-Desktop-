import math

board_size = 3
board = [''] * board_size * board_size
board_length = len(board)
players = ["X", "O"]
human = players[0]
ai = players[1]
count = 0


def print_board_console():
    for x in range(board_length):
        if (x + 1) % board_size == 0:
            print(board[x], end="\n")
        else:
            print(board[x], end=", ")


def make_move_human(index: int):
    board[index] = human
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
    best_move_index = 0
    for index in range(board_length):
        if board[index] == "":
            board[index] = ai
            score = alpha_beta_pruning(current_board=board, level=0,
                                       alpha=-math.inf, beta=math.inf,
                                       maximizing_player=False)
            board[index] = ""
            # print("score", score)
            if score > best_score:
                best_score = score
                best_move_index = index
                # print('updated best score:', best_score)
                # print('best move:', best_move)
    board[best_move_index] = ai
    print_board_console()
    winner = check_winner()
    if winner == "tie":
        print("Game tied!")
    elif winner != "":
        print(winner, "has won the game!")


def find_match(index_1: int, index_2: int, index_3: int):
    if board[index_1] == board[index_2] and board[index_2] == board[index_3] and board[index_1] != "":
        return board[index_1]


def check_winner():
    # global count
    # print(count)
    # count += 1
    winner = ""
    # Horizontal match
    result = find_match(0, 1, 2)
    if result:
        winner = result
    result = find_match(3, 4, 5)
    if result:
        winner = result
    result = find_match(6, 7, 8)
    if result:
        winner = result

    # Vertical match
    result = find_match(0, 3, 6)
    if result:
        winner = result
    result = find_match(1, 4, 7)
    if result:
        winner = result
    result = find_match(2, 5, 8)
    if result:
        winner = result

    # Diagonal match
    result = find_match(0, 4, 8)
    if result:
        winner = result
    result = find_match(2, 4, 6)
    if result:
        winner = result
    open_spots = 0
    for index in range(board_length):
        if board[index] == "":
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


def alpha_beta_pruning(current_board: list, level: int, alpha, beta, maximizing_player: bool):
    global count
    count += 1
    winner = check_winner()  # returns X or O or ""
    # print("winner", winner)
    # print("winner scores", get_scores(winner))
    if winner != "":
        return get_scores(winner)  # returning the game value
    if maximizing_player:
        max_score = -math.inf
        for index in range(board_length):
            if current_board[index] == "":
                current_board[index] = ai
                score = alpha_beta_pruning(current_board=current_board, level=level + 1,
                                           alpha=alpha, beta=beta,
                                           maximizing_player=False)
                # print(board)
                # print("current score", score)
                current_board[index] = ""  # taking the move back because we want to find the best move first
                max_score = max(max_score, score)
                # print("max score", max_score)
                alpha = max(alpha, score)
                if alpha > beta:
                    break
        return max_score
    else:
        min_score = math.inf
        for index in range(board_length):
            if current_board[index] == "":
                current_board[index] = human
                score = alpha_beta_pruning(current_board=current_board, level=level + 1,
                                           alpha=alpha, beta=beta,
                                           maximizing_player=True)
                # print(board)
                # print("current score", score)
                current_board[index] = ""  # taking the move back because we want to find the best move first
                min_score = min(min_score, score)
                # print("min score", min_score)
                beta = min(beta, score)
                if alpha > beta:
                    break
        return min_score
