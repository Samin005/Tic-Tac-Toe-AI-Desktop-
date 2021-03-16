from game import game_board
import sys
from PyQt5 import QtWidgets
from gui import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.comboBox_mode.currentIndexChanged.connect(
    lambda: change_mode(ui.comboBox_mode.currentIndex())
)


def change_mode(mode_index: int):
    mode_details_text = game_board.get_mode_details(mode_index=mode_index)
    ui.label_modeDetails.setText(mode_details_text)


ui.pushButton_startGame.clicked.connect(lambda: start_game())


def start_game():
    reset_game()
    ui.stackedWidget.setCurrentIndex(1)


ui.pushButton_reset.clicked.connect(lambda: reset_game())


def reset_game():
    enable_all_buttons()
    for x in range(9):
        btn = get_button(x)
        btn.setText("")
        btn.setProperty("styleSheet", "")
    game_board.reset_board()
    ui.label_gameBottomText.setText(game_board.initial_game_bottom_text[game_board.current_mode_index])


ui.pushButton_quit.clicked.connect(lambda: quit_game())


def quit_game():
    reset_game()
    ui.stackedWidget.setCurrentIndex(0)


# Game board buttons click events
ui.pushButton_gameBoard_0.clicked.connect(lambda: make_move(btn=ui.pushButton_gameBoard_0))
ui.pushButton_gameBoard_1.clicked.connect(lambda: make_move(btn=ui.pushButton_gameBoard_1))
ui.pushButton_gameBoard_2.clicked.connect(lambda: make_move(btn=ui.pushButton_gameBoard_2))
ui.pushButton_gameBoard_3.clicked.connect(lambda: make_move(btn=ui.pushButton_gameBoard_3))
ui.pushButton_gameBoard_4.clicked.connect(lambda: make_move(btn=ui.pushButton_gameBoard_4))
ui.pushButton_gameBoard_5.clicked.connect(lambda: make_move(btn=ui.pushButton_gameBoard_5))
ui.pushButton_gameBoard_6.clicked.connect(lambda: make_move(btn=ui.pushButton_gameBoard_6))
ui.pushButton_gameBoard_7.clicked.connect(lambda: make_move(btn=ui.pushButton_gameBoard_7))
ui.pushButton_gameBoard_8.clicked.connect(lambda: make_move(btn=ui.pushButton_gameBoard_8))

button_styles = {
    game_board.players[0]: "background-color: #6eb1ff;\n"
                           "color: white;",
    game_board.players[1]: "background-color: #ff7373;\n"
                           "color: white;",
    "winner": "background-color: #89fc83;\n"
                           "color: black;"
}


def make_move(btn: QtWidgets.QPushButton):
    move_index_player1 = game_board.make_move_human(int(btn.objectName()[-1]))
    if move_index_player1 is not None:
        update_button(btn=btn)
        update_board_after_move()
        if game_board.current_mode_index == 0 and not game_board.is_game_over:
            move_index_player2 = game_board.make_best_move_ai()
            update_button(btn=get_button(move_index_player2))
            update_board_after_move()
        elif game_board.current_mode_index == 1 and not game_board.is_game_over:
            move_index_player2 = game_board.make_random_move_ai()
            update_button(btn=get_button(move_index_player2))
            update_board_after_move()
    ui.label_gameBottomText.setText(game_board.game_status_text)


def update_button(btn: QtWidgets.QPushButton):
    btn.setText(game_board.current_player)
    btn.setProperty("styleSheet", button_styles[game_board.current_player])
    btn.setDisabled(True)


def update_board_after_move():
    game_board.update_current_player()
    if game_board.is_game_over:
        if game_board.game_status_text != "Game tied!":
            for btn_index in game_board.winner_cell_indexes:
                btn = get_button(btn_index)
                btn.setProperty("styleSheet", button_styles["winner"])
        disable_all_buttons()


def disable_all_buttons():
    for x in range(9):
        btn = get_button(x)
        btn.setDisabled(True)


def enable_all_buttons():
    for x in range(9):
        btn = get_button(x)
        btn.setDisabled(False)


def get_button(button_index):
    if button_index == 0:
        return ui.pushButton_gameBoard_0
    elif button_index == 1:
        return ui.pushButton_gameBoard_1
    elif button_index == 2:
        return ui.pushButton_gameBoard_2
    elif button_index == 3:
        return ui.pushButton_gameBoard_3
    elif button_index == 4:
        return ui.pushButton_gameBoard_4
    elif button_index == 5:
        return ui.pushButton_gameBoard_5
    elif button_index == 6:
        return ui.pushButton_gameBoard_6
    elif button_index == 7:
        return ui.pushButton_gameBoard_7
    elif button_index == 8:
        return ui.pushButton_gameBoard_8


MainWindow.show()
sys.exit(app.exec_())
