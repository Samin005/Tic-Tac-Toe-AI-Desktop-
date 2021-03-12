from game import game_board
import timeit
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


ui.pushButton_startGame.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(1))
ui.pushButton_quit.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(0))

MainWindow.show()
sys.exit(app.exec_())
#
# start = timeit.default_timer()
#
# game_board.print_board_console()
# game_board.make_best_move_ai()
#
# stop = timeit.default_timer()
# print('Time: ', stop - start)
