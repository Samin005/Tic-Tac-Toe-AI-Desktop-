from game import game_board, minimax
import timeit

start = timeit.default_timer()

game_board.print_board_console()
game_board.make_best_move_ai()
print("states checked:", minimax.count)

stop = timeit.default_timer()
print('Time: ', stop - start)
