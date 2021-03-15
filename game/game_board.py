from . import minimax
import math
import random

board_size = 3
board = [''] * board_size * board_size
board_length = len(board)
players = ["X", "O"]
human = players[0]
ai = players[1]
current_player = players[0]

# Game Options
modes = {
    "Hard": "Mode Details:\n"
            "You will play against an AI that uses the Minimax Alpha Beta Pruning Algorithm\n"
            "to make the best move possible.\n"
            "You won\'t win, the best thing you can do is a tie!",
    "Easy": "Mode Details:\n"
            "You will play against an AI that randomly chooses its next move.",
    "2 Players": "Mode Details:\n"
                 "You can play with your friend in a friendly game of Tic Tac Toe."
}
current_mode_index = 0
initial_game_bottom_text = [
    "The AI let's you go first out of pity.",
    "Your can go first.",
    current_player + "'s turn."
]
game_status_text = ""
winner_cell_indexes = (0, 1, 2)
is_game_over = False


def print_board_console():
    for x in range(board_length):
        if (x + 1) % board_size == 0:
            print(board[x], end="\n")
        else:
            print(board[x], end=", ")


def update_current_player():
    global current_player
    if current_player == players[0]:
        current_player = players[1]
    elif current_player == players[1]:
        current_player = players[0]


def make_move_human(index: int):
    global game_status_text, is_game_over
    if index < board_length and board[index] == "":
        board[index] = current_player
        print_board_console()
        run_after_moves_checks()
        return index
    else:
        game_status_text = "Invalid move!"
        print(game_status_text)


def make_best_move_ai():
    best_score = -math.inf
    best_move_index = 0
    for index in range(board_length):
        if board[index] == "":
            board[index] = ai
            score = minimax.alpha_beta_pruning(current_board=board, level=0,
                                               alpha=-math.inf, beta=math.inf,
                                               maximizing_player=False)
            board[index] = ""
            if score > best_score:
                best_score = score
                best_move_index = index
    board[best_move_index] = ai
    print_board_console()
    run_after_moves_checks()
    return best_move_index


def make_random_move_ai():
    empty_cells = list()
    for x in range(board_length):
        if board[x] == "":
            empty_cells.append(x)
    empty_cells_length = len(empty_cells)
    if empty_cells_length > 0:
        random_index = random.randint(0, len(empty_cells)-1)
    else:
        random_index = 0
    random_move_index = empty_cells[random_index]
    board[random_move_index] = ai
    run_after_moves_checks()
    return random_move_index


def run_after_moves_checks():
    global game_status_text, is_game_over
    winner = check_winner()
    if winner == "":
        if current_player == players[0]:
            game_status_text = players[1] + "'s turn."
        elif current_player == players[1]:
            game_status_text = players[0] + "'s turn."
    elif winner == "tie":
        game_status_text = "Game tied!"
        print(game_status_text)
        is_game_over = True
    elif winner != "":
        game_status_text = winner + " has won the game!"
        print(game_status_text)
        is_game_over = True


def find_match(index_1: int, index_2: int, index_3: int):
    global winner_cell_indexes
    if board[index_1] == board[index_2] and board[index_2] == board[index_3] and board[index_1] != "":
        winner_cell_indexes = (index_1, index_2, index_3)
        return board[index_1]


def check_winner():
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
        return "tie"
    else:
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


def get_mode_details(mode_index: int):
    global current_mode_index
    current_mode_index = mode_index
    return modes[list(modes.keys())[mode_index]]


def reset_board():
    global board, is_game_over, current_player
    board = [''] * board_size * board_size
    is_game_over = False
    current_player = players[0]
