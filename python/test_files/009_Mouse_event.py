import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаём экземпляр класса метки
        self.label = QLabel("Click in this window")
        # Устанавливаем виджет по центру окна
        self.setCentralWidget(self.label)

        # Включение отслеживания мыши при движении
        # self.tabWidget.setMouseTracking(True)
        # self.centralWidget.setMouseTracking(True)
        self.setMouseTracking(True)

    # Функция перемещения мыши
    def mouseMoveEvent(self, e):
        self.label.setMouseTracking(True)
        self.label.setText("mouseMoveEvent")

    # Функция кнопка мыши нажата
    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    # Функция кнопка мыши отпущена
    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    # Функция обнаружения двойного клика
    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
