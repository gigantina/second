import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
import random
import traceback


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)

    text += ''.join(traceback.format_tb(tb))

    print(text)

    sys.exit()


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_drawing = False
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.is_drawing:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.is_drawing = True
        self.repaint()

    def draw_flag(self, qp):
        for i in range(3):
            qp.setBrush(QColor(255, 255, 0))
            x = random.randint(10, 500)
            y = random.randint(10, 500)
            w = random.randint(100, 300)
            qp.drawEllipse(x, y, w, w)


if __name__ == '__main__':
    sys.excepthook = log_uncaught_exceptions
    app = QApplication(sys.argv)
    ex = Main_Window()

    ex.show()
    sys.exit(app.exec_())
