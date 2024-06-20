import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Задаём название окна
        self.setWindowTitle("My App")

        # # Задаём фиксированный размер окна (ширина, высота)
        # self.setFixedSize(QSize(400, 300))
        # Задаём минимальный и максимальный размер окна (ширина, высота)
        # Если убрать строку self.setMaximumSize(QSize(800, 600)), то окно можно развернуть на максимум.
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(800, 600))
        
        # Создаём кнопку с надписью
        button = QPushButton("Press me!")
        # Устанавливаем виджет (кнопку) в центр окна
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()