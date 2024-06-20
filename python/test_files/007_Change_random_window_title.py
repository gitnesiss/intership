import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# Добавление библиотеки для работы со случайными числами
from random import choice

# Создаём список названий заголовков окна
window_titles = [
    'Моё приложение',
    'Моё приложение',
    'Всё ещё моё приложение',
    'Всё ещё моё приложение',
    'Что за фигня',
    'Что за фигня',
    'Это удивительно',
    'Это удивительно',
    'Что-то пошло не так'
]

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Переменная содержащая количество нажатий на кнопку
        self.n_times_ckicked = 0

        # Задаём название окна
        self.setWindowTitle("My App - Random window title")

        # Задаём минимальный и максимальный размер окна (ширина, высота)
        self.setMinimumSize(QSize(400, 300))

        # Создаём кнопку с надписью
        self.button = QPushButton("Нажми меня!")

        # Создаём сигал clicked от QPushButton по нажатию кнопки
        self.button.clicked.connect(self.the_button_was_clicked)

        # Создаём сигал windowTitleChanged (изменение названия окна), соединённый с пользовательским методом the_window_title_changed()
        self.windowTitleChanged.connect(self.the_window_title_changed)

        # Устанавливаем виджет (кнопку) в центр окна
        self.setCentralWidget(self.button)

    # Функция выводит информацию о том, что нажата сейчас кнопка или нет (как переключатель вкл/выкл)
    def the_button_was_clicked(self):
        print("Нажато.")
        # Создаём переменную и записываем в неё название заголовка, выбранное случайным образом
        new_window_title = choice(window_titles)
        print("Установлен заголовок окна: %s" % new_window_title)
        self.setWindowTitle(new_window_title)
        # Увеличиваем счётчик нажатий на кнопку на 1
        self.n_times_ckicked += 1
        print("Совершено нажатий на кнопку: %s" % self.n_times_ckicked)

    # Функция выводит информацию о том, что нажата сейчас кнопка или нет (как переключатель вкл/выкл)
    def the_window_title_changed(self, window_titles):
        print("Заголовок окна изменён: %s" % window_titles)

        # Если заголовок окна изменится на 'Somethig went wrong'- кнопка отключится
        if window_titles == 'Что-то пошло не так':
            # Устанавливаем кнопке состояние отключена ("не активна")
            self.button.setDisabled(True)
            print("Кнопка заблокирована.")
            # Меняем текст на кнопке на 'Кнопка не активна'
            self.button.setText("Кнопка не активна")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()