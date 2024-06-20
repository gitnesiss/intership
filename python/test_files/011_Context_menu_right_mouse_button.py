import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Задаём название окна
        self.setWindowTitle("My App - Context menu on right mouse button event")

        # Задаём минимальный размер окна (ширина, высота)
        self.setMinimumSize(QSize(400, 300))

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

'''
# Второй вариант класса для создания контекстного меню
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()

        # Задаём название окна
        self.setWindowTitle("My App - Context menu on right mouse button event")

        # Задаём минимальный размер окна (ширина, высота)
        self.setMinimumSize(QSize(400, 300))

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))
'''


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()