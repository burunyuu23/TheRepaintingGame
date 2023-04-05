from numpy import random

from PyQt5.QtGui import *

COLORS = {
    1: QColor('#a5260a'),  # Бисмарк-фуриозо
    2: QColor('#f36223'),  # Морковный
    3: QColor('#ff9218'),  # Последний вздох Жако
    4: QColor('#3caa3c'),  # Цвет влюблённой жабы
    5: QColor('#1fcecb'),  # Цвет яиц странствующего дрозда
    6: QColor('#7442c8')  # Пурпурное сердце
}


class Game:
    MAX_ROUNDS = 22

    STATUS = {
        "PLAYING": 0, 'LOSE': 1, 'WON': 2
    }

    COLOR_STATUS = {
        "PLAYING": 0, 'WON': 1
    }

    def __init__(self):
        self.map = [[Cell() for i in range(12)] for j in range(12)]
        self.color_map_count = [0 for i in range(len(COLORS))]
        self.main_cell = self.map[0][0]
        self.main_cell.captured(self.main_cell.value)
        self._status = Game.STATUS["PLAYING"]
        self.round = 0

        self.best = 23
        self.best_text = '∞'

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def step(self, num):
        self.color_map_count = [0 for i in range(len(COLORS))]
        if self.main_cell.value != num and self.status == Game.STATUS["PLAYING"]:
            self.map[0][0].change_value(num)
            self.map = self.map_capture()
            self.round += 1
            # self.status = Game.STATUS["WON"]

            if self.check_map:
                self.status = Game.STATUS["WON"]

            if self.status == Game.STATUS["WON"]:
                print('you won!')
                print(self.best)
                print(self.round)
                if self.best >= self.round:
                    self.best = self.round
                    self.best_text = str(self.best)

            if self.status != Game.STATUS["WON"] and self.round == Game.MAX_ROUNDS:
                print('you lose!')
                self.status = Game.STATUS["LOSE"]

    def restart(self):
        self.map = [[Cell(color=2) for i in range(12)] for j in range(12)]
        self.map[0][0] = Cell(color=1)
        self.map[0][1] = Cell(color=3)
        self.map[1][1] = Cell(color=4)

        self.map = [[Cell() for i in range(12)] for j in range(12)]  # Delete it if you want test fast win

        self.main_cell = self.map[0][0]
        self.main_cell.captured(self.main_cell.value)

        while self.map[0][1].value == self.main_cell.value:
            self.map[0][1] = Cell()
        while self.map[1][0].value == self.main_cell.value:
            self.map[1][0] = Cell()

        self.status = Game.STATUS["PLAYING"]
        self.round = 0

    def map_capture(self):
        old_map = self.map
        reached_map = [[False for _ in range(12)] for __ in range(12)]
        reached_map[0][0] = False

        max_i = len(old_map)
        max_j = len(old_map[0])

        def check(m, k, target):
            return (old_map[m][k].is_captured is True or old_map[m][k].value == target) and reached_map[m][k] is False

        def check_brother(i, j, value):
            if check(i, j, value):
                old_map[i][j].captured(value)
                i_check(i, j)

        def j_check(x, y, num):
            if y == 0:
                check_brother(x, y + 1, num)
            elif y == max_j - 1:
                check_brother(x, y - 1, num)
            else:
                check_brother(x, y + 1, num)
                check_brother(x, y - 1, num)

        def i_check(i, j):
            if old_map[i][j].is_captured is True and reached_map[i][j] is False:
                value = old_map[i][j].value
                reached_map[i][j] = True

                if i == 0:
                    check_brother(i + 1, j, value)
                elif i == max_i - 1:
                    check_brother(i - 1, j, value)
                else:
                    check_brother(i + 1, j, value)
                    check_brother(i - 1, j, value)

                j_check(i, j, value)

        i_check(0, 0)

        return old_map

    @property
    def check_map(self):
        main_cell = self.map[0][0]
        for line in self.map:
            for cell in line:
                if cell != main_cell:
                    return False
        return True


class Cell:
    def __init__(self, color=None):
        if color is None:
            self.value = random.randint(1, len(COLORS) + 1)
        else:
            self.value = color
        self.is_captured = False

    def captured(self, value):
        self.is_captured = True
        self.value = value

    def change_value(self, value):
        self.value = value

    def __repr__(self):
        return f"is_captured<{self.is_captured}>: value = {self.value}"

    def __str__(self):
        return f"is_captured<{self.is_captured}>: value = {self.value}"

    def __eq__(self, other):
        return self.value == other.value
