import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        # Задаём название окна
        self.setWindowTitle("My App - Current state widget")

        # Задаём минимальный и максимальный размер окна (ширина, высота)
        self.setMinimumSize(QSize(400, 300))

        # Создаём кнопку с надписью
        self.button = QPushButton("Нажми меня!")
        # Проверка на то, что нажата/переключена кнопка или нет
        self.button.setCheckable(True)

        # Создаём сигнал released от QPushButton по нажатию кнопки происходит проверка зажата или нет кнопка
        # Сигнал released срабатывает, когда кнопка отпускается, при этом состояние нажатия не отправляется. 
        # Его получают из кнопки в обработчике, используя .isChecked()
        self.button.released.connect(self.the_button_was_released)
        # Создаём сигнал clicked от QPushButton по нажатию кнопки происходит проверка зажата или нет кнопка
        self.button.setChecked(self.button_is_checked)

        # Устанавливаем виджет (кнопку) в центр окна
        self.setCentralWidget(self.button)

    # Функция выводит информацию о том, что нажата сейчас кнопка или нет (как переключатель вкл/выкл)
    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()