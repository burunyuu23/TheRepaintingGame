# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gameWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 1000)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/game_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(128, 128))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.field_table = QtWidgets.QTableView(self.centralwidget)
        self.field_table.setGeometry(QtCore.QRect(99, 205, 602, 602))
        self.field_table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.field_table.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged)
        self.field_table.setDragDropOverwriteMode(False)
        self.field_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.field_table.setIconSize(QtCore.QSize(9, 0))
        self.field_table.setObjectName("field_table")
        self.r_button = QtWidgets.QPushButton(self.centralwidget)
        self.r_button.setGeometry(QtCore.QRect(75, 830, 100, 100))
        self.r_button.setObjectName("r_button")
        self.o_button = QtWidgets.QPushButton(self.centralwidget)
        self.o_button.setGeometry(QtCore.QRect(185, 830, 100, 100))
        self.o_button.setObjectName("o_button")
        self.g_button = QtWidgets.QPushButton(self.centralwidget)
        self.g_button.setGeometry(QtCore.QRect(405, 830, 100, 100))
        self.g_button.setObjectName("g_button")
        self.y_button = QtWidgets.QPushButton(self.centralwidget)
        self.y_button.setGeometry(QtCore.QRect(295, 830, 100, 100))
        self.y_button.setObjectName("y_button")
        self.b_button = QtWidgets.QPushButton(self.centralwidget)
        self.b_button.setGeometry(QtCore.QRect(515, 830, 100, 100))
        self.b_button.setObjectName("b_button")
        self.p_button = QtWidgets.QPushButton(self.centralwidget)
        self.p_button.setGeometry(QtCore.QRect(625, 830, 100, 100))
        self.p_button.setObjectName("p_button")
        self.cur_counter_label = QtWidgets.QLabel(self.centralwidget)
        self.cur_counter_label.setGeometry(QtCore.QRect(100, 130, 600, 90))
        font = QtGui.QFont()
        font.setFamily("Matura MT Script Capitals")
        font.setPointSize(72)
        self.cur_counter_label.setFont(font)
        self.cur_counter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cur_counter_label.setObjectName("cur_counter_label")
        self.best_label = QtWidgets.QLabel(self.centralwidget)
        self.best_label.setGeometry(QtCore.QRect(0, -20, 151, 101))
        self.best_label.setMinimumSize(QtCore.QSize(151, 101))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(48)
        self.best_label.setFont(font)
        self.best_label.setAlignment(QtCore.Qt.AlignCenter)
        self.best_label.setObjectName("best_label")
        self.best_counter_label = QtWidgets.QLabel(self.centralwidget)
        self.best_counter_label.setGeometry(QtCore.QRect(0, 50, 151, 101))
        self.best_counter_label.setMinimumSize(QtCore.QSize(151, 101))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(72)
        self.best_counter_label.setFont(font)
        self.best_counter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.best_counter_label.setObjectName("best_counter_label")
        self.re_button = QtWidgets.QPushButton(self.centralwidget)
        self.re_button.setGeometry(QtCore.QRect(590, 10, 90, 90))
        self.re_button.setObjectName("re_button")
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(690, 10, 90, 90))
        self.home_button.setObjectName("home_button")
        self.re_label = QtWidgets.QLabel(self.centralwidget)
        self.re_label.setEnabled(False)
        self.re_label.setGeometry(QtCore.QRect(590, 10, 91, 91))
        self.re_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.re_label.setText("")
        self.re_label.setScaledContents(True)
        self.re_label.setObjectName("re_label")
        self.home_label = QtWidgets.QLabel(self.centralwidget)
        self.home_label.setEnabled(False)
        self.home_label.setGeometry(QtCore.QRect(690, 10, 91, 91))
        self.home_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.home_label.setText("")
        self.home_label.setScaledContents(True)
        self.home_label.setObjectName("home_label")
        self.winlogo = QtWidgets.QLabel(self.centralwidget)
        self.winlogo.setGeometry(QtCore.QRect(10, 150, 800, 1000))
        self.winlogo.setText("")
        self.winlogo.setPixmap(QtGui.QPixmap(":/win/images/win_logo.png"))
        self.winlogo.setObjectName("winlogo")
        self.winmenu = QtWidgets.QLabel(self.centralwidget)
        self.winmenu.setGeometry(QtCore.QRect(220, 120, 800, 1000))
        self.winmenu.setMinimumSize(QtCore.QSize(800, 1000))
        self.winmenu.setText("")
        self.winmenu.setPixmap(QtGui.QPixmap(":/win/images/win_menu.jpeg"))
        self.winmenu.setObjectName("winmenu")
        self.minion_win = QtWidgets.QLabel(self.centralwidget)
        self.minion_win.setGeometry(QtCore.QRect(150, 730, 500, 281))
        self.minion_win.setText("")
        self.minion_win.setPixmap(QtGui.QPixmap(":/gif/gifs/win.gif"))
        self.minion_win.setObjectName("minion_win")
        self.buttons_frame = QtWidgets.QLabel(self.centralwidget)
        self.buttons_frame.setGeometry(QtCore.QRect(530, -110, 260, 216))
        font = QtGui.QFont()
        font.setPointSize(700)
        font.setBold(True)
        font.setWeight(75)
        self.buttons_frame.setFont(font)
        self.buttons_frame.setScaledContents(True)
        self.buttons_frame.setObjectName("buttons_frame")
        self.loser_label = QtWidgets.QLabel(self.centralwidget)
        self.loser_label.setGeometry(QtCore.QRect(410, 140, 311, 111))
        self.loser_label.setText("")
        self.loser_label.setPixmap(QtGui.QPixmap(":/gif/images/looser.gif"))
        self.loser_label.setObjectName("loser_label")
        self.buttons_frame.raise_()
        self.field_table.raise_()
        self.r_button.raise_()
        self.o_button.raise_()
        self.g_button.raise_()
        self.y_button.raise_()
        self.b_button.raise_()
        self.p_button.raise_()
        self.cur_counter_label.raise_()
        self.best_label.raise_()
        self.best_counter_label.raise_()
        self.re_label.raise_()
        self.home_label.raise_()
        self.home_button.raise_()
        self.re_button.raise_()
        self.winlogo.raise_()
        self.winmenu.raise_()
        self.minion_win.raise_()
        self.loser_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Перекраска"))
        self.r_button.setText(_translate("MainWindow", "R"))
        self.o_button.setText(_translate("MainWindow", "O"))
        self.g_button.setText(_translate("MainWindow", "G"))
        self.y_button.setText(_translate("MainWindow", "Y"))
        self.b_button.setText(_translate("MainWindow", "B"))
        self.p_button.setText(_translate("MainWindow", "P"))
        self.cur_counter_label.setText(_translate("MainWindow", "0/22"))
        self.best_label.setText(_translate("MainWindow", "BEST"))
        self.best_counter_label.setText(_translate("MainWindow", "22"))
        self.re_button.setText(_translate("MainWindow", "re:"))
        self.home_button.setText(_translate("MainWindow", "home"))
        self.buttons_frame.setText(_translate("MainWindow", "-"))
import background_game_rc
