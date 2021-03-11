import minimax
import timeit

start = timeit.default_timer()

# minimax.board[0, 0] = "X"
# minimax.board[1, 2] = "X"
# minimax.board[0, 1] = "O"
# minimax.board[1, 0] = "O"
# minimax.board[1, 2] = "X"
# minimax.board[2, 0] = "O"
minimax.print_board_console()
minimax.make_best_move_ai()
print("states checked:", minimax.count)
stop = timeit.default_timer()

print('Time: ', stop - start)


