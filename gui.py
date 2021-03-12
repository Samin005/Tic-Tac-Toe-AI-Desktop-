# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 515)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_main)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_home)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_mainHomePage = QtWidgets.QFrame(self.page_home)
        self.frame_mainHomePage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mainHomePage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mainHomePage.setObjectName("frame_mainHomePage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_mainHomePage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton_startGame = QtWidgets.QPushButton(self.frame_mainHomePage)
        self.pushButton_startGame.setObjectName("pushButton_startGame")
        self.gridLayout_4.addWidget(self.pushButton_startGame, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 2, 1, 1)
        self.frame_mode = QtWidgets.QFrame(self.frame_mainHomePage)
        self.frame_mode.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mode.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mode.setObjectName("frame_mode")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_mode)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox_mode = QtWidgets.QComboBox(self.frame_mode)
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_mode, 0, 1, 1, 1)
        self.label_selectMode = QtWidgets.QLabel(self.frame_mode)
        self.label_selectMode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_selectMode.setObjectName("label_selectMode")
        self.gridLayout_5.addWidget(self.label_selectMode, 0, 0, 1, 1)
        self.scrollArea_modeDetails = QtWidgets.QScrollArea(self.frame_mode)
        self.scrollArea_modeDetails.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_modeDetails.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_modeDetails.setWidgetResizable(True)
        self.scrollArea_modeDetails.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea_modeDetails.setObjectName("scrollArea_modeDetails")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 501, 306))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_modeDetails = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_modeDetails.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_modeDetails.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_modeDetails.setObjectName("frame_modeDetails")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_modeDetails)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_modeDetails = QtWidgets.QLabel(self.frame_modeDetails)
        self.label_modeDetails.setAlignment(QtCore.Qt.AlignCenter)
        self.label_modeDetails.setObjectName("label_modeDetails")
        self.gridLayout_7.addWidget(self.label_modeDetails, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_modeDetails, 0, 0, 1, 1)
        self.scrollArea_modeDetails.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea_modeDetails, 1, 0, 1, 2)
        self.gridLayout_4.addWidget(self.frame_mode, 0, 0, 1, 3)
        self.gridLayout_3.addWidget(self.frame_mainHomePage, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_home)
        self.page_game = QtWidgets.QWidget()
        self.page_game.setObjectName("page_game")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_game)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_game = QtWidgets.QFrame(self.page_game)
        self.frame_game.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_game.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_game.setObjectName("frame_game")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_game)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem2, 0, 1, 1, 1)
        self.frame_gameBoard = QtWidgets.QFrame(self.frame_game)
        self.frame_gameBoard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_gameBoard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gameBoard.setObjectName("frame_gameBoard")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_gameBoard)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton_gameBoard_5 = QtWidgets.QPushButton(self.frame_gameBoard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gameBoard_5.sizePolicy().hasHeightForWidth())
        self.pushButton_gameBoard_5.setSizePolicy(sizePolicy)
        self.pushButton_gameBoard_5.setText("")
        self.pushButton_gameBoard_5.setObjectName("pushButton_gameBoard_5")
        self.gridLayout_10.addWidget(self.pushButton_gameBoard_5, 1, 1, 1, 1)
        self.pushButton_gameBoard_6 = QtWidgets.QPushButton(self.frame_gameBoard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gameBoard_6.sizePolicy().hasHeightForWidth())
        self.pushButton_gameBoard_6.setSizePolicy(sizePolicy)
        self.pushButton_gameBoard_6.setText("")
        self.pushButton_gameBoard_6.setObjectName("pushButton_gameBoard_6")
        self.gridLayout_10.addWidget(self.pushButton_gameBoard_6, 2, 0, 1, 1)
        self.pushButton_gameBoard_0 = QtWidgets.QPushButton(self.frame_gameBoard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gameBoard_0.sizePolicy().hasHeightForWidth())
        self.pushButton_gameBoard_0.setSizePolicy(sizePolicy)
        self.pushButton_gameBoard_0.setText("")
        self.pushButton_gameBoard_0.setObjectName("pushButton_gameBoard_0")
        self.gridLayout_10.addWidget(self.pushButton_gameBoard_0, 0, 0, 1, 1)
        self.pushButton_gameBoard_10 = QtWidgets.QPushButton(self.frame_gameBoard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gameBoard_10.sizePolicy().hasHeightForWidth())
        self.pushButton_gameBoard_10.setSizePolicy(sizePolicy)
        self.pushButton_gameBoard_10.setText("")
        self.pushButton_gameBoard_10.setObjectName("pushButton_gameBoard_10")
        self.gridLayout_10.addWidget(self.pushButton_gameBoard_10, 2, 2, 1, 1)
        self.pushButton_gameBoard_2 = QtWidgets.QPushButton(self.frame_gameBoard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gameBoard_2.sizePolicy().hasHeightForWidth())
        self.pushButton_gameBoard_2.setSizePolicy(sizePolicy)
        self.pushButton_gameBoard_2.setText("")
        self.pushButton_gameBoard_2.setObjectName("pushButton_gameBoard_2")
        self.gridLayout_10.addWidget(self.pushButton_gameBoard_2, 0, 2, 1, 1)
        self.pushButton_gameBoard_1 = QtWidgets.QPushButton(self.frame_gameBoard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gameBoard_1.sizePolicy().hasHeightForWidth())
        self.pushButton_gameBoard_1.setSizePolicy(sizePolicy)
        self.pushButton_gameBoard_1.setText("")
        self.pushButton_gameBoard_1.setObjectName("pushButton_gameBoard_1")
        self.gridLayout_10.addWidget(self.pushButton_gameBoard_1, 0, 1, 1, 1)
        self.pushButton_gameBoard_8 = QtWidgets.QPushButton(self.frame_gameBoard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gameBoard_8.sizePolicy().hasHeightForWidth())
        self.pushButton_gameBoard_8.setSizePolicy(sizePolicy)
        self.pushButton_gameBoard_8.setText("")
        self.pushButton_gameBoard_8.setObjectName("pushButton_gameBoard_8")
        self.gridLayout_10.addWidget(self.pushButton_gameBoard_8, 2, 1, 1, 1)
        self.pushButton_gameBoard_3 = QtWidgets.QPushButton(self.frame_gameBoard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gameBoard_3.sizePolicy().hasHeightForWidth())
        self.pushButton_gameBoard_3.setSizePolicy(sizePolicy)
        self.pushButton_gameBoard_3.setText("")
        self.pushButton_gameBoard_3.setObjectName("pushButton_gameBoard_3")
        self.gridLayout_10.addWidget(self.pushButton_gameBoard_3, 1, 0, 1, 1)
        self.pushButton_gameBoard_9 = QtWidgets.QPushButton(self.frame_gameBoard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gameBoard_9.sizePolicy().hasHeightForWidth())
        self.pushButton_gameBoard_9.setSizePolicy(sizePolicy)
        self.pushButton_gameBoard_9.setText("")
        self.pushButton_gameBoard_9.setObjectName("pushButton_gameBoard_9")
        self.gridLayout_10.addWidget(self.pushButton_gameBoard_9, 1, 2, 1, 1)
        self.gridLayout_9.addWidget(self.frame_gameBoard, 1, 0, 1, 2)
        self.pushButton_quit = QtWidgets.QPushButton(self.frame_game)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.gridLayout_9.addWidget(self.pushButton_quit, 0, 0, 1, 1)
        self.label_gameBottomText = QtWidgets.QLabel(self.frame_game)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_gameBottomText.sizePolicy().hasHeightForWidth())
        self.label_gameBottomText.setSizePolicy(sizePolicy)
        self.label_gameBottomText.setObjectName("label_gameBottomText")
        self.gridLayout_9.addWidget(self.label_gameBottomText, 2, 0, 1, 2)
        self.gridLayout_8.addWidget(self.frame_game, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_game)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe-AI (Desktop)"))
        self.pushButton_startGame.setText(_translate("MainWindow", "Start Game!"))
        self.comboBox_mode.setItemText(0, _translate("MainWindow", "Hard"))
        self.comboBox_mode.setItemText(1, _translate("MainWindow", "Easy"))
        self.comboBox_mode.setItemText(2, _translate("MainWindow", "2 Players"))
        self.label_selectMode.setText(_translate("MainWindow", "Select Mode:"))
        self.label_modeDetails.setText(_translate("MainWindow", "Mode Details:\n"
"You will play against an AI that uses the Minimax Alpha Beta Pruning Algorithm\n"
"to make the best move possible.\n"
"You won\'t win, the best thing you can do is a tie!"))
        self.pushButton_quit.setText(_translate("MainWindow", "Quit"))
        self.label_gameBottomText.setText(_translate("MainWindow", "The AI let\'s you go first out of pity."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
