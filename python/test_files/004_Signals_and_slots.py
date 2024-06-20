import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Задаём название окна
        self.setWindowTitle("My App - Slots and signals")
        
        # Задаём положение окна на экране и начальный размер 
        self.setGeometry(200, 100, 100, 100)
        # Размеры окна заданные выше перепишутся параметрами self.setMinimumSize()
        # Задаём минимальный и максимальный размер окна (ширина, высота)
        # Если убрать строку self.setMaximumSize(QSize(800, 600)), то окно можно развернуть на максимум.
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(800, 600))


        # Создаём кнопку с надписью
        button = QPushButton("Press me!")
        # Проверка на то, что нажата/переключена кнопка или нет
        button.setCheckable(True)
        # Создаём сигал clicked от QPushButton по нажатию кнопки
        button.clicked.connect(self.the_button_was_clicked)
        # Создаём сигнал clicked от QPushButton по нажатию кнопки происходит проверка зажата или нет кнопка
        button.clicked.connect(self.the_button_was_toggle)

        # Устанавливаем виджет (кнопку) в центр окна
        self.setCentralWidget(button)
    
    # Функция выводит инофрмацию о том, что кнопка была нажата
    def the_button_was_clicked(self):
        print("Clicked!")
    
    # Функция выводит информацию о том, что нажата сейчас кнопка или нет (как переключатель вкл/выкл)
    def the_button_was_toggle(self, checked):
        print("Checked?", checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()