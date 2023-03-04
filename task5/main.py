import copy
import os
import sys
from threading import Timer

from PyQt5 import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie, QIcon, QPixmap
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *

from task5 import game
from task5.game import COLORS
from windows.mainWindow import Ui_MainWindow as UI_Main
from windows.optionsWindow import Ui_MainWindow as UI_Options
from windows.gameWindow import Ui_MainWindow as UI_Game


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.game = game.Game()
        self.ui = UI_Main()
        self.initUI()

    def add_music(self, path):
        full_file_path = os.path.join(os.getcwd(), path)
        url = QUrl.fromLocalFile(full_file_path)
        self.playlist.addMedia(QMediaContent(url))

    def _player_init(self):
        self.playlist = QMediaPlaylist()

        self.add_music('music/muffled_soundtrack.mp3')
        self.add_music('music/soundtrack.mp3')

        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)

        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.play()
        self.player.setVolume(5)

    def _effect_init(self):
        self.effect = QGraphicsColorizeEffect()
        self.ui.game_name_text.setGraphicsEffect(self.effect)
        an = QPropertyAnimation(self.effect, b"color", self)

        an.setStartValue(game.COLORS.get(1))
        for i in range(1, 7):
            an.setKeyValueAt(i / 12.0, game.COLORS.get(i))
            an.setKeyValueAt((6 + i) / 12.0, game.COLORS.get(i))
        an.setEndValue(game.COLORS.get(1))

        an.setDuration(12000)
        an.setLoopCount(-1)
        an.start()

    def _movie_init(self):
        movie = QMovie("gifs/lego-painting.gif")
        self.ui.bob_ross.setMovie(movie)
        movie.start()

    @pyqtSlot()
    def _play_click(self):
        self.cams = GameWindow(self)
        self.cams.show()
        self.hide()

    def change_song(self):
        position = self.player.position()
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player.playlist().next()
        self.player.setPosition(position)
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        self.player.play()

    @pyqtSlot()
    def _options_click(self):
        self.cams = OptionsWindow(self)
        self.cams.show()
        self.hide()
        self.change_song()

    @pyqtSlot()
    def showEvent(self, event):
        super(MainWindow, self).showEvent(event)
        super().showEvent(event)

    @pyqtSlot()
    def _info_click(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Это информация о данном продукте мозговой деятельности на языке PyPy!")
        dlg.setText("Левый верхний квадратик в «Перекраске» всегда работает для достижения своих целей. " +
                    "Тем не менее, игра прекрасно показывает, как стремление цветов к своим стремлениям формирует то, "
                    "кем они становятся. " +
                    "Те, кто выбирает нечестные средства, будут разоблачены, кто они на самом деле, и останутся ни с "
                    "чем, кроме смущения и стыда. " +
                    "С другой стороны, такие, как левый верхний квадрат и его цвет, будут прославлены за их "
                    "способность преодолевать трудности с надеждой и позитивным настроем. " +
                    "То, как первый квадрат достигает своей мечты, имеет решающее значение и будет иметь долгосрочные "
                    "последствия. " +
                    "Ленивый никогда не завоюет чьего-либо уважения.\n\n\n" +
                    "Автор шедевра:                                                               " +
                    "                                                         Я\n" +
                    "Режессер:                                                                    " +
                    "                                                              Я\n" +
                    "Сценарист:                                                                   " +
                    "                                                             Я\n" +
                    "Я:                                                                           " +
                    "                                           Koshenyatkovv23\n")

        dlg.exec()

    @pyqtSlot()
    def _exit_click(self):
        sys.exit(app.exec())

    def initUI(self):
        self.setFixedSize(1200, 800)
        self.ui.setupUi(self)
        ui = self.ui

        self._movie_init()
        self._effect_init()
        self._player_init()

        ui.play_button.clicked.connect(self._play_click)
        ui.options_button.clicked.connect(self._options_click)
        ui.info_button.clicked.connect(self._info_click)
        ui.exit_button.clicked.connect(self._exit_click)


class GameWindow(QMainWindow):
    def __init__(self, main_window):
        super(GameWindow, self).__init__()
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()

        self.init_music()

        self.parent = main_window
        self.ui = UI_Game()
        self.game = self.parent.game
        self.game.restart()

        self.initUI()

        self.ui.home_button.clicked.connect(self._home_click)
        self.ui.re_button.clicked.connect(self._restart_click)

    def initUI(self):
        self.setFixedSize(800, 1000)
        self.ui.setupUi(self)
        self.window().setWindowIcon(QIcon("./images/game_icon.png"))

        self.ui.best_counter_label.setText(self.game.best_text)

        self.ui.winlogo.hide()
        self.ui.winmenu.hide()
        self.ui.minion_win.hide()

        model = TableModel(self.game)
        self.ui.field_table.setModel(model)

        buttons = [self.ui.r_button, self.ui.o_button, self.ui.y_button,
                   self.ui.g_button, self.ui.b_button, self.ui.p_button]

        for i in range(len(buttons)):
            num = copy.copy(i + 1)
            buttons[i].setStyleSheet('QPushButton {background-color: ' + game.COLORS[num].name()
                                     + '; color: ' + game.COLORS[num].name() + '}')
            buttons[i].setText(str(num))
            buttons[i].clicked.connect(self.change_color_on_click)

        self.ui.field_table.horizontalHeader().hide()
        self.ui.field_table.verticalHeader().hide()
        self.ui.field_table.horizontalHeader().setResizeContentsPrecision(QHeaderView.Fixed)
        self.ui.field_table.verticalHeader().setResizeContentsPrecision(QHeaderView.Fixed)
        self.ui.field_table.horizontalHeader().setDefaultSectionSize(50)
        self.ui.field_table.verticalHeader().setDefaultSectionSize(50)

        self._movie_init()

    def _movie_init(self):
        movie = QMovie("gifs/re_button.gif")
        self.ui.re_label.setMovie(movie)
        self.ui.re_button.setStyleSheet("""QPushButton,
        QPushButton:default,
        QPushButton:hover,
        QPushButton:selected,
        QPushButton:disabled,
        QPushButton:pressed {
            background-color: transparent;
            border-color: transparent;
            color: transparent;
        }""")
        movie.start()

        movie = QMovie("gifs/home_button.gif")
        self.ui.home_label.setMovie(movie)
        self.ui.home_button.setStyleSheet("""QPushButton,
QPushButton:default,
QPushButton:hover,
QPushButton:selected,
QPushButton:disabled,
QPushButton:pressed {
    background-color: transparent;
    border-color: transparent;
    color: transparent;
}""")
        movie.start()

    @pyqtSlot()
    def _restart_click(self):
        self.game.restart()

        self.ui.winlogo.hide()
        self.ui.winmenu.hide()
        self.ui.minion_win.hide()
        self.ui.loser_label.hide()
        self.player.stop()

        model = TableModel(self.game)
        self.ui.field_table.setModel(model)
        self.ui.cur_counter_label.setText(str(self.game.round) + '/' + str(self.game.MAX_ROUNDS))

    @pyqtSlot()
    def change_color_on_click(self):
        s_game = self.game
        if s_game.status == 0:
            button = self.sender()
            text = button.text()
            self.ui.field_table.repaint()
            s_game.step(int(text))
            self.ui.field_table.setModel(TableModel(s_game))
            self.ui.cur_counter_label.setText(str(s_game.round) + '/' + str(s_game.MAX_ROUNDS))

            if s_game.status == 2:
                self.ui.best_counter_label.setText(self.game.best_text)
                self.ui.winlogo.show()
                self.ui.winmenu.show()
                self.ui.minion_win.show()

                self.playlist.setCurrentIndex(0)
                self.player.play()

                movie = QMovie("gifs/win.gif")
                self.ui.minion_win.setMovie(movie)
                movie.start()

            if s_game.status == 1:
                self.ui.cur_counter_label.setText('посмешише!!!')

                self.playlist.setCurrentIndex(1)
                self.player.play()

                self.ui.loser_label.show()
                movie = QMovie("gifs/looser.gif")
                self.ui.loser_label.setMovie(movie)
                movie.start()

    @pyqtSlot()
    def _home_click(self):
        self.parent.show()
        self.hide()

    def init_music(self):
        full_file_path = os.path.join(os.getcwd(), 'music/win_sound.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        self.playlist.addMedia(QMediaContent(url))

        full_file_path = os.path.join(os.getcwd(), 'music/looser.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        self.playlist.addMedia(QMediaContent(url))

        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemOnce)

        self.player.setPlaylist(self.playlist)
        self.player.setVolume(20)


class TableModel(QAbstractTableModel):
    def __init__(self, table_game):
        super().__init__()
        self.headers = ["" for i in range(12)]
        self.rows = table_game.map

    def rowCount(self, parent):
        # How many rows are there?
        return len(self.rows)

    def columnCount(self, parent):
        # How many columns?
        return len(self.headers)

    def data(self, index, role):
        if role == Qt.BackgroundRole:
            return game.COLORS[int(self.rows[index.row()][index.column()].value)]

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        # What's the header for the given column?
        return self.headers[section]


class OptionsWindow(QMainWindow):
    def __init__(self, main_window):
        super(OptionsWindow, self).__init__()
        self.parent = main_window
        self.ui = UI_Options()
        self.initUI()

        self.ui.sound_colok.valueChanged.connect(self.dialer_changed)
        self.ui.back_button.clicked.connect(self._home_click)

        QAction("Quit", self).triggered.connect(self.closeEvent)

    @pyqtSlot()
    def dialer_changed(self):
        getValue = self.ui.sound_colok.value()
        self.ui.colok_percentage_label.setText(str(getValue) + "%")
        self.parent.player.setVolume(getValue)

    def closeEvent(self, event):
        event.accept()

    def _movie_init(self):
        movie = QMovie("gifs/options.gif")
        self.ui.movie_label.setMovie(movie)
        movie.start()

    def _backmovie_init(self):
        movie = QMovie("gifs/options_to_menu.gif")

        rect = self.ui.back_movie.geometry()
        size = QSize(min(rect.width(), rect.width()), min(rect.height(), rect.height()))

        movie.setScaledSize(size)
        for elem in self.ui.centralwidget.children():
            elem.hide()
        self.ui.back_movie.show()
        self.ui.back_movie.setMovie(movie)
        movie.start()

    def initUI(self):
        self.setFixedSize(1200, 800)
        self.ui.setupUi(self)

        self.window().setWindowIcon(QIcon("./images/options_icon.png"))

        self.buttons = [self.ui.r_button, self.ui.o_button, self.ui.y_button,
                        self.ui.g_button, self.ui.b_button, self.ui.p_button]

        for i in range(len(self.buttons)):
            num = copy.copy(i + 1)
            self.buttons[i].setStyleSheet('QPushButton {background-color: ' + game.COLORS[num].name()
                                          + '; color: ' + game.COLORS[num].name() + '}')
            self.buttons[i].setText(str(num))
            self.buttons[i].clicked.connect(self._color_change_click)

        volume = self.parent.player.volume()
        self.ui.colok_percentage_label.setText(str(volume) + "%")
        self.parent.player.setVolume(volume)

        self._movie_init()

    def _bye_bye(self):
        self.parent.show()
        self.hide()
        self.parent.change_song()

    @pyqtSlot()
    def _home_click(self):
        self._backmovie_init()
        Timer(2.5, self._bye_bye).start()

    @pyqtSlot()  # TODO
    def _color_change_click(self, ):
        button = self.sender()
        text = button.text()
        value = int(text)

        color = QColorDialog.getColor()
        game.COLORS[value] = color
        button.setStyleSheet('QPushButton {background-color: ' + game.COLORS[value].name()
                                      + '; color: ' + game.COLORS[value].name() + '}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle('Fusion')

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
