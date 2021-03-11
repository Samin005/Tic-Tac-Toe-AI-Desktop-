from . import game_board
import math


def alpha_beta_pruning(current_board: list, level: int, alpha, beta, maximizing_player: bool):
    winner = game_board.check_winner()  # returns X or O or ""
    if winner != "":
        return game_board.get_scores(winner)  # returning the game value
    if maximizing_player:
        max_score = -math.inf
        for index in range(game_board.board_length):
            if current_board[index] == "":
                current_board[index] = game_board.ai
                score = alpha_beta_pruning(current_board=current_board, level=level + 1,
                                           alpha=alpha, beta=beta,
                                           maximizing_player=False)
                current_board[index] = ""  # taking the move back because we want to find the best move first
                max_score = max(max_score, score)
                alpha = max(alpha, score)
                if alpha > beta:
                    break
        return max_score
    else:
        min_score = math.inf
        for index in range(game_board.board_length):
            if current_board[index] == "":
                current_board[index] = game_board.human
                score = alpha_beta_pruning(current_board=current_board, level=level + 1,
                                           alpha=alpha, beta=beta,
                                           maximizing_player=True)
                current_board[index] = ""  # taking the move back because we want to find the best move first
                min_score = min(min_score, score)
                beta = min(beta, score)
                if alpha > beta:
                    break
        return min_score
