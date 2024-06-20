import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        # Задаём название окна
        self.setWindowTitle("My App - Button unavailable")

        # Задаём минимальный и максимальный размер окна (ширина, высота)
        self.setMinimumSize(QSize(400, 300))

        # Создаём кнопку с надписью
        self.button = QPushButton("Нажми меня!")

        # Создаём сигал clicked от QPushButton по нажатию кнопки
        self.button.clicked.connect(self.the_button_was_clicked)        

        # Устанавливаем виджет (кнопку) в центр окна
        self.setCentralWidget(self.button)

    # Функция выводит информацию о том, что нажата сейчас кнопка или нет (как переключатель вкл/выкл)
    def the_button_was_clicked(self):
        # Меняем текст на кнопке (при нажатии на кнопку)
        self.button.setText("Меня уже нажали")
        # Отключаем кнопку
        self.button.setEnabled(False)

        # Меняем заголовок окна
        self.setWindowTitle("Моё приложение \"Один выстрел\"")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
