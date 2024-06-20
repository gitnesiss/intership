import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Задаём название окна
        self.setWindowTitle("My App - Mouse button event")

        # Задаём минимальный размер окна (ширина, высота)
        self.setMinimumSize(QSize(400, 300))

        # Создаём экземпляр класса метки
        self.label = QLabel("Click in this window")
        # Устанавливаем виджет по центру окна
        self.setCentralWidget(self.label)

        # Включение отслеживания мыши при движении
        # self.tabWidget.setMouseTracking(True)
        # self.centralWidget.setMouseTracking(True)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent   ")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent   ")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent   ")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent   ")

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # здесь обрабатываем нажатие левой кнопки
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            # здесь обрабатываем нажатие средней кнопки.
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            # здесь обрабатываем нажатие правой кнопки.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
