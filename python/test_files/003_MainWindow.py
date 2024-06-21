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


        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('&File')
        edit_menu = menu_bar.addMenu('&Edit')
        help_menu = menu_bar.addMenu('&Help')

        file_menu.addAction('New', lambda: self.windowIconTextChanged.clear())
        file_menu.addAction('Open', lambda: print('Open'))
        file_menu.addAction('Exit', self.destroy)

        # Устанавливаем виджет (кнопку) в центр окна
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()